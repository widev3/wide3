from enum import Enum
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox


class MessageBox(QWidget):
    def __init__(self, text: str, title: str, icon: Enum, buttons):
        super().__init__()
        self.__text = text
        self.__title = title
        self.__icon = icon
        self.__buttons = buttons
        self.__msg = QMessageBox()
        self.__msg.setText(self.__text)
        self.__msg.setWindowTitle(self.__title)
        self.__msg.setIcon(self.__icon)
        self.__msg.setStandardButtons(self.__buttons)

    def result(self):
        self.__result = self.__msg.exec()
        return self.__result
