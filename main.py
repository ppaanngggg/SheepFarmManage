from add_CHAN_GAO import *
from add_YANG import *
from add_CHAN_YANG_GUAN_XI import *

class CMainWindow(QWidget):
    def __init__(self, parent=None):
        super(CMainWindow, self).__init__(parent)

        self.label_main=QLabel('欢迎使用湖羊数据管理系统')

        self.button_add_CHAN_GAO=QPushButton('添加产羔记录')
        self.button_add_CHAN_GAO.clicked.connect(self.button_add_CHAN_GAO_clicked)

        self.button_add_YANG=QPushButton('添加湖羊数据')
        self.button_add_YANG.clicked.connect(self.button_add_YANG_clicked)

        self.button_add_CHAN_YANG_GUAN_XI=QPushButton('添加产羊关系')
        self.button_add_CHAN_YANG_GUAN_XI.clicked.connect(self.button_add_CHAN_YANG_GUAN_XI_clicked)

        self.main_layout=QVBoxLayout()
        self.main_layout.addWidget(self.label_main)
        self.main_layout.addWidget(self.button_add_CHAN_GAO)
        self.main_layout.addWidget(self.button_add_YANG)
        self.main_layout.addWidget(self.button_add_CHAN_YANG_GUAN_XI)

        self.setLayout(self.main_layout)
        self.setWindowTitle('湖羊数据管理系统')

    def button_add_CHAN_GAO_clicked(self):
        self.add_CHAN_GAO_dialog=CAdd_CHAN_GAO_Dialog()
        self.add_CHAN_GAO_dialog.show()

    def button_add_YANG_clicked(self):
        self.add_YANG_dialog=CAdd_YANG_Dialog()
        self.add_YANG_dialog.show()

    def button_add_CHAN_YANG_GUAN_XI_clicked(self):
        self.add_CHAN_YANG_GUAN_XI_dialog=CAdd_CHAN_YANG_GUAN_XI_Dialog()
        self.add_CHAN_YANG_GUAN_XI_dialog.show()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    main_window = CMainWindow()
    main_window.show()

    sys.exit(app.exec_())