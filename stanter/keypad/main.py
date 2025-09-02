import sys

sys.dont_write_bytecode = True

from os import path
from PySide6.QtWidgets import QApplication
from despyner.SingletonSplash import SingletonSplash


def abs_path(filename, ref_position=__file__):
    return path.abspath(path.join(path.dirname(ref_position), filename))


app = QApplication(sys.argv)
SingletonSplash(abs_path("SOME_IMAGE_TO_DISPLAY", __file__))
SingletonSplash().message("Loading...")

from ux.Keypad import Keypad
from ui.Keypad import Ui_Dialog
from despyner.QtMger import WindowManager

if __name__ == "__main__":
    SingletonSplash().message("Starting...")
    win = WindowManager(Ui_Dialog, Keypad)
    win.show()
    SingletonSplash().close()
    sys.exit(app.exec())
