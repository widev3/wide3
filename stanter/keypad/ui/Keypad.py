# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keypad.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
    QDoubleSpinBox,
    QFrame,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(452, 332)
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
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonAcquire = QPushButton(self.frame)
        self.pushButtonAcquire.setObjectName("pushButtonAcquire")
        self.pushButtonAcquire.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.pushButtonAcquire, 0, 2, 1, 1)

        self.lineEditEndpoint = QLineEdit(self.frame)
        self.lineEditEndpoint.setObjectName("lineEditEndpoint")

        self.gridLayout.addWidget(self.lineEditEndpoint, 0, 1, 1, 1)

        self.lineEditSID = QLineEdit(self.frame)
        self.lineEditSID.setObjectName("lineEditSID")
        self.lineEditSID.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditSID, 1, 1, 1, 2)

        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 2)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.label_3, 0, 1, 1, 1)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")

        self.gridLayout_5.addWidget(self.doubleSpinBox_3, 0, 0, 1, 1)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")

        self.gridLayout_5.addWidget(self.doubleSpinBox_4, 1, 0, 1, 1)

        self.pushButtonALTAZ = QPushButton(self.frame_2)
        self.pushButtonALTAZ.setObjectName("pushButtonALTAZ")
        self.pushButtonALTAZ.setIconSize(QSize(25, 25))

        self.gridLayout_5.addWidget(self.pushButtonALTAZ, 2, 0, 1, 2)

        self.gridLayout_3.addWidget(self.frame_2, 3, 0, 1, 1)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.doubleSpinBox_2 = QDoubleSpinBox(self.frame_3)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_2.setDecimals(6)

        self.gridLayout_4.addWidget(self.doubleSpinBox_2, 0, 1, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.frame_3)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setDecimals(6)

        self.gridLayout_4.addWidget(self.doubleSpinBox, 3, 1, 1, 1)

        self.pushButtonRADEC = QPushButton(self.frame_3)
        self.pushButtonRADEC.setObjectName("pushButtonRADEC")
        self.pushButtonRADEC.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.pushButtonRADEC, 4, 1, 1, 2)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName("label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label, 0, 2, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_2, 3, 2, 1, 1)

        self.gridLayout_3.addWidget(self.frame_3, 2, 0, 1, 1)

        self.frameDirections = QFrame(Dialog)
        self.frameDirections.setObjectName("frameDirections")
        self.frameDirections.setEnabled(False)
        self.frameDirections.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameDirections.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frameDirections)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonS = QPushButton(self.frameDirections)
        self.pushButtonS.setObjectName("pushButtonS")
        self.pushButtonS.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.pushButtonS, 2, 1, 1, 1)

        self.pushButtonW = QPushButton(self.frameDirections)
        self.pushButtonW.setObjectName("pushButtonW")
        self.pushButtonW.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.pushButtonW, 1, 0, 1, 1)

        self.pushButtonE = QPushButton(self.frameDirections)
        self.pushButtonE.setObjectName("pushButtonE")
        self.pushButtonE.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.pushButtonE, 1, 2, 1, 1)

        self.pushButtonN = QPushButton(self.frameDirections)
        self.pushButtonN.setObjectName("pushButtonN")
        self.pushButtonN.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.pushButtonN, 0, 1, 1, 1)

        self.pushButtonStop = QPushButton(self.frameDirections)
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.pushButtonStop.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.pushButtonStop, 1, 1, 1, 1)

        self.gridLayout_3.addWidget(self.frameDirections, 2, 1, 2, 1)

        QWidget.setTabOrder(self.pushButtonN, self.pushButtonS)
        QWidget.setTabOrder(self.pushButtonS, self.pushButtonE)
        QWidget.setTabOrder(self.pushButtonE, self.pushButtonW)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.pushButtonAcquire.setText(
            QCoreApplication.translate("Dialog", "acquire", None)
        )
        self.lineEditEndpoint.setText("")
        self.lineEditEndpoint.setPlaceholderText(
            QCoreApplication.translate("Dialog", "server endpoint", None)
        )
        self.lineEditSID.setPlaceholderText(
            QCoreApplication.translate("Dialog", "session", None)
        )
        self.label_4.setText(QCoreApplication.translate("Dialog", "AZ", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", "ALT", None))
        self.pushButtonALTAZ.setText(
            QCoreApplication.translate("Dialog", "PushButton", None)
        )
        self.pushButtonRADEC.setText(
            QCoreApplication.translate("Dialog", "PushButton", None)
        )
        self.label.setText(QCoreApplication.translate("Dialog", "RA", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", "DEC", None))
        self.pushButtonS.setText(QCoreApplication.translate("Dialog", "S", None))
        self.pushButtonW.setText(QCoreApplication.translate("Dialog", "W", None))
        self.pushButtonE.setText(QCoreApplication.translate("Dialog", "E", None))
        self.pushButtonN.setText(QCoreApplication.translate("Dialog", "N", None))
        self.pushButtonStop.setText(QCoreApplication.translate("Dialog", "Stop", None))

    # retranslateUi
