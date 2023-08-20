import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pymysql
from qt_material import apply_stylesheet
from PyQt5.QtSql import QSqlQuery


class Ui_Register(QWidget):
    SuccessReg = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(834, 600)
        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QRect(260, 60, 400, 420))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_psw2 = QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_psw2, 2, 0, 1, 1)
        self.label_psw1 = QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_psw1, 1, 0, 1, 1)
        self.label_role = QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_role, 3, 0, 1, 1)
        self.label_account = QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_account, 0, 0, 1, 1)
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
        self.label_yanzheng = QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_yanzheng, 9, 0, 1, 1)
        self.ReginAccount = QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.ReginAccount, 0, 1, 1, 1)
        self.PassWord = QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.PassWord, 1, 1, 1, 1)
        self.PassWordSure = QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.PassWordSure, 2, 1, 1, 1)
        self.comboBox =QComboBox(self.gridLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)
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
        self.yanzheng = QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.yanzheng, 9, 1, 1, 1)
        self.ConfirmButton = QPushButton(self)
        self.ConfirmButton.setGeometry(QRect(300, 480, 101, 41))
        self.CancelButton= QPushButton(self)
        self.CancelButton.setGeometry(QRect(520, 480, 101, 41))
        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "注册界面"))
        self.label_psw2.setText(_translate("Form", "请确认密码"))
        self.label_psw1.setText(_translate("Form", "请输入密码"))
        self.label_role.setText(_translate("Form", "用户类型"))
        self.label_account.setText(_translate("Form", "注册账号"))
        self.label_department.setText(_translate("Form", "部门"))
        self.label_name.setText(_translate("Form", "姓名"))
        self.label_age.setText(_translate("Form", "年龄"))
        self.label_job.setText(_translate("Form", "工号"))
        self.label_telephone.setText(_translate("Form", "手机号码"))
        self.label_yanzheng.setText(_translate("Form", "验证码"))
        self.comboBox.setItemText(0, _translate("Form", "工作人员"))
        self.comboBox.setItemText(1, _translate("Form", "操作人员"))
        self.comboBox.setItemText(2, _translate("Form", "管理员"))
        self.ConfirmButton.setText(_translate("Form", "确认"))
        self.CancelButton.setText(_translate("Form", "取消"))

        self.PassWord.setEchoMode(QLineEdit.Password)  # 密码隐藏
        self.PassWordSure.setEchoMode(QLineEdit.Password)
        self.comboBox.setCurrentIndex(99)  # 设置默认值 为空
        self.comboBox.activated.connect(self.emit_identity)  # 当选中下拉框时发射信号
        self.ReginAccount.textChanged.connect(self.emit_Account)  # 注册账号
        self.PassWord.textChanged.connect(self.emit_Password)  # 密码
        self.PassWordSure.textChanged.connect(self.emit_ConPassword)  # 确认密码
        self.ConfirmButton.clicked.connect(self.emit_Confir_Button)  # 确认
        self.CancelButton.clicked.connect(self.emit_Cancel)  # 取消


    def emit_Account(self):
        print("Account发生改变")

    def emit_Username(self):
        print("UserName发生改变")

    def emit_Password(self):
        print("PassWord发生改变")

    def emit_ConPassword(self):
        print("ConPassword发生改变")

    def emit_identity(self):  # 发射身份信号
        print(self.comboBox.currentText())

    def emit_Confir_Button(self):

        Yanzheng = self.yanzheng.text()
        if Yanzheng == 'xust':

            if len(self.PassWord.text()) < 6:
                QMessageBox.information(self, "warning", "密码小于6位")
            elif self.PassWord.text() != self.PassWordSure.text():
                try:
                    QMessageBox.information(self, "error", "两次密码输入不一致")
                except Exception as str:
                    print("未知错误 %s" % (str))
            else:
                conn = pymysql.connect(host='localhost', port=3306, user='', password="", db="mysql")
                cur = conn.cursor()
                conn.commit()
                UserID1 = self.ReginAccount.text()
                PassWord1 = self.PassWord.text()
                UserRole1 = self.comboBox.currentText()
                Department1 =self.department.text()
                Name1 = self.name.text()
                Age1 = self.age.text()
                Job_Number1 = self.job.text()
                Telephone_Number1 = self.telephone.text()
                select_sql = "select UserId,PassWord,UserRole from management WHERE UserId=%s"
                cur.execute(select_sql, [UserID1])
                result = cur.fetchone()
                s = "insert into management(UserId, PassWord, UserRole,Department,Name,Age,Job_Number,Telephone_Number) values( '%s', '%s', '%s','%s','%s','%s','%s','%s')" %\
                    (UserID1, PassWord1, UserRole1,Department1,Name1,Age1,Job_Number1,Telephone_Number1)
                if result is None:
                    try:
                        cur.execute(s)
                        conn.commit()
                        cur.close()
                        conn.close()
                    except:
                        conn.rollback()
                    self.ReginAccount.setText('')
                    self.PassWord.setText('')
                    self.PassWordSure.setText('')
                    self.department.setText('')
                    self.name.setText('')
                    self.age.setText('')
                    self.job.setText('')
                    self.telephone.setText('')
                    self.yanzheng.setText('')
                    self.comboBox.setCurrentIndex(99)  # 设置默认值 为空
                    QMessageBox.information(self, "QAQ", "注册成功")
                else:
                    QMessageBox.information(self, "QAQ", "注册失败, 该账户已经存在")

                self.SuccessReg.emit()
        else:
            self.yanzheng.setText('')
            QMessageBox.information(self, "QAQ", "验证码错误")

    def emit_Cancel(self):
        self.close()
        self.SuccessReg.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow1=Ui_Register()
    apply_stylesheet(app, theme='dark_cyan.xml')

    MainWindow1.show()
    sys.exit(app.exec_())
