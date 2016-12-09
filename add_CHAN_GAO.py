from CHAN_GAO import *


class CAdd_CHAN_GAO_Dialog(CCHAN_GAO_Dialog):
    def __init__(self, parent=None):
        super(CAdd_CHAN_GAO_Dialog, self).__init__(parent)

        self.USER=parent.USER
        self.PASSWD=parent.PASSWD

        self.label_add_CHAN_GAO_dialog = QLabel('\n注：(*)为必填项\n')

        self.button_add_CHAN_GAO_dialog = QPushButton('添加产羔信息')
        self.button_add_CHAN_GAO_dialog.clicked.connect(self.button_add_CHAN_GAO_dialog_clicked)

        self.layout_CHAN_GAO_dialog.addWidget(self.label_add_CHAN_GAO_dialog)
        self.layout_CHAN_GAO_dialog.addWidget(self.button_add_CHAN_GAO_dialog)

        self.setWindowTitle('添加产羔信息')

    def button_add_CHAN_GAO_dialog_clicked(self):
        if self.add_CHAN_GAO_info():
            QMessageBox.information(self, '添加产羔信息', '添加成功。')
            self.close()