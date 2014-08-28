import mysql.connector
from mysql.connector import errorcode
from sheet import *


class CSheet_ZHONG_MU_YANG_HOU_YI_Dialog(CSheet):
    def __init__(self, parent=None):
        super(CSheet_ZHONG_MU_YANG_HOU_YI_Dialog, self).__init__(parent)

        self.USER=parent.USER
        self.PASSWD=parent.PASSWD

        text, ok = QInputDialog.getText(self, '种母羊后裔表', '请输入母羊号：', QLineEdit.Normal)

        if ok and text and not text.isspace():
            self.table_sheet.setColumnCount(9)
            self.sheet_header=['与配公羊', '胎次', '产羔', '活羔', '羊羔编号', '羊羔性别', '羊羔出生重', '羊羔断奶重', '羊羔六月重',
                               '羊羔去向']
            self.table_sheet.setHorizontalHeaderLabels(self.sheet_header)
            self.table_sheet.setRowCount(1)

            self.sheet_ZHONG_MU_YANG_HOU_YI(text)
            
            self.setWindowTitle('种母羊后裔表')
            self.show()
        else:
            if ok:
                QMessageBox.information(self, '输入错误', '无母羊号输入。')

    def sheet_ZHONG_MU_YANG_HOU_YI(self, text):
        try:
            cnx = mysql.connector.connect(user=self.USER,
                                          password=self.PASSWD,
                                          database='pang_da_nong_ye',
                                          host='115.29.168.27')
            cursor_CHAN_GAO = cnx.cursor(buffered=True)
            cursor_YANG = cnx.cursor(buffered=True)

            cursor_CHAN_GAO.execute(
                'select chan_gao_hao,gong_yang_hao,tai_ci,chan_gao,huo_gao from chan_gao where mu_yang_hao="'
                + text + '"')
            for CHAN_GAO_info_item in cursor_CHAN_GAO:
                # print(CHAN_GAO_info_item)
                for index in range(1, 5):
                    if CHAN_GAO_info_item[index]:
                        self.table_sheet.setItem(
                            self.table_sheet.rowCount() - 1,
                            index - 1,
                            QTableWidgetItem(str(CHAN_GAO_info_item[index])))
                cursor_YANG.execute(
                    'select bian_hao,xing_bie,chu_sheng_zhong,duan_nai_zhong,liu_yue_zhong,qu_xiang from yang' +
                    ' where chan_gao_hao="' + CHAN_GAO_info_item[0] + '"')
                YANG_info_item = cursor_YANG.fetchone()
                if YANG_info_item is not None:
                    while YANG_info_item is not None:
                        for index in range(0, YANG_info_item.__len__()):
                            if YANG_info_item[index]:
                                self.table_sheet.setItem(
                                    self.table_sheet.rowCount() - 1,
                                    index + 4,
                                    QTableWidgetItem(str(YANG_info_item[index])))
                        self.table_sheet.setRowCount(
                            self.table_sheet.rowCount() + 1)
                        YANG_info_item = cursor_YANG.fetchone()
                else:
                    self.table_sheet.setRowCount(
                        self.table_sheet.rowCount() + 1)
            cursor_CHAN_GAO.close()
            cursor_YANG.close()
            cnx.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                QMessageBox.information(self, '数据库错误', '登录数据库错误。')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                QMessageBox.information(self, '数据库错误', '数据库不存在。')
            elif err.errno == errorcode.ER_NO_SUCH_TABLE:
                QMessageBox.information(self, '数据库错误', '表单不存在。')
            else:
                QMessageBox.information(self, '数据库错误', str(err))