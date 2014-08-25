import mysql.connector
from mysql.connector import errorcode
from sheet import *
from datetime import *


class CSheet_CHENG_ZHONG_JI_LU_Dialog(CSheet):
    def __init__(self, parent=None):
        super(CSheet_CHENG_ZHONG_JI_LU_Dialog, self).__init__(parent)
        text, ok = QInputDialog.getText(self, '称重记录表', '请输入棚号：', QLineEdit.Normal)

        if ok and text and not text.isspace():
            self.table_sheet.setColumnCount(17)
            self.sheet_header = ['栏号', '出生日期', '性别', '耳号', '出生重', '第一次称重日期', '第一次称重重量', '日增量',
                                 '月增量', '第二次称重日期', '第二次称重重量', '日增量', '月增量', '第三次称重日期',
                                 '第三次称重重量', '日增量', '月增量']
            self.table_sheet.setHorizontalHeaderLabels(self.sheet_header)
            self.table_sheet.setRowCount(1)

            self.sheet_CHENG_ZHONG_JI_LU(text)

            self.setWindowTitle('称重记录表')
            self.show()
        else:
            if ok:
                QMessageBox.information(self, '输入错误', '无棚号输入。')


    def sheet_CHENG_ZHONG_JI_LU(self, text):
        try:
            cnx = mysql.connector.connect(user='root', database='test')
            cursor_CHAN_GAO = cnx.cursor(buffered=True)
            cursor_YANG = cnx.cursor(buffered=True)

            cursor_YANG.execute(
                'select chan_gao_hao,lan_hao,xing_bie,er_hao,chu_sheng_zhong,duan_nai_zhong,' +
                'liu_yue_zhong,zhou_sui_zhong from yang where peng_hao="' + text + '" order by lan_hao')

            for YANG_info_item in cursor_YANG:
                print(YANG_info_item)
                current_row = self.table_sheet.rowCount() - 1
                if YANG_info_item[1]:
                    self.table_sheet.setItem(current_row,
                                             0, QTableWidgetItem(YANG_info_item[1]))
                for index in range(2, 5):
                    if YANG_info_item[index]:
                        self.table_sheet.setItem(current_row,
                                                 index, QTableWidgetItem(str(YANG_info_item[index])))
                for index in range(0, 3):
                    if YANG_info_item[index + 5]:
                        self.table_sheet.setItem(current_row,
                                                 6 + index * 4,
                                                 QTableWidgetItem(str(YANG_info_item[index + 5])))
                cursor_CHAN_GAO.execute(
                    'select chan_gao_ri_qi,duan_nai_ri_qi from chan_gao where chan_gao_hao="' + YANG_info_item[0] + '"')
                CHAN_GAO_info_item = cursor_CHAN_GAO.fetchone()
                if CHAN_GAO_info_item:
                    print(CHAN_GAO_info_item)
                    if CHAN_GAO_info_item[0]:
                        self.table_sheet.setItem(current_row, 1,
                                                 QTableWidgetItem(str(CHAN_GAO_info_item[0])))
                        self.table_sheet.setItem(current_row, 9, QTableWidgetItem(
                            str(CHAN_GAO_info_item[0] + timedelta(days=365 / 2))))
                        self.table_sheet.setItem(current_row, 13, QTableWidgetItem(
                            str(CHAN_GAO_info_item[0] + timedelta(days=365))))
                    if CHAN_GAO_info_item[1]:
                        self.table_sheet.setItem(current_row,
                                                 5, QTableWidgetItem(str(CHAN_GAO_info_item[1])))
                    if CHAN_GAO_info_item[1] and CHAN_GAO_info_item[0] \
                            and YANG_info_item[5] and YANG_info_item[5] > 0 \
                            and YANG_info_item[4] and YANG_info_item[4] > 0:
                        self.table_sheet.setItem(
                            current_row, 7,
                            QTableWidgetItem('%.3f' % ((YANG_info_item[5] - YANG_info_item[4]) / (
                                CHAN_GAO_info_item[1] - CHAN_GAO_info_item[0]).days)))
                        self.table_sheet.setItem(
                            current_row, 8,
                            QTableWidgetItem('%.3f' % ((YANG_info_item[5] - YANG_info_item[4]) / (
                                CHAN_GAO_info_item[1] - CHAN_GAO_info_item[0]).days * 30)))
                    if CHAN_GAO_info_item[1] and CHAN_GAO_info_item[0] \
                            and YANG_info_item[6] and YANG_info_item[6] > 0 \
                            and YANG_info_item[5] and YANG_info_item[5] > 0:
                        self.table_sheet.setItem(
                            current_row, 11,
                            QTableWidgetItem('%.3f' % ((YANG_info_item[6] - YANG_info_item[5]) / (
                                CHAN_GAO_info_item[0] + timedelta(days=365 / 2) - CHAN_GAO_info_item[1]).days)))
                        self.table_sheet.setItem(
                            current_row, 12,
                            QTableWidgetItem('%.3f' % ((YANG_info_item[6] - YANG_info_item[5]) / (
                                CHAN_GAO_info_item[0] + timedelta(days=365 / 2) - CHAN_GAO_info_item[1]).days * 30)))
                    if CHAN_GAO_info_item[0] \
                            and YANG_info_item[7] and YANG_info_item[7] > 0 \
                            and YANG_info_item[6] and YANG_info_item[6] > 0:
                        self.table_sheet.setItem(
                            current_row, 15,
                            QTableWidgetItem(
                                '%.3f' % ((YANG_info_item[7] - YANG_info_item[6]) / timedelta(days=365 / 2).days)))
                        self.table_sheet.setItem(
                            current_row, 16,
                            QTableWidgetItem(
                                '%.3f' % ((YANG_info_item[7] - YANG_info_item[6]) / timedelta(days=365 / 2).days * 30)))
                self.table_sheet.setRowCount(self.table_sheet.rowCount() + 1)

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