from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtSql import QSqlDatabase
from logindialogueUI import Ui_LoginDialog


class logindialogue(QDialog):

    def __init__(self):
        super().__init__()
        self.UI = Ui_LoginDialog()
        self.UI.setupUi(self)


        # 测试使用
        self.UI.lineEdit_IPaddress.setText("localhost")
        self.UI.lineEdit_account.setText('root')
        self.UI.lineEdit_password.setText('Jiqirenxueyuan@308')


        self.UI.pushButton_exit.clicked.connect(self.close)
        self.UI.pushButton_login.clicked.connect(self.pushButton_login_clicked)

    def pushButton_login_clicked(self):
        self.IPaddress = self.UI.lineEdit_IPaddress.text()
        self.account = self.UI.lineEdit_account.text()
        self.password = self.UI.lineEdit_password.text()

        db = QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName(self.IPaddress)
        db.setUserName(self.account)
        db.setPassword(self.password)
        db.setDatabaseName('project')

        if not db.open():
            QMessageBox.warning(self, "错误", "连接失败")
        else:
            db.close()
            self.accept()