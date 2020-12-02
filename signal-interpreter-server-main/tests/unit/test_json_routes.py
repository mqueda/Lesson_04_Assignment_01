"""
Module for implementing the unit tests
"""
from unittest.mock import patch, mock_open
import pytest
from signal_interpreter_server.json_parser import LoadAndParse, json


RAW_JSON_DATA = '{ "json" : "json reference!" }'
PROCESSED_JSON_DATA = {"json": "json reference!"}


def test_open_file():
    """
    Action : Test mocking json file open.
    Expected Results : No difference from normal application usage.
    Returns: N/A.
    """
    with patch("builtins.open", mock_open(read_data=RAW_JSON_DATA)):
        json_parser = LoadAndParse()
        json_parser.load_file("file/path")
        assert json_parser.data == PROCESSED_JSON_DATA


def test_file_load():
    """
    Action : Test mocking json file loading.
    Expected Results : No difference from normal application usage.
    Returns: N/A.
    """
    with patch(
            "builtins.open", mock_open(read_data=RAW_JSON_DATA))\
            as mock_file_object:
        with patch.object(
                json, "load", return_value=PROCESSED_JSON_DATA)\
                as mock_json_load:
            json_parser = LoadAndParse()
            json_parser.load_file("path/to/json/file")
            mock_json_load.assert_called_with(mock_file_object.return_value)
            assert json_parser.data == PROCESSED_JSON_DATA


def test_interpretation_01():
    """
    Action : Test mocking interpretation.
    Expected Results : No difference from normal application usage.
    Returns: N/A.
    """
    json_parser = LoadAndParse()
    json_parser.data = {"services": [{"title": "Security Access", "id": "27"}]}
    assert json_parser.return_signal_by_title("27") == "Security Access"


@pytest.mark.parametrize("reqid, expected_result",  [
    ("11", "ECU Reset"),
    ("27", "Security Access"),
    ("32.", "Service not suported!"),
    ("47", "Service not suported!"),
    ("", "Service not suported!"),
])
def test_interpretation_02(reqid, expected_result):
    """
    Action : Test mocking interpretation.
    Expected Results : No difference from normal application usage.
    Returns: N/A.
    """
    json_parser = LoadAndParse()
    json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"},
                                     {"title": "Security Access", "id": "27"}]}
    assert json_parser.return_signal_by_title(reqid) == expected_result
