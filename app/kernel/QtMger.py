import csv
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Qt
from enum import IntEnum, Enum
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QTableWidget
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QCheckBox


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
    def __init__(self, ui, bh=None, args=None, parent=None):
        super().__init__(parent)
        self.ui = ui()
        self.ui.setupUi(self)

        if bh:
            self.bh = bh(self.ui, self, args)

    def closeEvent(self, event):
        if hasattr(self, "on_close"):
            self.on_close()
        event.accept()
