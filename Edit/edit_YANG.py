import mysql.connector
from PyQt5.QtWidgets import (
    QInputDialog,
    QLineEdit,
    QMessageBox,
    QLabel,
    QPushButton,
    QHBoxLayout,
)
from mysql.connector import errorcode

from utils.YANG import CYANG_Dialog


class CEdit_YANG_Dialog(CYANG_Dialog):
    def __init__(self, parent=None):
        super(CEdit_YANG_Dialog, self).__init__(parent)

        self.USER = parent.USER
        self.PASSWD = parent.PASSWD

        text, ok = QInputDialog.getText(self, "修改湖羊数据", "请输入编号：", QLineEdit.Normal)

        if ok and text and not text.isspace():
            YANG_info = self.get_YANG_info(text)
            if YANG_info:
                self.edit_BIAN_HAO.setText(YANG_info[0][0])
                self.edit_BIAN_HAO.setEnabled(False)
                if YANG_info[0][1]:
                    self.edit_PENG_HAO.setText(YANG_info[0][1])
                if YANG_info[0][2]:
                    self.edit_LAN_HAO.setText(YANG_info[0][2])
                if YANG_info[0][3]:
                    self.edit_CHAN_GAO_HAO.setText(YANG_info[0][3])
                if YANG_info[0][4]:
                    self.edit_XING_BIE.setCurrentText(YANG_info[0][4])
                if YANG_info[0][5]:
                    self.edit_ER_HAO.setText(YANG_info[0][5])
                if YANG_info[0][6]:
                    self.edit_CHU_SHENG_ZHONG.setText(str(YANG_info[0][6]))
                if YANG_info[0][7]:
                    self.edit_DUAN_NAI_ZHONG.setText(str(YANG_info[0][7]))
                if YANG_info[0][8]:
                    self.edit_LIU_YUE_ZHONG.setText(str(YANG_info[0][8]))
                if YANG_info[0][9]:
                    self.edit_ZHOU_SUI_ZHONG.setText(str(YANG_info[0][9]))
                if YANG_info[0][10]:
                    self.edit_QU_XIANG.setText(str(YANG_info[0][10]))

                self.label_edit_YANG_dialog = QLabel("\n注：(*)为必填项\n")
                self.button_edit_YANG_dialog = QPushButton("修改湖羊数据")
                self.button_edit_YANG_dialog.clicked.connect(
                    self.button_edit_YANG_dialog_clicked
                )
                self.button_delete_YANG_dialog = QPushButton("删除湖羊数据")
                self.button_delete_YANG_dialog.clicked.connect(
                    self.button_delete_YANG_dialog_clicked
                )
                self.layout_button = QHBoxLayout()
                self.layout_button.addWidget(self.button_edit_YANG_dialog)
                self.layout_button.addWidget(self.button_delete_YANG_dialog)
                self.layout_YANG_dialog.addWidget(self.label_edit_YANG_dialog)
                self.layout_YANG_dialog.addLayout(self.layout_button)
                self.setWindowTitle("修改湖羊数据")

                self.show()
            else:
                QMessageBox.information(self, "输入错误", "无该湖羊信息。")
        else:
            if ok:
                QMessageBox.information(self, "输入错误", "无编号输入。")

    def button_edit_YANG_dialog_clicked(self):
        if self.delete_YANG_info(self.edit_BIAN_HAO.text()) and self.add_YANG_info():
            QMessageBox.information(self, "修改湖羊数据", "修改成功。")
            self.close()

    def button_delete_YANG_dialog_clicked(self):
        if self.delete_YANG_info(self.edit_BIAN_HAO.text()):
            QMessageBox.information(self, "修改湖羊数据", "删除成功。")
            self.close()

    def get_YANG_info(self, text):
        YANG_info = []
        try:
            cnx = mysql.connector.connect(
                user=self.USER,
                password=self.PASSWD,
                database="pang_da_nong_ye",
                host="127.0.0.1",
            )
            cursor = cnx.cursor()
            cursor.execute('select * from yang where bian_hao="' + text + '"')

            for YANG_info_item in cursor:
                YANG_info.append(YANG_info_item)
            # print(YANG_info)

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

    def delete_YANG_info(self, text):
        try:
            cnx = mysql.connector.connect(
                user=self.USER,
                password=self.PASSWD,
                database="pang_da_nong_ye",
                host="127.0.0.1",
            )
            cursor = cnx.cursor()
            cursor.execute('delete from yang where bian_hao="' + text + '"')
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                QMessageBox.information(self, "数据库错误", "登录数据库错误。")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                QMessageBox.information(self, "数据库错误", "数据库不存在。")
            elif err.errno == errorcode.ER_NO_SUCH_TABLE:
                QMessageBox.information(self, "数据库错误", "表单不存在。")
            else:
                QMessageBox.information(self, "数据库错误", str(err))
