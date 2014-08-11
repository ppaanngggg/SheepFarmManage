from YANG import *


class CAdd_YANG_Dialog(CYANG_Dialog):
    def __init__(self, parent=None):
        super(CAdd_YANG_Dialog, self).__init__(parent)

        self.button_add_YANG_dialog=QPushButton('添加湖羊信息')
        self.label_add_YANG_dialog=QLabel('\n注：(*)为必填项\n')

        self.layout_YANG_dialog.addWidget(self.label_add_YANG_dialog)
        self.layout_YANG_dialog.addWidget(self.button_add_YANG_dialog)

        self.setWindowTitle('添加湖羊信息')