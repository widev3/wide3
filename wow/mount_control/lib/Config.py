from basic_view import basic_view_show_message


class Config:
    def __init__(self, config=None):
        if config:
            self.data = config
        else:
            basic_view_show_message("Mount control", "Cannot find a configuration file")
            raise Exception("Cannot find a configuration file")
