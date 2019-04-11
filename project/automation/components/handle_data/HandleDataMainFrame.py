from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt


class HandleDataMainFrame(QWidget):
    def __init__(self):
        super(HandleDataMainFrame,self).__init__()

        self.mainPanel = QHBoxLayout()
        self.mainPanel.setAlignment(Qt.AlignAbsolute)
        self.mainPanel.addWidget(QPushButton())
        self.setLayout(self.mainPanel)
        self.setMinimumSize(1500,750)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)
        e.setDropAction(Qt.MoveAction)
        e.accept()
