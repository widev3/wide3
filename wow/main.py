import importlib
from Config import Config


if __name__ == "__main__":
    config = Config()
    app = ""
    if "app" in config.data:
        app = config.data["app"]

    if app:
        module = importlib.import_module(f"{app}.view.view")
        function = getattr(module, "view")
        function(config.data["args"] if "args" in config.data else None)
    else:
        print("open all")
