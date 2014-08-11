from CHAN_YANG_GUAN_XI import *

class CAdd_CHAN_YANG_GUAN_XI_Dialog(CCHAN_YANG_GUAN_XI_Dialog):
    def __init__(self, parent=None):
        super(CAdd_CHAN_YANG_GUAN_XI_Dialog, self).__init__(parent)

        self.button_add_CHAN_YANG_GUAN_XI_dialog=QPushButton('添加产羊关系')
        self.label_add_CHAN_YANG_GUAN_XI_dialog=QLabel('\n注：(*)为必填项\n')

        self.layout_CHAN_YANG_GUAN_XI_dialog.addWidget(self.label_add_CHAN_YANG_GUAN_XI_dialog)
        self.layout_CHAN_YANG_GUAN_XI_dialog.addWidget(self.button_add_CHAN_YANG_GUAN_XI_dialog)

        self.setWindowTitle('添加产羊关系')