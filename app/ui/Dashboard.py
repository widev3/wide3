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
    QCheckBox,
    QComboBox,
    QDialog,
    QDockWidget,
    QDoubleSpinBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
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
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
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
        self.labelMin = QLabel(self.dockWidgetContentsInstr)
        self.labelMin.setObjectName("labelMin")

        self.gridLayout_11.addWidget(self.labelMin, 3, 1, 1, 1)

        self.labelSpan = QLabel(self.dockWidgetContentsInstr)
        self.labelSpan.setObjectName("labelSpan")

        self.gridLayout_11.addWidget(self.labelSpan, 2, 1, 1, 1)

        self.doubleSpinBoxCenter = QDoubleSpinBox(self.dockWidgetContentsInstr)
        self.doubleSpinBoxCenter.setObjectName("doubleSpinBoxCenter")
        self.doubleSpinBoxCenter.setDecimals(6)

        self.gridLayout_11.addWidget(self.doubleSpinBoxCenter, 0, 5, 1, 1)

        self.labelOffsetsInstr = QLabel(self.dockWidgetContentsInstr)
        self.labelOffsetsInstr.setObjectName("labelOffsetsInstr")

        self.gridLayout_11.addWidget(self.labelOffsetsInstr, 5, 1, 1, 1)

        self.checkBoxMax = QCheckBox(self.dockWidgetContentsInstr)
        self.checkBoxMax.setObjectName("checkBoxMax")

        self.gridLayout_11.addWidget(self.checkBoxMax, 4, 2, 1, 1)

        self.checkBoxSpan = QCheckBox(self.dockWidgetContentsInstr)
        self.checkBoxSpan.setObjectName("checkBoxSpan")

        self.gridLayout_11.addWidget(self.checkBoxSpan, 2, 2, 1, 1)

        self.checkBoxCenter = QCheckBox(self.dockWidgetContentsInstr)
        self.checkBoxCenter.setObjectName("checkBoxCenter")

        self.gridLayout_11.addWidget(self.checkBoxCenter, 0, 2, 1, 1)

        self.labelDriver = QLabel(self.dockWidgetContentsInstr)
        self.labelDriver.setObjectName("labelDriver")

        self.gridLayout_11.addWidget(self.labelDriver, 7, 4, 1, 1)

        self.label_7 = QLabel(self.dockWidgetContentsInstr)
        self.label_7.setObjectName("label_7")

        self.gridLayout_11.addWidget(self.label_7, 10, 1, 1, 1)

        self.horizontalSliderCenter = QSlider(self.dockWidgetContentsInstr)
        self.horizontalSliderCenter.setObjectName("horizontalSliderCenter")
        self.horizontalSliderCenter.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSliderCenter.setTickInterval(1)

        self.gridLayout_11.addWidget(self.horizontalSliderCenter, 0, 4, 1, 1)

        self.doubleSpinBoxMax = QDoubleSpinBox(self.dockWidgetContentsInstr)
        self.doubleSpinBoxMax.setObjectName("doubleSpinBoxMax")
        self.doubleSpinBoxMax.setDecimals(6)

        self.gridLayout_11.addWidget(self.doubleSpinBoxMax, 4, 5, 1, 1)

        self.doubleSpinBoxMin = QDoubleSpinBox(self.dockWidgetContentsInstr)
        self.doubleSpinBoxMin.setObjectName("doubleSpinBoxMin")
        self.doubleSpinBoxMin.setDecimals(6)

        self.gridLayout_11.addWidget(self.doubleSpinBoxMin, 3, 5, 1, 1)

        self.labelIDN = QLabel(self.dockWidgetContentsInstr)
        self.labelIDN.setObjectName("labelIDN")

        self.gridLayout_11.addWidget(self.labelIDN, 6, 4, 1, 1)

        self.label_3 = QLabel(self.dockWidgetContentsInstr)
        self.label_3.setObjectName("label_3")

        self.gridLayout_11.addWidget(self.label_3, 6, 1, 1, 1)

        self.doubleSpinBoxSpan = QDoubleSpinBox(self.dockWidgetContentsInstr)
        self.doubleSpinBoxSpan.setObjectName("doubleSpinBoxSpan")
        self.doubleSpinBoxSpan.setDecimals(6)

        self.gridLayout_11.addWidget(self.doubleSpinBoxSpan, 2, 5, 1, 1)

        self.label_4 = QLabel(self.dockWidgetContentsInstr)
        self.label_4.setObjectName("label_4")

        self.gridLayout_11.addWidget(self.label_4, 7, 1, 1, 1)

        self.horizontalSliderMin = QSlider(self.dockWidgetContentsInstr)
        self.horizontalSliderMin.setObjectName("horizontalSliderMin")
        self.horizontalSliderMin.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSliderMin.setTickInterval(1)

        self.gridLayout_11.addWidget(self.horizontalSliderMin, 3, 4, 1, 1)

        self.comboBoxOffsetsInstr = QComboBox(self.dockWidgetContentsInstr)
        self.comboBoxOffsetsInstr.setObjectName("comboBoxOffsetsInstr")

        self.gridLayout_11.addWidget(self.comboBoxOffsetsInstr, 5, 4, 1, 1)

        self.checkBoxMin = QCheckBox(self.dockWidgetContentsInstr)
        self.checkBoxMin.setObjectName("checkBoxMin")

        self.gridLayout_11.addWidget(self.checkBoxMin, 3, 2, 1, 1)

        self.labelCenter = QLabel(self.dockWidgetContentsInstr)
        self.labelCenter.setObjectName("labelCenter")

        self.gridLayout_11.addWidget(self.labelCenter, 0, 1, 1, 1)

        self.label_5 = QLabel(self.dockWidgetContentsInstr)
        self.label_5.setObjectName("label_5")

        self.gridLayout_11.addWidget(self.label_5, 8, 1, 1, 1)

        self.horizontalSliderSpan = QSlider(self.dockWidgetContentsInstr)
        self.horizontalSliderSpan.setObjectName("horizontalSliderSpan")
        self.horizontalSliderSpan.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSliderSpan.setTickInterval(1)

        self.gridLayout_11.addWidget(self.horizontalSliderSpan, 2, 4, 1, 1)

        self.label_6 = QLabel(self.dockWidgetContentsInstr)
        self.label_6.setObjectName("label_6")

        self.gridLayout_11.addWidget(self.label_6, 9, 1, 1, 1)

        self.labelMax = QLabel(self.dockWidgetContentsInstr)
        self.labelMax.setObjectName("labelMax")

        self.gridLayout_11.addWidget(self.labelMax, 4, 1, 1, 1)

        self.horizontalSliderMax = QSlider(self.dockWidgetContentsInstr)
        self.horizontalSliderMax.setObjectName("horizontalSliderMax")
        self.horizontalSliderMax.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSliderMax.setTickInterval(1)

        self.gridLayout_11.addWidget(self.horizontalSliderMax, 4, 4, 1, 1)

        self.labelVISA = QLabel(self.dockWidgetContentsInstr)
        self.labelVISA.setObjectName("labelVISA")

        self.gridLayout_11.addWidget(self.labelVISA, 8, 4, 1, 1)

        self.labelName = QLabel(self.dockWidgetContentsInstr)
        self.labelName.setObjectName("labelName")

        self.gridLayout_11.addWidget(self.labelName, 9, 4, 1, 1)

        self.labelOptions = QLabel(self.dockWidgetContentsInstr)
        self.labelOptions.setObjectName("labelOptions")

        self.gridLayout_11.addWidget(self.labelOptions, 10, 4, 1, 1)

        self.dockWidgetInstr.setWidget(self.dockWidgetContentsInstr)

        self.gridLayout_13.addWidget(
            self.dockWidgetInstr, 1, 1, 1, 1, Qt.AlignmentFlag.AlignTop
        )

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

        self.gridLayout_4.addWidget(
            self.labelOffsetsView, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft
        )

        self.label = QLabel(self.dockWidgetContentsView)
        self.label.setObjectName("label")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.comboBoxOffsetsView = QComboBox(self.dockWidgetContentsView)
        self.comboBoxOffsetsView.setObjectName("comboBoxOffsetsView")

        self.gridLayout_4.addWidget(self.comboBoxOffsetsView, 0, 1, 1, 1)

        self.labelFilename = QLabel(self.dockWidgetContentsView)
        self.labelFilename.setObjectName("labelFilename")

        self.gridLayout_4.addWidget(self.labelFilename, 1, 1, 1, 1)

        self.dockWidget.setWidget(self.dockWidgetContentsView)

        self.gridLayout_3.addWidget(
            self.dockWidget, 1, 1, 1, 1, Qt.AlignmentFlag.AlignTop
        )

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
        self.labelMin.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.labelSpan.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.labelOffsetsInstr.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.checkBoxMax.setText("")
        self.checkBoxSpan.setText("")
        self.checkBoxCenter.setText("")
        self.labelDriver.setText(QCoreApplication.translate("Dialog", "---", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", "Options", None))
        self.labelIDN.setText(QCoreApplication.translate("Dialog", "---", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", "IDN", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", "Driver", None))
        self.checkBoxMin.setText("")
        self.labelCenter.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.label_5.setText(QCoreApplication.translate("Dialog", "VISA", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", "Name", None))
        self.labelMax.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.labelVISA.setText(QCoreApplication.translate("Dialog", "---", None))
        self.labelName.setText(QCoreApplication.translate("Dialog", "---", None))
        self.labelOptions.setText(QCoreApplication.translate("Dialog", "---", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInstr), "")
        self.labelOffsetsView.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.label.setText(QCoreApplication.translate("Dialog", "Filename", None))
        self.labelFilename.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabView), "")

    # retranslateUi
