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
    QComboBox,
    QDialog,
    QDockWidget,
    QDoubleSpinBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSlider,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(1052, 1115)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush
        )
        brush1 = QBrush(QColor(36, 31, 49, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        brush2 = QBrush(QColor(54, 46, 73, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        brush3 = QBrush(QColor(45, 38, 61, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3
        )
        brush4 = QBrush(QColor(18, 15, 24, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        brush5 = QBrush(QColor(24, 21, 33, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush
        )
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush
        )
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush6)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush6)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush4
        )
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush7
        )
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush6
        )
        brush8 = QBrush(QColor(255, 255, 255, 127))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush8
        )
        # endif
        # if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush6)
        # endif
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush
        )
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1
        )
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3
        )
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush
        )
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush
        )
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush6)
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1
        )
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush6
        )
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush4
        )
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush7
        )
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush6
        )
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush8
        )
        # endif
        # if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush6
        )
        # endif
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4
        )
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1
        )
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3
        )
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush
        )
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4
        )
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1
        )
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush6
        )
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1
        )
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush7
        )
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush6
        )
        brush9 = QBrush(QColor(18, 15, 24, 127))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush9
        )
        # endif
        brush10 = QBrush(QColor(25, 22, 35, 255))
        brush10.setStyle(Qt.BrushStyle.SolidPattern)
        # if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush10
        )
        # endif
        Dialog.setPalette(palette)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setIconSize(QSize(25, 25))
        self.tabInstr = QWidget()
        self.tabInstr.setObjectName("tabInstr")
        self.gridLayout_8 = QGridLayout(self.tabInstr)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frameButtonsInstr = QFrame(self.tabInstr)
        self.frameButtonsInstr.setObjectName("frameButtonsInstr")
        self.horizontalLayout_2 = QHBoxLayout(self.frameButtonsInstr)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonConnect = QPushButton(self.frameButtonsInstr)
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.pushButtonConnect.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButtonConnect)

        self.pushButtonRecord = QPushButton(self.frameButtonsInstr)
        self.pushButtonRecord.setObjectName("pushButtonRecord")
        self.pushButtonRecord.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButtonRecord)

        self.gridLayout_8.addWidget(
            self.frameButtonsInstr,
            0,
            0,
            1,
            1,
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop,
        )

        self.framePlotsInstr = QFrame(self.tabInstr)
        self.framePlotsInstr.setObjectName("framePlotsInstr")
        self.framePlotsInstr.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePlotsInstr.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.framePlotsInstr)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.dockWidgetFreqInstr = QDockWidget(self.framePlotsInstr)
        self.dockWidgetFreqInstr.setObjectName("dockWidgetFreqInstr")
        self.dockWidgetFreqInstr.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetFloatable
            | QDockWidget.DockWidgetFeature.DockWidgetMovable
        )
        self.dockWidgetContentsFreqInstr = QWidget()
        self.dockWidgetContentsFreqInstr.setObjectName("dockWidgetContentsFreqInstr")
        self.gridLayout_10 = QGridLayout(self.dockWidgetContentsFreqInstr)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayoutFreqInstr = QVBoxLayout()
        self.verticalLayoutFreqInstr.setObjectName("verticalLayoutFreqInstr")

        self.gridLayout_10.addLayout(self.verticalLayoutFreqInstr, 0, 0, 1, 1)

        self.dockWidgetFreqInstr.setWidget(self.dockWidgetContentsFreqInstr)

        self.gridLayout_13.addWidget(self.dockWidgetFreqInstr, 0, 1, 1, 1)

        self.dockWidgetSpecInstr = QDockWidget(self.framePlotsInstr)
        self.dockWidgetSpecInstr.setObjectName("dockWidgetSpecInstr")
        self.dockWidgetSpecInstr.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetFloatable
            | QDockWidget.DockWidgetFeature.DockWidgetMovable
        )
        self.dockWidgetContentsSpecInstr = QWidget()
        self.dockWidgetContentsSpecInstr.setObjectName("dockWidgetContentsSpecInstr")
        self.gridLayout_12 = QGridLayout(self.dockWidgetContentsSpecInstr)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayoutSpecInstr = QVBoxLayout()
        self.verticalLayoutSpecInstr.setObjectName("verticalLayoutSpecInstr")

        self.gridLayout_12.addLayout(self.verticalLayoutSpecInstr, 0, 0, 1, 1)

        self.dockWidgetSpecInstr.setWidget(self.dockWidgetContentsSpecInstr)

        self.gridLayout_13.addWidget(self.dockWidgetSpecInstr, 0, 0, 1, 1)

        self.dockWidgetTimeInstr = QDockWidget(self.framePlotsInstr)
        self.dockWidgetTimeInstr.setObjectName("dockWidgetTimeInstr")
        self.dockWidgetTimeInstr.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetFloatable
            | QDockWidget.DockWidgetFeature.DockWidgetMovable
        )
        self.dockWidgetContentsTimeInstr = QWidget()
        self.dockWidgetContentsTimeInstr.setObjectName("dockWidgetContentsTimeInstr")
        self.gridLayout_9 = QGridLayout(self.dockWidgetContentsTimeInstr)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayoutTimeInstr = QVBoxLayout()
        self.verticalLayoutTimeInstr.setObjectName("verticalLayoutTimeInstr")

        self.gridLayout_9.addLayout(self.verticalLayoutTimeInstr, 0, 0, 1, 1)

        self.dockWidgetTimeInstr.setWidget(self.dockWidgetContentsTimeInstr)

        self.gridLayout_13.addWidget(self.dockWidgetTimeInstr, 1, 0, 1, 1)

        self.dockWidgetInstr = QDockWidget(self.framePlotsInstr)
        self.dockWidgetInstr.setObjectName("dockWidgetInstr")
        self.dockWidgetInstr.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetFloatable
            | QDockWidget.DockWidgetFeature.DockWidgetMovable
        )
        self.dockWidgetContentsInstr = QWidget()
        self.dockWidgetContentsInstr.setObjectName("dockWidgetContentsInstr")
        self.gridLayout_11 = QGridLayout(self.dockWidgetContentsInstr)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.scrollArea = QScrollArea(self.dockWidgetContentsInstr)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 445, 459))
        self.gridLayout_14 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.doubleSpinBoxSpan = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBoxSpan.setObjectName("doubleSpinBoxSpan")
        self.doubleSpinBoxSpan.setDecimals(0)
        self.doubleSpinBoxSpan.setMaximum(3000000000.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBoxSpan, 1, 1, 1, 1)

        self.labelStartTime = QLabel(self.scrollAreaWidgetContents)
        self.labelStartTime.setObjectName("labelStartTime")

        self.gridLayout_14.addWidget(self.labelStartTime, 6, 0, 1, 1)

        self.doubleSpinBoxCenter = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBoxCenter.setObjectName("doubleSpinBoxCenter")
        self.doubleSpinBoxCenter.setDecimals(0)
        self.doubleSpinBoxCenter.setMaximum(3000000000.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBoxCenter, 0, 1, 1, 1)

        self.labelSweep = QLabel(self.scrollAreaWidgetContents)
        self.labelSweep.setObjectName("labelSweep")

        self.gridLayout_14.addWidget(self.labelSweep, 4, 0, 1, 1)

        self.labelSpan = QLabel(self.scrollAreaWidgetContents)
        self.labelSpan.setObjectName("labelSpan")

        self.gridLayout_14.addWidget(self.labelSpan, 1, 0, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")

        self.gridLayout_14.addWidget(self.label_5, 10, 0, 1, 1)

        self.lineEditOptions = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditOptions.setObjectName("lineEditOptions")
        self.lineEditOptions.setReadOnly(True)

        self.gridLayout_14.addWidget(self.lineEditOptions, 12, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")

        self.gridLayout_14.addWidget(self.label_6, 11, 0, 1, 1)

        self.lineEditVisa = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditVisa.setObjectName("lineEditVisa")
        self.lineEditVisa.setReadOnly(True)

        self.gridLayout_14.addWidget(self.lineEditVisa, 10, 1, 1, 1)

        self.lineEditName = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditName.setReadOnly(True)

        self.gridLayout_14.addWidget(self.lineEditName, 11, 1, 1, 1)

        self.labelMax = QLabel(self.scrollAreaWidgetContents)
        self.labelMax.setObjectName("labelMax")

        self.gridLayout_14.addWidget(self.labelMax, 3, 0, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")

        self.gridLayout_14.addWidget(self.label_7, 12, 0, 1, 1)

        self.doubleSpinBoxMin = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBoxMin.setObjectName("doubleSpinBoxMin")
        self.doubleSpinBoxMin.setDecimals(0)
        self.doubleSpinBoxMin.setMaximum(3000000000.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBoxMin, 2, 1, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")

        self.gridLayout_14.addWidget(self.label_4, 9, 0, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")

        self.gridLayout_14.addWidget(self.label_13, 1, 2, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName("label_15")

        self.gridLayout_14.addWidget(self.label_15, 3, 2, 1, 1)

        self.doubleSpinBoxMax = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBoxMax.setObjectName("doubleSpinBoxMax")
        self.doubleSpinBoxMax.setDecimals(0)
        self.doubleSpinBoxMax.setMaximum(3000000000.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBoxMax, 3, 1, 1, 1)

        self.lineEditDriver = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditDriver.setObjectName("lineEditDriver")
        self.lineEditDriver.setReadOnly(True)

        self.gridLayout_14.addWidget(self.lineEditDriver, 9, 1, 1, 1)

        self.lineEditIDN = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditIDN.setObjectName("lineEditIDN")
        self.lineEditIDN.setReadOnly(True)

        self.gridLayout_14.addWidget(self.lineEditIDN, 8, 1, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")

        self.gridLayout_14.addWidget(self.label_3, 8, 0, 1, 1)

        self.labelOffsetsInstr = QLabel(self.scrollAreaWidgetContents)
        self.labelOffsetsInstr.setObjectName("labelOffsetsInstr")

        self.gridLayout_14.addWidget(self.labelOffsetsInstr, 5, 0, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")

        self.gridLayout_14.addWidget(self.label_8, 0, 2, 1, 1)

        self.doubleSpinBoxSweep = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBoxSweep.setObjectName("doubleSpinBoxSweep")
        self.doubleSpinBoxSweep.setDecimals(0)
        self.doubleSpinBoxSweep.setMaximum(3000000000.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBoxSweep, 4, 1, 1, 1)

        self.labelCenter = QLabel(self.scrollAreaWidgetContents)
        self.labelCenter.setObjectName("labelCenter")

        self.gridLayout_14.addWidget(self.labelCenter, 0, 0, 1, 1)

        self.lineEditStartTime = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditStartTime.setObjectName("lineEditStartTime")
        self.lineEditStartTime.setReadOnly(True)

        self.gridLayout_14.addWidget(self.lineEditStartTime, 6, 1, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName("label_14")

        self.gridLayout_14.addWidget(self.label_14, 2, 2, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")

        self.gridLayout_14.addWidget(self.label_16, 4, 2, 1, 1)

        self.comboBoxOffsetsInstr = QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxOffsetsInstr.setObjectName("comboBoxOffsetsInstr")

        self.gridLayout_14.addWidget(self.comboBoxOffsetsInstr, 5, 1, 1, 1)

        self.labelMin = QLabel(self.scrollAreaWidgetContents)
        self.labelMin.setObjectName("labelMin")

        self.gridLayout_14.addWidget(self.labelMin, 2, 0, 1, 1)

        self.labelSlices = QLabel(self.scrollAreaWidgetContents)
        self.labelSlices.setObjectName("labelSlices")

        self.gridLayout_14.addWidget(self.labelSlices, 7, 0, 1, 1)

        self.lineEditSlices = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditSlices.setObjectName("lineEditSlices")
        self.lineEditSlices.setReadOnly(True)

        self.gridLayout_14.addWidget(self.lineEditSlices, 7, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_11.addWidget(self.scrollArea, 1, 2, 1, 1)

        self.dockWidgetInstr.setWidget(self.dockWidgetContentsInstr)

        self.gridLayout_13.addWidget(self.dockWidgetInstr, 1, 1, 1, 1)

        self.gridLayout_8.addWidget(self.framePlotsInstr, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tabInstr, "")
        self.tabView = QWidget()
        self.tabView.setObjectName("tabView")
        self.gridLayout_2 = QGridLayout(self.tabView)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frameButtonsView = QFrame(self.tabView)
        self.frameButtonsView.setObjectName("frameButtonsView")
        self.horizontalLayout = QHBoxLayout(self.frameButtonsView)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonFileOpen = QPushButton(self.frameButtonsView)
        self.pushButtonFileOpen.setObjectName("pushButtonFileOpen")
        self.pushButtonFileOpen.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButtonFileOpen)

        self.gridLayout_2.addWidget(
            self.frameButtonsView,
            0,
            0,
            1,
            1,
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop,
        )

        self.framePlotsView = QFrame(self.tabView)
        self.framePlotsView.setObjectName("framePlotsView")
        self.framePlotsView.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePlotsView.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.framePlotsView)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.dockWidgetTime = QDockWidget(self.framePlotsView)
        self.dockWidgetTime.setObjectName("dockWidgetTime")
        self.dockWidgetTime.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetFloatable
            | QDockWidget.DockWidgetFeature.DockWidgetMovable
        )
        self.dockWidgetContentsTime = QWidget()
        self.dockWidgetContentsTime.setObjectName("dockWidgetContentsTime")
        self.gridLayout_7 = QGridLayout(self.dockWidgetContentsTime)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayoutTime = QVBoxLayout()
        self.verticalLayoutTime.setObjectName("verticalLayoutTime")

        self.gridLayout_7.addLayout(self.verticalLayoutTime, 0, 0, 1, 1)

        self.dockWidgetTime.setWidget(self.dockWidgetContentsTime)

        self.gridLayout_3.addWidget(self.dockWidgetTime, 1, 0, 1, 1)

        self.dockWidgetSpec = QDockWidget(self.framePlotsView)
        self.dockWidgetSpec.setObjectName("dockWidgetSpec")
        self.dockWidgetSpec.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetFloatable
            | QDockWidget.DockWidgetFeature.DockWidgetMovable
        )
        self.dockWidgetContentsSpec = QWidget()
        self.dockWidgetContentsSpec.setObjectName("dockWidgetContentsSpec")
        self.gridLayout_5 = QGridLayout(self.dockWidgetContentsSpec)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayoutSpec = QVBoxLayout()
        self.verticalLayoutSpec.setObjectName("verticalLayoutSpec")

        self.gridLayout_5.addLayout(self.verticalLayoutSpec, 0, 0, 1, 1)

        self.dockWidgetSpec.setWidget(self.dockWidgetContentsSpec)

        self.gridLayout_3.addWidget(self.dockWidgetSpec, 0, 0, 1, 1)

        self.dockWidgetFreq = QDockWidget(self.framePlotsView)
        self.dockWidgetFreq.setObjectName("dockWidgetFreq")
        self.dockWidgetFreq.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetFloatable
            | QDockWidget.DockWidgetFeature.DockWidgetMovable
        )
        self.dockWidgetContentsFreq = QWidget()
        self.dockWidgetContentsFreq.setObjectName("dockWidgetContentsFreq")
        self.gridLayout_6 = QGridLayout(self.dockWidgetContentsFreq)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayoutFreq = QVBoxLayout()
        self.verticalLayoutFreq.setObjectName("verticalLayoutFreq")

        self.gridLayout_6.addLayout(self.verticalLayoutFreq, 0, 0, 1, 1)

        self.dockWidgetFreq.setWidget(self.dockWidgetContentsFreq)

        self.gridLayout_3.addWidget(self.dockWidgetFreq, 0, 1, 1, 1)

        self.dockWidget = QDockWidget(self.framePlotsView)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidget.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetFloatable
            | QDockWidget.DockWidgetFeature.DockWidgetMovable
        )
        self.dockWidgetContentsView = QWidget()
        self.dockWidgetContentsView.setObjectName("dockWidgetContentsView")
        self.gridLayout_4 = QGridLayout(self.dockWidgetContentsView)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labelOffsetsView = QLabel(self.dockWidgetContentsView)
        self.labelOffsetsView.setObjectName("labelOffsetsView")

        self.gridLayout_4.addWidget(self.labelOffsetsView, 1, 0, 1, 1)

        self.horizontalSliderGammaView = QSlider(self.dockWidgetContentsView)
        self.horizontalSliderGammaView.setObjectName("horizontalSliderGammaView")
        self.horizontalSliderGammaView.setMaximum(1000)
        self.horizontalSliderGammaView.setSingleStep(1)
        self.horizontalSliderGammaView.setPageStep(50)
        self.horizontalSliderGammaView.setSliderPosition(500)
        self.horizontalSliderGammaView.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.horizontalSliderGammaView, 2, 2, 1, 1)

        self.labelFilename = QLabel(self.dockWidgetContentsView)
        self.labelFilename.setObjectName("labelFilename")

        self.gridLayout_4.addWidget(self.labelFilename, 3, 2, 1, 1)

        self.comboBoxOffsetsView = QComboBox(self.dockWidgetContentsView)
        self.comboBoxOffsetsView.setObjectName("comboBoxOffsetsView")

        self.gridLayout_4.addWidget(self.comboBoxOffsetsView, 1, 2, 1, 2)

        self.label_11 = QLabel(self.dockWidgetContentsView)
        self.label_11.setObjectName("label_11")

        self.gridLayout_4.addWidget(self.label_11, 5, 0, 1, 1)

        self.label_9 = QLabel(self.dockWidgetContentsView)
        self.label_9.setObjectName("label_9")

        self.gridLayout_4.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_10 = QLabel(self.dockWidgetContentsView)
        self.label_10.setObjectName("label_10")

        self.gridLayout_4.addWidget(self.label_10, 4, 2, 1, 1)

        self.label_2 = QLabel(self.dockWidgetContentsView)
        self.label_2.setObjectName("label_2")

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_12 = QLabel(self.dockWidgetContentsView)
        self.label_12.setObjectName("label_12")

        self.gridLayout_4.addWidget(self.label_12, 5, 2, 1, 1)

        self.labelGammaView = QLabel(self.dockWidgetContentsView)
        self.labelGammaView.setObjectName("labelGammaView")

        self.gridLayout_4.addWidget(self.labelGammaView, 2, 3, 1, 1)

        self.label = QLabel(self.dockWidgetContentsView)
        self.label.setObjectName("label")

        self.gridLayout_4.addWidget(self.label, 3, 0, 1, 1)

        self.dockWidget.setWidget(self.dockWidgetContentsView)

        self.gridLayout_3.addWidget(
            self.dockWidget, 1, 1, 1, 1, Qt.AlignmentFlag.AlignTop
        )

        self.gridLayout_2.addWidget(self.framePlotsView, 1, 0, 1, 1)

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
        self.pushButtonRecord.setText("")
        self.labelStartTime.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.labelSweep.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.labelSpan.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", "VISA", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", "Name", None))
        self.labelMax.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", "Options", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", "Driver", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", "Hz", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", "Hz", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", "IDN", None))
        self.labelOffsetsInstr.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.label_8.setText(QCoreApplication.translate("Dialog", "Hz", None))
        self.labelCenter.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.label_14.setText(QCoreApplication.translate("Dialog", "Hz", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", "s", None))
        self.labelMin.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.labelSlices.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInstr), "")
        self.labelOffsetsView.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.labelFilename.setText(QCoreApplication.translate("Dialog", "---", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", "f. pwr", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", "t. pwr", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", "---", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", "gamma", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", "---", None))
        self.labelGammaView.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.label.setText(QCoreApplication.translate("Dialog", "Filename", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabView), "")

    # retranslateUi
