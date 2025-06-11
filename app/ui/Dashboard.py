# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(968, 625)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabView = QWidget()
        self.tabView.setObjectName("tabView")
        self.gridLayout_2 = QGridLayout(self.tabView)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QFrame(self.tabView)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setObjectName("tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.tabView)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonRefresh = QPushButton(self.frame_2)
        self.pushButtonRefresh.setObjectName("pushButtonRefresh")
        self.pushButtonRefresh.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButtonRefresh)

        self.pushButtonFileOpen = QPushButton(self.frame_2)
        self.pushButtonFileOpen.setObjectName("pushButtonFileOpen")
        self.pushButtonFileOpen.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButtonFileOpen)

        self.pushButtonSettings = QPushButton(self.frame_2)
        self.pushButtonSettings.setObjectName("pushButtonSettings")
        self.pushButtonSettings.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButtonSettings)

        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1, Qt.AlignLeft)

        self.tabWidget.addTab(self.tabView, "")
        self.tabPositioning = QWidget()
        self.tabPositioning.setObjectName("tabPositioning")
        self.tabWidget.addTab(self.tabPositioning, "")
        self.tabAcquisition = QWidget()
        self.tabAcquisition.setObjectName("tabAcquisition")
        self.tabWidget.addTab(self.tabAcquisition, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName("label")

        self.horizontalLayout_2.addWidget(self.label)

        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(-1)

        self.horizontalLayout_2.addWidget(self.progressBar)

        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "Whistle Of Wind", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabView),
            QCoreApplication.translate("Dialog", "View", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabPositioning),
            QCoreApplication.translate("Dialog", "Positioning", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabAcquisition),
            QCoreApplication.translate("Dialog", "Acquisition", None),
        )
        self.label.setText("")

    # retranslateUi
