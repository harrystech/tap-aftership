"""REST client handling, including AfterShipStream base class."""

from pathlib import Path
from typing import Any, Dict, Optional

import requests
from singer_sdk.authenticators import APIKeyAuthenticator
from singer_sdk.streams import RESTStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class AfterShipStream(RESTStream):
    """AfterShip stream class."""

    url_base = "https://api.aftership.com"
    records_jsonpath = "$[*]"  # Or override `parse_response`.
    next_page_token_jsonpath = "$.data.page"

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Return a new authenticator object."""
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="aftership-api-key",
            value=str(self.config.get("api_key")),
            location="header",
        )

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        response_json = response.json()
        if response_json["data"] and response.status_code == 200:
            return response_json["data"]["page"] + 1
        else:
            return None

    def validate_response(self, response: requests.Response) -> None:
        """Validate HTTP response.

        Overridden from base class to check for status_code == 400, which is how
        AfterShip denotes hitting the pagination limit.
        """
        #  Aftership responds with a 400 when pagination limit is hit, ignore it
        if response.status_code != 400:
            super(AfterShipStream, self).validate_response(response)

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        if next_page_token:
            params["page"] = next_page_token
        if "end_date" in self.config:
            params["created_at_max"] = self.config["end_date"]
        params["created_at_min"] = self.config["start_date"]

        return params
