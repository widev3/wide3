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
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(1311, 823)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush
        )
        brush1 = QBrush(QColor(0, 25, 75, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        brush2 = QBrush(QColor(0, 37, 112, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        brush3 = QBrush(QColor(0, 31, 93, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3
        )
        brush4 = QBrush(QColor(0, 12, 37, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        brush5 = QBrush(QColor(0, 17, 50, 255))
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
        brush9 = QBrush(QColor(0, 12, 37, 127))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush9
        )
        # endif
        brush10 = QBrush(QColor(0, 17, 53, 255))
        brush10.setStyle(Qt.BrushStyle.SolidPattern)
        # if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(
            QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush10
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
        self.widgetButtonsInstr = QWidget(Dialog)
        self.widgetButtonsInstr.setObjectName("widgetButtonsInstr")
        self.horizontalLayout_2 = QHBoxLayout(self.widgetButtonsInstr)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonConnect = QPushButton(self.widgetButtonsInstr)
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.pushButtonConnect.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButtonConnect.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButtonConnect)

        self.pushButtonSaveData = QPushButton(self.widgetButtonsInstr)
        self.pushButtonSaveData.setObjectName("pushButtonSaveData")
        self.pushButtonSaveData.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButtonSaveData.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButtonSaveData)

        self.pushButtonHide = QPushButton(self.widgetButtonsInstr)
        self.pushButtonHide.setObjectName("pushButtonHide")
        self.pushButtonHide.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButtonHide.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButtonHide)

        self.pushButtonClear = QPushButton(self.widgetButtonsInstr)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.pushButtonClear.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButtonClear.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButtonClear)

        self.gridLayout.addWidget(
            self.widgetButtonsInstr, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft
        )

        self.widgetPlotsInstr = QWidget(Dialog)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 284, 916))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName("frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labelPresets = QLabel(self.frame_7)
        self.labelPresets.setObjectName("labelPresets")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPresets.sizePolicy().hasHeightForWidth())
        self.labelPresets.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.labelPresets, 0, 0, 1, 1)

        self.comboBoxPresets = QComboBox(self.frame_7)
        self.comboBoxPresets.setObjectName("comboBoxPresets")

        self.gridLayout_5.addWidget(self.comboBoxPresets, 0, 1, 1, 1)

        self.pushButtonSavePreset = QPushButton(self.frame_7)
        self.pushButtonSavePreset.setObjectName("pushButtonSavePreset")
        self.pushButtonSavePreset.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButtonSavePreset.setIconSize(QSize(25, 25))

        self.gridLayout_5.addWidget(self.pushButtonSavePreset, 1, 0, 1, 2)

        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.doubleSpinBoxCenter = QDoubleSpinBox(self.frame_2)
        self.doubleSpinBoxCenter.setObjectName("doubleSpinBoxCenter")
        self.doubleSpinBoxCenter.setDecimals(0)
        self.doubleSpinBoxCenter.setMaximum(3000000000.000000000000000)

        self.gridLayout_9.addWidget(self.doubleSpinBoxCenter, 0, 1, 1, 1)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.gridLayout_9.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName("label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.gridLayout_9.addWidget(self.label_10, 1, 2, 1, 1)

        self.doubleSpinBoxSpan = QDoubleSpinBox(self.frame_2)
        self.doubleSpinBoxSpan.setObjectName("doubleSpinBoxSpan")
        self.doubleSpinBoxSpan.setDecimals(0)
        self.doubleSpinBoxSpan.setMaximum(3000000000.000000000000000)

        self.gridLayout_9.addWidget(self.doubleSpinBoxSpan, 1, 1, 1, 1)

        self.labelSpan = QLabel(self.frame_2)
        self.labelSpan.setObjectName("labelSpan")
        sizePolicy.setHeightForWidth(self.labelSpan.sizePolicy().hasHeightForWidth())
        self.labelSpan.setSizePolicy(sizePolicy)

        self.gridLayout_9.addWidget(self.labelSpan, 1, 0, 1, 1)

        self.labelCenter = QLabel(self.frame_2)
        self.labelCenter.setObjectName("labelCenter")
        sizePolicy.setHeightForWidth(self.labelCenter.sizePolicy().hasHeightForWidth())
        self.labelCenter.setSizePolicy(sizePolicy)

        self.gridLayout_9.addWidget(self.labelCenter, 0, 0, 1, 1)

        self.pushButtonApply1 = QPushButton(self.frame_2)
        self.pushButtonApply1.setObjectName("pushButtonApply1")
        self.pushButtonApply1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButtonApply1.setIconSize(QSize(25, 25))

        self.gridLayout_9.addWidget(self.pushButtonApply1, 2, 0, 1, 3)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.doubleSpinBoxMin = QDoubleSpinBox(self.frame)
        self.doubleSpinBoxMin.setObjectName("doubleSpinBoxMin")
        self.doubleSpinBoxMin.setDecimals(0)
        self.doubleSpinBoxMin.setMaximum(3000000000.000000000000000)

        self.gridLayout_7.addWidget(self.doubleSpinBoxMin, 1, 1, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName("label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.label_12, 1, 2, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName("label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.label_13, 2, 2, 1, 1)

        self.doubleSpinBoxMax = QDoubleSpinBox(self.frame)
        self.doubleSpinBoxMax.setObjectName("doubleSpinBoxMax")
        self.doubleSpinBoxMax.setDecimals(0)
        self.doubleSpinBoxMax.setMaximum(3000000000.000000000000000)

        self.gridLayout_7.addWidget(self.doubleSpinBoxMax, 2, 1, 1, 1)

        self.labelMin = QLabel(self.frame)
        self.labelMin.setObjectName("labelMin")
        sizePolicy.setHeightForWidth(self.labelMin.sizePolicy().hasHeightForWidth())
        self.labelMin.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.labelMin, 1, 0, 1, 1)

        self.labelMax = QLabel(self.frame)
        self.labelMax.setObjectName("labelMax")
        sizePolicy.setHeightForWidth(self.labelMax.sizePolicy().hasHeightForWidth())
        self.labelMax.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.labelMax, 2, 0, 1, 1)

        self.pushButtonApply2 = QPushButton(self.frame)
        self.pushButtonApply2.setObjectName("pushButtonApply2")
        self.pushButtonApply2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButtonApply2.setIconSize(QSize(25, 25))

        self.gridLayout_7.addWidget(self.pushButtonApply2, 3, 0, 1, 3)

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName("frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_8)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.doubleSpinBoxSweep = QDoubleSpinBox(self.frame_8)
        self.doubleSpinBoxSweep.setObjectName("doubleSpinBoxSweep")
        self.doubleSpinBoxSweep.setDecimals(2)
        self.doubleSpinBoxSweep.setMinimum(0.010000000000000)
        self.doubleSpinBoxSweep.setMaximum(86400.000000000000000)

        self.gridLayout_13.addWidget(self.doubleSpinBoxSweep, 0, 1, 1, 1)

        self.pushButtonApply3 = QPushButton(self.frame_8)
        self.pushButtonApply3.setObjectName("pushButtonApply3")
        self.pushButtonApply3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButtonApply3.setIconSize(QSize(25, 25))

        self.gridLayout_13.addWidget(self.pushButtonApply3, 1, 0, 1, 3)

        self.labelSweep = QLabel(self.frame_8)
        self.labelSweep.setObjectName("labelSweep")
        sizePolicy.setHeightForWidth(self.labelSweep.sizePolicy().hasHeightForWidth())
        self.labelSweep.setSizePolicy(sizePolicy)

        self.gridLayout_13.addWidget(self.labelSweep, 0, 0, 1, 1)

        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName("label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)

        self.gridLayout_13.addWidget(self.label_14, 0, 2, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName("frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_9)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.comboBoxOffsetsInstr = QComboBox(self.frame_9)
        self.comboBoxOffsetsInstr.setObjectName("comboBoxOffsetsInstr")

        self.gridLayout_14.addWidget(self.comboBoxOffsetsInstr, 0, 1, 1, 1)

        self.labelOffsetsInstr = QLabel(self.frame_9)
        self.labelOffsetsInstr.setObjectName("labelOffsetsInstr")
        sizePolicy.setHeightForWidth(
            self.labelOffsetsInstr.sizePolicy().hasHeightForWidth()
        )
        self.labelOffsetsInstr.setSizePolicy(sizePolicy)

        self.gridLayout_14.addWidget(self.labelOffsetsInstr, 0, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.labelDuration = QLabel(self.frame_4)
        self.labelDuration.setObjectName("labelDuration")
        sizePolicy.setHeightForWidth(
            self.labelDuration.sizePolicy().hasHeightForWidth()
        )
        self.labelDuration.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.labelDuration, 2, 0, 1, 1)

        self.lineEditSlices = QLineEdit(self.frame_4)
        self.lineEditSlices.setObjectName("lineEditSlices")
        self.lineEditSlices.setReadOnly(True)

        self.gridLayout_10.addWidget(self.lineEditSlices, 3, 1, 1, 1)

        self.labelSlices = QLabel(self.frame_4)
        self.labelSlices.setObjectName("labelSlices")
        sizePolicy.setHeightForWidth(self.labelSlices.sizePolicy().hasHeightForWidth())
        self.labelSlices.setSizePolicy(sizePolicy)

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
        sizePolicy.setHeightForWidth(
            self.labelStartTime.sizePolicy().hasHeightForWidth()
        )
        self.labelStartTime.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.labelStartTime, 1, 0, 1, 1)

        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName("label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.label_19, 2, 2, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_4)

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
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

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
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)

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
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.label_4, 5, 0, 1, 1)

        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName("label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.label_15, 2, 0, 1, 1)

        self.lineEditVisa = QLineEdit(self.frame_3)
        self.lineEditVisa.setObjectName("lineEditVisa")
        self.lineEditVisa.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEditVisa, 6, 1, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.label_5, 6, 0, 1, 1)

        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName("label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.label_17, 4, 0, 1, 1)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.label_7, 8, 0, 1, 1)

        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName("label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)

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

        self.gridLayout_4.addLayout(self.verticalLayoutSpecInstr, 0, 2, 1, 1)

        self.gridLayout.addWidget(self.widgetPlotsInstr, 1, 0, 1, 1)

        QWidget.setTabOrder(self.scrollArea, self.comboBoxPresets)
        QWidget.setTabOrder(self.comboBoxPresets, self.doubleSpinBoxCenter)
        QWidget.setTabOrder(self.doubleSpinBoxCenter, self.doubleSpinBoxSpan)
        QWidget.setTabOrder(self.doubleSpinBoxSpan, self.doubleSpinBoxMin)
        QWidget.setTabOrder(self.doubleSpinBoxMin, self.doubleSpinBoxMax)
        QWidget.setTabOrder(self.doubleSpinBoxMax, self.doubleSpinBoxSweep)
        QWidget.setTabOrder(self.doubleSpinBoxSweep, self.comboBoxOffsetsInstr)
        QWidget.setTabOrder(self.comboBoxOffsetsInstr, self.lineEditStartTime)
        QWidget.setTabOrder(self.lineEditStartTime, self.lineEditDuration)
        QWidget.setTabOrder(self.lineEditDuration, self.lineEditSlices)
        QWidget.setTabOrder(self.lineEditSlices, self.lineEditResourceName)
        QWidget.setTabOrder(self.lineEditResourceName, self.lineEditManufacturer)
        QWidget.setTabOrder(self.lineEditManufacturer, self.lineEditModelName)
        QWidget.setTabOrder(self.lineEditModelName, self.lineEditSerialNumber)
        QWidget.setTabOrder(self.lineEditSerialNumber, self.lineEditFW)
        QWidget.setTabOrder(self.lineEditFW, self.lineEditDriver)
        QWidget.setTabOrder(self.lineEditDriver, self.lineEditVisa)
        QWidget.setTabOrder(self.lineEditVisa, self.lineEditName)
        QWidget.setTabOrder(self.lineEditName, self.lineEditOptions)

        self.retranslateUi(Dialog)

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
        self.labelPresets.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButtonSavePreset.setText(
            QCoreApplication.translate("Dialog", "Save preset", None)
        )
        self.label_8.setText(QCoreApplication.translate("Dialog", "Hz", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", "Hz", None))
        self.labelSpan.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.labelCenter.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButtonApply1.setText(
            QCoreApplication.translate("Dialog", "Apply", None)
        )
        self.label_12.setText(QCoreApplication.translate("Dialog", "Hz", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", "Hz", None))
        self.labelMin.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.labelMax.setText(QCoreApplication.translate("Dialog", "TextLabel", None))
        self.pushButtonApply2.setText(
            QCoreApplication.translate("Dialog", "Apply", None)
        )
        self.pushButtonApply3.setText(
            QCoreApplication.translate("Dialog", "Apply", None)
        )
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

    # retranslateUi
