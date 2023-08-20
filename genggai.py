import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qt_material import apply_stylesheet
import pymysql

import  csv
class Ui_Genggai(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(834, 600)
        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QRect(260, 60, 400, 420))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_xaunze = QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_xaunze, 0, 0, 1, 1)
        self.label_account = QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_account, 1, 0, 1, 1)
        self.label_psw = QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_psw, 2, 0, 1, 1)
        self.label_role = QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_role, 3, 0, 1, 1)
        self.label_department=QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_department, 4, 0, 1, 1)
        self.label_name = QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_name, 5, 0, 1, 1)
        self.label_age = QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_age, 6, 0, 1, 1)
        self.label_job = QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_job, 7, 0, 1, 1)
        self.label_telephone = QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_telephone, 8, 0, 1, 1)
        self.comobox =QComboBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.comobox, 0, 1, 1, 1)
        self.ReginAccount = QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.ReginAccount, 1, 1, 1, 1)
        self.PassWord = QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.PassWord, 2, 1, 1, 1)
        self.Role =QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.Role, 3, 1, 1, 1)
        self.department = QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.department, 4, 1, 1, 1)
        self.name = QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.name, 5, 1, 1, 1)
        self.age = QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.age, 6, 1, 1, 1)
        self.job = QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.job, 7, 1, 1, 1)
        self.telephone = QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.telephone, 8, 1, 1, 1)
        self.ConfirmButton = QPushButton(self)
        self.ConfirmButton.setGeometry(QRect(300, 480, 101, 41))
        self.CancelButton= QPushButton(self)
        self.CancelButton.setGeometry(QRect(520, 480, 101, 41))
        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "修改信息"))
        self.label_xaunze.setText(_translate("Form", "请选择:"))
        self.label_psw.setText(_translate("Form", "请输入密码:"))
        self.label_role.setText(_translate("Form", "用户类型:"))
        self.label_account.setText(_translate("Form", "注册账号:"))
        self.label_department.setText(_translate("Form", "部门:"))
        self.label_name.setText(_translate("Form", "姓名:"))
        self.label_age.setText(_translate("Form", "年龄:"))
        self.label_job.setText(_translate("Form", "工号:"))
        self.label_telephone.setText(_translate("Form", "手机号码:"))
        self.ConfirmButton.setText(_translate("Form", "确认"))
        self.CancelButton.setText(_translate("Form", "返回"))
        conn = pymysql.connect(host='localhost', port=3306, user='', password="", db="mysql")
        cur = conn.cursor()
        conn.commit()
        select_sql = "select UserId from management"
        cur.execute(select_sql)
        result = cur.fetchall()
        #####################从数据库中获取UserId
        a=[0,12,32,321,321,5315,1212,3,5315,13,123,151,2312,321,5315,53155315,1,3,2,321,3,45,6,4,1233,123,2113,12312,3123,325,346,23,4123,13213,1242,12]
        for i in range(len(result)):
            a[i]=str(result[i]).replace("(","")
            a[i]=a[i].replace(")","")
            a[i] = a[i].replace("(", "")
            a[i] = a[i].replace(",", "")
            a[i] = a[i].replace("'", "")
        #print(a)
        print(len(result))
        #########################将UserId写入下拉框
        for i in range(len(result)):
            self.comobox.addItem(str(a[i]))

        self.comobox.activated.connect(self.huoqu)
        self.ConfirmButton.clicked.connect(self.change)
        self.CancelButton.clicked.connect(self.cancel)


    def huoqu(self,text):###################################将选中的信息显示出来
        self.id=self.comobox.itemText(text)
        conn = pymysql.connect(host='localhost', port=3306, user='', password="", db="mysql")
        cur = conn.cursor()
        conn.commit()
        select_sql = "select UserId,PassWord,UserRole,Department,Name,Age,Job_Number,Telephone_Number from management WHERE UserId=%s"
        cur.execute(select_sql, self.id)
        result = cur.fetchone()
        self.ReginAccount.setText(result[0])
        self.PassWord.setText(result[1])
        self.Role.setText(result[2])
        self.department.setText(result[3])
        self.name.setText(result[4])
        self.age.setText(result[5])
        self.job.setText(result[6])
        self.telephone.setText(result[7])
        conn.close()

    def change(self):
        conn = pymysql.connect(host='localhost', port=3306, user='', password="", db="mysql")
        cur = conn.cursor()
        conn.commit()
        delete_sql = "delete  from management WHERE UserId=%s"#############在数据库中删除
        cur.execute(delete_sql, self.id)
        conn.commit()
        UserID1=self.ReginAccount.text()
        PassWord1 =self.PassWord.text()
        UserRole1 =self.Role.text()
        Department1 =self.department.text()
        Name1 = self.name.text()
        Age1 = self.age.text()
        Job_Number1 =self.job.text()
        Telephone_Number1 =self.telephone.text()
        s = "insert into management(UserId, PassWord, UserRole,Department,Name,Age,Job_Number,Telephone_Number) values( '%s', '%s', '%s','%s','%s','%s','%s','%s')" % \
            (UserID1, PassWord1, UserRole1, Department1, Name1, Age1, Job_Number1, Telephone_Number1)
        cur.execute(s)
        ########################重新插入
        conn.commit()
        conn.close()
        QMessageBox.information(self, "提示", "修改成功")

    def cancel(self):#####################返回函数
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow1=Ui_Genggai()
    apply_stylesheet(app, theme='dark_cyan.xml')

    MainWindow1.show()
    sys.exit(app.exec_())