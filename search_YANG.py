import mysql.connector
from mysql.connector import errorcode
from PyQt5.QtWidgets import *


class CSearch_YANG_Dialog(QWidget):
    def __init__(self, parent=None):
        super(CSearch_YANG_Dialog, self).__init__(parent)
        
        self.table_search_YANG=QTableWidget()
        
        YANG_info=self.get_YANG_info()
        self.output_YANG_info(YANG_info)

        self.layout_search_YANG_dialog=QVBoxLayout()
        self.layout_search_YANG_dialog.addWidget(self.table_search_YANG)

        self.setLayout(self.layout_search_YANG_dialog)
        self.setWindowTitle('查询湖羊数据')

    def get_YANG_info(self):
        try:
            cnx = mysql.connector.connect(user='root', database='test')
            cursor = cnx.cursor()
            cursor.execute('select * from yang')

            YANG_info = []
            for YANG_info_item in cursor:
                YANG_info.append(YANG_info_item)
            # print(YANG_info)

            cursor.close()
            cnx.close()
            
            return YANG_info
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                QMessageBox.information(self, '数据库错误', '登录数据库错误。')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                QMessageBox.information(self, '数据库错误', '数据库不存在。')
            elif err.errno == errorcode.ER_NO_SUCH_TABLE:
                QMessageBox.information(self, '数据库错误', '表单不存在。')
            else:
                QMessageBox.information(self, '数据库错误', str(err))

    def output_YANG_info(self,YANG_info):
        if YANG_info:
            self.table_search_YANG.setColumnCount(YANG_info[0].__len__())
            self.table_search_YANG.setRowCount(YANG_info.__len__())
            self.table_search_YANG.setHorizontalHeaderLabels(
                ['编号', '棚号', '栏号', '产羔号', '性别', '耳号', '出生重', '断奶重', '六月重', '周岁重', '去向'])

            for row in range(0, YANG_info.__len__()):
                for col in range(0, YANG_info[0].__len__()):
                    if YANG_info[row][col]:
                        self.table_search_YANG.setItem(row, col, QTableWidgetItem(str(YANG_info[row][col])))
        else:
            QMessageBox.information(self, '查询湖羊数据', '无湖羊数据。')