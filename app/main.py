import sys

sys.dont_write_bytecode = True

from os import path
from PySide6.QtWidgets import QApplication
from kernel.SingletonSplash import SingletonSplash


def abs_path(filename):
    return path.abspath(path.join(path.dirname(__file__), filename))


app = QApplication(sys.argv)
SingletonSplash(abs_path("icons/whistle_of_wind.png"))
SingletonSplash().message("Loading...")

import Config
from kernel.QtMger import WindowManager
from cwd.Dashboard import Ui_Dialog
from ux.Dashboard import Dashboard

if __name__ == "__main__":
    SingletonSplash().message("Starting...")
    Config.Config("config.json")
    c = Config.Config().instance().config
    win = WindowManager(Ui_Dialog, Dashboard, c)
    win.show()
    SingletonSplash().finish(win)
    sys.exit(app.exec())
