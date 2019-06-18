import mysql.connector
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from mysql.connector import errorcode

from .sheet import CSheet


class CSheet_CHAN_GAO_JI_LU_Dialog(CSheet):
    def __init__(self, begin_date, end_date, parent=None):
        super(CSheet_CHAN_GAO_JI_LU_Dialog, self).__init__(parent)

        self.USER = parent.USER
        self.PASSWD = parent.PASSWD

        self.table_sheet.setColumnCount(14)
        self.sheet_header = [
            "棚号",
            "栏号",
            "母羊号",
            "公羊号",
            "胎次",
            "配种日期",
            "产羔日期",
            "产羔数",
            "活羔数",
            "羊羔编号",
            "羊羔性别",
            "羊羔出生重",
            "羊羔断奶重",
            "断奶日期",
        ]
        self.table_sheet.setHorizontalHeaderLabels(self.sheet_header)
        self.table_sheet.setRowCount(1)

        self.sheet_CHAN_GAO_JI_LU(begin_date, end_date)

        self.setWindowTitle("产羔记录表")
        self.show()

    def sheet_CHAN_GAO_JI_LU(self, begin_date, end_date):
        try:
            cnx = mysql.connector.connect(
                user=self.USER,
                password=self.PASSWD,
                database="pang_da_nong_ye",
                host="127.0.0.1",
            )
            cur = cnx.cursor()

            cur.execute(
                """
                SELECT c.chan_gao_hao,c.peng_hao,c.lan_hao,c.mu_yang_hao,c.gong_yang_hao,c.tai_ci,
                    c.pei_zhong_ri_qi,c.chan_gao_ri_qi,c.chan_gao,c.huo_gao,
                    y.bian_hao,y.xing_bie,y.chu_sheng_zhong,y.duan_nai_zhong,
                    c.duan_nai_ri_qi
                FROM chan_gao AS c JOIN yang AS y ON c.chan_gao_hao=y.chan_gao_hao
                WHERE c.chan_gao_ri_qi>="{}" AND c.chan_gao_ri_qi<="{}"
                ORDER BY c.chan_gao_hao
                """.format(
                    begin_date, end_date
                )
            )
            last_chan_gao_hao = None
            for d in cur:
                # 0. parse data
                cur_row = self.table_sheet.rowCount() - 1
                cur_chan_gao_hao = d[0]
                values = d[1:]
                # 1. save chan_gao info
                if cur_chan_gao_hao != last_chan_gao_hao:
                    for i in range(9):
                        if values[i]:
                            self.table_sheet.setItem(
                                cur_row, i, QTableWidgetItem(str(values[i]))
                            )
                    if values[-1]:
                        self.table_sheet.setItem(
                            cur_row, 13, QTableWidgetItem(str(values[-1]))
                        )
                    last_chan_gao_hao = cur_chan_gao_hao
                # 2. save yang info
                for i in range(9, 13):
                    if values[i]:
                        self.table_sheet.setItem(
                            cur_row, i, QTableWidgetItem(str(values[i]))
                        )
                # 3. inc row
                self.table_sheet.setRowCount(self.table_sheet.rowCount() + 1)

            cur.close()
            cnx.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                QMessageBox.information(self, "数据库错误", "登录数据库错误。")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                QMessageBox.information(self, "数据库错误", "数据库不存在。")
            elif err.errno == errorcode.ER_NO_SUCH_TABLE:
                QMessageBox.information(self, "数据库错误", "表单不存在。")
            else:
                QMessageBox.information(self, "数据库错误", str(err))
