from PyQt5.QtWidgets import *

from add_CHAN_GAO import *

class CMainWindow(QWidget):
    def __init__(self, parent=None):
        super(CMainWindow, self).__init__(parent)

        self.main_title=QLabel('欢迎使用湖羊数据管理系统')

        self.button_add_CHAN_GAO=QPushButton('添加产羔记录')
        self.button_add_CHAN_GAO.clicked.connect(self.button_add_CHAN_GAO_clicked)

        self.button_add_YANG=QPushButton('添加湖羊数据')

        self.main_layout=QVBoxLayout()
        self.main_layout.addWidget(self.main_title)
        self.main_layout.addWidget(self.button_add_CHAN_GAO)
        self.main_layout.addWidget(self.button_add_YANG)

        self.setLayout(self.main_layout)

    def button_add_CHAN_GAO_clicked(self):
        self.add_CHAN_GAO_dialog=CAdd_CHAN_GAO_Dialog()
        self.add_CHAN_GAO_dialog.show()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    main_window = CMainWindow()
    main_window.show()

    sys.exit(app.exec_())