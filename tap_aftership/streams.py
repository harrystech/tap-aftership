"""Stream type classes for tap-aftership."""

from pathlib import Path

from tap_aftership.client import AfterShipStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class TrackingsStream(AfterShipStream):
    """Define custom stream."""

    name = "trackings"
    path = "/v4/trackings"
    primary_keys = ["id"]
    replication_key = None

    schema_filepath = SCHEMAS_DIR / "tracking.json"
    records_jsonpath = "$.data.trackings[*]"
