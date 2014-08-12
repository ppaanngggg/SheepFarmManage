from PyQt5.QtWidgets import *


class CYANG_Dialog(QDialog):
    def __init__(self, parent=None):
        super(CYANG_Dialog, self).__init__(parent)

        self.label_BIAN_HAO=QLabel('编号(*)：')
        self.edit_BIAN_HAO=QLineEdit()
        self.layout_BIAN_HAO=QHBoxLayout()
        self.layout_BIAN_HAO.addWidget(self.label_BIAN_HAO)
        self.layout_BIAN_HAO.addWidget(self.edit_BIAN_HAO)
        
        self.label_CHAN_GAO_HAO=QLabel('产羔号(*)：')
        self.edit_CHAN_GAO_HAO=QLineEdit()
        self.layout_CHAN_GAO_HAO=QHBoxLayout()
        self.layout_CHAN_GAO_HAO.addWidget(self.label_CHAN_GAO_HAO)
        self.layout_CHAN_GAO_HAO.addWidget(self.edit_CHAN_GAO_HAO)
        
        self.label_XING_BIE=QLabel('性别(*)：')
        self.edit_XING_BIE=QLineEdit()
        self.layout_XING_BIE=QHBoxLayout()
        self.layout_XING_BIE.addWidget(self.label_XING_BIE)
        self.layout_XING_BIE.addWidget(self.edit_XING_BIE)
        
        self.label_ER_HAO=QLabel('耳号：')
        self.edit_ER_HAO=QLineEdit()
        self.layout_ER_HAO=QHBoxLayout()
        self.layout_ER_HAO.addWidget(self.label_ER_HAO)
        self.layout_ER_HAO.addWidget(self.edit_ER_HAO)
        
        self.label_CHU_SHENG_ZHONG=QLabel('出生重：')
        self.edit_CHU_SHENG_ZHONG=QLineEdit()
        self.layout_CHU_SHENG_ZHONG=QHBoxLayout()
        self.layout_CHU_SHENG_ZHONG.addWidget(self.label_CHU_SHENG_ZHONG)
        self.layout_CHU_SHENG_ZHONG.addWidget(self.edit_CHU_SHENG_ZHONG)
        
        self.label_DUAN_NAI_ZHONG=QLabel('断奶重：')
        self.edit_DUAN_NAI_ZHONG=QLineEdit()
        self.layout_DUAN_NAI_ZHONG=QHBoxLayout()
        self.layout_DUAN_NAI_ZHONG.addWidget(self.label_DUAN_NAI_ZHONG)
        self.layout_DUAN_NAI_ZHONG.addWidget(self.edit_DUAN_NAI_ZHONG)
        
        self.label_LIU_YUE_ZHONG=QLabel('六月重：')
        self.edit_LIU_YUE_ZHONG=QLineEdit()
        self.layout_LIU_YUE_ZHONG=QHBoxLayout()
        self.layout_LIU_YUE_ZHONG.addWidget(self.label_LIU_YUE_ZHONG)
        self.layout_LIU_YUE_ZHONG.addWidget(self.edit_LIU_YUE_ZHONG)
        
        self.label_ZHOU_SUI_ZHONG=QLabel('周岁重：')
        self.edit_ZHOU_SUI_ZHONG=QLineEdit()
        self.layout_ZHOU_SUI_ZHONG=QHBoxLayout()
        self.layout_ZHOU_SUI_ZHONG.addWidget(self.label_ZHOU_SUI_ZHONG)
        self.layout_ZHOU_SUI_ZHONG.addWidget(self.edit_ZHOU_SUI_ZHONG)
        
        self.label_QU_XIANG=QLabel('去向：')
        self.edit_QU_XIANG=QLineEdit()
        self.layout_QU_XIANG=QHBoxLayout()
        self.layout_QU_XIANG.addWidget(self.label_QU_XIANG)
        self.layout_QU_XIANG.addWidget(self.edit_QU_XIANG)

        self.label_CHAN_GAO_BIAN_HAO=QLabel('产羔编号(母羊号或公羊号)：')
        self.edit_CHAN_GAO_BIAN_HAO=QLineEdit()
        self.layout_CHAN_GAO_BIAN_HAO=QHBoxLayout()
        self.layout_CHAN_GAO_BIAN_HAO.addWidget(self.label_CHAN_GAO_BIAN_HAO)
        self.layout_CHAN_GAO_BIAN_HAO.addWidget(self.edit_CHAN_GAO_BIAN_HAO)
        
        self.layout_YANG_dialog=QVBoxLayout()
        self.layout_YANG_dialog.addLayout(self.layout_BIAN_HAO)
        self.layout_YANG_dialog.addLayout(self.layout_CHAN_GAO_HAO)
        self.layout_YANG_dialog.addLayout(self.layout_XING_BIE)
        self.layout_YANG_dialog.addLayout(self.layout_ER_HAO)
        self.layout_YANG_dialog.addLayout(self.layout_CHU_SHENG_ZHONG)
        self.layout_YANG_dialog.addLayout(self.layout_DUAN_NAI_ZHONG)
        self.layout_YANG_dialog.addLayout(self.layout_LIU_YUE_ZHONG)
        self.layout_YANG_dialog.addLayout(self.layout_ZHOU_SUI_ZHONG)
        self.layout_YANG_dialog.addLayout(self.layout_QU_XIANG)
        self.layout_YANG_dialog.addLayout(self.layout_CHAN_GAO_BIAN_HAO)

        self.setLayout(self.layout_YANG_dialog)