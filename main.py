from PyQt5.QtWidgets import *


class CMainWindow(QWidget):
    def __init__(self, parent=None):
        super(CMainWindow, self).__init__(parent)

        self.main_layout=QVBoxLayout()


        self.setLayout(self.main_layout)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    main_window = CMainWindow()
    main_window.show()

    sys.exit(app.exec_())