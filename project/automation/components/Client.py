import sys
import time

from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QMainWindow
from project.automation.components.LeftTree import QVBoxLayout, QHBoxLayout, QApplication, QWidget, QSplitter, Qt, QTextEdit
from project.automation.components.LeftTree import Tree
from project.automation.components.handle_data.HandleDataMainWholeFrame import HandleDataMainWholeFrame


class Client(QMainWindow):
    ##分割的组件
    split = None
    ##左边分割部分的树状组件
    tree = None
    tmp = None

    def __init__(self):
        self.split = QSplitter(Qt.Horizontal)
        ##左边分割部分的树状组件
        self.tree = Tree()

        self.tmp = QTextEdit()
        self.handleDataMainFrame = HandleDataMainWholeFrame()

        super(Client,self).__init__()
        ## 本界面的设置
        self.setWindowTitle("牛逼哄哄的大系统")
        self.move(500,500)
        self.showMaximized()
        ## 其他的设置
        self.configThisWindow()
        self.connectAll()

    def configThisWindow(self):
        self.split.addWidget(self.tree)
        self.split.addWidget(self.tmp)

        self.split.setStretchFactor(0,1)
        self.split.setStretchFactor(1,7)

        mainLayout = QHBoxLayout(self)
        mainLayout.addWidget(self.split)
        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)

        self.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

    def connectAll(self):
        self.tree.clicked.connect(self.onClicked)
    def onClicked(self):
        item = self.tree.currentItem()
        print('Key=%s,value=%s' % (item.text(0), item.text(1)))
        if item.text(0) == '处理数据 流程控制面板':
            self.split.replaceWidget(1,self.handleDataMainFrame)
            self.split.setStretchFactor(0, 1)
            self.split.setStretchFactor(1, 7)
        elif item.text(0) == '查询人员信息':
            self.on_pushButton2_clicked()
        else:
            print('返回主界面')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tree = Client()
    tree.show()
    sys.exit(app.exec_())
