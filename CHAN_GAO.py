from PyQt5.QtWidgets import *
import mysql.connector
from mysql.connector import errorcode
from datetime import date


class CCHAN_GAO_Dialog(QDialog):
    def __init__(self, parent=None):
        super(CCHAN_GAO_Dialog, self).__init__(parent)

        self.label_CHAN_GAO_HAO = QLabel('产羔号(*)：')
        self.edit_CHAN_GAO_HAO = QLineEdit()
        self.layout_CHAN_GAO_HAO = QHBoxLayout()
        self.layout_CHAN_GAO_HAO.addWidget(self.label_CHAN_GAO_HAO)
        self.layout_CHAN_GAO_HAO.addWidget(self.edit_CHAN_GAO_HAO)

        self.label_PENG_HAO = QLabel('棚号(*)：')
        self.edit_PENG_HAO = QLineEdit()
        self.layout_PENG_HAO = QHBoxLayout()
        self.layout_PENG_HAO.addWidget(self.label_PENG_HAO)
        self.layout_PENG_HAO.addWidget(self.edit_PENG_HAO)

        self.label_LAN_HAO = QLabel('栏号(*)：')
        self.edit_LAN_HAO = QLineEdit()
        self.layout_LAN_HAO = QHBoxLayout()
        self.layout_LAN_HAO.addWidget(self.label_LAN_HAO)
        self.layout_LAN_HAO.addWidget(self.edit_LAN_HAO)

        self.label_MU_YANG_HAO = QLabel('母羊号(*)：')
        self.edit_MU_YANG_HAO = QLineEdit()
        self.layout_MU_YANG_HAO = QHBoxLayout()
        self.layout_MU_YANG_HAO.addWidget(self.label_MU_YANG_HAO)
        self.layout_MU_YANG_HAO.addWidget(self.edit_MU_YANG_HAO)

        self.label_GONG_YANG_HAO = QLabel('公羊号(*)：')
        self.edit_GONG_YANG_HAO = QLineEdit()
        self.layout_GONG_YANG_HAO = QHBoxLayout()
        self.layout_GONG_YANG_HAO.addWidget(self.label_GONG_YANG_HAO)
        self.layout_GONG_YANG_HAO.addWidget(self.edit_GONG_YANG_HAO)

        self.label_TAI_CI = QLabel('胎次：')
        self.edit_TAI_CI = QLineEdit()
        self.layout_TAI_CI = QHBoxLayout()
        self.layout_TAI_CI.addWidget(self.label_TAI_CI)
        self.layout_TAI_CI.addWidget(self.edit_TAI_CI)

        self.label_PEI_ZHONG_RI_QI = QLabel('配种日期：')
        self.edit_PEI_ZHONG_RI_QI_year = QLineEdit()
        self.label_PEI_ZHONG_RI_QI_year = QLabel('年')
        self.edit_PEI_ZHONG_RI_QI_month = QLineEdit()
        self.label_PEI_ZHONG_RI_QI_month = QLabel('月')
        self.edit_PEI_ZHONG_RI_QI_day = QLineEdit()
        self.label_PEI_ZHONG_RI_QI_day = QLabel('日')
        self.layout_PEI_ZHONG_RI_QI = QHBoxLayout()
        self.layout_PEI_ZHONG_RI_QI.addWidget(self.label_PEI_ZHONG_RI_QI)
        self.layout_PEI_ZHONG_RI_QI.addWidget(self.edit_PEI_ZHONG_RI_QI_year)
        self.layout_PEI_ZHONG_RI_QI.addWidget(self.label_PEI_ZHONG_RI_QI_year)
        self.layout_PEI_ZHONG_RI_QI.addWidget(self.edit_PEI_ZHONG_RI_QI_month)
        self.layout_PEI_ZHONG_RI_QI.addWidget(self.label_PEI_ZHONG_RI_QI_month)
        self.layout_PEI_ZHONG_RI_QI.addWidget(self.edit_PEI_ZHONG_RI_QI_day)
        self.layout_PEI_ZHONG_RI_QI.addWidget(self.label_PEI_ZHONG_RI_QI_day)

        self.label_CHAN_GAO_RI_QI = QLabel('产羔日期(*)：')
        self.edit_CHAN_GAO_RI_QI_year = QLineEdit()
        self.label_CHAN_GAO_RI_QI_year = QLabel('年')
        self.edit_CHAN_GAO_RI_QI_month = QLineEdit()
        self.label_CHAN_GAO_RI_QI_month = QLabel('月')
        self.edit_CHAN_GAO_RI_QI_day = QLineEdit()
        self.label_CHAN_GAO_RI_QI_day = QLabel('日')
        self.layout_CHAN_GAO_RI_QI = QHBoxLayout()
        self.layout_CHAN_GAO_RI_QI.addWidget(self.label_CHAN_GAO_RI_QI)
        self.layout_CHAN_GAO_RI_QI.addWidget(self.edit_CHAN_GAO_RI_QI_year)
        self.layout_CHAN_GAO_RI_QI.addWidget(self.label_CHAN_GAO_RI_QI_year)
        self.layout_CHAN_GAO_RI_QI.addWidget(self.edit_CHAN_GAO_RI_QI_month)
        self.layout_CHAN_GAO_RI_QI.addWidget(self.label_CHAN_GAO_RI_QI_month)
        self.layout_CHAN_GAO_RI_QI.addWidget(self.edit_CHAN_GAO_RI_QI_day)
        self.layout_CHAN_GAO_RI_QI.addWidget(self.label_CHAN_GAO_RI_QI_day)

        self.label_CHAN_GAO = QLabel('产羔数(*)：')
        self.edit_CHAN_GAO = QLineEdit()
        self.layout_CHAN_GAO = QHBoxLayout()
        self.layout_CHAN_GAO.addWidget(self.label_CHAN_GAO)
        self.layout_CHAN_GAO.addWidget(self.edit_CHAN_GAO)
        
        self.label_HUO_GAO=QLabel('活羔数(*)：')
        self.edit_HUO_GAO=QLineEdit()
        self.layout_HUO_GAO=QHBoxLayout()
        self.layout_HUO_GAO.addWidget(self.label_HUO_GAO)
        self.layout_HUO_GAO.addWidget(self.edit_HUO_GAO)
        
        self.label_DUAN_NAI_RI_QI = QLabel('断奶日期：')
        self.edit_DUAN_NAI_RI_QI_year = QLineEdit()
        self.label_DUAN_NAI_RI_QI_year = QLabel('年')
        self.edit_DUAN_NAI_RI_QI_month = QLineEdit()
        self.label_DUAN_NAI_RI_QI_month = QLabel('月')
        self.edit_DUAN_NAI_RI_QI_day = QLineEdit()
        self.label_DUAN_NAI_RI_QI_day = QLabel('日')
        self.layout_DUAN_NAI_RI_QI = QHBoxLayout()
        self.layout_DUAN_NAI_RI_QI.addWidget(self.label_DUAN_NAI_RI_QI)
        self.layout_DUAN_NAI_RI_QI.addWidget(self.edit_DUAN_NAI_RI_QI_year)
        self.layout_DUAN_NAI_RI_QI.addWidget(self.label_DUAN_NAI_RI_QI_year)
        self.layout_DUAN_NAI_RI_QI.addWidget(self.edit_DUAN_NAI_RI_QI_month)
        self.layout_DUAN_NAI_RI_QI.addWidget(self.label_DUAN_NAI_RI_QI_month)
        self.layout_DUAN_NAI_RI_QI.addWidget(self.edit_DUAN_NAI_RI_QI_day)
        self.layout_DUAN_NAI_RI_QI.addWidget(self.label_DUAN_NAI_RI_QI_day)

        self.layout_CHAN_GAO_dialog = QVBoxLayout()
        self.layout_CHAN_GAO_dialog.addLayout(self.layout_CHAN_GAO_HAO)
        self.layout_CHAN_GAO_dialog.addLayout(self.layout_PENG_HAO)
        self.layout_CHAN_GAO_dialog.addLayout(self.layout_LAN_HAO)
        self.layout_CHAN_GAO_dialog.addLayout(self.layout_MU_YANG_HAO)
        self.layout_CHAN_GAO_dialog.addLayout(self.layout_GONG_YANG_HAO)
        self.layout_CHAN_GAO_dialog.addLayout(self.layout_TAI_CI)
        self.layout_CHAN_GAO_dialog.addLayout(self.layout_PEI_ZHONG_RI_QI)
        self.layout_CHAN_GAO_dialog.addLayout(self.layout_CHAN_GAO_RI_QI)
        self.layout_CHAN_GAO_dialog.addLayout(self.layout_CHAN_GAO)
        self.layout_CHAN_GAO_dialog.addLayout(self.layout_HUO_GAO)
        self.layout_CHAN_GAO_dialog.addLayout(self.layout_DUAN_NAI_RI_QI)

        self.setLayout(self.layout_CHAN_GAO_dialog)

    def add_CHAN_GAO_info(self):
        try:
            cnx = mysql.connector.connect(user=self.USER,
                                          password=self.PASSWD,
                                          database='pang_da_nong_ye',
                                          host='self.HOST')
            cursor = cnx.cursor()

            add_CHAN_GAO_index = 'insert into chan_gao ('
            add_CHAN_GAO_values = ') values ('

            if self.edit_CHAN_GAO_HAO.text() and not self.edit_CHAN_GAO_HAO.text().isspace():
                add_CHAN_GAO_index += 'chan_gao_hao,'
                add_CHAN_GAO_values += '"'+self.edit_CHAN_GAO_HAO.text() + '",'
            else:
                QMessageBox.information(self, '输入错误', '产羔号为必填项。')
                return False

            if self.edit_PENG_HAO.text() and not self.edit_PENG_HAO.text().isspace():
                add_CHAN_GAO_index += 'peng_hao,'
                add_CHAN_GAO_values += '"'+self.edit_PENG_HAO.text() + '",'
            else:
                QMessageBox.information(self, '输入错误', '棚号为必填项。')
                return False

            if self.edit_LAN_HAO.text() and not self.edit_LAN_HAO.text().isspace():
                add_CHAN_GAO_index += 'lan_hao,'
                add_CHAN_GAO_values += '"'+self.edit_LAN_HAO.text() + '",'
            else:
                QMessageBox.information(self, '输入错误', '栏号为必填项。')
                return False

            if self.edit_MU_YANG_HAO.text() and not self.edit_MU_YANG_HAO.text().isspace():
                add_CHAN_GAO_index += 'mu_yang_hao,'
                add_CHAN_GAO_values += '"'+self.edit_MU_YANG_HAO.text() + '",'
            else:
                QMessageBox.information(self, '输入错误', '母羊号为必填项。')
                return False

            if self.edit_GONG_YANG_HAO.text() and not self.edit_GONG_YANG_HAO.text().isspace():
                add_CHAN_GAO_index += 'gong_yang_hao,'
                add_CHAN_GAO_values += '"'+self.edit_GONG_YANG_HAO.text() + '",'
            else:
                QMessageBox.information(self, '输入错误', '公羊号为必填项。')
                return False

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
                    return False

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
                    return False
            else:
                QMessageBox.information(self, '输入错误', '产羔日期为必填项。')
                return False

            if self.edit_CHAN_GAO.text() and not self.edit_CHAN_GAO.text().isspace():
                add_CHAN_GAO_index += 'chan_gao,'
                add_CHAN_GAO_values += self.edit_CHAN_GAO.text() + ','
            else:
                QMessageBox.information(self, '输入错误', '产羔数为必填项。')
                return False

            if self.edit_HUO_GAO.text() and not self.edit_HUO_GAO.text().isspace():
                add_CHAN_GAO_index += 'huo_gao,'
                add_CHAN_GAO_values += self.edit_HUO_GAO.text() + ','
            else:
                QMessageBox.information(self, '输入错误', '活羔数为必填项。')
                return False

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
                    return False

            add_CHAN_GAO_index = add_CHAN_GAO_index[:-1]
            add_CHAN_GAO_values = add_CHAN_GAO_values[:-1]
            add_CHAN_GAO=add_CHAN_GAO_index + add_CHAN_GAO_values + ');'
            # print(add_CHAN_GAO)

            cursor.execute(add_CHAN_GAO)
            cnx.commit()
            cursor.close()
            cnx.close()

            return True
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
            elif err.errno == errorcode.ER_TRUNCATED_WRONG_VALUE_FOR_FIELD:
                QMessageBox.information(self, '数据库错误', '数据类型有误。')
            else:
                QMessageBox.information(self, '数据库错误', str(err))