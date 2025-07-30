from single_include import QLabel, QVBoxLayout, Qt, QTimer, QPixmap


class UXPopupDialog(object):
    def __init__(self, ui, dialog, args=None):
        self.ui = ui
        self.dialog = dialog
        self.dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        duration = 1200

        if args:
            if "text" in args:
                self.ui.label.setText(args["text"])

            icon_pixmap = None
            frame_layout = QVBoxLayout(self.ui.frame)
            self.ui.frame.setLayout(frame_layout)
            icon_label = QLabel(self.ui.frame)
            icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            if "icon" in args:
                icon_pixmap = self.ui.frame.style().standardPixmap(args["icon"])
            elif "image" in args:
                icon_pixmap = QPixmap(args["image"])

            if icon_pixmap:
                icon_pixmap = icon_pixmap.scaled(
                    64,
                    64,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
                icon_label.setPixmap(icon_pixmap)
                frame_layout.addWidget(icon_label)

            if "duration" in args:
                duration = float(args["duration"])

        QTimer.singleShot(duration, self.dialog.close)
