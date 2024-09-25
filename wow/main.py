import importlib
from Config import Config


if __name__ == "__main__":
    config = Config()
    startup = ""
    if "startup" in config.data:
        startup = config.data["startup"]

    if startup:
        module = importlib.import_module(f"{startup}.view.view")
        function = getattr(module, "view")
        function(config.data[startup] if startup in config.data else None)
    else:
        print("open all")
