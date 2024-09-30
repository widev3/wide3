import importlib
import os
import json
from os.path import dirname
from Config import Config
from basic_view import basic_view, plt, basic_view_text_input
from matplotlib.widgets import Button


def start_a_module(startup, config):
    module = importlib.import_module(f"{startup}.view.view")
    function = getattr(module, "view")
    function(config.data[startup] if startup in config.data else None)


if __name__ == "__main__":
    config = Config()
    startup = ""
    if "startup" in config.data:
        startup = config.data["startup"]

    if startup:
        start_a_module(startup, config)
    else:
        folders = list(
            filter(
                lambda x: not x.startswith("__"), next(os.walk(dirname(__file__)))[1]
            )
        )

        side = int(len(folders) ** (1 / 2)) + 1
        mosaic = [[None for _ in range(side)] for _ in range(side)]
        index = 0
        folders_config = {}
        for i in range(side):
            for j in range(side):
                if index < len(folders):
                    folder = folders[index]
                    mosaic[i][j] = folder
                    index += 1
                    with open(f"{folder}/config.json", "r") as file:
                        folders_config[folder] = json.load(file)

        fig, ax = basic_view(
            "wow",
            mosaic,
            [1 for _ in range(side)],
            [1 for _ in range(side)],
            show_toolbar=False,
            maximize=False,
        )

        buttons = []
        for folder_config in folders_config:
            button = Button(ax[folder_config], folders_config[folder_config]["name"])
            button.on_clicked(lambda x: start_a_module(x.inaxes.get_label(), config))
            buttons.append(button)

        plt.show(block=True)
