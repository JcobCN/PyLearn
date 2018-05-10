#! python3
import sys
import win32api
from PyQt5.QtWidgets import QApplication, QWidget, \
    QToolTip, QPushButton
from PyQt5.QtGui import QIcon, QFont

'''
#面向过程
app = QApplication(sys.argv)
w = QWidget()
w.resize(300, 150)
w.setFixedSize(700, 400)
x, y = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
w.move((x - 250) / 2, (y - 150) / 2)
w.setWindowTitle('将图片转换为jpg 1920*1080')
w.show()
sys.exit(app.exec_())
'''
class Example(QWidget):
    def __init__(self):
        super().__init__()#调用父类构造函数
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        x, y = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
        self.setGeometry((x-700)/2, (y-400)/2, 700, 400)
        self.setFixedSize(700, 400)
        self.setWindowTitle('将图片转换成jpg 1080')
        self.setWindowIcon(QIcon('46.jpg'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
