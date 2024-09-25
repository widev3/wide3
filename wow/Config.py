import json


class Config:
    def __default_config(self):
        self.data = {}

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
