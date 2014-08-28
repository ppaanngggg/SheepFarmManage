from PyQt5.QtWidgets import *

class CLogin_Database_Dialog(QDialog):
    def __init__(self,user_and_passwd, parent=None):
        super(CLogin_Database_Dialog, self).__init__(parent)

        self.user_and_passwd=user_and_passwd

        self.label_user=QLabel('用户名：')
        self.edit_user=QLineEdit()
        self.label_passwd=QLabel('密码：')
        self.edit_passwd=QLineEdit()
        self.edit_passwd.setEchoMode(QLineEdit.Password)
        self.button_login=QPushButton('登录')
        self.button_login.clicked.connect(self.button_login_clicked)

        self.layout_login=QGridLayout()
        self.layout_login.addWidget(self.label_user,0,0)
        self.layout_login.addWidget(self.edit_user,0,1)
        self.layout_login.addWidget(self.label_passwd,1,0)
        self.layout_login.addWidget(self.edit_passwd,1,1)
        self.layout_login.addWidget(self.button_login,2,1)

        self.setWindowTitle('登录数据库')
        self.setLayout(self.layout_login)

    def button_login_clicked(self):
        self.user_and_passwd[0]=self.edit_user.text()
        self.user_and_passwd[1]=self.edit_passwd.text()
        self.accept()