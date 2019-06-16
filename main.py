import logging

import mysql.connector
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QGridLayout,
    QDialog,
    QMessageBox,
    QFileDialog,
    QApplication,
    QPushButton,
)
from mysql.connector import errorcode

from Add import CAdd_CHAN_GAO_Dialog, CAdd_YANG_Dialog, add_from_sheet
from Edit import CEdit_YANG_Dialog, CEdit_CHAN_GAO_Dialog
from Search import CSearch_YANG_Dialog, CSearch_CHAN_GAO_Dialog
from avg_CHU_SHENG_DUAN_NAI_ZHONG import avg_CHU_SHENG_DUAN_NAI_ZHONG
from sheet_CHAN_GAO_JI_LU import CSheet_CHAN_GAO_JI_LU_Dialog
from sheet_CHENG_ZHONG_JI_LU import CSheet_CHENG_ZHONG_JI_LU_Dialog
from sheet_YU_ZHONG_JI_LU import CSheet_YU_ZHONG_JI_LU_Dialog
from sheet_ZHONG_GONG_YANG_HOU_YI import CSheet_ZHONG_GONG_YANG_HOU_YI_Dialog
from sheet_ZHONG_MU_YANG_HOU_YI import CSheet_ZHONG_MU_YANG_HOU_YI_Dialog
from utils.login_database import CLogin_Database_Dialog

logging.basicConfig(level=logging.INFO)


class CMainWindow(QWidget):
    def __init__(self, parent=None):
        super(CMainWindow, self).__init__(parent)

        self.USER = ""
        self.PASSWD = ""

        # login
        if not self.login_database():
            sys.exit(1)

        # window
        self.setWindowTitle("湖羊数据管理系统")
        layout_plane = QGridLayout()
        layout_plane.setHorizontalSpacing(30)
        self.setLayout(layout_plane)

        # plane
        self.create_add_plane(layout_plane)
        self.create_search_plane(layout_plane)
        self.create_edit_plane(layout_plane)

        # self.label_sheet = QLabel("生成表格：")
        # self.button_sheet_CHAN_GAO_JI_LU = QPushButton("产羔记录表")
        # self.button_sheet_CHAN_GAO_JI_LU.clicked.connect(
        #     self.button_sheet_CHAN_GAO_JI_LU_clicked
        # )
        # self.button_sheet_CHENG_ZHONG_JI_LU = QPushButton("称重记录表")
        # self.button_sheet_CHENG_ZHONG_JI_LU.clicked.connect(
        #     self.button_sheet_CHENG_ZHONG_JI_LU_clicked
        # )
        # self.button_sheet_YU_ZHONG_JI_LU = QPushButton("育种记录表")
        # self.button_sheet_YU_ZHONG_JI_LU.clicked.connect(
        #     self.button_sheet_YU_ZHONG_JI_LU_clicked
        # )
        # self.button_sheet_ZHONG_MU_YANG_HOU_YI = QPushButton("种母羊后裔表")
        # self.button_sheet_ZHONG_MU_YANG_HOU_YI.clicked.connect(
        #     self.button_sheet_ZHONG_MU_YANG_HOU_YI_clicked
        # )
        # self.button_sheet_ZHONG_GONG_YANG_HOU_YI = QPushButton("种公羊后裔表")
        # self.button_sheet_ZHONG_GONG_YANG_HOU_YI.clicked.connect(
        #     self.button_sheet_ZHONG_GONG_YANG_HOU_YI_clicked
        # )
        # self.layout_sheet = QVBoxLayout()
        # self.layout_sheet.setSpacing(10)
        # self.layout_sheet.addWidget(self.label_sheet)
        # self.layout_sheet.addWidget(self.button_sheet_CHAN_GAO_JI_LU)
        # self.layout_sheet.addWidget(self.button_sheet_CHENG_ZHONG_JI_LU)
        # self.layout_sheet.addWidget(self.button_sheet_YU_ZHONG_JI_LU)
        # self.layout_sheet.addWidget(self.button_sheet_ZHONG_MU_YANG_HOU_YI)
        # self.layout_sheet.addWidget(self.button_sheet_ZHONG_GONG_YANG_HOU_YI)
        #
        # self.label_statistic = QLabel("数据统计：")
        # self.button_avg_CHU_SHENG_DUAN_NAI_ZHONG = QPushButton("出生重，断奶重平均值")
        # self.button_avg_CHU_SHENG_DUAN_NAI_ZHONG.clicked.connect(
        #     self.button_avg_CHU_SHENG_DUAN_NAI_ZHONG_clicked
        # )
        # self.layout_statistic = QVBoxLayout()
        # self.layout_statistic.setSpacing(10)
        # self.layout_statistic.addWidget(self.label_statistic)
        # self.layout_statistic.addWidget(self.button_avg_CHU_SHENG_DUAN_NAI_ZHONG)

        self.show()

    def login_database(self):
        """
        登录

        :return: succeed or failed
        """
        user_and_passwd = ["", ""]
        login_database_dialog = CLogin_Database_Dialog(user_and_passwd, self)
        if login_database_dialog.exec() == QDialog.Accepted:
            try:
                cnx = mysql.connector.connect(
                    user=user_and_passwd[0],
                    password=user_and_passwd[1],
                    database="pang_da_nong_ye",
                    host="127.0.0.1",
                )
                cnx.close()
                self.USER = user_and_passwd[0]
                self.PASSWD = user_and_passwd[1]
                return True
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    QMessageBox.information(self, "数据库错误", "用户名或密码错误。")
                elif err.errno == errorcode.ER_DBACCESS_DENIED_ERROR:
                    QMessageBox.information(self, "数据库错误", "该用户无访问权限")
                elif err.errno == errorcode.CR_CONN_HOST_ERROR:
                    QMessageBox.information(self, "数据库错误", "无法连接到服务器")
                else:
                    QMessageBox.information(self, "数据库错误", str(err))
                return False
        else:
            return False

    def create_add_plane(self, _layout, _col=0):
        """
        添加数据部分
        """

        def button_add_from_sheet_clicked():
            str_path, str_filter = QFileDialog.getOpenFileName(
                self, "从表格导入数据", "", "Excel Files (*.xls)"
            )
            if str_path and not str_path.isspace():
                add_from_sheet(str_path, self)

        def button_add_CHAN_GAO_clicked():
            self.add_CHAN_GAO_dialog = CAdd_CHAN_GAO_Dialog(self)
            self.add_CHAN_GAO_dialog.show()

        def button_add_YANG_clicked():
            self.add_YANG_dialog = CAdd_YANG_Dialog(self)
            self.add_YANG_dialog.show()

        _layout.addWidget(QLabel("添加数据："), 0, _col)
        _layout.addWidget(QLabel(), 1, _col)
        button_add_from_sheet = QPushButton("从表格导入数据")
        button_add_from_sheet.clicked.connect(button_add_from_sheet_clicked)
        _layout.addWidget(button_add_from_sheet, 2, _col)
        button_add_CHAN_GAO = QPushButton("添加产羔记录")
        button_add_CHAN_GAO.clicked.connect(button_add_CHAN_GAO_clicked)
        _layout.addWidget(button_add_CHAN_GAO, 3, _col)
        button_add_YANG = QPushButton("添加湖羊数据")
        button_add_YANG.clicked.connect(button_add_YANG_clicked)
        _layout.addWidget(button_add_YANG, 4, _col)

    def create_search_plane(self, _layout, _col=1):
        """
        搜索数据部分
        """

        def button_search_CHAN_GAO_clicked():
            self.search_CHAN_GAO_dialog = CSearch_CHAN_GAO_Dialog(self)

        def button_search_YANG_clicked():
            self.search_YANG_dialog = CSearch_YANG_Dialog(self)

        _layout.addWidget(QLabel("查询数据："), 0, _col)
        _layout.addWidget(QLabel(), 1, _col)
        button_search_CHAN_GAO = QPushButton("查询产羔记录")
        button_search_CHAN_GAO.clicked.connect(button_search_CHAN_GAO_clicked)
        _layout.addWidget(button_search_CHAN_GAO, 2, _col)
        button_search_YANG = QPushButton("查询湖羊数据")
        button_search_YANG.clicked.connect(button_search_YANG_clicked)
        _layout.addWidget(button_search_YANG, 3, _col)

    def create_edit_plane(self, _layout, _col=2):
        """
        修改数据部分
        """

        def button_edit_CHAN_GAO_clicked():
            self.edit_CHAN_GAO_dialog = CEdit_CHAN_GAO_Dialog(self)

        def button_edit_YANG_clicked():
            self.edit_YANG_dialog = CEdit_YANG_Dialog(self)

        _layout.addWidget(QLabel("修改数据："), 0, _col)
        _layout.addWidget(QLabel(), 1, _col)
        button_edit_CHAN_GAO = QPushButton("修改产羔记录")
        button_edit_CHAN_GAO.clicked.connect(button_edit_CHAN_GAO_clicked)
        _layout.addWidget(button_edit_CHAN_GAO, 2, _col)
        button_edit_YANG = QPushButton("修改湖羊数据")
        button_edit_YANG.clicked.connect(button_edit_YANG_clicked)
        _layout.addWidget(button_edit_YANG, 3, _col)

    def button_sheet_CHAN_GAO_JI_LU_clicked(self):
        self.sheet_CHAN_GAO_JI_LU_dialog = CSheet_CHAN_GAO_JI_LU_Dialog(self)

    def button_sheet_CHENG_ZHONG_JI_LU_clicked(self):
        self.sheet_CHENG_ZHONG_JI_LU_dialog = CSheet_CHENG_ZHONG_JI_LU_Dialog(self)

    def button_sheet_YU_ZHONG_JI_LU_clicked(self):
        self.sheet_YU_ZHONG_JI_LU_dialog = CSheet_YU_ZHONG_JI_LU_Dialog(self)

    def button_sheet_ZHONG_MU_YANG_HOU_YI_clicked(self):
        self.sheet_ZHONG_MU_YANG_HOU_YI_dialog = CSheet_ZHONG_MU_YANG_HOU_YI_Dialog(
            self
        )

    def button_sheet_ZHONG_GONG_YANG_HOU_YI_clicked(self):
        self.sheet_ZHONG_GONG_YANG_HOU_YI_dialog = CSheet_ZHONG_GONG_YANG_HOU_YI_Dialog(
            self
        )

    def button_avg_CHU_SHENG_DUAN_NAI_ZHONG_clicked(self):
        avg_CHU_SHENG_DUAN_NAI_ZHONG(self)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main_window = CMainWindow()

    sys.exit(app.exec_())
