import os
import matplotlib

matplotlib.use("qtagg")
import matplotlib.pyplot as plt
import PackageViewer

from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from matplotlib.widgets import Button, CheckButtons, RadioButtons, Slider, TextBox
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
from matplotlib.image import AxesImage
from matplotlib import cm
from matplotlib.backend_bases import MouseButton
from matplotlib.ticker import AutoMinorLocator

from PyQt6.QtWidgets import (
    QPushButton,
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
    QTableWidget,
    QTableWidgetItem,
    QFileDialog,
    QHeaderView,
)


app = QApplication([])


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


def buttons_frame(s, ax, current_package):
    s.__buttons_frame = {}
    for package, view in PackageViewer.PackageViewer().instance().packages.items():
        if view._View__conf["package"] in ax:
            s.__buttons_frame[package] = Button(
                ax=ax[view._View__conf["package"]], label=view._View__conf["name"]
            )
            if view._View__conf["package"] == current_package:
                s.__buttons_frame[package].on_clicked(lambda event: None)
                s.__buttons_frame[package].color = "gray"
                s.__buttons_frame[package].hovercolor = "gray"
            else:
                s.__buttons_frame[package].on_clicked(
                    lambda event: PackageViewer.PackageViewer()
                    .instance()
                    .packages[event.inaxes._label]
                    .view()
                )


def create(title, mosaic, icon, unwanted_buttons=[], size=None):
    plt.ion()
    fig, ax = plt.subplot_mosaic(
        mosaic=mosaic,
        empty_sentinel=None,
        width_ratios=[1] * len(mosaic[0]),
        height_ratios=[1] * len(mosaic),
    )

    plt.subplots_adjust(
        left=0.03,
        bottom=0.05,
        right=0.98,
        top=0.98,
        wspace=1,
        hspace=1,
    )

    set_title(fig=fig, title=title)
    mng = plt.get_current_fig_manager()

    if size:
        mng.window.resize(*size)
    else:
        mng.window.showMaximized()

    mng.window.setWindowIcon(QtGui.QIcon(icon))

    for x in mng.toolbar.actions():
        if (unwanted_buttons is None) or (x.text() in unwanted_buttons):
            mng.toolbar.removeAction(x)

    return fig, ax


def set_title(fig, title=None, subtitles=[]):
    if not title:
        title = fig.canvas.manager.get_window_title().split(" - ", 1)[0]

    if not title and not subtitles:
        return

    title = title + (" - " + " - ".join(subtitles) if subtitles else "")
    mng = plt.get_current_fig_manager()
    mng.window.setWindowTitle(title)


def show():
    plt.show(block=True)


def refresh():
    plt.show(block=False)


def connect(string, event):
    plt.connect(string, event)


def show_message(title, message, icon):
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

    class MainWindow(QDialog):
        def __init__(self):
            super().__init__()
            msg_box = QMessageBox()
            msg_box.setWindowTitle(title)
            msg_box.resize(800, 600)
            msg_box.setText(message)
            msg_box.setIcon(icon)
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

    window = MainWindow()


def file_dialog(title, message, filter):
    class TextInputDialogView(QDialog):
        def __init__(self, title, message, filter):
            super().__init__()
            self.setWindowTitle(title)
            self.resize(800, 600)

            layout = QVBoxLayout()
            self.btn = QPushButton(message)
            self.btn.clicked.connect(self.get_file)
            layout.addWidget(self.btn)

            self.setLayout(layout)

        def get_file(self):
            file = QFileDialog.getOpenFileName(
                self,
                caption=message,
                directory=os.path.abspath(os.getcwd()),
                filter=filter,
            )

            self.accept()
            return file[0]

    dialog = TextInputDialogView(title, message, filter)
    dialog.show()
    input_text = dialog.get_file()
    return input_text


def text_input(title, message):
    class TextInputDialogView(QDialog):
        def __init__(self, title, message):
            super().__init__()
            self.setWindowTitle(title)
            self.resize(800, 600)

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
    dialog.show()
    input_text = dialog.get_text()
    return input_text


def checkbox_list(title, message, items_key, items_value, single):
    class CheckBoxListDialog(QDialog):
        def __init__(self, title, message, items_key, items_value, single):
            super().__init__()
            self.setWindowTitle(title)
            self.resize(800, 600)

            self.label = QLabel(message, self)

            layout = QVBoxLayout()
            layout.addWidget(self.label)

            self.list_widget = QListWidget()
            for item in items_value:
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

            self.selected_items_value = []
            self.selected_indices = []
            self.selected_items_key = []

        def on_ok_button_clicked(self):
            selected_items = []
            selected_indices = []
            for index in range(self.list_widget.count()):
                item = self.list_widget.item(index)
                checkbox = self.list_widget.itemWidget(item)
                if checkbox.isChecked():
                    selected_items.append(checkbox.text())
                    selected_indices.append(index)

            self.selected_items_value = selected_items
            self.selected_indices = selected_indices
            self.selected_items_key = list(
                map(lambda x: items_key[x], self.selected_indices)
            )

            if single:
                self.selected_items_value = self.selected_items_value[0]
                self.selected_indices = self.selected_indices[0]
                self.selected_items_key = self.selected_items_key[0]

            self.accept()

        def on_cancel_button_clicked(self):
            self.reject()

    dialog = CheckBoxListDialog(title, message, items_key, items_value, single)
    dialog.show()
    dialog.exec_()
    return (
        dialog.selected_items_value,
        dialog.selected_indices,
        dialog.selected_items_key,
    )


def table(title, dataframe):
    class TablePopup(QDialog):
        def __init__(self, title, dataframe):
            super().__init__()
            self.setWindowTitle(title)
            self.resize(800, 600)

            layout = QVBoxLayout()
            self.setLayout(layout)

            table = QTableWidget(self)
            table.setRowCount(dataframe.shape[0])
            table.setColumnCount(dataframe.shape[1])
            table.setHorizontalHeaderLabels(dataframe.columns)

            for row_idx in range(dataframe.shape[0]):
                for col_idx in range(dataframe.shape[1]):
                    cell_value = str(dataframe.iat[row_idx, col_idx])
                    table.setItem(row_idx, col_idx, QTableWidgetItem(cell_value))

            header = table.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)

            layout.addWidget(table)

            close_btn = QPushButton("Close")
            close_btn.clicked.connect(self.close)
            layout.addWidget(close_btn)

    popup = TablePopup(title=title, dataframe=dataframe)
    popup.exec_()


def generate_array(x, y, element=None):
    return [[element for _ in range(x)] for _ in range(y)]


def fill_with_string(array, start, end, string, pad=(0, 0)):
    start_x, start_y = start[0] - 1 + pad[0], start[1] - 1 + pad[1]
    end_x, end_y = end[0] - 1, end[1] - 1
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            array[y][x] = string


def fill_row_with_array(array, start, end, fill, pad=(0, 0)):
    start_x, start_y = start[0] - 1 + pad[0], start[1] - 1 + pad[1]
    end_x, end_y = end[0] - 1, end[1] - 1
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            index = int((x - start_x) / int((end_x - start_x + 1) / len(fill)))
            if len(fill) > index:
                array[y][x] = fill[index]


def fill_col_with_array(array, start, end, fill, pad=(0, 0)):
    start_x, start_y = start[0] - 1 + pad[0], start[1] - 1 + pad[1]
    end_x, end_y = end[0] - 1, end[1] - 1
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            index = int((y - start_y) / int((end_y - start_y + 1) / len(fill)))
            if len(fill) > index:
                array[y][x] = fill[index]


def cla_leaving_attributes(axes):
    title = axes.get_title()
    x_label = axes.get_xlabel()
    y_label = axes.get_ylabel()
    axes.cla()
    axes.set_title(title)
    axes.set_xlabel(x_label)
    axes.set_ylabel(y_label)
