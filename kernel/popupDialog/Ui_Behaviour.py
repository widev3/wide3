from single_include import QLabel, QVBoxLayout, Qt, QTimer


class Ui_Behaviour(object):
    def __init__(self, ui, dialog, args=None):
        self.ui = ui
        self.dialog = dialog

        if args:
            if "text" in args:
                self.ui.label.setText(args["text"])

            if "icon" in args:
                frame_layout = QVBoxLayout(self.ui.frame)
                self.ui.frame.setLayout(frame_layout)

                icon_label = QLabel(self.ui.frame)
                icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

                icon_pixmap = self.ui.frame.style().standardPixmap(args["icon"])
                icon_pixmap = icon_pixmap.scaled(
                    32,
                    32,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
                icon_label.setPixmap(icon_pixmap)
                frame_layout.addWidget(icon_label)

            dur = 1200
            if "dur" in args:
                dur = float(args["dur"])

            QTimer.singleShot(dur, self.dialog.close)
