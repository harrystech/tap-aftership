"""Tests standard tap features using the built-in SDK tests library."""

import datetime

import requests_mock
from singer_sdk.testing import get_standard_tap_tests

from tap_aftership.streams import TrackingsStream
from tap_aftership.tap import TapAfterShip

now = datetime.datetime.now(datetime.timezone.utc)
SAMPLE_CONFIG = {
    "start_date": (now - datetime.timedelta(days=1)).strftime("%Y-%m-%d"),
    "end_date": now.strftime("%Y-%m-%d"),
    "api_key": "test-api-key",
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    with requests_mock.Mocker() as m:
        path = (
            f"{TrackingsStream.path}?"
            f"created_at_max={SAMPLE_CONFIG['end_date']}"
            f"&created_at_min={SAMPLE_CONFIG['start_date']}"
        )
        m.get(path, status_code=200, text='{"data": {"page": 1, "trackings": []}}')
        m.get(
            f"{path}&page=2",
            status_code=400,
            text='{"data": {"page": 2, "trackings": []}}',
        )
        tests = get_standard_tap_tests(TapAfterShip, config=SAMPLE_CONFIG)
        for test in tests:
            test()
