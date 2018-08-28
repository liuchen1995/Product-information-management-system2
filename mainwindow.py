from PyQt5.QtWidgets import QMainWindow, QMessageBox, QAbstractItemView
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from re import search

from mainwindowUI import Ui_MainWindow
from logindialogue import logindialogue
from newproducttabledialogue import newproducttabledialogue

class mainwindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)

        self.UI.action_mn1_1.triggered.connect(self.action_mn1_1_triggered)
        self.UI.action_mn1_2.triggered.connect(self.close)
        self.UI.action_mn2_1.triggered.connect(self.action_mn2_1_triggered)
        self.UI.action_mn2_2.triggered.connect(self.action_mn2_2_triggered)

        self.UI.listView_pg1_gp1_1.clicked.connect(self.listView_pg1_gp1_1_clicked)
        self.UI.listView_pg1_gp1_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.UI.pushButton_pg1_gp1_1.clicked.connect(self.pushButton_pg1_gp1_1_clicked)
        self.UI.pushButton_pg1_gp1_2.clicked.connect(self.pushButton_pg1_gp1_2_clicked)
        self.UI.pushButton_pg1_gp1_3.clicked.connect(self.pushButton_pg1_gp1_3_clicked)

        self.UI.pushButton_pg1_gp2_1.clicked.connect(self.pushButton_pg1_gp2_1_clicked)
        self.UI.pushButton_pg1_gp2_2.clicked.connect(self.pushButton_pg1_gp2_2_clicked)
        self.UI.pushButton_pg1_gp2_3.clicked.connect(self.pushButton_pg1_gp2_3_clicked)
        self.UI.pushButton_pg1_gp2_4.clicked.connect(self.pushButton_pg1_gp2_4_clicked)
        self.UI.pushButton_pg1_gp2_5.clicked.connect(self.pushButton_pg1_gp2_5_clicked)

        self.UI.stackedWidget.setCurrentIndex(2)
        self.show()

        logindialog = logindialogue()
        if logindialog.exec_():
            self.IPaddress = logindialog.IPaddress
            self.account = logindialog.account
            self.password = logindialog.password
        else:
            self.close()

    def action_mn1_1_triggered(self):
        """主菜单注销"""
        self.UI.stackedWidget.setCurrentIndex(2)
        logindialog = logindialogue()
        if logindialog.exec_():
            self.IPaddress = logindialog.IPaddress
            self.account = logindialog.account
            self.password = logindialog.password
        else:
            self.close()

    def action_mn2_1_triggered(self):
        """主菜单，产品，管理"""
        self.UI.stackedWidget.setCurrentIndex(0)
        self.UI.groupBox_pg1_2.setDisabled(True)

        db = QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName(self.IPaddress)
        db.setUserName(self.account)
        db.setPassword(self.password)
        db.setDatabaseName('project')
        db.open()

        self.standarditemmodel = QStandardItemModel()
        for i in db.tables():
            t = QStandardItem(i)
            t.setTextAlignment(Qt.AlignCenter)
            self.standarditemmodel.appendRow(t)
        self.UI.listView_pg1_gp1_1.setModel(self.standarditemmodel)

        db.close()

    def action_mn2_2_triggered(self):
        """主菜单，产品，分析"""
        self.UI.stackedWidget.setCurrentIndex(1)

    def pushButton_pg1_gp1_1_clicked(self):
        """第0页，第一组，删除按钮"""
        selectionmodel = self.UI.listView_pg1_gp1_1.selectionModel()
        modelindexlist = selectionmodel.selectedRows()
        for i in modelindexlist:
            reply = QMessageBox.question(self, "提示", "确定要删除" + i.data() + "产品的所有数据", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                query = QSqlQuery()
                query.exec("drop table " + i.data())
                self.standarditemmodel.removeRow(i.row())

    def pushButton_pg1_gp1_2_clicked(self):
        """第0页，第一组，新建按钮"""
        newproducttabledialog = newproducttabledialogue(self.IPaddress, self.account, self.password)
        if newproducttabledialog.exec_():
            db = QSqlDatabase.addDatabase('QMYSQL')
            db.setHostName(self.IPaddress)
            db.setUserName(self.account)
            db.setPassword(self.password)
            db.setDatabaseName('project')
            db.open()
            self.standarditemmodel = QStandardItemModel()
            for i in db.tables():
                t = QStandardItem(i)
                t.setTextAlignment(Qt.AlignCenter)
                self.standarditemmodel.appendRow(t)
            self.UI.listView_pg1_gp1_1.setModel(self.standarditemmodel)
            db.close()
        self.UI.groupBox_pg1_2.setDisabled(True)


    def pushButton_pg1_gp1_3_clicked(self):
        """第0页，第一组，查询按钮"""
        keyword = str(self.UI.lineEdit_pg1_gp1_1.text())
        db = QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName(self.IPaddress)
        db.setUserName(self.account)
        db.setPassword(self.password)
        db.setDatabaseName('project')
        db.open()
        self.standarditemmodel = QStandardItemModel()
        for i in db.tables():
            if search(keyword, i):
                t = QStandardItem(i)
                t.setTextAlignment(Qt.AlignCenter)
                self.standarditemmodel.appendRow(t)
        self.UI.listView_pg1_gp1_1.setModel(self.standarditemmodel)
        db.close()


    def listView_pg1_gp1_1_clicked(self, index):
        """"第0页，第一组，列表被点击"""
        self.UI.groupBox_pg1_2.setDisabled(False)
        self.UI.groupBox_pg1_2.setTitle(index.data() + '数据：')
        self.UI.comboBox_pg1_gp2_1.clear()
        self.sqltablemodel = QSqlTableModel()
        self.sqltablemodel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.sqltablemodel.setTable(index.data())
        self.sqltablemodel.select()
        for i in range(self.sqltablemodel.columnCount()):
            self.UI.comboBox_pg1_gp2_1.addItem(self.sqltablemodel.headerData(i, Qt.Horizontal))
        self.UI.tableView_pg1_gp2_1.setModel(self.sqltablemodel)

    def pushButton_pg1_gp2_1_clicked(self):
        """第0页，第二组， 增加按钮"""
        record = self.sqltablemodel.record()
        self.sqltablemodel.insertRecord(self.sqltablemodel.rowCount(), record)

    def pushButton_pg1_gp2_2_clicked(self):
        """第0页，第二组， 删除按钮"""
        selectionmodel = self.UI.tableView_pg1_gp2_1.selectionModel()
        modelindexlist = selectionmodel.selectedRows()
        for i in modelindexlist:
            self.sqltablemodel.removeRow(i.row())

    def pushButton_pg1_gp2_3_clicked(self):
        """第0页，第二组， 确定按钮"""
        if self.sqltablemodel.submitAll():
            QMessageBox.information(self, '提示', '提交成功')
        else:
            QMessageBox.warning(self, '错误', 'ID相同，提交失败')

    def pushButton_pg1_gp2_4_clicked(self):
        """第0页，第二组， 取消按钮"""
        self.sqltablemodel.revertAll()
        self.sqltablemodel.submitAll()

    def pushButton_pg1_gp2_5_clicked(self):
        """第0页，第二组， 查找按钮"""
        if len(self.UI.lineEdit_pg1_gp2_1.text()):
            filterword = self.UI.comboBox_pg1_gp2_1.currentText() + ' = ' + self.UI.lineEdit_pg1_gp2_1.text()
            self.sqltablemodel.setFilter(filterword)
            self.sqltablemodel.select()
        else:
            self.sqltablemodel.setFilter('')
            self.sqltablemodel.select()