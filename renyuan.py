
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from qt_material import apply_stylesheet
import pymysql
from genggai import Ui_Genggai
from tianjia import Ui_Tianjia



class Ui_table_xinxi(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI(self)

    def setupUI(self, table_xinxi):
        table_xinxi.setObjectName("table_xinxi")
        table_xinxi.resize(860, 516)
        self.tableWidget =QTableWidget(table_xinxi)
        self.tableWidget.setGeometry(QRect(40, 40, 760, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(99999)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item =QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.pushButton_shuaxin = QPushButton(table_xinxi)
        self.pushButton_shuaxin.setGeometry(QRect(70, 420, 121, 41))
        self.pushButton_add = QPushButton(table_xinxi)
        self.pushButton_add.setGeometry(QRect(270, 420, 121, 41))
        self.pushButton_del = QPushButton(table_xinxi)
        self.pushButton_del.setGeometry(QRect(500, 420, 121, 41))
        self.pushButton_xiugai =QPushButton(table_xinxi)
        self.pushButton_xiugai.setGeometry(QRect(700, 420, 121, 41))
        self.retranslateUi(table_xinxi)
        QMetaObject.connectSlotsByName(table_xinxi)
        self.tableWidget

    def retranslateUi(self, table_xinxi):
        _translate = QCoreApplication.translate
        table_xinxi.setWindowTitle(_translate("table_xinxi", "员工信息管理"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("table_xinxi", "账号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("table_xinxi", "密码"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("table_xinxi", "权限"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("table_xinxi", "部门"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("table_xinxi", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("table_xinxi", "年龄"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("table_xinxi", "工号"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("table_xinxi", "手机号码"))
        self.pushButton_del.setText(_translate("table_xinxi", "删除"))
        self.pushButton_add.setText(_translate("table_xinxi", "添加"))
        self.pushButton_shuaxin.setText(_translate("table_xinxi", "刷新"))
        self.pushButton_xiugai.setText(_translate("table_xinxi", "修改"))
        self.duqu()
        self.tableWidget.itemClicked.connect(self.getPosContent)####################点击获取连接槽函数
        #self.tableWidget.currentItemChanged.connect(self.getItem)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pushButton_xiugai.clicked.connect(self.xiugai)
        self.pushButton_del.clicked.connect(self.delete)
        self.pushButton_shuaxin.clicked.connect(self.shuaxin)
        self.pushButton_add.clicked.connect(self.plus)

    def duqu(self):#################################遍历数据库，并将数据库内容读出
        conn = pymysql.connect(host='localhost', port=3306, user='', password="", db="mysql")
        cur = conn.cursor()
        conn.commit()
        # 查询的sql语句
        sql = "SELECT * FROM management"
        cur.execute(sql)
        # 获取查询到的数据, 是以二维元组的形式存储的, 所以读取需要使用 data[i][j] 下标定位
        data = cur.fetchall()
        # 打印测试
        # print(data)
        # print(data[0][0]) # 打印第1行第2个数据, 也就是小明
        x = 0
        for i in data:
            y = 0
            for j in i:
                self.tableWidget.setItem(x, y, QTableWidgetItem(str(data[x][y])))
                y = y + 1
            x = x + 1

    def getPosContent(self,Item = None):###########################获取函数
        # 如果单元格对象为空
        if Item is None:
            return
        else:
            self.row = Item.row()  # 获取行数
            self.col = Item.column()  # 获取列数 注意是column而不是col哦
             # 获取内容
            #self.text = Item.text()
            # 输出测试
            #print('row = ', self.row)
            #print('col =', self.col)

            self.content=self.tableWidget.item(self.row, 0).text()
            #print('text = ', self.dwad)

    def delete(self):#####################删除某一行
        conn = pymysql.connect(host='localhost', port=3306, user='', password="", db="mysql")
        cur = conn.cursor()
        conn.commit()
        print(self.content)
        self.tableWidget.removeRow(self.row)##################删除选中行
        delete_sql = "delete  from management WHERE UserId=%s"
        cur.execute(delete_sql, self.content)
        conn.commit()
        conn.close()

    def shuaxin(self):###############################更新表格数据
        self.tableWidget.clearContents()#############清空表格
        self.duqu()############重新写入

    def xiugai(self):
        self.genggai = Ui_Genggai()
        self.genggai.show()

    def plus(self):
        self.tianjia = Ui_Tianjia()
        self.tianjia.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    a=Ui_table_xinxi()
    apply_stylesheet(app, theme='dark_cyan.xml')

    a.show()
    sys.exit(app.exec_())




