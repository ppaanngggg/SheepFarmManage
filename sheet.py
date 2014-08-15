from PyQt5.QtWidgets import *

class CSheet(QWidget):
    def __init__(self, parent=None):
        super(CSheet, self).__init__(parent)
        
        self.table_sheet = QTableWidget()
        self.table_sheet.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.button_sheet = QPushButton('输出表格')

        self.layout_sheet = QVBoxLayout()
        self.layout_sheet.addWidget(self.table_sheet)
        self.layout_sheet.addWidget(self.button_sheet)

        self.setLayout(self.layout_sheet)