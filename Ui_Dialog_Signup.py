# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\GitHub\LoginUI\Dialog_Signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Signup(object):
    def setupUi(self, Dialog_Signup):
        Dialog_Signup.setObjectName("Dialog_Signup")
        Dialog_Signup.resize(492, 672)
        Dialog_Signup.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.label_signup = QtWidgets.QLabel(Dialog_Signup)
        self.label_signup.setGeometry(QtCore.QRect(170, 80, 181, 51))
        self.label_signup.setStyleSheet("font: 28pt \"Arial\";\n"
"color: rgb(226, 226, 226);")
        self.label_signup.setObjectName("label_signup")
        self.label_Email = QtWidgets.QLabel(Dialog_Signup)
        self.label_Email.setGeometry(QtCore.QRect(40, 230, 71, 41))
        self.label_Email.setStyleSheet("font: 16pt \"Arial\";\n"
"color: rgb(255, 0, 127);")
        self.label_Email.setObjectName("label_Email")
        self.lineEdit_email = QtWidgets.QLineEdit(Dialog_Signup)
        self.lineEdit_email.setGeometry(QtCore.QRect(180, 220, 281, 51))
        self.lineEdit_email.setStyleSheet("font: 12pt \"等线\";\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.label_Password = QtWidgets.QLabel(Dialog_Signup)
        self.label_Password.setGeometry(QtCore.QRect(40, 360, 131, 41))
        self.label_Password.setStyleSheet("font: 16pt \"Arial\";\n"
"color: rgb(255, 0, 127);")
        self.label_Password.setObjectName("label_Password")
        self.lineEdit_password = QtWidgets.QLineEdit(Dialog_Signup)
        self.lineEdit_password.setGeometry(QtCore.QRect(180, 350, 281, 51))
        self.lineEdit_password.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"等线\";")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_Signup = QtWidgets.QPushButton(Dialog_Signup)
        self.pushButton_Signup.setGeometry(QtCore.QRect(300, 560, 161, 41))
        self.pushButton_Signup.setStyleSheet("background-color: rgb(185, 185, 185);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";")
        self.pushButton_Signup.setObjectName("pushButton_Signup")
        self.label_Confirm = QtWidgets.QLabel(Dialog_Signup)
        self.label_Confirm.setGeometry(QtCore.QRect(40, 490, 101, 41))
        self.label_Confirm.setStyleSheet("font: 16pt \"Arial\";\n"
"color: rgb(255, 0, 127);")
        self.label_Confirm.setObjectName("label_Confirm")
        self.lineEdit_confirm = QtWidgets.QLineEdit(Dialog_Signup)
        self.lineEdit_confirm.setGeometry(QtCore.QRect(180, 480, 281, 51))
        self.lineEdit_confirm.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"等线\";")
        self.lineEdit_confirm.setObjectName("lineEdit_confirm")

        self.retranslateUi(Dialog_Signup)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Signup)

    def retranslateUi(self, Dialog_Signup):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Signup.setWindowTitle(_translate("Dialog_Signup", "Dialog"))
        self.label_signup.setText(_translate("Dialog_Signup", "Sign up"))
        self.label_Email.setText(_translate("Dialog_Signup", "Email"))
        self.label_Password.setText(_translate("Dialog_Signup", "Password"))
        self.pushButton_Signup.setText(_translate("Dialog_Signup", "Sign up"))
        self.label_Confirm.setText(_translate("Dialog_Signup", "Confirm"))
