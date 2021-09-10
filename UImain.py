import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDial, QDialog, QApplication
from PyQt5.QtGui import *
from Ui_Dialog_Login import *
from Ui_Dialog_Signup import *
 
class Ui_Login(QDialog,Ui_Dialog_Login):  
 
    def __init__(self): 
        super(Ui_Login, self).__init__()
        self.setupUi(self)
        # 将点击事件与槽函数进行连接
        self.pushButton_Login.clicked.connect(self.loginfunction)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_CreateAcc.clicked.connect(self.gotoCreateAcc)
    def loginfunction(self):
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()
        print("Successfully logged in with email:", email, "and password",password)
    def gotoCreateAcc(self):
        createAcc = CreateAcc()
        widget.addWidget(createAcc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QDialog,Ui_Dialog_Signup):  
 
    def __init__(self): 
        super(CreateAcc, self).__init__()
        self.setupUi(self)
        # 将点击事件与槽函数进行连接
        self.pushButton_Signup.clicked.connect(self.signupfunction)
    def signupfunction(self):
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()
        print("Successfully create account with email:", email, "and password",password)
    def gotoCreateAcc():
        createAcc = CreateAcc()
        widget.addWidget(createAcc)
        widget.setCurrentIndex(widget.currentIndex()+1)

if __name__ == '__main__': 
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Login()
    widget = QtWidgets.QStackedWidget() 
    widget.addWidget(window)
    widget.setFixedHeight(672)
    widget.setFixedWidth(492)
    widget.show() 
    sys.exit(app.exec_())