import pytest
import reports  #!!!Регистрирует отчеты!!!
from config import get_report


@pytest.mark.parametrize("report_name", [("clickbait")])
def test_valid_report_registreated(report_name):
    result = get_report(report_name)
    assert result


@pytest.mark.parametrize("report_name", [("rate")])
def test_invalid_report_registreated(report_name):
    with pytest.raises(ValueError):
        get_report(report_name)
