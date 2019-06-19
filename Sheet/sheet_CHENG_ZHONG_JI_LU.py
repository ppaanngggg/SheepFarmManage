from datetime import timedelta

import mysql.connector
from mysql.connector import errorcode
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox, QTableWidgetItem

from .sheet import CSheet


class CSheet_CHENG_ZHONG_JI_LU_Dialog(CSheet):
    def __init__(self, begin_date, end_date, parent=None):
        super(CSheet_CHENG_ZHONG_JI_LU_Dialog, self).__init__(parent)

        self.USER = parent.USER
        self.PASSWD = parent.PASSWD

        text, ok = QInputDialog.getText(self, "称重记录表", "请输入棚号：", QLineEdit.Normal)

        if ok and text and not text.isspace():
            self.table_sheet.setColumnCount(17)
            self.sheet_header = [
                "栏号",
                "出生日期",
                "性别",
                "耳号",
                "出生重",
                "第一次称重日期",
                "第一次称重重量",
                "日增量",
                "月增量",
                "第二次称重日期",
                "第二次称重重量",
                "日增量",
                "月增量",
                "第三次称重日期",
                "第三次称重重量",
                "日增量",
                "月增量",
            ]
            self.table_sheet.setHorizontalHeaderLabels(self.sheet_header)
            self.table_sheet.setRowCount(1)

            self.sheet_CHENG_ZHONG_JI_LU(begin_date, end_date, text)

            self.setWindowTitle("称重记录表")
            self.show()
        else:
            if ok:
                QMessageBox.information(self, "输入错误", "无棚号输入。")

    def sheet_CHENG_ZHONG_JI_LU(self, _begin_date, _end_date, _peng_hao):
        try:
            cnx = mysql.connector.connect(
                user=self.USER,
                password=self.PASSWD,
                database="pang_da_nong_ye",
                host="127.0.0.1",
            )
            cur = cnx.cursor(buffered=True)
            cur.execute(
                """
                SELECT y.lan_hao,c.chan_gao_ri_qi,y.xing_bie,y.er_hao,
                    y.chu_sheng_zhong,c.duan_nai_ri_qi,y.duan_nai_zhong,
                    y.liu_yue_zhong,y.zhou_sui_zhong
                FROM yang AS y JOIN chan_gao AS c ON y.chan_gao_hao=c.chan_gao_hao
                WHERE c.chan_gao_ri_qi>="{}" AND c.chan_gao_ri_qi<="{}" AND y.peng_hao="{}"
                """.format(
                    _begin_date, _end_date, _peng_hao
                )
            )
            for d in cur:
                current_row = self.table_sheet.rowCount() - 1
                for i, v in enumerate(d[:6]):
                    if v:
                        self.table_sheet.setItem(
                            current_row, i, QTableWidgetItem(str(v))
                        )
                for i, v in enumerate(d[6:9]):
                    if v:
                        self.table_sheet.setItem(
                            current_row, 6 + 4 * i, QTableWidgetItem(str(v))
                        )
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
