# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PipeDectection(object):
    def setupUi(self, PipeDectection):
        PipeDectection.setObjectName("PipeDectection")
        PipeDectection.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(PipeDectection)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 180, 1240, 600))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 30, 540, 540))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Background.jpeg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(660, 30, 540, 540))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Background.jpeg"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 30, 160, 120))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 30, 160, 120))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 30, 160, 120))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 30, 160, 120))
        self.pushButton_4.setObjectName("pushButton_4")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(1060, 30, 160, 120))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['请选择管类型','    超小型管','      小型管','      中型管','      大型管'])

        PipeDectection.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PipeDectection)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        PipeDectection.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PipeDectection)
        self.statusbar.setObjectName("statusbar")
        PipeDectection.setStatusBar(self.statusbar)

        self.retranslateUi(PipeDectection)
        QtCore.QMetaObject.connectSlotsByName(PipeDectection)

    def retranslateUi(self, PipeDectection):
        _translate = QtCore.QCoreApplication.translate
        PipeDectection.setWindowTitle(_translate("PipeDectection", "PipeDectection"))
        self.groupBox.setTitle(_translate("PipeDectection", "当前图片区"))
        # self.groupBox_2.setTitle(_translate("PipeDectection", "历史图片区"))
        self.pushButton.setText(_translate("PipeDectection", "运行"))
        self.pushButton.setStyleSheet("QPushButton{font-family:'宋体';font-size:30px;}")
        
        self.pushButton_2.setText(_translate("PipeDectection", "调试模式"))
        self.pushButton_2.setStyleSheet("QPushButton{font-family:'宋体';font-size:30px;}")

        self.pushButton_3.setText(_translate("PipeDectection", "关机"))
        self.pushButton_3.setStyleSheet("QPushButton{font-family:'宋体';font-size:30px;}")

        self.pushButton_4.setText(_translate("PipeDectection", "重启"))
        self.pushButton_4.setStyleSheet("QPushButton{font-family:'宋体';font-size:30px;}")


