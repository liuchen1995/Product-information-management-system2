from PyQt5.QtWidgets import QDialog, QMessageBox, QAbstractItemView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import Qt
from newproducttabledialogueUI import Ui_NewProductTableDialog


class newproducttabledialogue(QDialog):

    def __init__(self, IPaddress, account, password):
        super().__init__()
        self.UI = Ui_NewProductTableDialog()
        self.UI.setupUi(self)

        self.IPaddress = IPaddress
        self.account = account
        self.password = password

        self.UI.pushButton_1.clicked.connect(self.pushButton_1_clicked)
        self.UI.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        self.UI.pushButton_3.clicked.connect(self.pushButton_3_clicked)
        self.UI.pushButton_4.clicked.connect(self.pushButton_4_clicked)

        self.UI.tableView_1.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.UI.tableView_1.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.model = QStandardItemModel()
        self.model.setColumnCount(2)
        self.model.setHeaderData(0, Qt.Horizontal, '名称')
        self.model.setHeaderData(1, Qt.Horizontal, '类型')

        self.UI.tableView_1.setModel(self.model)

    def pushButton_1_clicked(self):
        """添加"""
        addname = self.UI.lineEdit_2.text()
        addtype = self.UI.comboBox_1.currentText()
        addnames = []
        for i in range(self.model.rowCount()):
            addnames.append(self.model.index(i, 0).data())
        if len(addname) == 0:
            QMessageBox.warning(self, "错误", "属性名称不能为空")
        elif addname in addnames:
            QMessageBox.warning(self, "错误", addname + "属性名称已存在")
        else:
            self.model.appendRow([QStandardItem(addname), QStandardItem(addtype)])
            self.UI.tableView_1.setModel(self.model)


    def pushButton_2_clicked(self):
        """删除"""
        selectionmodel = self.UI.tableView_1.selectionModel()
        modelindexlist = selectionmodel.selectedRows()
        for modelindex in modelindexlist:
            self.model.removeRow(modelindex.row())
        self.UI.tableView_1.setModel(self.model)

    def pushButton_3_clicked(self):
        """新建"""

        db = QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName(self.IPaddress)
        db.setUserName(self.account)
        db.setPassword(self.password)
        db.setDatabaseName('project')
        db.open()
        productnames = db.tables()
        addproductname = self.UI.lineEdit_1.text()

        if len(addproductname) == 0:
            QMessageBox.warning(self, "错误", '产品名不能为空')
        elif addproductname in productnames:
            QMessageBox.warning(self, "错误", '数据库中已有该产品')
        elif addproductname[0].isdigit():
            QMessageBox.warning(self, "错误", '产品名开头不能为数字')
        else:
            exword = 'create table ' + addproductname + '(ID int auto_increment primary key,'
            for i in range(self.model.rowCount()):
                # print(self.model.index(i, 0).data(), self.model.index(i, 1).data())
                exword = exword + ' ' + self.model.index(i, 0).data() + ' ' + self.model.index(i, 1).data() + ','
            exword = exword[:-1] + ')'
            query = QSqlQuery()
            query.exec(exword)
            QMessageBox.information(self, '提示', '创建成功')
            self.accept()
        db.close()


    def pushButton_4_clicked(self):
        """取消"""
        self.reject()
