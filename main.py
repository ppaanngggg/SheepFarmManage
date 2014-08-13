from PyQt5 import QtCore

from add_CHAN_GAO import *
from add_YANG import *
from search_CHAN_GAO import *
from search_YANG import *


class CMainWindow(QWidget):
    def __init__(self, parent=None):
        super(CMainWindow, self).__init__(parent)

        self.label_main=QLabel('欢迎使用湖羊数据管理系统')
        self.label_main.setAlignment(QtCore.Qt.AlignHCenter)

        self.label_add=QLabel('\n添加数据：')
        self.button_add_CHAN_GAO=QPushButton('添加产羔记录')
        self.button_add_CHAN_GAO.clicked.connect(self.button_add_CHAN_GAO_clicked)
        self.button_add_YANG=QPushButton('添加湖羊数据')
        self.button_add_YANG.clicked.connect(self.button_add_YANG_clicked)
        self.layout_add=QVBoxLayout()
        self.layout_add.setSpacing(10)
        self.layout_add.addWidget(self.label_add)
        self.layout_add.addWidget(self.button_add_CHAN_GAO)
        self.layout_add.addWidget(self.button_add_YANG)

        self.label_search=QLabel('\n查询数据：')
        self.button_search_CHAN_GAO=QPushButton('查询产羔记录')
        self.button_search_CHAN_GAO.clicked.connect(self.button_search_CHAN_GAO_clicked)
        self.button_search_YANG=QPushButton('查询湖羊数据')
        self.button_search_YANG.clicked.connect(self.button_search_YANG_clicked)
        self.layout_search=QVBoxLayout()
        self.layout_search.setSpacing(10)
        self.layout_search.addWidget(self.label_search)
        self.layout_search.addWidget(self.button_search_CHAN_GAO)
        self.layout_search.addWidget(self.button_search_YANG)

        self.layout_operate=QHBoxLayout()
        self.layout_operate.setSpacing(30)
        self.layout_operate.addLayout(self.layout_add)
        self.layout_operate.addLayout(self.layout_search)

        self.main_layout=QVBoxLayout()
        self.main_layout.addWidget(self.label_main)
        self.main_layout.addLayout(self.layout_operate)

        self.setLayout(self.main_layout)
        self.setWindowTitle('湖羊数据管理系统')

    def button_add_CHAN_GAO_clicked(self):
        self.add_CHAN_GAO_dialog=CAdd_CHAN_GAO_Dialog()
        self.add_CHAN_GAO_dialog.show()

    def button_add_YANG_clicked(self):
        self.add_YANG_dialog=CAdd_YANG_Dialog()
        self.add_YANG_dialog.show()

    def button_search_CHAN_GAO_clicked(self):
        self.search_CHAN_GAO_dialog=CSearch_CHAN_GAO_Dialog()
        self.search_CHAN_GAO_dialog.show()

    def button_search_YANG_clicked(self):
        self.search_YANG_dialog=CSearch_YANG_Dialog()
        self.search_YANG_dialog.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    main_window = CMainWindow()
    main_window.show()

    sys.exit(app.exec_())