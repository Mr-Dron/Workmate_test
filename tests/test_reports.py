import pytest
from reports.clickbait import clickbait_report


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            [
                {"title": "test1", "ctr": 21.2, "retention_rate": 25},
                {"title": "test2", "ctr": 24, "retention_rate": 24},
                {"title": "test3", "ctr": 23.2, "retention_rate": 23},
                {"title": "test4", "ctr": 13.2, "retention_rate": 23},
                {"title": "test5", "ctr": 26, "retention_rate": 43},
            ],
            [
                {"title": "test2", "ctr": 24, "retention_rate": 24},
                {"title": "test3", "ctr": 23.2, "retention_rate": 23},
                {"title": "test1", "ctr": 21.2, "retention_rate": 25},
            ],
        ),
        (
            [
                {"title": "test1", "ctr": 13.2, "retention_rate": 23},
                {"title": "test2", "ctr": 23.2, "retention_rate": 53},
                {"title": "test3", "ctr": 13.2, "retention_rate": 63},
            ],
            [],
        ),
    ],
)
def test_valid_clickbait(data, expected):
    result = clickbait_report(data)
    assert result == expected
