import mysql.connector
from mysql.connector import errorcode
from datetime import date

from CHAN_GAO import *


class CAdd_CHAN_GAO_Dialog(CCHAN_GAO_Dialog):
    def __init__(self, parent=None):
        super(CAdd_CHAN_GAO_Dialog, self).__init__(parent)

        self.label_add_CHAN_GAO_dialog = QLabel('\n注：(*)为必填项\n')

        self.button_add_CHAN_GAO_dialog = QPushButton('添加产羔信息')
        self.button_add_CHAN_GAO_dialog.clicked.connect(self.button_add_CHAN_GAO_dialog_clicked)

        self.layout_CHAN_GAO_dialog.addWidget(self.label_add_CHAN_GAO_dialog)
        self.layout_CHAN_GAO_dialog.addWidget(self.button_add_CHAN_GAO_dialog)

        self.setWindowTitle('添加产羔信息')

    def button_add_CHAN_GAO_dialog_clicked(self):
        try:
            cnx = mysql.connector.connect(user='root', database='test')
            cursor = cnx.cursor()

            add_CHAN_GAO_index = 'insert into chan_gao ('
            add_CHAN_GAO_values = ') values ('

            if self.edit_CHAN_GAO_HAO.text() and not self.edit_CHAN_GAO_HAO.text().isspace():
                add_CHAN_GAO_index += 'chan_gao_hao,'
                add_CHAN_GAO_values += '"'+self.edit_CHAN_GAO_HAO.text() + '",'
            else:
                QMessageBox.information(self, '输入错误', '产羔号为必填项。')
                return

            if self.edit_PENG_HAO.text() and not self.edit_PENG_HAO.text().isspace():
                add_CHAN_GAO_index += 'peng_hao,'
                add_CHAN_GAO_values += '"'+self.edit_PENG_HAO.text() + '",'
            else:
                QMessageBox.information(self, '输入错误', '棚号为必填项。')
                return

            if self.edit_LAN_HAO.text() and not self.edit_LAN_HAO.text().isspace():
                add_CHAN_GAO_index += 'lan_hao,'
                add_CHAN_GAO_values += '"'+self.edit_LAN_HAO.text() + '",'
            else:
                QMessageBox.information(self, '输入错误', '栏号为必填项。')
                return

            if self.edit_MU_YANG_HAO.text() and not self.edit_MU_YANG_HAO.text().isspace():
                add_CHAN_GAO_index += 'mu_yang_hao,'
                add_CHAN_GAO_values += '"'+self.edit_MU_YANG_HAO.text() + '",'
            else:
                QMessageBox.information(self, '输入错误', '母羊号为必填项。')
                return

            if self.edit_GONG_YANG_HAO.text() and not self.edit_GONG_YANG_HAO.text().isspace():
                add_CHAN_GAO_index += 'gong_yang_hao,'
                add_CHAN_GAO_values += '"'+self.edit_GONG_YANG_HAO.text() + '",'
            else:
                QMessageBox.information(self, '输入错误', '公羊号为必填项。')
                return

            if self.edit_TAI_CI.text() and not self.edit_TAI_CI.text().isspace():
                add_CHAN_GAO_index += 'tai_ci,'
                add_CHAN_GAO_values += self.edit_TAI_CI.text() + ','

            if self.edit_PEI_ZHONG_RI_QI_year.text() and not self.edit_PEI_ZHONG_RI_QI_year.text().isspace()\
                    and self.edit_PEI_ZHONG_RI_QI_month.text() and not self.edit_PEI_ZHONG_RI_QI_month.text().isspace()\
                    and self.edit_PEI_ZHONG_RI_QI_day.text() and not self.edit_PEI_ZHONG_RI_QI_day.text().isspace():
                try:
                    date_PEI_ZHONG_RI_QI=str(date(int(self.edit_PEI_ZHONG_RI_QI_year.text()),
                                                  int(self.edit_PEI_ZHONG_RI_QI_month.text()),
                                                  int(self.edit_PEI_ZHONG_RI_QI_day.text())))
                    add_CHAN_GAO_index += 'pei_zhong_ri_qi,'
                    add_CHAN_GAO_values += '"'+ date_PEI_ZHONG_RI_QI+ '",'
                except Exception:
                    QMessageBox.information(self, '输入错误', '配种日期输入错误。')
                    return

            if self.edit_CHAN_GAO_RI_QI_year.text() and not self.edit_CHAN_GAO_RI_QI_year.text().isspace()\
                    and self.edit_CHAN_GAO_RI_QI_month.text() and not self.edit_CHAN_GAO_RI_QI_month.text().isspace()\
                    and self.edit_CHAN_GAO_RI_QI_day.text() and not self.edit_CHAN_GAO_RI_QI_day.text().isspace():
                try:
                    date_CHAN_GAO_RI_QI=str(date(int(self.edit_CHAN_GAO_RI_QI_year.text()),
                                                 int(self.edit_CHAN_GAO_RI_QI_month.text()),
                                                 int(self.edit_CHAN_GAO_RI_QI_day.text())))
                    add_CHAN_GAO_index += 'chan_gao_ri_qi,'
                    add_CHAN_GAO_values += '"'+ date_CHAN_GAO_RI_QI+ '",'
                except Exception:
                    QMessageBox.information(self, '输入错误', '产羔日期输入错误。')
                    return
            else:
                QMessageBox.information(self, '输入错误', '产羔日期为必填项。')
                return

            if self.edit_CHAN_GAO.text() and not self.edit_CHAN_GAO.text().isspace():
                add_CHAN_GAO_index += 'chan_gao,'
                add_CHAN_GAO_values += self.edit_CHAN_GAO.text() + ','
            else:
                QMessageBox.information(self, '输入错误', '产羔数为必填项。')
                return

            if self.edit_HUO_GAO.text() and not self.edit_HUO_GAO.text().isspace():
                add_CHAN_GAO_index += 'huo_gao,'
                add_CHAN_GAO_values += self.edit_HUO_GAO.text() + ','
            else:
                QMessageBox.information(self, '输入错误', '活羔数为必填项。')
                return

            if self.edit_DUAN_NAI_RI_QI_year.text() and not self.edit_DUAN_NAI_RI_QI_year.text().isspace()\
                    and self.edit_DUAN_NAI_RI_QI_month.text() and not self.edit_DUAN_NAI_RI_QI_month.text().isspace()\
                    and self.edit_DUAN_NAI_RI_QI_day.text() and not self.edit_DUAN_NAI_RI_QI_day.text().isspace():
                try:
                    date_DUAN_NAI_RI_QI=str(date(int(self.edit_DUAN_NAI_RI_QI_year.text()),
                                                 int(self.edit_DUAN_NAI_RI_QI_month.text()),
                                                 int(self.edit_DUAN_NAI_RI_QI_day.text())))
                    add_CHAN_GAO_index += 'duan_nai_ri_qi,'
                    add_CHAN_GAO_values += '"'+ date_DUAN_NAI_RI_QI+ '",'
                except Exception:
                    QMessageBox.information(self, '输入错误', '产羔日期输入错误。')
                    return

            add_CHAN_GAO_index = add_CHAN_GAO_index[:-1]
            add_CHAN_GAO_values = add_CHAN_GAO_values[:-1]
            add_CHAN_GAO=add_CHAN_GAO_index + add_CHAN_GAO_values + ');'
            print(add_CHAN_GAO)

            cursor.execute(add_CHAN_GAO)
            cnx.commit()
            cursor.close()
            cnx.close()

            self.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                QMessageBox.information(self, '数据库错误', '登录数据库错误。')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                QMessageBox.information(self, '数据库错误', '数据库不存在。')
            elif err.errno == errorcode.ER_PARSE_ERROR:
                QMessageBox.information(self, '数据库错误', '无数据输入。')
            elif err.errno == errorcode.ER_DUP_ENTRY:
                QMessageBox.information(self, '数据库错误', '产羔号重复。')
            elif err.errno ==errorcode.ER_BAD_FIELD_ERROR:
                QMessageBox.information(self, '数据库错误', '数据类型有误。')
            else:
                QMessageBox.information(self, '数据库错误', str(err))