import json


class Config:
    def __default_config(self):
        self.data = {}
        self.data["filename"] = "Spectrogram.csv"
        self.data["separator"] = ","
        self.data["gamma"] = 0.3
        self.data["cmap"] = "magma"
        self.data["bands"] = {}
        self.data["bands"]["A"] = [10, 12]

    def __init__(self, config=None):
        if config:
            self.data = config
        else:
            self.__default_config()
