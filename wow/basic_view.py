import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
    QMessageBox,
    QDialog,
    QLineEdit,
    QLabel,
    QHBoxLayout,
)


def basic_view(
    title, mosaic, width_ratios, height_ratios, show_toolbar=True, maximize=True
):
    plt.ion()
    plt.switch_backend("qtagg")
    fig, ax = plt.subplot_mosaic(
        constrained_layout=True,
        mosaic=mosaic,
        empty_sentinel=None,
        width_ratios=width_ratios,
        height_ratios=height_ratios,
    )
    fig.canvas.manager.set_window_title(title=title)

    mng = plt.get_current_fig_manager()
    mng.window.setWindowTitle(title)

    if not maximize:
        print("ciao")
        # root = tk.Tk()
        # screen_width = root.winfo_screenwidth()
        # screen_height = root.winfo_screenheight()
        # root.withdraw()
        # window_width, window_height = 800, 600
        # x_pos = (screen_width // 2) - (window_width // 2)
        # y_pos = (screen_height // 2) - (window_height // 2)
        # mng.window.setGeometry(x_pos, y_pos, window_width, window_height)
    else:
        mng.window.showMaximized()

    unwanted_buttons = []
    for x in mng.toolbar.actions():
        if (x.text() in unwanted_buttons) or not show_toolbar:
            mng.toolbar.removeAction(x)

    return fig, ax


def basic_view_show_message(title, message, icon):
    class MainWindow(QWidget):
        def __init__(self):
            super().__init__()
            msg_box = QMessageBox()
            msg_box.setWindowTitle(title)
            msg_box.setText(message)
            msg_box.setIcon(icon)
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

    window = MainWindow()
    window.show()


def basic_view_file_dialog():
    class FileDialogView(QWidget):
        def __init__(self):
            super().__init__()

            self.selected_file = None
            self.setWindowTitle("Select a file")
            self.setGeometry(500, 500, 200, 100)

            layout = QVBoxLayout()
            self.button = QPushButton("Open File", self)
            self.button.clicked.connect(self.show_file_dialog)
            layout.addWidget(self.button)

            self.setLayout(layout)

        def show_file_dialog(self):
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(
                self,
                "Open File",
                "",
                "All Files (*);;csv Files (*.csv)",
                options=options,
            )

            self.selected_file = file_name
            self.close()

    window = FileDialogView()
    window.show()
    return window.selected_file


def basic_view_text_input(title, message):
    class TextInputDialogView(QDialog):
        def __init__(self, title=title, label_text=message):
            super().__init__()

            self.setWindowTitle(title)
            self.setGeometry(500, 500, 500, 100)

            layout = QVBoxLayout()
            h_layout = QHBoxLayout()

            self.label = QLabel(label_text, self)  # Add your custom text here
            h_layout.addWidget(self.label)

            self.text_input = QLineEdit(self)
            h_layout.addWidget(self.text_input)

            layout.addLayout(h_layout)

            self.ok_button = QPushButton("OK", self)
            self.ok_button.clicked.connect(self.on_ok_clicked)
            layout.addWidget(self.ok_button)

            self.setLayout(layout)

            layout.setSpacing(10)  # Adjust the vertical spacing if needed
            layout.addStretch()  # Add stretchable space at the bottom

        def on_ok_clicked(self):
            self.entered_text = self.text_input.text()
            self.accept()

        def get_text(self):
            if self.exec_() == QDialog.Accepted:
                return self.entered_text
            return None

    dialog = TextInputDialogView()
    input_text = dialog.get_text()
    return input_text
