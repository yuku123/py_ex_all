import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QSplitter, QVBoxLayout, QLabel, QGridLayout, QPushButton, QHBoxLayout, QApplication
from project.automation.components.handle_data.Element.Element import *


class ElementGallery(QWidget):
    def __init__(self):
        super(ElementGallery,self).__init__()
        ##数据处理类别
        handle = QWidget()
        handle_layout = QVBoxLayout()
        handle_layout.setAlignment(Qt.AlignTop)
        handle.setLayout(handle_layout)

        handle_label = QLabel()
        handle_label.setText("数据处理相关")
        handle_label.setAlignment(Qt.AlignCenter)
        handle_layout.addWidget(handle_label)

        handle_container = QWidget()
        handle_container_layout = QGridLayout()
        handle_container_layout.setAlignment(Qt.AlignCenter)
        handle_container.setLayout(handle_container_layout)

        #得到很多的组件列表
        self.a1 = e1()
        self.a2 = e2()

        ##在容器内增加上面的所有的组件
        handle_container_layout.addWidget(self.a1,1,1)
        handle_container_layout.addWidget(self.a2,1,2)

        ##填充容器
        handle_layout.addWidget(handle_container)

        ##添加到主窗口
        handleData = QVBoxLayout(self)
        handleData.addWidget(handle)
        self.setLayout(handleData)
        self.setStyleSheet("QWidget#aa{border: 1px solid #FF00FF; border-radius: 2px;};")
# app = QApplication(sys.argv)
# tp = ElementGallery()
# mainLayout = QVBoxLayout()
# mainLayout.addLayout(QHBoxLayout())
# mainLayout.addWidget(tp)
# tp.move(700,300)
# tp.show()
# app.exec_()