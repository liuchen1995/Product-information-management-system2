from PyQt5.QtWidgets import QApplication
from mainwindow import mainwindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainwindow = mainwindow()

    sys.exit(app.exec_())