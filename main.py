from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush
import random
from PyQt5 import uic, QtGui
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)
        self.crug.clicked.connect(self.onClicked)
        self.setWindowTitle('Желтые круги')
        self.show()
        self.flag = False

    def onClicked(self):
        self.flag = True
        self.update()

    def paintEvent(self, e):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawEll(qp)
            qp.end(

    def drawEll(self, qp):
        d = random.randint(10, 600)
        qp.setBrush(QColor(255, 255, 0))
        # qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.drawEllipse(random.randint(10, 600), random.randint(10, 600), d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())