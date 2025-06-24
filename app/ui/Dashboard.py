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
        self.dockWidgetTime = QDockWidget(self.framePlots)
        self.dockWidgetTime.setObjectName("dockWidgetTime")
        self.dockWidgetTime.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetFloatable
            | QDockWidget.DockWidgetFeature.DockWidgetMovable
        )
        self.dockWidgetContentsTime = QWidget()
        self.dockWidgetContentsTime.setObjectName("dockWidgetContentsTime")
        self.gridLayout_6 = QGridLayout(self.dockWidgetContentsTime)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayoutTime = QVBoxLayout()
        self.verticalLayoutTime.setObjectName("verticalLayoutTime")

        self.gridLayout_6.addLayout(self.verticalLayoutTime, 0, 0, 1, 1)

        self.dockWidgetTime.setWidget(self.dockWidgetContentsTime)

        self.gridLayout_3.addWidget(self.dockWidgetTime, 0, 1, 1, 1)

        self.dockWidgetSpec = QDockWidget(self.framePlots)
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

        self.dockWidget = QDockWidget(self.framePlots)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidget.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetFloatable
            | QDockWidget.DockWidgetFeature.DockWidgetMovable
        )
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.gridLayout_4 = QGridLayout(self.dockWidgetContents_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labelMax = QLabel(self.dockWidgetContents_4)
        self.labelMax.setObjectName("labelMax")
        self.labelMax.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.labelMax, 3, 0, 1, 1)

        self.labelCenter = QLabel(self.dockWidgetContents_4)
        self.labelCenter.setObjectName("labelCenter")
        self.labelCenter.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.labelCenter, 0, 0, 1, 1)

        self.horizontalSliderMin = QSlider(self.dockWidgetContents_4)
        self.horizontalSliderMin.setObjectName("horizontalSliderMin")
        self.horizontalSliderMin.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSliderMin.setTickInterval(1)

        self.gridLayout_4.addWidget(self.horizontalSliderMin, 2, 3, 1, 1)

        self.horizontalSliderMax = QSlider(self.dockWidgetContents_4)
        self.horizontalSliderMax.setObjectName("horizontalSliderMax")
        self.horizontalSliderMax.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSliderMax.setTickInterval(1)

        self.gridLayout_4.addWidget(self.horizontalSliderMax, 3, 3, 1, 1)

        self.horizontalSliderCenter = QSlider(self.dockWidgetContents_4)
        self.horizontalSliderCenter.setObjectName("horizontalSliderCenter")
        self.horizontalSliderCenter.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSliderCenter.setTickInterval(1)

        self.gridLayout_4.addWidget(self.horizontalSliderCenter, 0, 3, 1, 1)

        self.labelMin = QLabel(self.dockWidgetContents_4)
        self.labelMin.setObjectName("labelMin")
        self.labelMin.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.labelMin, 2, 0, 1, 1)

        self.horizontalSliderSpan = QSlider(self.dockWidgetContents_4)
        self.horizontalSliderSpan.setObjectName("horizontalSliderSpan")
        self.horizontalSliderSpan.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSliderSpan.setTickInterval(1)

        self.gridLayout_4.addWidget(self.horizontalSliderSpan, 1, 3, 1, 1)

        self.labelSpan = QLabel(self.dockWidgetContents_4)
        self.labelSpan.setObjectName("labelSpan")
        self.labelSpan.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.labelSpan, 1, 0, 1, 1)

        self.labelOffsets = QLabel(self.dockWidgetContents_4)
        self.labelOffsets.setObjectName("labelOffsets")
        self.labelOffsets.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.labelOffsets, 4, 0, 1, 1)

        self.comboBoxOffsets = QComboBox(self.dockWidgetContents_4)
        self.comboBoxOffsets.setObjectName("comboBoxOffsets")

        self.gridLayout_4.addWidget(self.comboBoxOffsets, 4, 3, 1, 1)

        self.doubleSpinBoxCenter = QDoubleSpinBox(self.dockWidgetContents_4)
        self.doubleSpinBoxCenter.setObjectName("doubleSpinBoxCenter")
        self.doubleSpinBoxCenter.setDecimals(6)

        self.gridLayout_4.addWidget(self.doubleSpinBoxCenter, 0, 4, 1, 1)

        self.doubleSpinBoxSpan = QDoubleSpinBox(self.dockWidgetContents_4)
        self.doubleSpinBoxSpan.setObjectName("doubleSpinBoxSpan")
        self.doubleSpinBoxSpan.setDecimals(6)

        self.gridLayout_4.addWidget(self.doubleSpinBoxSpan, 1, 4, 1, 1)

        self.doubleSpinBoxMin = QDoubleSpinBox(self.dockWidgetContents_4)
        self.doubleSpinBoxMin.setObjectName("doubleSpinBoxMin")
        self.doubleSpinBoxMin.setDecimals(6)

        self.gridLayout_4.addWidget(self.doubleSpinBoxMin, 2, 4, 1, 1)

        self.doubleSpinBoxMax = QDoubleSpinBox(self.dockWidgetContents_4)
        self.doubleSpinBoxMax.setObjectName("doubleSpinBoxMax")
        self.doubleSpinBoxMax.setDecimals(6)

        self.gridLayout_4.addWidget(self.doubleSpinBoxMax, 3, 4, 1, 1)

        self.dockWidget.setWidget(self.dockWidgetContents_4)

        self.gridLayout_3.addWidget(self.dockWidget, 1, 1, 1, 1)

        self.dockWidgetFreq = QDockWidget(self.framePlots)
        self.dockWidgetFreq.setObjectName("dockWidgetFreq")
        self.dockWidgetFreq.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetFloatable
            | QDockWidget.DockWidgetFeature.DockWidgetMovable
        )
        self.dockWidgetContentsFreq = QWidget()
        self.dockWidgetContentsFreq.setObjectName("dockWidgetContentsFreq")
        self.gridLayout_7 = QGridLayout(self.dockWidgetContentsFreq)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayoutFreq = QVBoxLayout()
        self.verticalLayoutFreq.setObjectName("verticalLayoutFreq")

        self.gridLayout_7.addLayout(self.verticalLayoutFreq, 0, 0, 1, 1)

        self.dockWidgetFreq.setWidget(self.dockWidgetContentsFreq)

        self.gridLayout_3.addWidget(self.dockWidgetFreq, 1, 0, 1, 1)

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
        self.pushButtonInfo.setText("")
        self.labelMax.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.labelCenter.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.labelMin.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.labelSpan.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.labelOffsets.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabView),
            QCoreApplication.translate("Dialog", "View", None),
        )

    # retranslateUi
