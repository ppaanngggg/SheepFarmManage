import mysql.connector
from mysql.connector import errorcode
from datetime import date

from CHAN_GAO import *


class CEdit_CHAN_GAO_Dialog(CCHAN_GAO_Dialog):
    def __init__(self, parent=None):
        super(CEdit_CHAN_GAO_Dialog, self).__init__(parent)

        self.USER=parent.USER
        self.PASSWD=parent.PASSWD

        text, ok = QInputDialog.getText(self, '修改产羔记录','请输入产羔号：', QLineEdit.Normal)

        if ok and text and not text.isspace():
            CHAN_GAO_info=self.get_CHAN_GAO_info(text)
            if CHAN_GAO_info:
                self.edit_CHAN_GAO_HAO.setText(CHAN_GAO_info[0][0])
                self.edit_CHAN_GAO_HAO.setEnabled(False)
                if CHAN_GAO_info[0][1]:
                    self.edit_PENG_HAO.setText(CHAN_GAO_info[0][1])
                if CHAN_GAO_info[0][2]:
                    self.edit_LAN_HAO.setText(CHAN_GAO_info[0][2])
                if CHAN_GAO_info[0][3]:
                    self.edit_MU_YANG_HAO.setText(CHAN_GAO_info[0][3])
                if CHAN_GAO_info[0][4]:
                    self.edit_GONG_YANG_HAO.setText(CHAN_GAO_info[0][4])
                if CHAN_GAO_info[0][5]:
                    self.edit_TAI_CI.setText(str(CHAN_GAO_info[0][5]))
                if CHAN_GAO_info[0][6]:
                    self.edit_PEI_ZHONG_RI_QI_year.setText(str(CHAN_GAO_info[0][6].year))
                    self.edit_PEI_ZHONG_RI_QI_month.setText(str(CHAN_GAO_info[0][6].month))
                    self.edit_PEI_ZHONG_RI_QI_day.setText(str(CHAN_GAO_info[0][6].day))
                if CHAN_GAO_info[0][7]:
                    self.edit_CHAN_GAO_RI_QI_year.setText(str(CHAN_GAO_info[0][7].year))
                    self.edit_CHAN_GAO_RI_QI_month.setText(str(CHAN_GAO_info[0][7].month))
                    self.edit_CHAN_GAO_RI_QI_day.setText(str(CHAN_GAO_info[0][7].day))
                if CHAN_GAO_info[0][8]:
                    self.edit_CHAN_GAO.setText(str(CHAN_GAO_info[0][8]))
                if CHAN_GAO_info[0][9]:
                    self.edit_HUO_GAO.setText(str(CHAN_GAO_info[0][9]))
                if CHAN_GAO_info[0][10]:
                    self.edit_DUAN_NAI_RI_QI_year.setText(str(CHAN_GAO_info[0][10].year))
                    self.edit_DUAN_NAI_RI_QI_month.setText(str(CHAN_GAO_info[0][10].month))
                    self.edit_DUAN_NAI_RI_QI_day.setText(str(CHAN_GAO_info[0][10].day))

                self.label_edit_CHAN_GAO_dialog = QLabel('\n注：(*)为必填项\n')
                self.button_edit_CHAN_GAO_dialog = QPushButton('修改产羔信息')
                self.button_edit_CHAN_GAO_dialog.clicked.connect(self.button_edit_CHAN_GAO_dialog_clicked)
                self.button_delete_CHAN_GAO_dialog = QPushButton('删除产羔信息')
                self.button_delete_CHAN_GAO_dialog.clicked.connect(self.button_delete_CHAN_GAO_dialog_clicked)
                self.layout_button=QHBoxLayout()
                self.layout_button.addWidget(self.button_edit_CHAN_GAO_dialog)
                self.layout_button.addWidget(self.button_delete_CHAN_GAO_dialog)
                self.layout_CHAN_GAO_dialog.addWidget(self.label_edit_CHAN_GAO_dialog)
                self.layout_CHAN_GAO_dialog.addLayout(self.layout_button)
                self.setWindowTitle('修改产羔信息')

                self.show()
            else:
                QMessageBox.information(self, '输入错误', '无该产羔信息。')
        else:
            if ok:
                QMessageBox.information(self, '输入错误', '无产羔号输入。')

    def button_edit_CHAN_GAO_dialog_clicked(self):
        if self.delete_CHAN_GAO_info(self.edit_CHAN_GAO_HAO.text()) and self.add_CHAN_GAO_info():
            QMessageBox.information(self, '修改产羔信息', '修改成功。')
            self.close()

    def button_delete_CHAN_GAO_dialog_clicked(self):
        if self.delete_CHAN_GAO_info(self.edit_CHAN_GAO_HAO.text()):
            QMessageBox.information(self, '修改产羔信息', '删除成功。')
            self.close()

    def get_CHAN_GAO_info(self,text):
        CHAN_GAO_info=[]
        try:
            cnx = mysql.connector.connect(user=self.USER,
                                          password=self.PASSWD,
                                          database='pang_da_nong_ye',
                                          host=self.HOST)
            cursor = cnx.cursor()
            cursor.execute('select * from chan_gao where chan_gao_hao="'+text+'"')

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

    def delete_CHAN_GAO_info(self,text):
        try:
            cnx = mysql.connector.connect(user=self.USER,
                                          password=self.PASSWD,
                                          database='pang_da_nong_ye',
                                          host=self.HOST)
            cursor = cnx.cursor()
            cursor.execute('delete from chan_gao where chan_gao_hao="'+text+'"')
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                QMessageBox.information(self, '数据库错误', '登录数据库错误。')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                QMessageBox.information(self, '数据库错误', '数据库不存在。')
            elif err.errno == errorcode.ER_NO_SUCH_TABLE:
                QMessageBox.information(self, '数据库错误', '表单不存在。')
            else:
                QMessageBox.information(self, '数据库错误', str(err))