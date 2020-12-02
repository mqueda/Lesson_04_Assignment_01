# exceptions.py


class JsonParserError_KeyError(Exception):
    """
    Class for the jason_parser KeyError exceptions.
    """
    def __init__(self, msg=''):
        Exception.__init__(self, "!!!!! Invalid data received !!!!!\n"
                                 "%s" % msg)


class JsonParserError_FileNotFoundError(Exception):
    """
    Class for the jason_parser KeyError exceptions.
    """
    def __init__(self, msg=''):
        Exception.__init__(self, "!!!!! Invalid file in '--file_path !!!!!\n"
                                 "%s" % msg)


class JsonParserError_DecodeError(Exception):
    """
    Class for the jason_parser KeyError exceptions.
    """
    def __init__(self, msg=''):
        Exception.__init__(self, "!!!!! Invalid JSON format file !!!!!\n"
                                 "%s" % msg)
