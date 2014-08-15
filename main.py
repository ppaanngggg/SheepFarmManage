from PyQt5 import QtCore

from add_CHAN_GAO import *
from add_YANG import *
from search_CHAN_GAO import *
from search_YANG import *
from edit_CHAN_GAO import *
from edit_YANG import *
from sheet_CHAN_GAO_JI_LU import *
from sheet_CHENG_ZHONG_JI_LU import *
from sheet_YU_ZHONG_JI_LU import *
from sheet_ZHONG_MU_YANG_HOU_YI import *
from sheet_ZHONG_GONG_YANG_HOU_YI import *

class CMainWindow(QWidget):
    def __init__(self, parent=None):
        super(CMainWindow, self).__init__(parent)

        self.label_main=QLabel('欢迎使用湖羊数据管理系统')
        self.label_main.setAlignment(QtCore.Qt.AlignHCenter)

        self.label_add=QLabel('添加数据：')
        self.button_add_CHAN_GAO=QPushButton('添加产羔记录')
        self.button_add_CHAN_GAO.clicked.connect(self.button_add_CHAN_GAO_clicked)
        self.button_add_YANG=QPushButton('添加湖羊数据')
        self.button_add_YANG.clicked.connect(self.button_add_YANG_clicked)
        self.layout_add=QVBoxLayout()
        self.layout_add.setSpacing(10)
        self.layout_add.addWidget(self.label_add)
        self.layout_add.addWidget(self.button_add_CHAN_GAO)
        self.layout_add.addWidget(self.button_add_YANG)

        self.label_search=QLabel('查询数据：')
        self.button_search_CHAN_GAO=QPushButton('查询产羔记录')
        self.button_search_CHAN_GAO.clicked.connect(self.button_search_CHAN_GAO_clicked)
        self.button_search_YANG=QPushButton('查询湖羊数据')
        self.button_search_YANG.clicked.connect(self.button_search_YANG_clicked)
        self.layout_search=QVBoxLayout()
        self.layout_search.setSpacing(10)
        self.layout_search.addWidget(self.label_search)
        self.layout_search.addWidget(self.button_search_CHAN_GAO)
        self.layout_search.addWidget(self.button_search_YANG)

        self.label_edit=QLabel('修改数据：')
        self.button_edit_CHAN_GAO=QPushButton('修改产羔记录')
        self.button_edit_CHAN_GAO.clicked.connect(self.button_edit_CHAN_GAO_clicked)
        self.button_edit_YANG=QPushButton('修改湖羊数据')
        self.button_edit_YANG.clicked.connect(self.button_edit_YANG_clicked)
        self.layout_edit=QVBoxLayout()
        self.layout_edit.setSpacing(10)
        self.layout_edit.addWidget(self.label_edit)
        self.layout_edit.addWidget(self.button_edit_CHAN_GAO)
        self.layout_edit.addWidget(self.button_edit_YANG)

        self.label_sheet=QLabel('生成表格：')
        self.button_sheet_CHAN_GAO_JI_LU=QPushButton('产羔记录表')
        self.button_sheet_CHAN_GAO_JI_LU.clicked.connect(self.button_sheet_CHAN_GAO_JI_LU_clicked)
        self.button_sheet_CHENG_ZHONG_JI_LU=QPushButton('称重记录表')
        self.button_sheet_CHENG_ZHONG_JI_LU.clicked.connect(self.button_sheet_CHENG_ZHONG_JI_LU_clicked)
        self.button_sheet_YU_ZHONG_JI_LU=QPushButton('育种记录表')
        self.button_sheet_YU_ZHONG_JI_LU.clicked.connect(self.button_sheet_YU_ZHONG_JI_LU_clicked)
        self.button_sheet_ZHONG_MU_YANG_HOU_YI=QPushButton('种母羊后裔表')
        self.button_sheet_ZHONG_MU_YANG_HOU_YI.clicked.connect(self.button_sheet_ZHONG_MU_YANG_HOU_YI_clicked)
        self.button_sheet_ZHONG_GONG_YANG_HOU_YI=QPushButton('种公羊后裔表')
        self.button_sheet_ZHONG_GONG_YANG_HOU_YI.clicked.connect(self.button_sheet_ZHONG_GONG_YANG_HOU_YI_clicked)
        self.layout_sheet=QVBoxLayout()
        self.layout_sheet.setSpacing(10)
        self.layout_sheet.addWidget(self.label_sheet)
        self.layout_sheet.addWidget(self.button_sheet_CHAN_GAO_JI_LU)
        self.layout_sheet.addWidget(self.button_sheet_CHENG_ZHONG_JI_LU)
        self.layout_sheet.addWidget(self.button_sheet_YU_ZHONG_JI_LU)
        self.layout_sheet.addWidget(self.button_sheet_ZHONG_MU_YANG_HOU_YI)
        self.layout_sheet.addWidget(self.button_sheet_ZHONG_GONG_YANG_HOU_YI)

        self.layout_operate=QHBoxLayout()
        self.layout_operate.setSpacing(30)
        self.layout_operate.addLayout(self.layout_add)
        self.layout_operate.addLayout(self.layout_search)
        self.layout_operate.addLayout(self.layout_edit)
        self.layout_operate.addLayout(self.layout_sheet)

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

    def button_edit_CHAN_GAO_clicked(self):
        self.edit_CHAN_GAO_dialog=CEdit_CHAN_GAO_Dialog()

    def button_edit_YANG_clicked(self):
        self.edit_YANG_dialog=CEdit_YANG_Dialog()

    def button_sheet_CHAN_GAO_JI_LU_clicked(self):
        self.sheet_CHAN_GAO_JI_LU_dialog=CSheet_CHAN_GAO_JI_LU_Dialog()

    def button_sheet_CHENG_ZHONG_JI_LU_clicked(self):
        self.sheet_CHENG_ZHONG_JI_LU_dialog=CSheet_CHENG_ZHONG_JI_LU_Dialog()

    def button_sheet_YU_ZHONG_JI_LU_clicked(self):
        self.sheet_YU_ZHONG_JI_LU_dialog=CSheet_YU_ZHONG_JI_LU_Dialog()

    def button_sheet_ZHONG_MU_YANG_HOU_YI_clicked(self):
        self.sheet_ZHONG_MU_YANG_HOU_YI_dialog=CSheet_ZHONG_MU_YANG_HOU_YI_Dialog()

    def button_sheet_ZHONG_GONG_YANG_HOU_YI_clicked(self):
        self.sheet_ZHONG_GONG_YANG_HOU_YI_dialog=CSheet_ZHONG_GONG_YANG_HOU_YI_Dialog()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    main_window = CMainWindow()
    main_window.show()

    sys.exit(app.exec_())