import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Tree(QTreeWidget):
    myControls = {}

    def __init__(self, parent=None):
        super(Tree,self).__init__()
        self.setWindowTitle('TreeWidget')
        self.myControls['tree'] = self

        self.setColumnCount(1)  # 说明是树形的表，
        self.setHeaderLabels(['Key'])  # 是表，则有表头
        ##填充树的样式
        self.build_tree()

    def build_tree(self):
        root = QTreeWidgetItem(self)
        root.setText(0, '功能')

        child1 = QTreeWidgetItem(root)  # 指出父结点
        child1.setText(0, '处理数据 流程控制面板')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, '模板配置 ')

        child3 = QTreeWidgetItem(root)
        child3.setText(0, '信息配置')

        child4 = QTreeWidgetItem(child3)
        child4.setText(0, '显示面板')

        child5 = QTreeWidgetItem(child3)
        child5.setText(0, '显示面板')

        # 以下两句是主窗口的设置
        self.addTopLevelItem(root)
        self.expandAll()


# app = QApplication(sys.argv)
# tp = Tree()
# mainLayout = QVBoxLayout()
# mainLayout.addLayout(QHBoxLayout())
# mainLayout.addWidget(tp)
# tp.move(700,300)
# tp.show()
# app.exec_()