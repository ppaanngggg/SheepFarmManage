from CHAN_GAO import *


class CAdd_CHAN_GAO_Dialog(CCHAN_GAO_Dialog):
    def __init__(self, parent=None):
        super(CAdd_CHAN_GAO_Dialog, self).__init__(parent)

        self.button_add_CHAN_GAO_dialog=QPushButton('添加产羔信息')
        self.label_add_CHAN_GAO_dialog=QLabel('\n注：(*)为必填项\n')

        self.layout_CHAN_GAO_dialog.addWidget(self.label_add_CHAN_GAO_dialog)
        self.layout_CHAN_GAO_dialog.addWidget(self.button_add_CHAN_GAO_dialog)

        self.setWindowTitle('添加产羔信息')