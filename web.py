
from PyQt5.QtWidgets import *

from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
class Ui_Web(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 50, 1200, 800)
        self.setWindowTitle('管理平台')


        self.browser = QWebEngineView()
        #加载外部的web页面
        self.browser.load(QUrl('http://vitant.xyz/resource.html'))
        self.setCentralWidget(self.browser)

