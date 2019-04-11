import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter, QTextEdit, QApplication, QVBoxLayout, QScrollArea, \
    QPushButton, QGridLayout
from functools import partial

from project.automation.components.handle_data.ElementGalleryFrame import ElementGallery
from project.automation.components.handle_data.Element.Element import *
from project.automation.components.handle_data.HandleDataMainFrame import HandleDataMainFrame


class HandleDataMainWholeFrame(QWidget):
    def __init__(self):
        super(HandleDataMainWholeFrame,self).__init__()
        split_w = QSplitter(Qt.Horizontal)
        split_n = QSplitter(Qt.Vertical)

        ##主要的操作界面面板
        scroll = QScrollArea()
        self.mainOperation = QWidget(scroll)
        self.mainOperation = HandleDataMainFrame()

        self.mainPanel = QHBoxLayout()
        self.mainPanel
        self.mainPanel.setAlignment(Qt.AlignAbsolute)
        self.mainPanel.addWidget(QPushButton())

        self.mainOperation.setLayout(self.mainPanel)

        self.mainOperation.setMinimumSize(1500,750)

        scroll.setAutoFillBackground(True)
        #scroll.setWidgetResizable(True)
        scroll.setWidget(self.mainOperation)


        split_n.addWidget(scroll)
        split_n.addWidget(QTextEdit())
        split_n.setStretchFactor(0, 8)
        split_n.setStretchFactor(1, 2)

        ## 添加主要的操作界面  添加界面对应的参数设置
        ## 添加最右侧的操作图标
        split_w.addWidget(split_n)
        ele = ElementGallery()
        split_w.addWidget(ele)
        ele.mainFram = self.mainOperation
        split_w.setStretchFactor(0, 8)
        split_w.setStretchFactor(1, 2)

        handleData = QHBoxLayout(self)
        handleData.addWidget(split_w)
        self.setLayout(handleData)

        ele.a2.clicked.connect(partial(self.addSelfToMain,ele.a2.objectName()))
# app = QApplication(sys.argv)
# tp = HandleDataMainFrame()
# mainLayout = QVBoxLayout()
# mainLayout.addLayout(QHBoxLayout())
# mainLayout.addWidget(tp)
# tp.move(700,300)
# tp.show()
# app.exec_()

    def addSelfToMain(self,name):
        self.mainOperation.mainPanel.addWidget(getElement(name))
        print("成功捕获到请求")
