import csv
import kernel
from enum import IntEnum, Enum
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QCheckBox
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QTableWidget
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QIcon


class QTWQPB(object):
    """QTableWidgetQPushButton"""

    def __init__(self, tooltip: str, icon: IntEnum, connect, parent):
        self.tooltip = tooltip
        self.icon = icon
        self.connect = connect
        self.parent = parent

    def get_qwidget(self, row):
        layout = QHBoxLayout()
        button = QPushButton()
        button.setIcon(self.parent.dialog.style().standardIcon(self.icon))
        button.setToolTip(self.tooltip)
        button.setFixedSize(35, 35)
        button.clicked.connect(lambda: self.connect(row))
        layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
        qwidget = QWidget()
        qwidget.setLayout(layout)
        return qwidget


class QTW(object):
    """QTableWidget"""

    def set_data(qtw: QTableWidget, data, action=None):
        qtw.setAlternatingRowColors(True)
        cc = qtw.columnCount()
        for i in reversed(range(cc)):
            qtw.removeColumn(i)

        data_columns = {}
        if len(data) > 0:
            for col in data[0]:
                col_idx = qtw.columnCount()
                data_columns[col] = col_idx
                qtw.insertColumn(col_idx)
                qtw.setHorizontalHeaderItem(col_idx, QTableWidgetItem(col))

        rc = qtw.rowCount()
        for i in reversed(range(rc)):
            qtw.removeRow(i)

        for row in data:
            row_idx = qtw.rowCount()
            qtw.insertRow(row_idx)
            for col in row:
                qtw.setItem(
                    row_idx,
                    data_columns[col],
                    QTableWidgetItem(str(row[col])),
                )
            if action:
                action(row_idx, row, qtw)

        qtw.resizeColumnsToContents()
        qtw.resizeRowsToContents()

    def add_data(qtw: QTableWidget, data):
        for row in data:
            row_idx = qtw.rowCount()
            qtw.insertRow(row_idx)
            for col in row:
                qtw.setItem(
                    row_idx,
                    QTW.all_cols(qtw, col),
                    QTableWidgetItem(str(row[col])),
                )

        qtw.resizeColumnsToContents()
        qtw.resizeRowsToContents()

    def add_qtwqpb(qtw: QTableWidget, qtwqpb, col_idx: int = None):
        if not col_idx:
            col_idx = qtw.columnCount()

        qtw.insertColumn(col_idx)
        qtw.setHorizontalHeaderItem(col_idx, QTableWidgetItem(qtwqpb.tooltip))
        for row_idx in range(qtw.rowCount()):
            qtw.setCellWidget(row_idx, col_idx, qtwqpb.get_qwidget(row_idx))

        qtw.resizeColumnsToContents()
        qtw.resizeRowsToContents()

    def add_checkbox(qtw: QTableWidget, title, col_idx: int = None):
        if col_idx is None:
            col_idx = qtw.columnCount()

        qtw.insertColumn(col_idx)
        qtw.setHorizontalHeaderItem(col_idx, QTableWidgetItem(title))
        for row in range(qtw.rowCount()):
            layout = QHBoxLayout()
            button = QCheckBox()
            layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
            qwidget = QWidget()
            qwidget.setLayout(layout)
            qtw.setCellWidget(row, col_idx, qwidget)

        qtw.resizeColumnsToContents()
        qtw.resizeRowsToContents()

    def get_checked_rows(qtw: QTableWidget, title):
        idx = QTW.all_cols(qtw, title)
        if idx is None:
            return None

        rows = []
        for row in range(qtw.rowCount()):
            if qtw.cellWidget(row, idx).findChild(QCheckBox).isChecked():
                rows.append(row)

        return rows

    def to_csv(qtw: QTableWidget, filename):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for row in range(qtw.rowCount()):
                row_data = [
                    qtw.item(row, col).text() if qtw.item(row, col) else ""
                    for col in range(qtw.columnCount())
                ]
                writer.writerow(row_data)

    def all_cols(qtw: QTableWidget, col_name: str = None):
        headers_dict = dict(
            map(
                lambda x: (qtw.horizontalHeaderItem(x).text(), x),
                range(qtw.columnCount()),
            )
        )

        if col_name is None:
            return headers_dict

        if col_name in headers_dict.keys():
            return headers_dict[col_name]

        return None


class WindowManager(QDialog):
    def __init__(self, ui, ux=None, args=None, parent=None):
        super().__init__(parent)
        self.ui = ui()
        self.ui.setupUi(self)

        if ux:
            self.ux = ux(self.ui, self, args)

    def closeEvent(self, event):
        if hasattr(self, "on_close"):
            self.on_close()
        event.accept()


class icon_types(Enum):
    REFRESH = 1
    SETTINGS = 2
    FILE_OPEN = 3
    CHECK = 4
    ADD_LINK = 5
    LINK_OFF = 6
    INFO = 7
    ADJUST = 8
    ARROW_RANGE = 9
    ARROW_MENU_CLOSE = 10
    ARROW_MENU_OPEN = 11
    CADENCE = 12
    CAMERA = 13
    NOTE_STACK = 14
    WAVES = 15
    AV_TIMER = 16
    HOURGLASS = 17
    LOCAL_PIZZA = 18


def get_icon_path(i_type: icon_types) -> str | None:
    icon_path = kernel.__path__._path[0] + "/icons/"
    icon_dict = {
        icon_types.REFRESH: "refresh_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.SETTINGS: "settings_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.FILE_OPEN: "file_open_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.CHECK: "check_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.ADD_LINK: "add_link_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.LINK_OFF: "link_off_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.INFO: "info_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.ADJUST: "adjust_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.ARROW_RANGE: "arrow_range_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.ARROW_MENU_CLOSE: "arrow_menu_close_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.ARROW_MENU_OPEN: "arrow_menu_open_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.CADENCE: "cadence_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.CAMERA: "camera_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.NOTE_STACK: "note_stack_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.WAVES: "waves_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.AV_TIMER: "av_timer_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.HOURGLASS: "hourglass_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
        icon_types.LOCAL_PIZZA: "local_pizza_128dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.png",
    }

    if i_type in icon_dict:
        return icon_path + icon_dict[i_type]

    return None


def get_icon(i_type: icon_types, size: tuple | None = None) -> QIcon | None:
    icon_path = get_icon_path(i_type)
    icon = QIcon()
    size = QSize(size[0], size[1]) if size else QSize()
    icon.addFile(icon_path, size, QIcon.Mode.Normal, QIcon.State.Off)

    return icon


def set_icon(ui_component, i_type: icon_types, size: tuple | None = None):
    if hasattr(ui_component, "setIcon"):
        ui_component.setIcon(get_icon(i_type))
    elif hasattr(ui_component, "setPicture"):
        icon_path = get_icon_path(i_type)
        pixmap = QPixmap(icon_path)
        if size:
            pixmap = pixmap.scaled(
                size[0],
                size[1],
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        ui_component.setPixmap(pixmap)


def remove_widgets(layout):
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().deleteLater()
