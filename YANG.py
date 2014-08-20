from PyQt5.QtWidgets import *
import mysql.connector
from mysql.connector import errorcode

class CYANG_Dialog(QDialog):
    def __init__(self, parent=None):
        super(CYANG_Dialog, self).__init__(parent)

        self.label_BIAN_HAO = QLabel('编号(*)：')
        self.edit_BIAN_HAO = QLineEdit()
        self.layout_BIAN_HAO = QHBoxLayout()
        self.layout_BIAN_HAO.addWidget(self.label_BIAN_HAO)
        self.layout_BIAN_HAO.addWidget(self.edit_BIAN_HAO)

        self.label_PENG_HAO = QLabel('棚号：')
        self.edit_PENG_HAO = QLineEdit()
        self.layout_PENG_HAO = QHBoxLayout()
        self.layout_PENG_HAO.addWidget(self.label_PENG_HAO)
        self.layout_PENG_HAO.addWidget(self.edit_PENG_HAO)

        self.label_LAN_HAO = QLabel('栏号：')
        self.edit_LAN_HAO = QLineEdit()
        self.layout_LAN_HAO = QHBoxLayout()
        self.layout_LAN_HAO.addWidget(self.label_LAN_HAO)
        self.layout_LAN_HAO.addWidget(self.edit_LAN_HAO)

        self.label_CHAN_GAO_HAO = QLabel('产羔号(*)：')
        self.edit_CHAN_GAO_HAO = QLineEdit()
        self.layout_CHAN_GAO_HAO = QHBoxLayout()
        self.layout_CHAN_GAO_HAO.addWidget(self.label_CHAN_GAO_HAO)
        self.layout_CHAN_GAO_HAO.addWidget(self.edit_CHAN_GAO_HAO)

        self.label_XING_BIE = QLabel('性别(*)：')
        # self.edit_XING_BIE = QLineEdit()
        self.edit_XING_BIE = QComboBox()
        self.edit_XING_BIE.addItems(['母','公'])
        self.layout_XING_BIE = QHBoxLayout()
        self.layout_XING_BIE.addWidget(self.label_XING_BIE)
        self.layout_XING_BIE.addWidget(self.edit_XING_BIE)

        self.label_ER_HAO = QLabel('耳号：')
        self.edit_ER_HAO = QLineEdit()
        self.layout_ER_HAO = QHBoxLayout()
        self.layout_ER_HAO.addWidget(self.label_ER_HAO)
        self.layout_ER_HAO.addWidget(self.edit_ER_HAO)

        self.label_MIAN_YI_HAO = QLabel('免疫号：')
        self.edit_MIAN_YI_HAO = QLineEdit()
        self.layout_MIAN_YI_HAO = QHBoxLayout()
        self.layout_MIAN_YI_HAO.addWidget(self.label_MIAN_YI_HAO)
        self.layout_MIAN_YI_HAO.addWidget(self.edit_MIAN_YI_HAO)

        self.label_CHU_SHENG_ZHONG = QLabel('出生重：')
        self.edit_CHU_SHENG_ZHONG = QLineEdit()
        self.layout_CHU_SHENG_ZHONG = QHBoxLayout()
        self.layout_CHU_SHENG_ZHONG.addWidget(self.label_CHU_SHENG_ZHONG)
        self.layout_CHU_SHENG_ZHONG.addWidget(self.edit_CHU_SHENG_ZHONG)

        self.label_DUAN_NAI_ZHONG = QLabel('断奶重：')
        self.edit_DUAN_NAI_ZHONG = QLineEdit()
        self.layout_DUAN_NAI_ZHONG = QHBoxLayout()
        self.layout_DUAN_NAI_ZHONG.addWidget(self.label_DUAN_NAI_ZHONG)
        self.layout_DUAN_NAI_ZHONG.addWidget(self.edit_DUAN_NAI_ZHONG)

        self.label_LIU_YUE_ZHONG = QLabel('六月重：')
        self.edit_LIU_YUE_ZHONG = QLineEdit()
        self.layout_LIU_YUE_ZHONG = QHBoxLayout()
        self.layout_LIU_YUE_ZHONG.addWidget(self.label_LIU_YUE_ZHONG)
        self.layout_LIU_YUE_ZHONG.addWidget(self.edit_LIU_YUE_ZHONG)

        self.label_ZHOU_SUI_ZHONG = QLabel('周岁重：')
        self.edit_ZHOU_SUI_ZHONG = QLineEdit()
        self.layout_ZHOU_SUI_ZHONG = QHBoxLayout()
        self.layout_ZHOU_SUI_ZHONG.addWidget(self.label_ZHOU_SUI_ZHONG)
        self.layout_ZHOU_SUI_ZHONG.addWidget(self.edit_ZHOU_SUI_ZHONG)

        self.label_QU_XIANG = QLabel('去向：')
        self.edit_QU_XIANG = QLineEdit()
        self.layout_QU_XIANG = QHBoxLayout()
        self.layout_QU_XIANG.addWidget(self.label_QU_XIANG)
        self.layout_QU_XIANG.addWidget(self.edit_QU_XIANG)

        self.label_CHAN_GAO_BIAN_HAO = QLabel('产羔编号(母羊号或公羊号)：')
        self.edit_CHAN_GAO_BIAN_HAO = QLineEdit()
        self.layout_CHAN_GAO_BIAN_HAO = QHBoxLayout()
        self.layout_CHAN_GAO_BIAN_HAO.addWidget(self.label_CHAN_GAO_BIAN_HAO)
        self.layout_CHAN_GAO_BIAN_HAO.addWidget(self.edit_CHAN_GAO_BIAN_HAO)

        self.layout_YANG_dialog = QVBoxLayout()
        self.layout_YANG_dialog.addLayout(self.layout_BIAN_HAO)
        self.layout_YANG_dialog.addLayout(self.layout_PENG_HAO)
        self.layout_YANG_dialog.addLayout(self.layout_LAN_HAO)
        self.layout_YANG_dialog.addLayout(self.layout_CHAN_GAO_HAO)
        self.layout_YANG_dialog.addLayout(self.layout_XING_BIE)
        self.layout_YANG_dialog.addLayout(self.layout_ER_HAO)
        self.layout_YANG_dialog.addLayout(self.layout_MIAN_YI_HAO)
        self.layout_YANG_dialog.addLayout(self.layout_CHU_SHENG_ZHONG)
        self.layout_YANG_dialog.addLayout(self.layout_DUAN_NAI_ZHONG)
        self.layout_YANG_dialog.addLayout(self.layout_LIU_YUE_ZHONG)
        self.layout_YANG_dialog.addLayout(self.layout_ZHOU_SUI_ZHONG)
        self.layout_YANG_dialog.addLayout(self.layout_QU_XIANG)
        self.layout_YANG_dialog.addLayout(self.layout_CHAN_GAO_BIAN_HAO)

        self.setLayout(self.layout_YANG_dialog)

    def add_YANG_info(self):
        try:
            cnx = mysql.connector.connect(user='root', database='test')
            cursor = cnx.cursor()

            add_YANG_index = 'insert into yang ('
            add_YANG_values = ') values ('

            if self.edit_BIAN_HAO.text() and not self.edit_BIAN_HAO.text().isspace():
                add_YANG_index += 'bian_hao,'
                add_YANG_values += '"'+self.edit_BIAN_HAO.text() + '",'
            else:
                QMessageBox.information(self, '输入错误', '编号为必填项。')
                return False

            if self.edit_PENG_HAO.text() and not self.edit_PENG_HAO.text().isspace():
                add_YANG_index += 'peng_hao,'
                add_YANG_values += '"'+self.edit_PENG_HAO.text() + '",'

            if self.edit_LAN_HAO.text() and not self.edit_LAN_HAO.text().isspace():
                add_YANG_index += 'lan_hao,'
                add_YANG_values += '"'+self.edit_LAN_HAO.text() + '",'

            if self.edit_CHAN_GAO_HAO.text() and not self.edit_CHAN_GAO_HAO.text().isspace():
                add_YANG_index += 'chan_gao_hao,'
                add_YANG_values += '"'+self.edit_CHAN_GAO_HAO.text() + '",'
            else:
                QMessageBox.information(self, '输入错误', '产羔号为必填项。')
                return False

            if self.edit_XING_BIE.currentText() and not self.edit_XING_BIE.currentText().isspace():
                add_YANG_index += 'xing_bie,'
                add_YANG_values += '"'+self.edit_XING_BIE.currentText() + '",'
            else:
                QMessageBox.information(self, '输入错误', '性别为必填项。')
                return False

            if self.edit_ER_HAO.text() and not self.edit_ER_HAO.text().isspace():
                add_YANG_index += 'er_hao,'
                add_YANG_values += '"'+self.edit_ER_HAO.text() + '",'

            if self.edit_MIAN_YI_HAO.text() and not self.edit_MIAN_YI_HAO.text().isspace():
                add_YANG_index += 'mian_yi_hao,'
                add_YANG_values += '"'+self.edit_MIAN_YI_HAO.text() + '",'

            if self.edit_CHU_SHENG_ZHONG.text() and not self.edit_CHU_SHENG_ZHONG.text().isspace():
                add_YANG_index += 'chu_sheng_zhong,'
                add_YANG_values += self.edit_CHU_SHENG_ZHONG.text() + ','

            if self.edit_DUAN_NAI_ZHONG.text() and not self.edit_DUAN_NAI_ZHONG.text().isspace():
                add_YANG_index += 'duan_nai_zhong,'
                add_YANG_values += self.edit_DUAN_NAI_ZHONG.text() + ','

            if self.edit_LIU_YUE_ZHONG.text() and not self.edit_LIU_YUE_ZHONG.text().isspace():
                add_YANG_index += 'liu_yue_zhong,'
                add_YANG_values += self.edit_LIU_YUE_ZHONG.text() + ','

            if self.edit_ZHOU_SUI_ZHONG.text() and not self.edit_ZHOU_SUI_ZHONG.text().isspace():
                add_YANG_index += 'zhou_sui_zhong,'
                add_YANG_values += self.edit_ZHOU_SUI_ZHONG.text() + ','

            if self.edit_QU_XIANG.text() and not self.edit_QU_XIANG.text().isspace():
                add_YANG_index += 'qu_xiang,'
                add_YANG_values += '"'+self.edit_QU_XIANG.text() + '",'

            if self.edit_CHAN_GAO_BIAN_HAO.text() and not self.edit_CHAN_GAO_BIAN_HAO.text().isspace():
                add_YANG_index += 'chan_gao_bian_hao,'
                add_YANG_values += '"'+self.edit_CHAN_GAO_BIAN_HAO.text() + '",'

            add_YANG_index = add_YANG_index[:-1]
            add_YANG_values = add_YANG_values[:-1]
            add_YANG=add_YANG_index + add_YANG_values + ');'
            print(add_YANG)

            cursor.execute(add_YANG)
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
                QMessageBox.information(self, '数据库错误', '编号重复。')
            elif err.errno ==errorcode.ER_BAD_FIELD_ERROR:
                QMessageBox.information(self, '数据库错误', '数据类型有误。')
            else:
                QMessageBox.information(self, '数据库错误', str(err))