from PySide6.QtGui import QPixmap
from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtWidgets import QWidget, QDialog, QLabel, QVBoxLayout, QHBoxLayout


class SingletonSplash(QDialog):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonSplash, cls).__new__(cls)
        return cls._instance

    def __init__(self, file: str | None = None, w=400, h=400, parent=None):
        if hasattr(self, "_initialized") and self._initialized:
            return
        super().__init__(parent)

        self._initialized = True
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowState(Qt.WindowMaximized)

        pixmap = QPixmap(file).scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label = QLabel()
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("background: transparent;")

        self.text_label = QLabel("Loading, please wait...")
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setStyleSheet("background: transparent;")

        self.container = QWidget()
        self.container.setFixedSize(pixmap.width(), pixmap.height() + 30)
        self.container.setStyleSheet("background: transparent;")

        inner_layout = QVBoxLayout()
        inner_layout.addWidget(self.image_label)
        inner_layout.addWidget(self.text_label)
        inner_layout.setContentsMargins(0, 0, 0, 0)
        inner_layout.setAlignment(Qt.AlignCenter)
        self.container.setLayout(inner_layout)

        outer_layout = QVBoxLayout()
        outer_layout.addStretch()
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.container)
        hbox.addStretch()
        outer_layout.addLayout(hbox)
        outer_layout.addStretch()
        outer_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(outer_layout)

        self.show()

    def message(self, mess: str):
        self.text_label.setText(mess)
        QCoreApplication.processEvents()
