# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 482)
        MainWindow.setStyleSheet("border-radius:10px ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border-radius:20px ")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop:0 rgb(26, 148, 190), stop:1 rgb(58, 209, 177));\n"
"border-radius:20px ")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.frame_4 = QtWidgets.QFrame(self.frame_6)
        self.frame_4.setStyleSheet("QFrame{\n"
"    image: none;\n"
"background-color: rgba(255, 255, 255, 20%);\n"
"border-radius:6px \n"
"}\n"
"QLabel{\n"
"\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setContentsMargins(24, 24, 24, 8)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 24)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_eye = QtWidgets.QPushButton(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_eye.setFont(font)
        self.pushButton_eye.setObjectName("pushButton_eye")
        self.verticalLayout_8.addWidget(self.pushButton_eye)
        self.verticalLayout_7.addWidget(self.frame_12)
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.LineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.LineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LineEdit.setFont(font)
        self.LineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LineEdit.setStyleSheet("border-radius:8px ;color:rgb(37, 2, 176)")
        self.LineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LineEdit.setObjectName("LineEdit")
        self.verticalLayout_7.addWidget(self.LineEdit)
        self.frame_16 = QtWidgets.QFrame(self.frame_4)
        self.frame_16.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lcd = QtWidgets.QLCDNumber(self.frame_16)
        self.lcd.setMinimumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lcd.setFont(font)
        self.lcd.setSmallDecimalPoint(False)
        self.lcd.setDigitCount(10)
        self.lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd.setObjectName("lcd")
        self.verticalLayout_10.addWidget(self.lcd)
        self.frame_14 = QtWidgets.QFrame(self.frame_16)
        self.frame_14.setMinimumSize(QtCore.QSize(0, 48))
        self.frame_14.setStyleSheet("border-radius:16px ;\n"
"background-color: rgba(255, 255, 255, 51);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setSpacing(12)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.startButton = QtWidgets.QPushButton(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("border-radius:8px ;")
        self.startButton.setFlat(False)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_8.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.frame_14)
        self.stopButton.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet("border-radius:8px ;")
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_8.addWidget(self.stopButton)
        self.resetButton = QtWidgets.QPushButton(self.frame_14)
        self.resetButton.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.resetButton.setFont(font)
        self.resetButton.setStyleSheet("border-radius:8px ;")
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_8.addWidget(self.resetButton)
        self.verticalLayout_10.addWidget(self.frame_14)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem2)
        self.exitButton = QtWidgets.QPushButton(self.frame_16)
        self.exitButton.setMinimumSize(QtCore.QSize(0, 48))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(11, 11, 11);\n"
"    border-radius:20px ;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout_10.addWidget(self.exitButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem3)
        self.verticalLayout_7.addWidget(self.frame_16)
        self.horizontalLayout_2.addWidget(self.frame_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_eye.setText(_translate("MainWindow", "睁眼"))
        self.label.setText(_translate("MainWindow", "设定时间（min）："))
        self.LineEdit.setText(_translate("MainWindow", "4"))
        self.startButton.setText(_translate("MainWindow", "开始"))
        self.stopButton.setText(_translate("MainWindow", "停止"))
        self.resetButton.setText(_translate("MainWindow", "复位"))
        self.exitButton.setText(_translate("MainWindow", "连接设备"))
import resources_rc
