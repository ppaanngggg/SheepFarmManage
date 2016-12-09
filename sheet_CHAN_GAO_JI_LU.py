import mysql.connector
from mysql.connector import errorcode
from sheet import *


class CSheet_CHAN_GAO_JI_LU_Dialog(CSheet):
    def __init__(self, parent=None):
        super(CSheet_CHAN_GAO_JI_LU_Dialog, self).__init__(parent)

        self.USER=parent.USER
        self.PASSWD=parent.PASSWD

        self.table_sheet.setColumnCount(14)
        self.sheet_header=['棚号', '栏号', '母羊号', '公羊号', '胎次', '配种日期', '产羔日期', '产羔数', '活羔数',
                           '羊羔编号', '羊羔性别', '羊羔出生重', '羊羔断奶重', '断奶日期']
        self.table_sheet.setHorizontalHeaderLabels(self.sheet_header)
        self.table_sheet.setRowCount(1)
        
        self.sheet_CHAN_GAO_JI_LU()

        self.setWindowTitle('产羔记录表')
        self.show()

    def sheet_CHAN_GAO_JI_LU(self):
        try:
            cnx = mysql.connector.connect(user=self.USER,
                                          password=self.PASSWD,
                                          database='pang_da_nong_ye',
                                          host=self.HOST)
            cursor_CHAN_GAO = cnx.cursor(buffered=True)
            cursor_YANG = cnx.cursor(buffered=True)

            cursor_CHAN_GAO.execute('select * from chan_gao')
            for CHAN_GAO_info_item in cursor_CHAN_GAO:
                # print(CHAN_GAO_info_item)
                for index in range(1, CHAN_GAO_info_item.__len__() - 1):
                    if CHAN_GAO_info_item[index]:
                        self.table_sheet.setItem(self.table_sheet.rowCount() - 1,
                                                                index - 1,
                                                                QTableWidgetItem(str(CHAN_GAO_info_item[index])))
                if CHAN_GAO_info_item[CHAN_GAO_info_item.__len__() - 1]:
                    self.table_sheet.setItem(self.table_sheet.rowCount() - 1,
                                                            self.table_sheet.columnCount() - 1,
                                                            QTableWidgetItem(str(
                                                                CHAN_GAO_info_item[CHAN_GAO_info_item.__len__() - 1])))
                cursor_YANG.execute(
                    'select bian_hao,xing_bie,chu_sheng_zhong,duan_nai_zhong from yang where chan_gao_hao="' +
                    CHAN_GAO_info_item[0] + '"')
                YANG_info_item=cursor_YANG.fetchone()
                if YANG_info_item is not None:
                    while YANG_info_item is not None:
                        for index in range(0, YANG_info_item.__len__()):
                            if YANG_info_item[index]:
                                self.table_sheet.setItem(self.table_sheet.rowCount() - 1,
                                                                        self.table_sheet.columnCount() - 5 + index,
                                                                        QTableWidgetItem(str(YANG_info_item[index])))
                        self.table_sheet.setRowCount(self.table_sheet.rowCount() + 1)
                        YANG_info_item=cursor_YANG.fetchone()
                else:
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