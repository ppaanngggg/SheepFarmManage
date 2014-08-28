from PyQt5.QtWidgets import *
import xlsxwriter

class CSheet(QDialog):
    def __init__(self, parent=None):
        super(CSheet, self).__init__(parent)
        
        self.table_sheet = QTableWidget()
        self.table_sheet.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.button_sheet = QPushButton('输出表格')
        self.button_sheet.clicked.connect(self.save_sheet)

        self.layout_sheet = QVBoxLayout()
        self.layout_sheet.addWidget(self.table_sheet)
        self.layout_sheet.addWidget(self.button_sheet)

        self.setLayout(self.layout_sheet)

    def save_sheet(self):
        str_path, str_filter=QFileDialog.getSaveFileName(self,'保存表格','','(*.xlsx)')

        # print(str_path)

        if str_path:
            if str_path[-5:]!='.xlsx':
                str_path+='.xlsx'
            self.save_sheet_detail(str_path)

    def save_sheet_detail(self,str_path):
        workbook = xlsxwriter.Workbook(str_path)
        worksheet = workbook.add_worksheet()

        for index in range(0,self.sheet_header.__len__()):
            worksheet.write(0,index,self.sheet_header[index])

        for row in range(0,self.table_sheet.rowCount()):
            for column in range(0,self.table_sheet.columnCount()):
                if self.table_sheet.item(row,column) and self.table_sheet.item(row,column).text():
                    worksheet.write(row+1,column,self.table_sheet.item(row,column).text())

        workbook.close()