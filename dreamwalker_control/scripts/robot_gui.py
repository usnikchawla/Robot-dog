#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot_gui4.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

import sys
import rospy
from PyQt5 import QtCore, QtGui, QtWidgets
from std_msgs.msg import String, Float32, Int32
from sensor_msgs.msg import Range
from dreamwalker_control.srv import Service_GUI_Command, Service_GUI_CommandResponse

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):

    #service client
    rospy.wait_for_service('command_service')
    commanded_service = rospy.ServiceProxy('command_service', Service_GUI_Command)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(420, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_forward = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_forward.setGeometry(QtCore.QRect(160, 40, 100, 80))
        self.pushButton_forward.setObjectName(_fromUtf8("pushButton_forward"))
        self.pushButton_backward = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_backward.setGeometry(QtCore.QRect(160, 220, 100, 80))
        self.pushButton_backward.setObjectName(_fromUtf8("pushButton_backward"))
        self.pushButton_right = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_right.setGeometry(QtCore.QRect(290, 120, 80, 100))
        self.pushButton_right.setObjectName(_fromUtf8("pushButton_right"))
        self.pushButton_left = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_left.setGeometry(QtCore.QRect(50, 120, 80, 100))
        self.pushButton_left.setObjectName(_fromUtf8("pushButton_left"))
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(170, 130, 80, 80))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName(_fromUtf8("pushButton_stop"))
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 350, 360, 200))
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton_spinLEFT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_spinLEFT.setGeometry(QtCore.QRect(50, 50, 90, 50))
        self.pushButton_spinLEFT.setObjectName(_fromUtf8("pushButton_spinLEFT"))
        self.pushButton_spinRIGHT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_spinRIGHT.setGeometry(QtCore.QRect(280, 50, 90, 50))
        self.pushButton_spinRIGHT.setObjectName(_fromUtf8("pushButton_spinRIGHT"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 320, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 610, 89, 25))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 610, 121, 25))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 570, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #QtCore.QObject.connect(self.pushButton_backward, QtCore.SIGNAL(_fromUtf8("clicked()")), self.goBackward)
        self.pushButton_backward.clicked.connect(self.goBackward)
        #QtCore.QObject.connect(self.pushButton_forward, QtCore.SIGNAL(_fromUtf8("clicked()")), self.goForward)
        self.pushButton_forward.clicked.connect(self.goForward)
        #QtCore.QObject.connect(self.pushButton_right, QtCore.SIGNAL(_fromUtf8("clicked()")), self.goRight)
        self.pushButton_right.clicked.connect(self.goRight)
        #QtCore.QObject.connect(self.pushButton_left, QtCore.SIGNAL(_fromUtf8("clicked()")), self.goLeft)
        self.pushButton_left.clicked.connect(self.goLeft)
        #QtCore.QObject.connect(self.pushButton_stop, QtCore.SIGNAL(_fromUtf8("clicked()")), self.stopMovement)
        self.pushButton_stop.clicked.connect(self.stopMovement)
        #QtCore.QObject.connect(self.pushButton_spinRIGHT, QtCore.SIGNAL(_fromUtf8("clicked()")), self.spinRight)
        self.pushButton_spinRIGHT.clicked.connect(self.spinRight)
        #QtCore.QObject.connect(self.pushButton_spinLEFT, QtCore.SIGNAL(_fromUtf8("clicked()")), self.spinLeft)
        self.pushButton_spinLEFT.clicked.connect(self.spinLeft)
        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.manual)
        self.pushButton.clicked.connect(self.manual)
        #QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.autonomous)
        self.pushButton_2.clicked.connect(self.autonomous)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_forward.setText(_translate("MainWindow", "FORWARD", None))
        self.pushButton_backward.setText(_translate("MainWindow", "BACKWARD", None))
        self.pushButton_right.setText(_translate("MainWindow", "RIGHT", None))
        self.pushButton_left.setText(_translate("MainWindow", "LEFT", None))
        self.pushButton_stop.setText(_translate("MainWindow", "STOP", None))
        self.pushButton_spinLEFT.setText(_translate("MainWindow", "SPIN LEFT", None))
        self.pushButton_spinRIGHT.setText(_translate("MainWindow", "SPIN RIGHT", None))
        self.label.setText(_translate("MainWindow", "Log info", None))
        self.pushButton.setText(_translate("MainWindow", "MANUAL", None))
        self.pushButton_2.setText(_translate("MainWindow", "AUTONOMOUS", None))
        self.label_2.setText(_translate("MainWindow", "Mode", None))

    def goBackward(self):
        command = self.commanded_service("BACKWARD")
        obtained_feedback = command.response
        self.textBrowser.append(obtained_feedback)

    def goForward(self):
        command = self.commanded_service("FORWARD")
        obtained_feedback = command.response
        self.textBrowser.append(obtained_feedback)

    def goRight(self):
        command = self.commanded_service("RIGHT")
        obtained_feedback = command.response
        self.textBrowser.append(obtained_feedback)

    def goLeft(self):
        command = self.commanded_service("LEFT")
        obtained_feedback = command.response
        self.textBrowser.append(obtained_feedback)

    def spinRight(self):
        command = self.commanded_service("SPIN_RIGHT")
        obtained_feedback = command.response
        self.textBrowser.append(obtained_feedback)

    def spinLeft(self):
        command = self.commanded_service("SPIN_LEFT")
        obtained_feedback = command.response
        self.textBrowser.append(obtained_feedback)

    def stopMovement(self):
        command = self.commanded_service("STOP")
        obtained_feedback = command.response
        self.textBrowser.append(obtained_feedback)

    def manual(self):
        command = self.commanded_service("MANUAL")
        obtained_feedback = command.response
        self.textBrowser.append(obtained_feedback)

    def autonomous(self):
        command = self.commanded_service("AUTO")
        obtained_feedback = command.response
        self.textBrowser.append(obtained_feedback)


if __name__ == "__main__":
    rospy.init_node('gui_node')
    r = rospy.Rate(100)
    rospy.loginfo("GUI initialized, let's get started!")

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
