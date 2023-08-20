from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time


class Wenjian_ProgressBar(QWidget):
    def __init__(self, parent=None):
        super(Wenjian_ProgressBar, self).__init__(parent)
        self.initUI()



    def initUI(self):
        self.resize(500, 32)
        self.progressBar = QProgressBar(self)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.progressBar.setGeometry(QRect(1, 80, 499, 28))
        self.timer = QBasicTimer()
        self.step = 0
        self.setGeometry(300, 300, 550, 200)
        self.setWindowTitle('文件处理中...')
        self.show()
        self.timer.start(100, self)

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.step = 0
            return
        if self.step < 99:
            self.step += 1
            self.progressBar.setValue(self.step)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    p = Wenjian_ProgressBar()
    p.show()
    sys.exit(app.exec_())