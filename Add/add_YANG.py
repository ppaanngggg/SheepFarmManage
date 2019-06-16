from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox

from utils.YANG import CYANG_Dialog


class CAdd_YANG_Dialog(CYANG_Dialog):
    def __init__(self, parent=None):
        super(CAdd_YANG_Dialog, self).__init__(parent)

        self.USER = parent.USER
        self.PASSWD = parent.PASSWD

        self.label_add_YANG_dialog = QLabel("\n注：(*)为必填项\n")

        self.button_add_YANG_dialog = QPushButton("添加湖羊信息")
        self.button_add_YANG_dialog.clicked.connect(self.button_add_YANG_dialog_clicked)

        self.layout_YANG_dialog.addWidget(self.label_add_YANG_dialog)
        self.layout_YANG_dialog.addWidget(self.button_add_YANG_dialog)

        self.setWindowTitle("添加湖羊信息")

    def button_add_YANG_dialog_clicked(self):
        if self.add_YANG_info():
            QMessageBox.information(self, "添加湖羊数据", "添加成功。")
            self.close()
