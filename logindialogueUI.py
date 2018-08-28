# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logindialogueUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(270, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginDialog.sizePolicy().hasHeightForWidth())
        LoginDialog.setSizePolicy(sizePolicy)
        LoginDialog.setMinimumSize(QtCore.QSize(270, 150))
        LoginDialog.setMaximumSize(QtCore.QSize(270, 150))
        self.gridLayout_2 = QtWidgets.QGridLayout(LoginDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtWidgets.QWidget(LoginDialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_login = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout.addWidget(self.pushButton_login)
        self.pushButton_exit = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout.addWidget(self.pushButton_exit)
        self.gridLayout_2.addWidget(self.widget_2, 2, 0, 1, 1)
        self.widget = QtWidgets.QWidget(LoginDialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_IPaddress = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_IPaddress.setObjectName("lineEdit_IPaddress")
        self.gridLayout.addWidget(self.lineEdit_IPaddress, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_account = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.gridLayout.addWidget(self.lineEdit_account, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "登录"))
        self.pushButton_login.setText(_translate("LoginDialog", "登录"))
        self.pushButton_exit.setText(_translate("LoginDialog", "退出"))
        self.label.setText(_translate("LoginDialog", "IP地址"))
        self.label_2.setText(_translate("LoginDialog", "账号"))
        self.label_3.setText(_translate("LoginDialog", "密码"))

