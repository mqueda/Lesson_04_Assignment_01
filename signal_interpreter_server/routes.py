"""
Module for implementing the routes
"""
import logging
from flask import Flask, request, jsonify, abort
from signal_interpreter_server.json_parser import LoadAndParse
from cfg.exceptions import JsonParserError_KeyError


signal_interpreter_app = Flask(__name__)
jsonparser = LoadAndParse()


logger = logging.getLogger(__name__)


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """
    Action : Make the received code interpretation.
    Expected Results : Proper code interpretation.
    Returns: jsonfy_data.
    """
    try:
        logging.info("Processing Request...")
        data = request.get_json()
        logging.debug('Requested Id : "%s"', data['service'])
        parsed_data = jsonparser.return_signal_by_title(data['service'])
        logging.debug('Answer : "%s"', parsed_data)
        jsonfy_data = jsonify(parsed_data)
        if jsonfy_data.json == "Service not suported!":
            logging.warning("The Requested Id is Not Avaiable")
            abort(503, description="Service Unavailable")
        logging.info("Sending data to client...")
        return (jsonfy_data), 201
    except Exception as err:
        logging.error("Exception %s occurred", str(err))
        raise JsonParserError_KeyError() from err


@signal_interpreter_app.errorhandler(500)
def internal_error(error):
    """
    Action : Log error if HTTP code 500 happens.
    Expected Results : Proper error logged.
    Returns: "Invalid data received!!!".
    """
    logging.info("Check the Data Sent !!!")
    return "Invalid data received!!!"
