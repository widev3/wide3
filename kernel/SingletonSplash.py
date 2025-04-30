from PyQt6.QtGui import QPixmap, QMovie
from PyQt6.QtCore import QCoreApplication, Qt
from PyQt6.QtWidgets import QSplashScreen, QWidget


class SingletonSplash(QSplashScreen):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonSplash, cls).__new__(cls)
        return cls._instance

    def __init__(self, file: str = None, width: int = 100, height: int = 100):
        if file:
            self.__movie = QMovie(file)
            pixmap = QPixmap(self.__movie.frameRect().size())
            self.__splash = QSplashScreen(pixmap)
            self.__movie.frameChanged.connect(
                lambda x: self.__splash.setPixmap(
                    self.__movie.currentPixmap().scaled(
                        width,
                        height,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation,
                    )
                )
            )
            self.__movie.jumpToFrame(0)
            self.__movie.start()
            self.__splash.show()

    def message(self, mess: str):
        self.__splash.showMessage(mess)
        QCoreApplication.processEvents()

    def finish(self, win: QWidget):
        self.__splash.finish(win)
