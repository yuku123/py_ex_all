from PyQt5.QtGui import QPixmap, QCursor, QIcon
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtCore import Qt, QSize
from project.automation.components.Utils import *


class e1(QLabel):
    def __init__(self):
        super(e1,self).__init__()
        self.setPixmap(QPixmap(getResource("f.png")).scaled(20, 20, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))


class e2(QPushButton):
    mainFrame = None
    def __init__(self,parent=None):
        super(e2, self).__init__(parent)
        self.setObjectName('a2')
        self.setIcon(QIcon(getResource("f.png")))
        self.setIconSize(QSize(20,20))
        self.setStyleSheet("QPushButton{background: transparent;}");
        self.setToolTip("吃饭")
        #self.setPixmap(QPixmap("./f.png").scaled(20, 20, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()
    def addSelfToMain(self):
        print("成功捕获到请求")

def getElement(name):
    if name == 'a2':
        return e2()