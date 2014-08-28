import mysql.connector
from mysql.connector import errorcode
from PyQt5.QtWidgets import *


class CSearch_CHAN_GAO_Dialog(QDialog):
    def __init__(self, parent=None):
        super(CSearch_CHAN_GAO_Dialog, self).__init__(parent)

        self.USER=parent.USER
        self.PASSWD=parent.PASSWD

        self.table_search_CHAN_GAO = QTableWidget()
        self.table_search_CHAN_GAO.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.layout_search_CHAN_GAO_dialog = QVBoxLayout()
        self.layout_search_CHAN_GAO_dialog.addWidget(self.table_search_CHAN_GAO)

        self.setLayout(self.layout_search_CHAN_GAO_dialog)
        self.setWindowTitle('查询产羔记录')

        CHAN_GAO_info = self.get_CHAN_GAO_info()
        if CHAN_GAO_info:
            self.output_CHAN_GAO_info(CHAN_GAO_info)
            self.show()
        else:
            QMessageBox.information(self, '查询产羔记录', '无产羔记录。')

    def get_CHAN_GAO_info(self):
        try:
            cnx = mysql.connector.connect(user=self.USER,
                                          password=self.PASSWD,
                                          database='pang_da_nong_ye',
                                          host='115.29.168.27')
            cursor = cnx.cursor()
            cursor.execute('select * from chan_gao')

            CHAN_GAO_info = []
            for CHAN_GAO_info_item in cursor:
                CHAN_GAO_info.append(CHAN_GAO_info_item)
            # print(CHAN_GAO_info)

            cursor.close()
            cnx.close()

            return CHAN_GAO_info
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                QMessageBox.information(self, '数据库错误', '登录数据库错误。')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                QMessageBox.information(self, '数据库错误', '数据库不存在。')
            elif err.errno == errorcode.ER_NO_SUCH_TABLE:
                QMessageBox.information(self, '数据库错误', '表单不存在。')
            else:
                QMessageBox.information(self, '数据库错误', str(err))

    def output_CHAN_GAO_info(self, CHAN_GAO_info):
        self.table_search_CHAN_GAO.setColumnCount(CHAN_GAO_info[0].__len__())
        self.table_search_CHAN_GAO.setRowCount(CHAN_GAO_info.__len__())
        self.table_search_CHAN_GAO.setHorizontalHeaderLabels(
            ['产羔号', '棚号', '栏号', '母羊号', '公羊号', '胎次', '配种日期', '产羔日期', '产羔数', '活羔数', '断奶日期'])

        for row in range(0, CHAN_GAO_info.__len__()):
            for col in range(0, CHAN_GAO_info[0].__len__()):
                if CHAN_GAO_info[row][col]:
                    self.table_search_CHAN_GAO.setItem(row, col, QTableWidgetItem(str(CHAN_GAO_info[row][col])))