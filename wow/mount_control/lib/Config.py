from basic_view import basic_view_show_message
import json


class Config:
    def __init__(self):
        try:
            with open("mount_control/config.json", "r") as file:
                self.data = json.load(file)
        except:
            basic_view_show_message(
                "Mount control", "Cannot find a configuration file", 2
            )
            raise Exception("Cannot find a configuration file")
