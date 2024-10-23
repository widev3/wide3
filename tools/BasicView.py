import sys
import matplotlib

matplotlib.use("qtagg")
import matplotlib.pyplot as plt
import matplotlib.text

from matplotlib.widgets import Button, CheckButtons, RadioButtons, Slider
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
from matplotlib.image import AxesImage
from matplotlib import cm
from matplotlib.backend_bases import MouseButton
from matplotlib.ticker import AutoMinorLocator

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
    QApplication,
    QListWidget,
    QListWidgetItem,
    QCheckBox,
    QRadioButton,
)


class BasicView:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BasicView, cls).__new__(cls)
        return cls._instance

    def __init__(self, custom_property=None):
        if not hasattr(self, "initialized"):
            self.__app = QApplication(sys.argv)
            self.initialized = True

    def exec_(self):
        return self.__app.exec_()

    @staticmethod
    def set_grid(ax):
        ax.grid(
            **{
                "visible": True,
                "linestyle": "--",
                "linewidth": 0.5,
                "alpha": 0.7,
                "color": "gray",
                "which": "both",
            }
        )
        ax.xaxis.set_minor_locator(AutoMinorLocator(5))
        ax.yaxis.set_minor_locator(AutoMinorLocator(5))

    @staticmethod
    def basic_view(title, mosaic, unwanted_buttons=[]):
        plt.ion()
        fig, ax = plt.subplot_mosaic(
            mosaic=mosaic,
            empty_sentinel=None,
            width_ratios=[1] * len(mosaic[0]),
            height_ratios=[1] * len(mosaic),
        )

        plt.subplots_adjust(
            left=0.08,
            bottom=0.08,
            right=0.96,
            top=0.96,
            wspace=1,
            hspace=1,
        )

        from PyQt5 import QtGui
        fig.canvas.manager.set_window_title(title=title)
        mng = plt.get_current_fig_manager()
        mng.window.setWindowIcon(QtGui.QIcon("settings_input_antenna_24dp_0000F5_FILL0_wght400_GRAD0_opsz24.ico"))
        mng.window.setWindowTitle(title)
        mng.resize(1500, 800)

        for x in mng.toolbar.actions():
            if x.text() in unwanted_buttons:
                mng.toolbar.removeAction(x)

        return fig, ax

    @staticmethod
    def show():
        plt.show(block=True)

    @staticmethod
    def refresh():
        plt.show()

    @staticmethod
    def connect(string, event):
        plt.connect(string, event)

    @staticmethod
    def basic_view_show_message(title, message, icon):
        """
        Instantiate a popup to show a message

        Parameters:
        title: The title of the popup
        message: The message you want to show
        icon:
            0: no icon
            1: information
            2: warning
            3: critical
            4: question
        """

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

    @staticmethod
    def basic_view_file_dialog(
        title, message, filter="All Files (*);;csv Files (*.csv)"
    ):
        class FileDialogView(QWidget):
            def __init__(self, title, message, filter):
                super().__init__()
                self.filter = filter

                self.selected_file = None
                self.setWindowTitle(title)
                self.setGeometry(500, 500, 500, 100)

                # layout = QVBoxLayout()
                # self.button = QPushButton(message, self)
                # self.button.clicked.connect(self.show_file_dialog)
                # layout.addWidget(self.button)

                # self.setLayout(layout)

                self.show_file_dialog()

            def show_file_dialog(self):
                options = QFileDialog.Options()
                file_name, _ = QFileDialog.getOpenFileName(
                    self,
                    "Open File",
                    "",
                    self.filter,
                    options=options,
                )

                self.selected_file = file_name
                self.close()

        dialog = FileDialogView(title, message, filter)
        dialog.show()
        # BasicView().exec_()
        return dialog.selected_file

    @staticmethod
    def basic_view_text_input(title, message):
        class TextInputDialogView(QDialog):
            def __init__(self, title, message):
                super().__init__()

                self.setWindowTitle(title)
                self.setGeometry(500, 500, 500, 100)

                layout = QVBoxLayout()
                h_layout = QHBoxLayout()

                self.label = QLabel(message, self)
                h_layout.addWidget(self.label)

                self.text_input = QLineEdit(self)
                h_layout.addWidget(self.text_input)

                layout.addLayout(h_layout)

                self.ok_button = QPushButton("OK", self)
                self.ok_button.clicked.connect(self.on_ok_clicked)
                layout.addWidget(self.ok_button)

                self.setLayout(layout)

                layout.setSpacing(10)
                layout.addStretch()

            def on_ok_clicked(self):
                self.entered_text = self.text_input.text()
                self.accept()

            def get_text(self):
                if self.exec_() == QDialog.Accepted:
                    return self.entered_text
                return None

        dialog = TextInputDialogView(title, message)
        input_text = dialog.get_text()
        return input_text

    @staticmethod
    def basic_view_checkbox_list(title, message, items, single=False):
        class CheckBoxListDialog(QDialog):
            def __init__(self, title, message, items, single):
                super().__init__()

                self.setWindowTitle(title)
                self.setGeometry(500, 500, 500, 500)

                self.label = QLabel(message, self)

                layout = QVBoxLayout()
                layout.addWidget(self.label)

                self.list_widget = QListWidget()
                for item in items:
                    list_item = QListWidgetItem()
                    if single:
                        checkbox = QRadioButton(item)
                    else:
                        checkbox = QCheckBox(item)
                        checkbox.setChecked(False)

                    list_item.setSizeHint(checkbox.sizeHint())
                    self.list_widget.addItem(list_item)
                    self.list_widget.setItemWidget(list_item, checkbox)

                layout.addWidget(self.list_widget)

                ok_button = QPushButton("OK")
                ok_button.clicked.connect(self.on_ok_button_clicked)

                cancel_button = QPushButton("Cancel")
                cancel_button.clicked.connect(self.on_cancel_button_clicked)

                button_layout = QHBoxLayout()
                button_layout.addWidget(ok_button)
                button_layout.addWidget(cancel_button)
                layout.addLayout(button_layout)

                self.setLayout(layout)

                self.selected_items = []
                self.selected_indices = []

            def on_ok_button_clicked(self):
                selected_items = []
                selected_indices = []
                for index in range(self.list_widget.count()):
                    item = self.list_widget.item(index)
                    checkbox = self.list_widget.itemWidget(item)
                    if checkbox.isChecked():
                        selected_items.append(checkbox.text())
                        selected_indices.append(index)

                self.selected_items = selected_items
                self.selected_indices = selected_indices
                if single:
                    self.selected_items = self.selected_items[0]
                    self.selected_indices = self.selected_indices[0]

                self.accept()

            def on_cancel_button_clicked(self):
                self.reject()

        dialog = CheckBoxListDialog(title, message, items, single)
        dialog.show()
        dialog.exec_()
        return dialog.selected_items, dialog.selected_indices


BasicView()
