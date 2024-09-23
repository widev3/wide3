import json


class Config:
    def __default_config(self):
        self.data["filename"] = "Spectrogram.csv"
        self.data["separator"] = ","
        self.data["gamma"] = 0.2
        self.data["cmap"] = "ocean"
        self.data["bands"]["A"] = [10, 12]

    def __init__(self):
        config = "config.json"
        try:
            with open(config, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.__default_config()
            print(f"File {config} not found. Fallback to default config")
            print(self.data)
        except json.JSONDecodeError:
            self.__default_config()
            print("Error decoding JSON. Fallback to default config")
            print(self.data)
