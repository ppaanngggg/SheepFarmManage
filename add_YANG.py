import mysql.connector
from mysql.connector import errorcode
from YANG import *


class CAdd_YANG_Dialog(CYANG_Dialog):
    def __init__(self, parent=None):
        super(CAdd_YANG_Dialog, self).__init__(parent)

        self.label_add_YANG_dialog=QLabel('\n注：(*)为必填项\n')

        self.button_add_YANG_dialog=QPushButton('添加湖羊信息')
        self.button_add_YANG_dialog.clicked.connect(self.button_add_YANG_dialog_clicked)

        self.layout_YANG_dialog.addWidget(self.label_add_YANG_dialog)
        self.layout_YANG_dialog.addWidget(self.button_add_YANG_dialog)

        self.setWindowTitle('添加湖羊信息')

    def button_add_YANG_dialog_clicked(self):
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
                return

            if self.edit_CHAN_GAO_HAO.text() and not self.edit_CHAN_GAO_HAO.text().isspace():
                add_YANG_index += 'chan_gao_hao,'
                add_YANG_values += '"'+self.edit_CHAN_GAO_HAO.text() + '",'
            else:
                QMessageBox.information(self, '输入错误', '产羔号为必填项。')
                return
            
            if self.edit_XING_BIE.text() and not self.edit_XING_BIE.text().isspace():
                add_YANG_index += 'xing_bie,'
                add_YANG_values += '"'+self.edit_XING_BIE.text() + '",'
            else:
                QMessageBox.information(self, '输入错误', '性别为必填项。')
                return
            
            if self.edit_ER_HAO.text() and not self.edit_ER_HAO.text().isspace():
                add_YANG_index += 'er_hao,'
                add_YANG_values += '"'+self.edit_ER_HAO.text() + '",'
                
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

            self.close()
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