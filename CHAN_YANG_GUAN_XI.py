from PyQt5.QtWidgets import *


class CCHAN_YANG_GUAN_XI_Dialog(QDialog):
    def __init__(self, parent=None):
        super(CCHAN_YANG_GUAN_XI_Dialog, self).__init__(parent)

        self.label_CHAN_GAO_HAO=QLabel('产羔号(*)：')
        self.edit_CHAN_GAO_HAO=QLineEdit()
        self.layout_CHAN_GAO_HAO=QHBoxLayout()
        self.layout_CHAN_GAO_HAO.addWidget(self.label_CHAN_GAO_HAO)
        self.layout_CHAN_GAO_HAO.addWidget(self.edit_CHAN_GAO_HAO)

        self.label_BIAN_HAO=QLabel('编号(*)：')
        self.edit_BIAN_HAO=QLineEdit()
        self.layout_BIAN_HAO=QHBoxLayout()
        self.layout_BIAN_HAO.addWidget(self.label_BIAN_HAO)
        self.layout_BIAN_HAO.addWidget(self.edit_BIAN_HAO)

        self.layout_CHAN_YANG_GUAN_XI_dialog=QVBoxLayout()
        self.layout_CHAN_YANG_GUAN_XI_dialog.addLayout(self.layout_CHAN_GAO_HAO)
        self.layout_CHAN_YANG_GUAN_XI_dialog.addLayout(self.layout_BIAN_HAO)

        self.setLayout(self.layout_CHAN_YANG_GUAN_XI_dialog)