import sys
import pytest
import reports  #!!!Регистрирует отчеты!!!
from utils import read_args


def test_read_args(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["prog", "--files", "test1.csv", "test2.csv", "--report", "clickbait"],
    )

    args = read_args()

    assert args.files == ["test1.csv", "test2.csv"]
    assert args.report == "clickbait"


@pytest.mark.parametrize(
    "data",
    [
        ["prog", "--files", "--report", "clickbait"],
        ["prog", "--files", "test1.csv", "test2.csv", "--report"],
        ["prog", "--report", "clickbait"],
        ["prog", "--files", "test1.csv", "test2.csv"],
        ["prog", "--files", "test1.csv", "test2.csv", "--report", "unknown"],
        ["prog"],
    ],
)
def test_invalid_read_args(monkeypatch, data):
    monkeypatch.setattr(sys, "argv", data)

    with pytest.raises(SystemExit):
        read_args()
