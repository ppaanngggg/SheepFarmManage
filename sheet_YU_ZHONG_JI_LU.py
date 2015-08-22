import mysql.connector
from mysql.connector import errorcode
from sheet import *


class CSheet_YU_ZHONG_JI_LU_Dialog(CSheet):
    def __init__(self, parent=None):
        super(CSheet_YU_ZHONG_JI_LU_Dialog, self).__init__(parent)

        self.USER=parent.USER
        self.PASSWD=parent.PASSWD

        self.table_sheet.setColumnCount(10)
        self.sheet_header=['耳号', '免疫号', '出生日期', '母亲号', '父亲号', '同胞数', '出生重', '断奶重', '六月重',
                           '周岁重']
        self.table_sheet.setHorizontalHeaderLabels(self.sheet_header)
        self.table_sheet.setRowCount(1)

        self.sheet_YU_ZHONG_JI_LU()

        self.setWindowTitle('育种记录表')
        self.show()

    def sheet_YU_ZHONG_JI_LU(self):
        try:
            cnx = mysql.connector.connect(user=self.USER,
                                          password=self.PASSWD,
                                          database='pang_da_nong_ye',
                                          host='121.40.132.148')
            cursor_CHAN_GAO = cnx.cursor(buffered=True)
            cursor_YANG = cnx.cursor(buffered=True)

            cursor_YANG.execute(
                'select chan_gao_hao,er_hao,bian_hao,chu_sheng_zhong,duan_nai_zhong,liu_yue_zhong,zhou_sui_zhong' +
                ' from yang')

            for YANG_info_item in cursor_YANG:
                # print(YANG_info_item)
                current_row = self.table_sheet.rowCount() - 1
                if YANG_info_item[1]:
                    self.table_sheet.setItem(current_row, 0, QTableWidgetItem(YANG_info_item[1]))
                if YANG_info_item[2]:
                    self.table_sheet.setItem(current_row, 1, QTableWidgetItem(YANG_info_item[2]))
                for index in range(3, 7):
                    if YANG_info_item[index]:
                        self.table_sheet.setItem(current_row, index + 3,
                                                                QTableWidgetItem(str(YANG_info_item[index])))
                cursor_CHAN_GAO.execute(
                    'select chan_gao_ri_qi,mu_yang_hao,gong_yang_hao,huo_gao from chan_gao where chan_gao_hao="'
                    + YANG_info_item[0] + '"')
                CHAN_GAO_info_item = cursor_CHAN_GAO.fetchone()
                if CHAN_GAO_info_item:
                    for index in range(0, 4):
                        if CHAN_GAO_info_item[index]:
                            self.table_sheet.setItem(current_row, index + 2,
                                                                    QTableWidgetItem(str(CHAN_GAO_info_item[index])))

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