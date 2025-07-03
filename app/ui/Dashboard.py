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
    QAbstractScrollArea,
    QApplication,
    QComboBox,
    QDialog,
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
    QSpacerItem,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(1565, 1115)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush
        )
        brush1 = QBrush(QColor(153, 193, 241, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        brush3 = QBrush(QColor(204, 224, 248, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3
        )
        brush4 = QBrush(QColor(76, 96, 120, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        brush5 = QBrush(QColor(102, 129, 161, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2
        )
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush
        )
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush3
        )
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush6
        )
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush
        )
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush7
        )
        # endif
        # if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush2)
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
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2
        )
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush
        )
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush2)
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1
        )
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush3
        )
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush6
        )
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush
        )
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush7
        )
        # endif
        # if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(
            QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush2
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
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2
        )
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4
        )
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1
        )
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1
        )
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush6
        )
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush
        )
        brush8 = QBrush(QColor(76, 96, 120, 127))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush8
        )
        # endif
        brush9 = QBrush(QColor(220, 236, 255, 255))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
        # if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush9
        )
        # endif
        Dialog.setPalette(palette)
        font = QFont()
        font.setFamilies(["Wix Madefor Display"])
        Dialog.setFont(font)
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
        self.widgetButtonsInstr = QWidget(self.tabInstr)
        self.widgetButtonsInstr.setObjectName("widgetButtonsInstr")
        self.horizontalLayout_2 = QHBoxLayout(self.widgetButtonsInstr)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonConnect = QPushButton(self.widgetButtonsInstr)
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.pushButtonConnect.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButtonConnect)

        self.pushButtonSaveData = QPushButton(self.widgetButtonsInstr)
        self.pushButtonSaveData.setObjectName("pushButtonSaveData")
        self.pushButtonSaveData.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButtonSaveData)

        self.pushButtonHide = QPushButton(self.widgetButtonsInstr)
        self.pushButtonHide.setObjectName("pushButtonHide")
        self.pushButtonHide.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButtonHide)

        self.pushButtonClear = QPushButton(self.widgetButtonsInstr)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.pushButtonClear.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButtonClear)

        self.gridLayout_8.addWidget(
            self.widgetButtonsInstr, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft
        )

        self.widgetPlotsInstr = QWidget(self.tabInstr)
        self.widgetPlotsInstr.setObjectName("widgetPlotsInstr")
        self.gridLayout_4 = QGridLayout(self.widgetPlotsInstr)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QScrollArea(self.widgetPlotsInstr)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(300, 0))
        self.scrollArea.setMaximumSize(QSize(300, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scrollArea.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents
        )
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 303, 1004))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName("frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButtonSavePreset = QPushButton(self.frame_7)
        self.pushButtonSavePreset.setObjectName("pushButtonSavePreset")
        self.pushButtonSavePreset.setIconSize(QSize(25, 25))

        self.gridLayout_5.addWidget(self.pushButtonSavePreset, 0, 2, 1, 1)

        self.labelPresets = QLabel(self.frame_7)
        self.labelPresets.setObjectName("labelPresets")

        self.gridLayout_5.addWidget(self.labelPresets, 0, 0, 1, 1)

        self.comboBoxPresets = QComboBox(self.frame_7)
        self.comboBoxPresets.setObjectName("comboBoxPresets")

        self.gridLayout_5.addWidget(self.comboBoxPresets, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 1, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalSpacer_3 = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_9.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)

        self.labelSpan = QLabel(self.frame_2)
        self.labelSpan.setObjectName("labelSpan")

        self.gridLayout_9.addWidget(self.labelSpan, 1, 0, 1, 1)

        self.doubleSpinBoxSpan = QDoubleSpinBox(self.frame_2)
        self.doubleSpinBoxSpan.setObjectName("doubleSpinBoxSpan")
        self.doubleSpinBoxSpan.setDecimals(0)
        self.doubleSpinBoxSpan.setMaximum(3000000000.000000000000000)

        self.gridLayout_9.addWidget(self.doubleSpinBoxSpan, 1, 1, 1, 1)

        self.labelCenter = QLabel(self.frame_2)
        self.labelCenter.setObjectName("labelCenter")

        self.gridLayout_9.addWidget(self.labelCenter, 0, 0, 1, 1)

        self.doubleSpinBoxCenter = QDoubleSpinBox(self.frame_2)
        self.doubleSpinBoxCenter.setObjectName("doubleSpinBoxCenter")
        self.doubleSpinBoxCenter.setDecimals(0)
        self.doubleSpinBoxCenter.setMaximum(3000000000.000000000000000)

        self.gridLayout_9.addWidget(self.doubleSpinBoxCenter, 0, 1, 1, 1)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")

        self.gridLayout_9.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName("label_10")

        self.gridLayout_9.addWidget(self.label_10, 1, 2, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.doubleSpinBoxMax = QDoubleSpinBox(self.frame)
        self.doubleSpinBoxMax.setObjectName("doubleSpinBoxMax")
        self.doubleSpinBoxMax.setDecimals(0)
        self.doubleSpinBoxMax.setMaximum(3000000000.000000000000000)

        self.gridLayout_7.addWidget(self.doubleSpinBoxMax, 2, 1, 1, 1)

        self.doubleSpinBoxMin = QDoubleSpinBox(self.frame)
        self.doubleSpinBoxMin.setObjectName("doubleSpinBoxMin")
        self.doubleSpinBoxMin.setDecimals(0)
        self.doubleSpinBoxMin.setMaximum(3000000000.000000000000000)

        self.gridLayout_7.addWidget(self.doubleSpinBoxMin, 1, 1, 1, 1)

        self.labelMin = QLabel(self.frame)
        self.labelMin.setObjectName("labelMin")

        self.gridLayout_7.addWidget(self.labelMin, 1, 0, 1, 1)

        self.labelMax = QLabel(self.frame)
        self.labelMax.setObjectName("labelMax")

        self.gridLayout_7.addWidget(self.labelMax, 2, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_7.addItem(self.horizontalSpacer_6, 3, 1, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName("label_12")

        self.gridLayout_7.addWidget(self.label_12, 1, 2, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName("label_13")

        self.gridLayout_7.addWidget(self.label_13, 2, 2, 1, 1)

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName("frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_8)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.labelSweep = QLabel(self.frame_8)
        self.labelSweep.setObjectName("labelSweep")

        self.gridLayout_13.addWidget(self.labelSweep, 0, 0, 1, 1)

        self.doubleSpinBoxSweep = QDoubleSpinBox(self.frame_8)
        self.doubleSpinBoxSweep.setObjectName("doubleSpinBoxSweep")
        self.doubleSpinBoxSweep.setDecimals(0)
        self.doubleSpinBoxSweep.setMaximum(3000000000.000000000000000)

        self.gridLayout_13.addWidget(self.doubleSpinBoxSweep, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_13.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName("label_14")

        self.gridLayout_13.addWidget(self.label_14, 0, 2, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName("frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_9)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.labelOffsetsInstr = QLabel(self.frame_9)
        self.labelOffsetsInstr.setObjectName("labelOffsetsInstr")

        self.gridLayout_14.addWidget(self.labelOffsetsInstr, 0, 0, 1, 1)

        self.comboBoxOffsetsInstr = QComboBox(self.frame_9)
        self.comboBoxOffsetsInstr.setObjectName("comboBoxOffsetsInstr")

        self.gridLayout_14.addWidget(self.comboBoxOffsetsInstr, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_14.addItem(self.horizontalSpacer_8, 1, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.labelDuration = QLabel(self.frame_4)
        self.labelDuration.setObjectName("labelDuration")

        self.gridLayout_10.addWidget(self.labelDuration, 2, 0, 1, 1)

        self.lineEditSlices = QLineEdit(self.frame_4)
        self.lineEditSlices.setObjectName("lineEditSlices")
        self.lineEditSlices.setReadOnly(True)

        self.gridLayout_10.addWidget(self.lineEditSlices, 3, 1, 1, 1)

        self.labelSlices = QLabel(self.frame_4)
        self.labelSlices.setObjectName("labelSlices")

        self.gridLayout_10.addWidget(self.labelSlices, 3, 0, 1, 1)

        self.lineEditDuration = QLineEdit(self.frame_4)
        self.lineEditDuration.setObjectName("lineEditDuration")
        self.lineEditDuration.setReadOnly(True)

        self.gridLayout_10.addWidget(self.lineEditDuration, 2, 1, 1, 1)

        self.lineEditStartTime = QLineEdit(self.frame_4)
        self.lineEditStartTime.setObjectName("lineEditStartTime")
        self.lineEditStartTime.setReadOnly(True)

        self.gridLayout_10.addWidget(self.lineEditStartTime, 1, 1, 1, 1)

        self.labelStartTime = QLabel(self.frame_4)
        self.labelStartTime.setObjectName("labelStartTime")

        self.gridLayout_10.addWidget(self.labelStartTime, 1, 0, 1, 1)

        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName("label_19")

        self.gridLayout_10.addWidget(self.label_19, 2, 2, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_4)

        self.verticalSpacer_3 = QSpacerItem(
            0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEditModelName = QLineEdit(self.frame_3)
        self.lineEditModelName.setObjectName("lineEditModelName")
        self.lineEditModelName.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEditModelName, 2, 1, 1, 1)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")

        self.gridLayout_6.addWidget(self.label_6, 7, 0, 1, 1)

        self.lineEditSerialNumber = QLineEdit(self.frame_3)
        self.lineEditSerialNumber.setObjectName("lineEditSerialNumber")
        self.lineEditSerialNumber.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEditSerialNumber, 3, 1, 1, 1)

        self.lineEditFW = QLineEdit(self.frame_3)
        self.lineEditFW.setObjectName("lineEditFW")
        self.lineEditFW.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEditFW, 4, 1, 1, 1)

        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName("label_16")

        self.gridLayout_6.addWidget(self.label_16, 3, 0, 1, 1)

        self.lineEditDriver = QLineEdit(self.frame_3)
        self.lineEditDriver.setObjectName("lineEditDriver")
        self.lineEditDriver.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEditDriver, 5, 1, 1, 1)

        self.lineEditOptions = QLineEdit(self.frame_3)
        self.lineEditOptions.setObjectName("lineEditOptions")
        self.lineEditOptions.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEditOptions, 8, 1, 1, 1)

        self.lineEditName = QLineEdit(self.frame_3)
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditName.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEditName, 7, 1, 1, 1)

        self.lineEditManufacturer = QLineEdit(self.frame_3)
        self.lineEditManufacturer.setObjectName("lineEditManufacturer")
        self.lineEditManufacturer.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEditManufacturer, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")

        self.gridLayout_6.addWidget(self.label_4, 5, 0, 1, 1)

        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName("label_15")

        self.gridLayout_6.addWidget(self.label_15, 2, 0, 1, 1)

        self.lineEditVisa = QLineEdit(self.frame_3)
        self.lineEditVisa.setObjectName("lineEditVisa")
        self.lineEditVisa.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEditVisa, 6, 1, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")

        self.gridLayout_6.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")

        self.gridLayout_6.addWidget(self.label_5, 6, 0, 1, 1)

        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName("label_17")

        self.gridLayout_6.addWidget(self.label_17, 4, 0, 1, 1)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")

        self.gridLayout_6.addWidget(self.label_7, 8, 0, 1, 1)

        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName("label_18")

        self.gridLayout_6.addWidget(self.label_18, 0, 0, 1, 1)

        self.lineEditResourceName = QLineEdit(self.frame_3)
        self.lineEditResourceName.setObjectName("lineEditResourceName")
        self.lineEditResourceName.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEditResourceName, 0, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 1, 1, 1)

        self.verticalLayoutSpecInstr = QVBoxLayout()
        self.verticalLayoutSpecInstr.setObjectName("verticalLayoutSpecInstr")

        self.gridLayout_4.addLayout(self.verticalLayoutSpecInstr, 0, 0, 1, 1)

        self.gridLayout_8.addWidget(self.widgetPlotsInstr, 1, 0, 1, 1)

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
        self.gridLayout_3 = QGridLayout(self.framePlotsView)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayoutTime = QVBoxLayout()
        self.verticalLayoutTime.setObjectName("verticalLayoutTime")

        self.gridLayout_3.addLayout(self.verticalLayoutTime, 1, 1, 1, 1)

        self.verticalLayoutFreq = QVBoxLayout()
        self.verticalLayoutFreq.setObjectName("verticalLayoutFreq")

        self.gridLayout_3.addLayout(self.verticalLayoutFreq, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(
            0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.verticalLayoutSpec = QVBoxLayout()
        self.verticalLayoutSpec.setObjectName("verticalLayoutSpec")

        self.gridLayout_3.addLayout(self.verticalLayoutSpec, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 2, 1, 1, 1)

        self.scrollAreaView = QScrollArea(self.framePlotsView)
        self.scrollAreaView.setObjectName("scrollAreaView")
        self.scrollAreaView.setMinimumSize(QSize(300, 0))
        self.scrollAreaView.setMaximumSize(QSize(300, 16777215))
        self.scrollAreaView.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOn
        )
        self.scrollAreaView.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scrollAreaView.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents
        )
        self.scrollAreaView.setWidgetResizable(True)
        self.scrollAreaWidgetContentsView = QWidget()
        self.scrollAreaWidgetContentsView.setObjectName("scrollAreaWidgetContentsView")
        self.scrollAreaWidgetContentsView.setGeometry(QRect(0, 0, 284, 494))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContentsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QFrame(self.scrollAreaWidgetContentsView)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_11 = QGridLayout(self.frame_5)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.labelOffsetsView = QLabel(self.frame_5)
        self.labelOffsetsView.setObjectName("labelOffsetsView")

        self.gridLayout_11.addWidget(self.labelOffsetsView, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")

        self.gridLayout_11.addWidget(self.label_2, 1, 0, 1, 1)

        self.horizontalSliderGammaView = QSlider(self.frame_5)
        self.horizontalSliderGammaView.setObjectName("horizontalSliderGammaView")
        self.horizontalSliderGammaView.setMaximum(1000)
        self.horizontalSliderGammaView.setSingleStep(1)
        self.horizontalSliderGammaView.setPageStep(50)
        self.horizontalSliderGammaView.setSliderPosition(500)
        self.horizontalSliderGammaView.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_11.addWidget(self.horizontalSliderGammaView, 1, 1, 1, 1)

        self.labelGammaView = QLabel(self.frame_5)
        self.labelGammaView.setObjectName("labelGammaView")

        self.gridLayout_11.addWidget(self.labelGammaView, 1, 2, 1, 1)

        self.comboBoxOffsetsView = QComboBox(self.frame_5)
        self.comboBoxOffsetsView.setObjectName("comboBoxOffsetsView")

        self.gridLayout_11.addWidget(self.comboBoxOffsetsView, 0, 1, 1, 2)

        self.verticalLayout.addWidget(self.frame_5)

        self.verticalSpacer_4 = QSpacerItem(
            0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.frame_6 = QFrame(self.scrollAreaWidgetContentsView)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_12 = QGridLayout(self.frame_6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName("label")

        self.gridLayout_12.addWidget(self.label, 0, 0, 1, 1)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName("label_9")

        self.gridLayout_12.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName("label_11")

        self.gridLayout_12.addWidget(self.label_11, 2, 0, 1, 1)

        self.lineEditFilename = QLineEdit(self.frame_6)
        self.lineEditFilename.setObjectName("lineEditFilename")
        self.lineEditFilename.setReadOnly(True)

        self.gridLayout_12.addWidget(self.lineEditFilename, 0, 2, 1, 1)

        self.lineEditTPwr = QLineEdit(self.frame_6)
        self.lineEditTPwr.setObjectName("lineEditTPwr")
        self.lineEditTPwr.setReadOnly(True)

        self.gridLayout_12.addWidget(self.lineEditTPwr, 1, 2, 1, 1)

        self.lineEditFPwr = QLineEdit(self.frame_6)
        self.lineEditFPwr.setObjectName("lineEditFPwr")
        self.lineEditFPwr.setReadOnly(True)

        self.gridLayout_12.addWidget(self.lineEditFPwr, 2, 2, 1, 1)

        self.verticalLayout.addWidget(self.frame_6)

        self.scrollAreaView.setWidget(self.scrollAreaWidgetContentsView)

        self.gridLayout_3.addWidget(
            self.scrollAreaView, 1, 2, 1, 1, Qt.AlignmentFlag.AlignRight
        )

        self.verticalSpacer_2 = QSpacerItem(
            0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_3.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 2, 2, 1, 1)

        self.gridLayout_2.addWidget(self.framePlotsView, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tabView, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "Whistle Of Wind", None)
        )
        self.pushButtonConnect.setText(
            QCoreApplication.translate("Dialog", "Connect", None)
        )
        self.pushButtonSaveData.setText(
            QCoreApplication.translate("Dialog", "Save data", None)
        )
        self.pushButtonHide.setText(QCoreApplication.translate("Dialog", "Hide", None))
        self.pushButtonClear.setText(
            QCoreApplication.translate("Dialog", "Clear", None)
        )
        self.pushButtonSavePreset.setText(
            QCoreApplication.translate("Dialog", "Save preset", None)
        )
        self.labelPresets.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.labelSpan.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.labelCenter.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.label_8.setText(QCoreApplication.translate("Dialog", "Hz", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", "Hz", None))
        self.labelMin.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.labelMax.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", "Hz", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", "Hz", None))
        self.labelSweep.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", "s", None))
        self.labelOffsetsInstr.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.labelDuration.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.labelSlices.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.labelStartTime.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.label_19.setText(QCoreApplication.translate("Dialog", "s", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", "Name", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", "SN", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", "Driver", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", "Model", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", "Brand", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", "VISA", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", "FW", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", "Options", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", "Resource", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInstr), "")
        self.pushButtonFileOpen.setText(
            QCoreApplication.translate("Dialog", "File open", None)
        )
        self.labelOffsetsView.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.label_2.setText(QCoreApplication.translate("Dialog", "gamma", None))
        self.labelGammaView.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.label.setText(QCoreApplication.translate("Dialog", "Filename", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", "t. pwr", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", "f. pwr", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabView), "")

    # retranslateUi
