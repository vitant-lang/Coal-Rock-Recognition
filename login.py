import sys
import time
from regist import *
import pymysql
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from gongneng_admin import *
from gongneng_caozuo import *
from gongneng_gongzuo import *
#from hello import *
from qt_material import apply_stylesheet
extra = {

    # Button colors
    'danger': '#dc3545',
    'warning': '#ffc107',
    #'success': '#17a2b8',
    'success': '#2dca1c',

    'font_family': 'Roboto',
    #'font_size': '13px',
    #'line_height': '13px',

    # Density
    #'density_scale': '0',

    # Button Shape
    'button_shape': 'default',

    'density_scale': '-1',
}

global UserName
UserP = {}

class Ui_MainWindow1(QMainWindow):

     def paintEvent(self,event):
         painter = QPainter(self)
         pixmap = QPixmap("denglu.png")#登录界面背景
         painter.drawPixmap(self.rect(), pixmap)

     def __init__(self):
         super(Ui_MainWindow1,self).__init__()
         self.setupUi(self)
         self.retranslateUi(self)
         self.paintEvent(self)

     def setupUi(self, MainWindow1):
         MainWindow1.setObjectName("MainWindow")
         MainWindow1.resize(800, 600)
         MainWindow1.setWindowIcon(QIcon('denglulog.png'))#登录界面图标
         self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)

         self.centralWidget = QWidget(MainWindow1)
         self.centralWidget.setObjectName("centralWidget")

         self.lineEdit = QLineEdit(self.centralWidget)
         self.lineEdit.setGeometry(QRect(400, 200, 150, 30))
         self.lineEdit.setText("")
         self.lineEdit_2 =QLineEdit(self.centralWidget)
         self.lineEdit_2.setGeometry(QRect(400, 250, 150, 30))
         self.lineEdit_2.setText("")
         self.lineEdit_2.setEchoMode(QLineEdit.Password)
         self.label = QLabel(self.centralWidget)
         self.label.setGeometry(QRect(350, 200, 50, 30))
         self.label.setTextFormat(Qt.AutoText)
         self.label_2 = QLabel(self.centralWidget)
         self.label_2.setGeometry(QRect(350, 250, 50, 30))
         self.pushButton = QPushButton(self.centralWidget)
         self.pushButton.setGeometry(QRect(350, 300, 80, 40))
         self.pushButton_2 = QPushButton(self.centralWidget)
         self.pushButton_2.setGeometry(QRect(490, 300, 80, 40))
         MainWindow1.setCentralWidget(self.centralWidget)
         self.pushButton.clicked.connect(self.login_button)############登录确定
         self.regist = Ui_Register()
         self.pushButton_2.clicked.connect(self.regist.show)##########注册
         self.retranslateUi(MainWindow1)
         QMetaObject.connectSlotsByName(MainWindow1)

         self.pushButton.setStyleSheet(''' 
                                      QPushButton
                                      {text-align : center;
                                      background-color : light gray;
                                      font: bold;
                                      border-color: gray;
                                      border-width: 2px;
                                      border-radius: 10px;
                                      padding: 6px;
                                      height : 14px;
                                      border-style: outset;
                                      font : 14px;}
                                      QPushButton:pressed
                                      {text-align : center;
                                      background-color : rgb(44,137,255);
                                      font: bold;
                                      border-color: gray;
                                      border-width: 2px;
                                      border-radius: 10px;
                                      padding: 6px;
                                      height : 14px;
                                      border-style: outset;
                                      font : 14px;}
                                      ''')
         self.pushButton_2.setStyleSheet(''' 
                                               QPushButton
                                               {text-align : center;
                                               background-color : light gray;
                                               font: bold;
                                               border-color: gray;
                                               border-width: 2px;
                                               border-radius: 10px;
                                               padding: 6px;
                                               height : 14px;
                                               border-style: outset;
                                               font : 14px;}
                                               QPushButton:pressed
                                               {text-align : center;
                                               background-color : rgb(44,137,255);
                                               font: bold;
                                               border-color: gray;
                                               border-width: 2px;
                                               border-radius: 10px;
                                               padding: 6px;
                                               height : 14px;
                                               border-style: outset;
                                               font : 14px;}
                                               ''')

     def retranslateUi(self, MainWindow1):
         _translate = QCoreApplication.translate
         MainWindow1.setWindowTitle(_translate("MainWindow1", "欢迎"))
         self.lineEdit.setPlaceholderText(_translate("MainWindow1", "请输入帐号"))
         self.lineEdit_2.setPlaceholderText(_translate("MainWindow1", "请输入密码"))
         self.label.setText(_translate("MainWindow1", "帐号:"))
         self.label_2.setText(_translate("MainWindow1", "密码:"))
         self.pushButton.setText(_translate("MainWindow1", "确定"))
         self.pushButton_2.setText(_translate("MainWindow1", "注册"))




     def login_button(self):

         # if QSqlDatabase.contains("qt_sql_default_connection"):
         # db = QSqlDatabase.database("qt_sql_default_connection")
         # else:
         # db = QSqlDatabase.addDatabase("QMYSQL")
         conn = pymysql.connect(host='localhost', port=3306, user='', password="", db="mysql")
         cur = conn.cursor()
         conn.commit()
         Login_User = self.lineEdit.text()
         Login_Passwd = self.lineEdit_2.text()
         # print(type(Login_User))
         # print(type(Login_Passwd))

         if Login_User == 0 or Login_Passwd.strip() == '':
             QMessageBox.information(self, "error", "输入错误")
         else:
             # self.config_ini()  # 加载用户密码配置文件
             select_sql = "select UserId,PassWord,UserRole from management WHERE UserId=%s"
             cur.execute(select_sql, [Login_User])
             result = cur.fetchone()

             if result[0] == Login_User and result[1] == Login_Passwd:  # 密码和账号都对的情况下
                 if result[2]=="工作人员":

                     """跳转到主界面"""
                     self.close()
                     self.Progressbar_gongzuo = Ui_ProgressBar_gongzuo()
                     self.Progressbar_gongzuo.show()
                     return True
                 elif result[2]=='操作人员':

                     """跳转到主界面"""
                     self.close()
                     self.Progressbar_caozuo = Ui_ProgressBar_caozuo()
                     self.Progressbar_caozuo.show()
                     return True
                 elif result[2]=='管理员':

                     """跳转到主界面"""
                     self.close()
                     self.Progressbar_admin = Ui_ProgressBar_admin()
                     self.Progressbar_admin.show()
                     return True
             elif result[0] != Login_User :
                 QMessageBox.information(self, "waining", "账号不存在", QMessageBox.Ok)
                 return False
             elif result[0] == Login_User and result[1] != Login_Passwd:
                 QMessageBox.information(self, "error!", "密码输入错误", QMessageBox.Ok)
                 return False

class Ui_ProgressBar_gongzuo(QWidget):
    def __init__(self, parent=None):
        super(Ui_ProgressBar_gongzuo, self).__init__(parent)
        self.initUI()
        #self.hello = Ui_Hello()
        self.gongzuo =Ui_MainWindow_gongzuo()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("www.jpg")#进度条背景
        painter.drawPixmap(self.rect(), pixmap)

    def initUI(self):
        self.resize(500, 32)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.progressBar_gongzuo = QProgressBar(self)
        self.progressBar_gongzuo.setMinimum(0)
        self.progressBar_gongzuo.setMaximum(100)
        self.progressBar_gongzuo.setValue(0)
        self.progressBar_gongzuo.setGeometry(QRect(1, 80, 499, 28))
        self.timer_gongzuo = QBasicTimer()
        self.step_gongzuo = 0
        self.setGeometry(300, 300, 550, 200)
        self.setWindowTitle('系统登录中...')
        self.show()
        self.timer_gongzuo.start(100, self)

    def timerEvent(self, e):
        if self.step_gongzuo >= 100:
            self.timer_gongzuo.stop()
            self.close()
            #apply_stylesheet(app, theme='dark_cyan.xml')#添加主题
            self.tttttt1 = QMainWindow()  ##启动
            self.gongzuo.setupUi(self.tttttt1)##启动创建一个工程gongneg
            #window.setupUi(form)
            apply_stylesheet(app, theme='dark_cyan.xml', extra=extra)
            self.tttttt1.show()
           # sys.exit(app2.exec_())
        else:
            self.step_gongzuo = self.step_gongzuo + 10
            self.progressBar_gongzuo.setValue(self.step_gongzuo)


class Ui_ProgressBar_caozuo(QWidget):
    def __init__(self, parent=None):
        super(Ui_ProgressBar_caozuo, self).__init__(parent)
        self.initUI()
        #self.hello = Ui_Hello()
        self.caozuo =Ui_MainWindow_caozuo()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("www.jpg")#进度条背景
        painter.drawPixmap(self.rect(), pixmap)

    def initUI(self):
        self.resize(500, 32)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.progressBar_caozuo = QProgressBar(self)
        self.progressBar_caozuo.setMinimum(0)
        self.progressBar_caozuo.setMaximum(100)
        self.progressBar_caozuo.setValue(0)
        self.progressBar_caozuo.setGeometry(QRect(1, 80, 499, 28))
        self.timer_caozuo = QBasicTimer()
        self.step_caozuo = 0
        self.setGeometry(300, 300, 550, 200)
        self.setWindowTitle('系统登录中...')
        self.show()
        self.timer_caozuo.start(100, self)

    def timerEvent(self, e):
        if self.step_caozuo >= 100:
            self.timer_caozuo.stop()
            self.close()
            #apply_stylesheet(app, theme='dark_cyan.xml')#添加主题
            self.tttttt2 = QMainWindow()  ##启动
            self.caozuo.setupUi(self.tttttt2)##启动创建一个工程gongneg
            #window.setupUi(form)
            apply_stylesheet(app, theme='dark_cyan.xml', extra=extra)
            self.tttttt2.show()
           # sys.exit(app2.exec_())
        else:
            self.step_caozuo = self.step_caozuo + 10
            self.progressBar_caozuo.setValue(self.step_caozuo)



class Ui_ProgressBar_admin(QWidget):
    def __init__(self, parent=None):
        super(Ui_ProgressBar_admin, self).__init__(parent)
        self.initUI()
        #self.hello = Ui_Hello()
        self.admin =Ui_MainWindow_admin()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("www.jpg")#进度条背景
        painter.drawPixmap(self.rect(), pixmap)

    def initUI(self):
        self.resize(500, 32)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.progressBar_admin = QProgressBar(self)
        self.progressBar_admin.setMinimum(0)
        self.progressBar_admin.setMaximum(100)
        self.progressBar_admin.setValue(0)
        self.progressBar_admin.setGeometry(QRect(1, 80, 499, 28))
        self.timer_admin = QBasicTimer()
        self.step_admin = 0
        self.setGeometry(300, 300, 550, 200)
        self.setWindowTitle('系统登录中...')
        self.show()
        self.timer_admin.start(100, self)

    def timerEvent(self, e):
        if self.step_admin >= 100:
            self.timer_admin.stop()
            self.close()
            #apply_stylesheet(app, theme='dark_cyan.xml')#添加主题
            self.tttttt3 = QMainWindow()  ##启动
            self.admin.setupUi(self.tttttt3)##启动创建一个工程gongneg
            #window.setupUi(form)
            apply_stylesheet(app, theme='dark_cyan.xml', extra=extra)
            self.tttttt3.show()
           # sys.exit(app2.exec_())
        else:
            self.step_admin = self.step_admin + 10
            self.progressBar_admin.setValue(self.step_admin)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow1=Ui_MainWindow1()

    MainWindow1.show()
    sys.exit(app.exec_())
