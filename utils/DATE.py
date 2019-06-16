from datetime import date

from PyQt5.QtWidgets import (
    QDialog,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
)


class DateDialog(QDialog):
    def __init__(self, parent=None):
        super(DateDialog, self).__init__(parent)

        self.setWindowTitle("请输入开始结束日期")

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel("开始日期："), 0, 0)
        self.edit_begin_year = QLineEdit()
        layout.addWidget(self.edit_begin_year, 0, 1)
        layout.addWidget(QLabel("年"), 0, 2)
        self.edit_begin_month = QLineEdit()
        layout.addWidget(self.edit_begin_month, 0, 3)
        layout.addWidget(QLabel("月"), 0, 4)
        self.edit_begin_day = QLineEdit()
        layout.addWidget(self.edit_begin_day, 0, 5)
        layout.addWidget(QLabel("日"), 0, 6)

        layout.addWidget(QLabel("结束日期："), 1, 0)
        self.edit_end_year = QLineEdit()
        layout.addWidget(self.edit_end_year, 1, 1)
        layout.addWidget(QLabel("年"), 1, 2)
        self.edit_end_month = QLineEdit()
        layout.addWidget(self.edit_end_month, 1, 3)
        layout.addWidget(QLabel("月"), 1, 4)
        self.edit_end_day = QLineEdit()
        layout.addWidget(self.edit_end_day, 1, 5)
        layout.addWidget(QLabel("日"), 1, 6)

        button = QPushButton("完成")
        button.clicked.connect(self.button_click)
        layout.addWidget(button, 3, 5)

        self.begin_date = None
        self.end_date = None

    def button_click(self):
        try:
            self.begin_date = date(
                year=int(self.edit_begin_year.text()),
                month=int(self.edit_begin_month.text()),
                day=int(self.edit_begin_day.text()),
            )
            self.end_date = date(
                year=int(self.edit_end_year.text()),
                month=int(self.edit_end_month.text()),
                day=int(self.edit_end_day.text()),
            )
            self.accept()
        except Exception:
            QMessageBox.information(self, "", "输入日期不正确")

    def get_result(self):
        return self.begin_date, self.end_date
