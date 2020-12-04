"""
Module for implementing the conftest file
"""
import os
import pytest
from signal_interpreter_server.json_parser import LoadAndParse


@pytest.fixture
def fixture_json_file_path():
    """
    Action : Return json file path.
    Expected Correct json file path returned.
    Returns: json file path.
    """
    test_basic_json_file = (os.path.join
                            (os.path.abspath(os.path.dirname(__file__)),
                             "fixtures\\test_basic.json"))
    return test_basic_json_file


@pytest.fixture(name="fixture_json_file")
def fixture_json_file_main():
    """
    Action : Return json file structure.
    Expected Correct json file structure returned.
    Returns: json file structure.
    """
    return {
                "services": [
                    {
                        "title": "ECU Reset",
                        "id": "11"
                    },
                    {
                        "title": "Security Access",
                        "id": "27"
                    }
                ]
            }


@pytest.fixture
def fixture_loadandparse_instance(fixture_json_file):
    """
    Action : LoadAndParce class instance.
    Expected Correct LoadAndParce class instance returned.
    Returns: LoadAndParce class instance.
    """
    load_and_parser = LoadAndParse()
    load_and_parser.data = fixture_json_file
    load_and_parser.title = None
    return load_and_parser
