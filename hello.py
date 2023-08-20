import progressbar
from web import *
from Table import *
import pyqtgraph as pg
import paragraph
import predict
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import glo
import sqlite3
from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery
from led import *
import xlwt
import datetime
from progressbar import *
from PIL import Image
import os
from tqdm import tqdm
from deeplab import DeeplabV3
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



class Ui_Hello(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("hello.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def initUI(self):
        self.setWindowTitle("hello")
        self.setWindowIcon(QIcon('logo2.png'))
        self.resize(800,600)
        self.label =QLabel("FMCJZ")
        self.button1 = QPushButton("图片检测")
        self.button1.clicked.connect(self.getpic)
        self.lineEdit = QLineEdit()
        self.button2 = QPushButton("确定")
        self.button2.clicked.connect(self.tiaozhuan)
        self.button6 = QPushButton("视频检测")
        self.button6.clicked.connect(self.getvedio)
        #self.progressbar = Wenjian_ProgressBar()
        self.button7 = QPushButton("文件夹检测")
        self.button7.clicked.connect(self.jiance)
        self.button3 = QPushButton("数据")
        self.Table = Ui_Table()
        self.button3.clicked.connect(self.Table.show)
        self.button4 = QPushButton("导入")
        self.button4.clicked.connect(self.send_data)
        self.web = Ui_Web()
        self.button5 = QPushButton("管理平台")
        self.button5.clicked.connect(self.web.show)
        self.button8 = QPushButton("图像")
        self.button8.clicked.connect(self.ttt1)
        self.button9 = QPushButton("保存到数据库")
        self.button9.clicked.connect(self.ttt2)
        self.button10 = QPushButton("导出xls文件")
        self.button10.clicked.connect(self.ttt3)
        self.button11 = QPushButton("启用摄像头")
        self.button11.clicked.connect(self.shexiangtou)

        self.my_thread = MyThread()
        self.progressBar = QProgressBar(self)
        self.progressBar.resize(500,50)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(100, self)


        layout =QVBoxLayout()
        layout.addWidget(self.label,0,Qt.AlignRight)
        layout.addWidget(self.button1,0,Qt.AlignRight)
        layout.addWidget(self.lineEdit,0,Qt.AlignRight)
        layout.addWidget(self.button2, 0, Qt.AlignRight)
        layout.addWidget(self.button6, 0, Qt.AlignRight)
        layout.addWidget(self.button7, 0, Qt.AlignRight)
        layout.addWidget(self.progressBar, 0, Qt.AlignRight)
        layout.addWidget(self.button3,0,Qt.AlignRight)
        layout.addWidget(self.button4,0,Qt.AlignRight)
        layout.addWidget(self.button5, 0, Qt.AlignRight)
        layout.addWidget(self.button8, 0, Qt.AlignRight)
        layout.addWidget(self.button9, 0, Qt.AlignRight)
        layout.addWidget(self.button10, 0, Qt.AlignRight)
        layout.addWidget(self.button11, 0, Qt.AlignRight)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def out(self):
        self.w.label.setText(str(self.sum1))

    def ttt1(self):
        paragraph.view.show()
        pg.exec()

    def shexiangtou(self):
        ss=1
        predict.shibievideo(ss)



    def getpic(self):

        self.fileName1,self.fileType1= QFileDialog.getOpenFileName(self, "选取文件", "./",
                                                          "All Files (*);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔
        #print(self.fileType1)
        predict.shibiepic(str(self.fileName1))

    def getvedio(self):
        #self.l.show()
        self.fileName2,self.fileType2= QFileDialog.getOpenFileName(self, "选取文件", "./",
                                                          "All Files (*);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔
        predict.shibievideo(str(self.fileName2))

        print(glo.A,glo.B)


    def tiaozhuan(self):
        predict.shibievideo(str(self.lineEdit.text()))
        #glo.jjjj=ttest.caozuo(glo.jjjj)

    def ttt2(self):
        database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        database.setDatabaseName('mysql.db')
        database.open()

        query = QSqlQuery()  #######
        query.prepare('create table shuju (xiangsu varchar(30),zhanbi varchar(30))')
        if not query.exec_():
            query.lastError()
        else:
            print('create a table')
        for i in range(len(glo.A)):
            insert_sql = 'insert into shuju values (?,?)'
            query.prepare(insert_sql)
            query.addBindValue(glo.A[i])
            query.addBindValue(glo.B[i])
            query.execBatch()
            if not query.exec_():
                print(query.lastError())
            else:
                print('inserted')



    def send_data(self):
        for row in range(len(glo.A)):
            item1 = str(glo.A[row])
            item2 = str(glo.B[row])
            self.Table.tablewidget.setItem(row, 0, QTableWidgetItem(item1))
            self.Table.tablewidget.setItem(row, 1, QTableWidgetItem(item2))

    def ttt3(self):
        print("hello")
        book = xlwt.Workbook()
        sheet = book.add_sheet('数据表')
        sheet.write(0,0,'煤像素点')
        sheet.write(0,1,'煤占比')
        for i in range(0, self.Table.tablewidget.rowCount()):
            for j in range(0, self.Table.tablewidget.columnCount()):
                try:
                    sheet.write(i+1, j, self.Table.tablewidget.item(i, j).text())
                except:
                    continue
        now_time = datetime.datetime.now()
        now_time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d')
        print(str(now_time_str),".xls")
        book.save(now_time_str+'.xls')


    def jiance(self):
        self.my_thread.is_on = True
        self.my_thread.start()
        glo.directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")# 启动线程
        while 1:

                if glo.KLM >= 95:
                    self.timer.stop()
                    self.progressBar.setValue(100)
                    time.sleep(0.5)
                    self.progressBar.setValue(0)
                    break

                else:
                    self.step = self.step + 10
                    time.sleep(0.5)
                    self.progressBar.setValue(glo.KLM)
        QMessageBox.warning(self, "提示", "文件檢測完畢", QMessageBox.Yes)


class MyThread(QThread):  # 线程类
    my_signal = pyqtSignal(int)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串

    def __init__(self):
        super(MyThread, self).__init__()
        self.count = 0
        self.is_on = True
        #self.h = Ui_Hello()
    def run(self):
        print("22")

          # 起始路径
        while self.is_on:
            print("11")
            deeplab = DeeplabV3()
            dir_origin_path = str(glo.directory)
            dir_save_path = "outtest/"
            img_names = os.listdir(dir_origin_path)
            for img_name in tqdm(img_names):
                if img_name.lower().endswith(
                        ('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
                    image_path = os.path.join(dir_origin_path, img_name)
                    image = Image.open(image_path)
                    r_image = deeplab.detect_image(image)
                    self.count += 1
                    glo.KLM=self.count
                    self.my_signal.emit(int(self.count))

                    print(self.count)
                    if not os.path.exists(dir_save_path):
                        os.makedirs(dir_save_path)

                    r_image.save(os.path.join(dir_save_path, img_name))
                    #self.sleep(1)
            print("dir finshed")
            self.my_thread.is_on = False
            self.my_thread.count = 0
            break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Hello()
    ex.show()
    apply_stylesheet(app, theme='dark_blue.xml')
    sys.exit(app.exec_())




