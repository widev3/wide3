import importlib
import os
from os.path import dirname
from Config import Config
from basic_view import basic_view, plt


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
        folders = list(
            filter(
                lambda x: not x.startswith("__"), next(os.walk(dirname(__file__)))[1]
            )
        )

        side = int(len(folders) ** (1 / 2)) + 1
        mosaic = [[None for _ in range(side)] for _ in range(side)]
        index = 0
        for i in range(side):
            for j in range(side):
                if index < len(folders):
                    mosaic[i][j] = folders[index]
                    index += 1
        fig, ax = basic_view(
            "wow", mosaic, [1 for _ in range(side)], [1 for _ in range(side)]
        )
        plt.show(block=True)
