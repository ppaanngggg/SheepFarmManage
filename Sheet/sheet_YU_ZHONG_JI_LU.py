import mysql.connector
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QComboBox, QLabel
from mysql.connector import errorcode

from utils.DATE import DateDialog
from .sheet import CSheet


class YU_ZHONG_DateDialog(DateDialog):
    def __init__(self, parent=None):
        super(YU_ZHONG_DateDialog, self).__init__(parent)

        layout = self.layout()
        layout.addWidget(QLabel("是否仅包含种羊？"), 2, 0)
        self.only_er_hao = QComboBox()
        self.only_er_hao.addItems(["是", "否"])
        layout.addWidget(self.only_er_hao, 2, 1)
        layout.addWidget(QLabel("性别："), 2, 2)
        self.xing_bie = QComboBox()
        self.xing_bie.addItems(["全部", "公", "母"])
        layout.addWidget(self.xing_bie, 2, 3)

    def get_result(self):
        begin_date, end_date = super().get_result()
        return (
            begin_date,
            end_date,
            self.only_er_hao.currentText(),
            self.xing_bie.currentText(),
        )


class CSheet_YU_ZHONG_JI_LU_Dialog(CSheet):
    def __init__(self, begin_date, end_date, only_er_hao, xing_bie, parent=None):
        super(CSheet_YU_ZHONG_JI_LU_Dialog, self).__init__(parent)

        self.USER = parent.USER
        self.PASSWD = parent.PASSWD

        self.table_sheet.setColumnCount(14)
        self.sheet_header = [
            "耳号",
            "免疫号",
            "出生日期",
            "母亲号",
            "父亲号",
            "祖母",
            "祖父",
            "外祖母",
            "外祖父",
            "同胞数",
            "出生重",
            "断奶重",
            "六月重",
            "周岁重",
        ]
        self.table_sheet.setHorizontalHeaderLabels(self.sheet_header)
        self.table_sheet.setRowCount(1)

        self.sheet_YU_ZHONG_JI_LU(begin_date, end_date, only_er_hao, xing_bie)

        self.setWindowTitle("育种记录表")
        self.show()

    def _find_mu_yang_gong_yang_by_er_hao(self, _cnx, _er_hao):
        cur = _cnx.cursor()
        try:
            cur.execute(
                """
                SELECT c.mu_yang_hao,c.gong_yang_hao
                FROM chan_gao AS c JOIN yang AS y ON c.chan_gao_hao=y.chan_gao_hao
                WHERE y.er_hao="{}"
                """.format(
                    _er_hao
                )
            )
            ret = cur.fetchone()
            if ret is None:
                return None, None
            else:
                return ret
        finally:
            cur.close()

    def sheet_YU_ZHONG_JI_LU(self, _begin_date, _end_date, only_er_hao, xing_bie):
        try:
            query = """
                SELECT y.er_hao,y.bian_hao,c.chan_gao_ri_qi,c.mu_yang_hao,c.gong_yang_hao,
                    c.huo_gao,y.chu_sheng_zhong,y.duan_nai_zhong,y.liu_yue_zhong,y.zhou_sui_zhong
                FROM yang AS y JOIN chan_gao AS c ON y.chan_gao_hao=c.chan_gao_hao
                WHERE c.chan_gao_ri_qi>="{}" AND c.chan_gao_ri_qi<="{}"
            """.format(
                _begin_date, _end_date
            )
            if only_er_hao == "是":
                query += " AND y.er_hao IS NOT NULL"
            if xing_bie != "全部":
                query += " AND y.xing_bie='{}'".format(xing_bie)

            cnx = mysql.connector.connect(
                user=self.USER,
                password=self.PASSWD,
                database="pang_da_nong_ye",
                host="127.0.0.1",
            )
            cur = cnx.cursor(buffered=True)

            cur.execute(query)

            for d in cur:
                mu_yang = d[3]
                gong_yang = d[4]
                tmp = (
                    d[:5]
                    + self._find_mu_yang_gong_yang_by_er_hao(cnx, gong_yang)
                    + self._find_mu_yang_gong_yang_by_er_hao(cnx, mu_yang)
                    + d[5:]
                )
                cur_row = self.table_sheet.rowCount() - 1
                for i, v in enumerate(tmp):
                    if v:
                        self.table_sheet.setItem(cur_row, i, QTableWidgetItem(str(v)))
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
