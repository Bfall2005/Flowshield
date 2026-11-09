# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flowshield.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1035, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"/* FlowShield background */\n"
"QMainWindow,\n"
"QWidget#centralwidget,\n"
"QWidget#pageConfiguration,\n"
"QWidget#pageResults {\n"
"    background-color: #EAF2F5;\n"
"}\n"
"\n"
"/* Text and headings */\n"
"QLabel {\n"
"    color: #17324D;\n"
"}\n"
"\n"
"/* Input fields */\n"
"QSpinBox, QComboBox {\n"
"    background-color: #FFFFFF;\n"
"    color: #263746;\n"
"    border: 1px solid #B8CDD5;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    min-height: 24px;\n"
"}\n"
"\n"
"/* Highlight selected inputs */\n"
"QSpinBox:focus, QComboBox:focus {\n"
"    border: 2px solid #087F8C;\n"
"}\n"
"\n"
"/* Run Simulation button */\n"
"QPushButton#btnRunSimulation {\n"
"    background-color: #087F8C;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 12px;\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QPushButton#btnRunSimulation:hover {\n"
"    background-color: #066773;\n"
"}\n"
"\n"
"/* Button pressed */\n"
"QPushButton#btnRunSimulat"
                        "ion:pressed {\n"
"    background-color: #054F59;\n"
"}")
        self.pageConfirmation = QWidget()
        self.pageConfirmation.setObjectName(u"pageConfirmation")
        self.pageConfirmation.setStyleSheet(u"QWidget#pageConfiguration {\n"
"    background-color: #EAF2F5;\n"
"}")
        self.frame_3 = QFrame(self.pageConfirmation)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(-20, 0, 1061, 551))
        self.frame_3.setStyleSheet(u"QWidget#frame_3 {\n"
"    background-color: #EAF2F5;\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(430, 10, 160, 43))
        self.label_5.setStyleSheet(u"font: 700 24pt \"Segoe UI\";")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 80, 258, 28))
        self.label_6.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(130, 120, 751, 123))
        self.frame.setStyleSheet(u"Q_Frame{\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #D5E3E8;\n"
"    border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.label_2)

        self.spinAge = QSpinBox(self.frame)
        self.spinAge.setObjectName(u"spinAge")
        self.spinAge.setMinimum(18)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.spinAge)

        self.comboSex = QComboBox(self.frame)
        self.comboSex.addItem("")
        self.comboSex.addItem("")
        self.comboSex.setObjectName(u"comboSex")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboSex)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(130, 250, 751, 191))
        self.frame_2.setStyleSheet(u"Qframe_2 {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #D5E3E8;\n"
"    border-radius: 10px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 2)

        self.spinInitialVolume = QSpinBox(self.frame_2)
        self.spinInitialVolume.setObjectName(u"spinInitialVolume")
        self.spinInitialVolume.setMaximum(700)

        self.gridLayout.addWidget(self.spinInitialVolume, 2, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.comboDuration = QComboBox(self.frame_2)
        self.comboDuration.addItem("")
        self.comboDuration.addItem("")
        self.comboDuration.addItem("")
        self.comboDuration.addItem("")
        self.comboDuration.addItem("")
        self.comboDuration.addItem("")
        self.comboDuration.addItem("")
        self.comboDuration.addItem("")
        self.comboDuration.addItem("")
        self.comboDuration.setObjectName(u"comboDuration")

        self.gridLayout.addWidget(self.comboDuration, 2, 1, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.btnRunSimulation = QPushButton(self.frame_3)
        self.btnRunSimulation.setObjectName(u"btnRunSimulation")
        self.btnRunSimulation.setGeometry(QRect(320, 470, 331, 45))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRunSimulation.sizePolicy().hasHeightForWidth())
        self.btnRunSimulation.setSizePolicy(sizePolicy)
        self.btnRunSimulation.setStyleSheet(u"QPushButton#btnRunSimulation {\n"
"    background-color: #087F8C;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}")
        self.stackedWidget.addWidget(self.pageConfirmation)
        self.pageResults = QWidget()
        self.pageResults.setObjectName(u"pageResults")
        self.label_13 = QLabel(self.pageResults)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 70, 271, 31))
        self.label_13.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.frameSummary = QFrame(self.pageResults)
        self.frameSummary.setObjectName(u"frameSummary")
        self.frameSummary.setGeometry(QRect(30, 110, 951, 91))
        self.frameSummary.setStyleSheet(u"/* Parent frame containing all three boxes */\n"
"QFrame#frameSummary {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Individual white summary boxes */\n"
"QFrame#frameInitialVolume,\n"
"QFrame#frameFinalVolume,\n"
"QFrame#frameAlertStatus {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #D5E3E8;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"/* Heading labels */\n"
"QLabel#lblInitialTitle,\n"
"QLabel#lblFinalTitle,\n"
"QLabel#lblAlertTitle {\n"
"    color: #526778;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Value labels */\n"
"QLabel#lblInitialVolume,\n"
"QLabel#lblFinalVolume,\n"
"QLabel#lblAlertStatus {\n"
"    color: #087F8C;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 21px;\n"
"    font-weight: bold;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.frameSummary.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameSummary.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameSummary)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frameInitialVolume = QFrame(self.frameSummary)
        self.frameInitialVolume.setObjectName(u"frameInitialVolume")
        self.frameInitialVolume.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameInitialVolume.setFrameShadow(QFrame.Shadow.Raised)
        self.lblInitialTitle = QLabel(self.frameInitialVolume)
        self.lblInitialTitle.setObjectName(u"lblInitialTitle")
        self.lblInitialTitle.setGeometry(QRect(20, 10, 101, 16))
        self.lblInitialTitle.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.lblInitialVolume = QLabel(self.frameInitialVolume)
        self.lblInitialVolume.setObjectName(u"lblInitialVolume")
        self.lblInitialVolume.setGeometry(QRect(20, 40, 111, 21))

        self.horizontalLayout.addWidget(self.frameInitialVolume)

        self.frameFinalVolume = QFrame(self.frameSummary)
        self.frameFinalVolume.setObjectName(u"frameFinalVolume")
        self.frameFinalVolume.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameFinalVolume.setFrameShadow(QFrame.Shadow.Raised)
        self.lblFinalTitle = QLabel(self.frameFinalVolume)
        self.lblFinalTitle.setObjectName(u"lblFinalTitle")
        self.lblFinalTitle.setGeometry(QRect(10, 10, 101, 21))
        self.lblFinalTitle.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.lblFinalVolume = QLabel(self.frameFinalVolume)
        self.lblFinalVolume.setObjectName(u"lblFinalVolume")
        self.lblFinalVolume.setGeometry(QRect(20, 40, 121, 21))

        self.horizontalLayout.addWidget(self.frameFinalVolume)

        self.frameAlertStatus = QFrame(self.frameSummary)
        self.frameAlertStatus.setObjectName(u"frameAlertStatus")
        self.frameAlertStatus.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameAlertStatus.setFrameShadow(QFrame.Shadow.Raised)
        self.lblAlertTitle = QLabel(self.frameAlertStatus)
        self.lblAlertTitle.setObjectName(u"lblAlertTitle")
        self.lblAlertTitle.setGeometry(QRect(10, 10, 81, 21))
        self.lblAlertTitle.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.lblAlertStatus = QLabel(self.frameAlertStatus)
        self.lblAlertStatus.setObjectName(u"lblAlertStatus")
        self.lblAlertStatus.setGeometry(QRect(10, 30, 91, 31))

        self.horizontalLayout.addWidget(self.frameAlertStatus)

        self.frame_5 = QFrame(self.pageResults)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(700, 240, 301, 221))
        self.frame_5.setStyleSheet(u"/* Heading labels */\n"
"QLabel#lblDuration,\n"
"QLabel#lblBladderState{\n"
"    color: #526778;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Value labels */\n"
"QLabel#lbltime,\n"
"QLabel#label_18{\n"
"    color: #087F8C;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 21px;\n"
"    font-weight: bold;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lblDuration = QLabel(self.frame_5)
        self.lblDuration.setObjectName(u"lblDuration")

        self.verticalLayout_3.addWidget(self.lblDuration)

        self.lbltime = QLabel(self.frame_5)
        self.lbltime.setObjectName(u"lbltime")

        self.verticalLayout_3.addWidget(self.lbltime)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblBladderState = QLabel(self.frame_5)
        self.lblBladderState.setObjectName(u"lblBladderState")

        self.verticalLayout.addWidget(self.lblBladderState)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout.addWidget(self.label_18)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.pageResults)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(50, 200, 631, 261))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.graphContainer = QWidget(self.frame_4)
        self.graphContainer.setObjectName(u"graphContainer")

        self.verticalLayout_2.addWidget(self.graphContainer)

        self.label_12 = QLabel(self.pageResults)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(400, 10, 160, 43))
        self.label_12.setStyleSheet(u"font: 700 24pt \"Segoe UI\";")
        self.frame_Navigation = QFrame(self.pageResults)
        self.frame_Navigation.setObjectName(u"frame_Navigation")
        self.frame_Navigation.setGeometry(QRect(30, 470, 951, 61))
        self.frame_Navigation.setStyleSheet(u"/* Bottom navigation frame */\n"
"QFrame#frame_Navigation {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #D5E3E8;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* Back to Setup button */\n"
"QPushButton#btnBack {\n"
"    background-color: #FFFFFF;\n"
"    color: #087F8C;\n"
"    border: 1px solid #087F8C;\n"
"    border-radius: 7px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"/* Back button hover */\n"
"QPushButton#btnBack:hover {\n"
"    background-color: #DDEEF0;\n"
"}\n"
"\n"
"/* Run Again button */\n"
"QPushButton#btnRun {\n"
"    background-color: #087F8C;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 7px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"/* Run Again hover */\n"
"QPushButton#btnRun:hover {\n"
"    background-color: #066773;\n"
"}")
        self.frame_Navigation.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Navigation.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_Navigation)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnBack = QPushButton(self.frame_Navigation)
        self.btnBack.setObjectName(u"btnBack")

        self.horizontalLayout_4.addWidget(self.btnBack)

        self.btnRun = QPushButton(self.frame_Navigation)
        self.btnRun.setObjectName(u"btnRun")

        self.horizontalLayout_4.addWidget(self.btnRun)

        self.label_14 = QLabel(self.pageResults)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(710, 200, 271, 31))
        self.label_14.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.stackedWidget.addWidget(self.pageResults)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1035, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Flowshield", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Bladder Monitoring Setup", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"User Information", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.comboSex.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.comboSex.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Simulation Duration", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"400-600 mL", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Illustrative adult reference range, not an individualized prediction.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Initial Bladder Volume (mL)", None))
        self.comboDuration.setItemText(0, QCoreApplication.translate("MainWindow", u"1 min", None))
        self.comboDuration.setItemText(1, QCoreApplication.translate("MainWindow", u"5 min", None))
        self.comboDuration.setItemText(2, QCoreApplication.translate("MainWindow", u"10 min", None))
        self.comboDuration.setItemText(3, QCoreApplication.translate("MainWindow", u"30 min", None))
        self.comboDuration.setItemText(4, QCoreApplication.translate("MainWindow", u"1 hour", None))
        self.comboDuration.setItemText(5, QCoreApplication.translate("MainWindow", u"2 hours", None))
        self.comboDuration.setItemText(6, QCoreApplication.translate("MainWindow", u"5 hours", None))
        self.comboDuration.setItemText(7, QCoreApplication.translate("MainWindow", u"10 hours", None))
        self.comboDuration.setItemText(8, QCoreApplication.translate("MainWindow", u"24 hours", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Simulation Details", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Reference Bladder Capacity", None))
        self.btnRunSimulation.setText(QCoreApplication.translate("MainWindow", u"Run Simulation", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Bladder Simulation Results", None))
        self.lblInitialTitle.setText(QCoreApplication.translate("MainWindow", u"Initial Volume", None))
        self.lblInitialVolume.setText(QCoreApplication.translate("MainWindow", u"299 mL", None))
        self.lblFinalTitle.setText(QCoreApplication.translate("MainWindow", u"Final Volume", None))
        self.lblFinalVolume.setText(QCoreApplication.translate("MainWindow", u"353 mL", None))
        self.lblAlertTitle.setText(QCoreApplication.translate("MainWindow", u"Final Alert", None))
        self.lblAlertStatus.setText(QCoreApplication.translate("MainWindow", u"Warning", None))
        self.lblDuration.setText(QCoreApplication.translate("MainWindow", u"Duration:", None))
        self.lbltime.setText(QCoreApplication.translate("MainWindow", u"1 hour", None))
        self.lblBladderState.setText(QCoreApplication.translate("MainWindow", u"Current Bladder State:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Filling", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Flowshield", None))
        self.btnBack.setText(QCoreApplication.translate("MainWindow", u"Back to Setup", None))
        self.btnRun.setText(QCoreApplication.translate("MainWindow", u"Run Again", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Simulation Summary", None))
    # retranslateUi

