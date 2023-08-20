import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


from hello import *
import json
import glo


class Ui_Table(QTableWidget):
    def __init__(self):
        super(Ui_Table, self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("数据")
        self.resize(600,400)
        layout = QHBoxLayout()
        self.tablewidget = QTableWidget()
        self.tablewidget.setRowCount(200)
        self.tablewidget.setColumnCount(3)
        layout.addWidget(self.tablewidget)
        self.tablewidget.setHorizontalHeaderLabels(['煤像素点','煤占比','  '])
        self.setLayout(layout)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    Table=Ui_Table()
    Table.show()
    sys.exit(app.exec_())
