from PyQt5 import QtCore

from login_database import *
from add_from_sheet import *
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
from avg_CHU_SHENG_DUAN_NAI_ZHONG import *


class CMainWindow(QWidget):

    def __init__(self, parent=None):
        super(CMainWindow, self).__init__(parent)

        self.USER = ''
        self.PASSWD = ''
        self.HOST = '127.0.0.1'

        if self.login_database() == True:
            self.label_main = QLabel('欢迎使用湖羊数据管理系统')
            self.label_main.setAlignment(QtCore.Qt.AlignHCenter)

            self.label_add = QLabel('添加数据：')
            self.button_add_from_sheet = QPushButton('从表格导入数据')
            self.button_add_from_sheet.clicked.connect(
                self.button_add_from_sheet_clicked)
            self.button_add_CHAN_GAO = QPushButton('添加产羔记录')
            self.button_add_CHAN_GAO.clicked.connect(
                self.button_add_CHAN_GAO_clicked)
            self.button_add_YANG = QPushButton('添加湖羊数据')
            self.button_add_YANG.clicked.connect(self.button_add_YANG_clicked)
            self.layout_add = QVBoxLayout()
            self.layout_add.setSpacing(10)
            self.layout_add.addWidget(self.label_add)
            self.layout_add.addWidget(self.button_add_from_sheet)
            self.layout_add.addWidget(self.button_add_CHAN_GAO)
            self.layout_add.addWidget(self.button_add_YANG)

            self.label_search = QLabel('查询数据：')
            self.button_search_CHAN_GAO = QPushButton('查询产羔记录')
            self.button_search_CHAN_GAO.clicked.connect(
                self.button_search_CHAN_GAO_clicked)
            self.button_search_YANG = QPushButton('查询湖羊数据')
            self.button_search_YANG.clicked.connect(
                self.button_search_YANG_clicked)
            self.layout_search = QVBoxLayout()
            self.layout_search.setSpacing(10)
            self.layout_search.addWidget(self.label_search)
            self.layout_search.addWidget(self.button_search_CHAN_GAO)
            self.layout_search.addWidget(self.button_search_YANG)

            self.label_edit = QLabel('修改数据：')
            self.button_edit_CHAN_GAO = QPushButton('修改产羔记录')
            self.button_edit_CHAN_GAO.clicked.connect(
                self.button_edit_CHAN_GAO_clicked)
            self.button_edit_YANG = QPushButton('修改湖羊数据')
            self.button_edit_YANG.clicked.connect(
                self.button_edit_YANG_clicked)
            self.layout_edit = QVBoxLayout()
            self.layout_edit.setSpacing(10)
            self.layout_edit.addWidget(self.label_edit)
            self.layout_edit.addWidget(self.button_edit_CHAN_GAO)
            self.layout_edit.addWidget(self.button_edit_YANG)

            self.label_sheet = QLabel('生成表格：')
            self.button_sheet_CHAN_GAO_JI_LU = QPushButton('产羔记录表')
            self.button_sheet_CHAN_GAO_JI_LU.clicked.connect(
                self.button_sheet_CHAN_GAO_JI_LU_clicked)
            self.button_sheet_CHENG_ZHONG_JI_LU = QPushButton('称重记录表')
            self.button_sheet_CHENG_ZHONG_JI_LU.clicked.connect(
                self.button_sheet_CHENG_ZHONG_JI_LU_clicked)
            self.button_sheet_YU_ZHONG_JI_LU = QPushButton('育种记录表')
            self.button_sheet_YU_ZHONG_JI_LU.clicked.connect(
                self.button_sheet_YU_ZHONG_JI_LU_clicked)
            self.button_sheet_ZHONG_MU_YANG_HOU_YI = QPushButton('种母羊后裔表')
            self.button_sheet_ZHONG_MU_YANG_HOU_YI.clicked.connect(
                self.button_sheet_ZHONG_MU_YANG_HOU_YI_clicked)
            self.button_sheet_ZHONG_GONG_YANG_HOU_YI = QPushButton('种公羊后裔表')
            self.button_sheet_ZHONG_GONG_YANG_HOU_YI.clicked.connect(
                self.button_sheet_ZHONG_GONG_YANG_HOU_YI_clicked)
            self.layout_sheet = QVBoxLayout()
            self.layout_sheet.setSpacing(10)
            self.layout_sheet.addWidget(self.label_sheet)
            self.layout_sheet.addWidget(self.button_sheet_CHAN_GAO_JI_LU)
            self.layout_sheet.addWidget(self.button_sheet_CHENG_ZHONG_JI_LU)
            self.layout_sheet.addWidget(self.button_sheet_YU_ZHONG_JI_LU)
            self.layout_sheet.addWidget(self.button_sheet_ZHONG_MU_YANG_HOU_YI)
            self.layout_sheet.addWidget(
                self.button_sheet_ZHONG_GONG_YANG_HOU_YI)

            self.label_statistic = QLabel('数据统计：')
            self.button_avg_CHU_SHENG_DUAN_NAI_ZHONG = QPushButton(
                '出生重，断奶重平均值')
            self.button_avg_CHU_SHENG_DUAN_NAI_ZHONG.clicked.connect(
                self.button_avg_CHU_SHENG_DUAN_NAI_ZHONG_clicked)
            self.layout_statistic = QVBoxLayout()
            self.layout_statistic.setSpacing(10)
            self.layout_statistic.addWidget(self.label_statistic)
            self.layout_statistic.addWidget(
                self.button_avg_CHU_SHENG_DUAN_NAI_ZHONG)

            self.layout_operate = QHBoxLayout()
            self.layout_operate.setSpacing(30)
            self.layout_operate.addLayout(self.layout_add)
            self.layout_operate.addLayout(self.layout_search)
            self.layout_operate.addLayout(self.layout_edit)
            self.layout_operate.addLayout(self.layout_sheet)
            self.layout_operate.addLayout(self.layout_statistic)

            self.main_layout = QVBoxLayout()
            self.main_layout.addWidget(self.label_main)
            self.main_layout.addLayout(self.layout_operate)

            self.setLayout(self.main_layout)
            self.setWindowTitle('湖羊数据管理系统')

            # self.test_database()
            self.show()
            # self.close()
        else:
            import sys

            sys.exit(1)

    def login_database(self):
        user_and_passwd = ['', '']
        login_database_dialog = CLogin_Database_Dialog(user_and_passwd, self)
        if login_database_dialog.exec() == QDialog.Accepted:
            try:
                cnx = mysql.connector.connect(user=user_and_passwd[0],
                                              password=user_and_passwd[1],
                                              database='pang_da_nong_ye',
                                              host=self.HOST)
                cnx.close()
                self.USER = user_and_passwd[0]
                self.PASSWD = user_and_passwd[1]
                return True
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    QMessageBox.information(self, '数据库错误', '用户名或密码错误。')
                elif err.errno == errorcode.ER_DBACCESS_DENIED_ERROR:
                    QMessageBox.information(self, '数据库错误', '该用户无访问权限')
                elif err.errno == errorcode.CR_CONN_HOST_ERROR:
                    QMessageBox.information(self, '数据库错误', '无法连接到服务器')
                else:
                    QMessageBox.information(self, '数据库错误', str(err))
                return False
        else:
            return False

    # def test_database(self):
    # try:
    #         cnx = mysql.connector.connect(user='root')
    #         cursor = cnx.cursor()
    #
    #         try:
    #             cnx.database = 'test'
    #         except mysql.connector.Error as err:
    #             if err.errno == errorcode.ER_BAD_DB_ERROR:
    #                 try:
    #                     cursor.execute('create database test character set gbk')
    #                     cnx.database = 'test'
    #                 except mysql.connector.Error as err:
    #                     QMessageBox.information(self, '数据库错误', str(err))
    #             else:
    #                 QMessageBox.information(self, '数据库错误', str(err))
    #
    #         add_table_chan_gao = '''
    #             create table chan_gao
    #             (
    #                 chan_gao_hao char(30) not null primary key,
    #                 peng_hao char(5) not null,
    #                 lan_hao char(5) not null,
    #                 mu_yang_hao char(10) not null,
    #                 gong_yang_hao char(10) not null,
    #                 tai_ci int,
    #                 pei_zhong_ri_qi date,
    #                 chan_gao_ri_qi date not null,
    #                 chan_gao int not null,
    #                 huo_gao int not null,
    #                 duan_nai_ri_qi date
    #             );
    #         '''
    #         try:
    #             cursor.execute(add_table_chan_gao)
    #         except mysql.connector.Error as err:
    #             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
    #                 print('table_chan_gao 存在。')
    #             else:
    #                 QMessageBox.information(self, '数据库错误', str(err))
    #
    #         add_table_yang = '''
    #             create table yang
    #             (
    #                 bian_hao char(10) not null primary key,
    #                 peng_hao char(5),
    #                 lan_hao char(5),
    #                 chan_gao_hao char(30) not null,
    #                 xing_bie char(5) not null,
    #                 er_hao char(10),
    #                 chu_sheng_zhong float(10,1),
    #                 duan_nai_zhong float(10,1),
    #                 liu_yue_zhong float(10,1),
    #                 zhou_sui_zhong float(10,1),
    #                 qu_xiang char(20)
    #             );
    #         '''
    #         try:
    #             cursor.execute(add_table_yang)
    #         except mysql.connector.Error as err:
    #             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
    #                 print('table_yang 存在。')
    #             else:
    #                 QMessageBox.information(self, '数据库错误', str(err))
    #
    #         cursor.close()
    #         cnx.close()
    #
    #     except mysql.connector.Error as err:
    #         QMessageBox.information(self, '数据库错误', str(err))

    def button_add_from_sheet_clicked(self):
        str_path, str_filter = QFileDialog.getOpenFileName(
            self, '从表格导入数据', '', '(*.xlsx | *.xls)')
        if str_path and not str_path.isspace():
            add_from_sheet(str_path, self)

    def button_add_CHAN_GAO_clicked(self):
        self.add_CHAN_GAO_dialog = CAdd_CHAN_GAO_Dialog(self)
        self.add_CHAN_GAO_dialog.show()

    def button_add_YANG_clicked(self):
        self.add_YANG_dialog = CAdd_YANG_Dialog(self)
        self.add_YANG_dialog.show()

    def button_search_CHAN_GAO_clicked(self):
        self.search_CHAN_GAO_dialog = CSearch_CHAN_GAO_Dialog(self)

    def button_search_YANG_clicked(self):
        self.search_YANG_dialog = CSearch_YANG_Dialog(self)

    def button_edit_CHAN_GAO_clicked(self):
        self.edit_CHAN_GAO_dialog = CEdit_CHAN_GAO_Dialog(self)

    def button_edit_YANG_clicked(self):
        self.edit_YANG_dialog = CEdit_YANG_Dialog(self)

    def button_sheet_CHAN_GAO_JI_LU_clicked(self):
        self.sheet_CHAN_GAO_JI_LU_dialog = CSheet_CHAN_GAO_JI_LU_Dialog(self)

    def button_sheet_CHENG_ZHONG_JI_LU_clicked(self):
        self.sheet_CHENG_ZHONG_JI_LU_dialog = CSheet_CHENG_ZHONG_JI_LU_Dialog(
            self)

    def button_sheet_YU_ZHONG_JI_LU_clicked(self):
        self.sheet_YU_ZHONG_JI_LU_dialog = CSheet_YU_ZHONG_JI_LU_Dialog(self)

    def button_sheet_ZHONG_MU_YANG_HOU_YI_clicked(self):
        self.sheet_ZHONG_MU_YANG_HOU_YI_dialog = CSheet_ZHONG_MU_YANG_HOU_YI_Dialog(
            self)

    def button_sheet_ZHONG_GONG_YANG_HOU_YI_clicked(self):
        self.sheet_ZHONG_GONG_YANG_HOU_YI_dialog = CSheet_ZHONG_GONG_YANG_HOU_YI_Dialog(
            self)

    def button_avg_CHU_SHENG_DUAN_NAI_ZHONG_clicked(self):
        avg_CHU_SHENG_DUAN_NAI_ZHONG(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    main_window = CMainWindow()
    # main_window.show()

    sys.exit(app.exec_())
