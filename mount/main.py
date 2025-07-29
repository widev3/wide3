import sys

sys.dont_write_bytecode = True

from os import path
from PySide6.QtWidgets import QApplication
from despyner.SingletonSplash import SingletonSplash


def abs_path(filename, ref_position=__file__):
    return path.abspath(path.join(path.dirname(ref_position), filename))


app = QApplication(sys.argv)
SingletonSplash(abs_path("whistle_of_wind.png", __file__))
SingletonSplash().message("Loading...")

from despyner.QtMger import WindowManager
from ui.Dashboard import Ui_Dialog
from ux.Dashboard.Dashboard import Dashboard

if __name__ == "__main__":
    SingletonSplash().message("Starting...")
    win = WindowManager(Ui_Dialog, Dashboard)
    win.show()
    SingletonSplash().close()
    sys.exit(app.exec())
