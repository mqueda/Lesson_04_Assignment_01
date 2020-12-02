"""
Module for implementing the main file
"""
import logging
import logging.config
from argparse import ArgumentParser
import yaml
from signal_interpreter_server.routes import signal_interpreter_app, jsonparser


# Remeber to set the parameter " --file_path ..\signal_database.json "


with open(r"cfg\logger_configuration.yaml", "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logger = logging.getLogger(__name__)


def get_arguments():
    """
    Action : Load the specified arguments.
    Expected Results : Proper arguments load.
    Returns: parser.parse_args().
    """
    parser = ArgumentParser()
    parser.add_argument('--file_path', required=True)
    logging.debug("Using JSON from file : %s", parser.parse_args().file_path)
    return parser.parse_args()


def main():
    """
    Action : Start the server application.
    Expected Results : Proper file load.
    Returns: N/A.
    """
    try:
        args = get_arguments()
        jsonparser.load_file(args.file_path)
        logging.info("!!!!! Starting the Server !!!!!")
        signal_interpreter_app.run()
    except AttributeError as err:
        logging.error("ExceptionMLQ %s occurred", AttributeError)
        raise AttributeError from err


def init():
    """
    Sets the init values
    """
    if __name__ == '__main__':
        main()


init()
