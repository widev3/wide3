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
    QLabel,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTabWidget,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(968, 625)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
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

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabView = QWidget()
        self.tabView.setObjectName("tabView")
        self.gridLayout_2 = QGridLayout(self.tabView)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frameButtons = QFrame(self.tabView)
        self.frameButtons.setObjectName("frameButtons")
        self.horizontalLayout = QHBoxLayout(self.frameButtons)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonConnect = QPushButton(self.frameButtons)
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.pushButtonConnect.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButtonConnect)

        self.pushButtonFileOpen = QPushButton(self.frameButtons)
        self.pushButtonFileOpen.setObjectName("pushButtonFileOpen")
        self.pushButtonFileOpen.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButtonFileOpen)

        self.pushButtonSettings = QPushButton(self.frameButtons)
        self.pushButtonSettings.setObjectName("pushButtonSettings")
        self.pushButtonSettings.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButtonSettings)

        self.pushButtonInfo = QPushButton(self.frameButtons)
        self.pushButtonInfo.setObjectName("pushButtonInfo")
        self.pushButtonInfo.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButtonInfo)

        self.gridLayout_2.addWidget(
            self.frameButtons,
            0,
            0,
            1,
            1,
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop,
        )

        self.framePlots = QFrame(self.tabView)
        self.framePlots.setObjectName("framePlots")
        self.framePlots.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePlots.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.framePlots)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frameSpec = QFrame(self.framePlots)
        self.frameSpec.setObjectName("frameSpec")
        self.frameSpec.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameSpec.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frameSpec)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.gridLayout_3.addWidget(self.frameSpec, 0, 0, 1, 1)

        self.frameFreq = QFrame(self.framePlots)
        self.frameFreq.setObjectName("frameFreq")
        self.frameFreq.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameFreq.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frameFreq)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_7.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.gridLayout_3.addWidget(self.frameFreq, 1, 0, 1, 1)

        self.frameTime = QFrame(self.framePlots)
        self.frameTime.setObjectName("frameTime")
        self.frameTime.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTime.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frameTime)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_5.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.gridLayout_3.addWidget(self.frameTime, 0, 1, 1, 1)

        self.frameSettings = QFrame(self.framePlots)
        self.frameSettings.setObjectName("frameSettings")
        self.frameSettings.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frameSettings)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalSpacer_4 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_6.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.gridLayout_3.addWidget(self.frameSettings, 1, 1, 1, 1)

        self.gridLayout_2.addWidget(self.framePlots, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tabView, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "Whistle Of Wind", None)
        )
        self.label.setText("")
        self.pushButtonInfo.setText("")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabView),
            QCoreApplication.translate("Dialog", "View", None),
        )

    # retranslateUi
