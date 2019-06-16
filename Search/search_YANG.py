import mysql.connector
from PyQt5.QtWidgets import (
    QDialog,
    QTableWidget,
    QAbstractItemView,
    QVBoxLayout,
    QMessageBox,
    QTableWidgetItem,
)
from mysql.connector import errorcode


class CSearch_YANG_Dialog(QDialog):
    def __init__(self, begin_date, end_date, parent=None):
        super(CSearch_YANG_Dialog, self).__init__(parent)

        self.USER = parent.USER
        self.PASSWD = parent.PASSWD

        self.table_search_YANG = QTableWidget()
        self.table_search_YANG.setEditTriggers(QAbstractItemView.NoEditTriggers)

        layout = QVBoxLayout()
        layout.addWidget(self.table_search_YANG)

        self.setLayout(layout)
        self.setWindowTitle("查询湖羊数据")
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        YANG_info = self.get_YANG_info(begin_date, end_date)
        if YANG_info:
            self.output_YANG_info(YANG_info)
            self.show()
        else:
            QMessageBox.information(self, "查询湖羊数据", "无湖羊数据。")

    def get_YANG_info(self, begin_date, end_date):
        try:
            cnx = mysql.connector.connect(
                user=self.USER,
                password=self.PASSWD,
                database="pang_da_nong_ye",
                host="127.0.0.1",
            )
            cursor = cnx.cursor()
            cursor.execute(
                """
                SELECT t1.* 
                FROM yang AS t1 JOIN chan_gao AS t2
                ON t1.chan_gao_hao=t2.chan_gao_hao
                WHERE t2.chan_gao_ri_qi>"{}" AND t2.chan_gao_ri_qi<"{}"
                ORDER BY t2.chan_gao_ri_qi
                """.format(
                    begin_date, end_date
                )
            )

            YANG_info = []
            for YANG_info_item in cursor:
                YANG_info.append(YANG_info_item)

            cursor.close()
            cnx.close()

            return YANG_info
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                QMessageBox.information(self, "数据库错误", "登录数据库错误。")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                QMessageBox.information(self, "数据库错误", "数据库不存在。")
            elif err.errno == errorcode.ER_NO_SUCH_TABLE:
                QMessageBox.information(self, "数据库错误", "表单不存在。")
            else:
                QMessageBox.information(self, "数据库错误", str(err))

    def output_YANG_info(self, YANG_info):
        self.table_search_YANG.setColumnCount(YANG_info[0].__len__())
        self.table_search_YANG.setRowCount(YANG_info.__len__())
        self.table_search_YANG.setHorizontalHeaderLabels(
            ["编号", "棚号", "栏号", "产羔号", "性别", "耳号", "出生重", "断奶重", "六月重", "周岁重", "去向"]
        )

        for row in range(0, YANG_info.__len__()):
            for col in range(0, YANG_info[0].__len__()):
                if YANG_info[row][col]:
                    self.table_search_YANG.setItem(
                        row, col, QTableWidgetItem(str(YANG_info[row][col]))
                    )
