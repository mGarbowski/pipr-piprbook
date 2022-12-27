import sys

from PySide2.QtWidgets import QMainWindow, QApplication

from gui.ui_piprbook_desktop import Ui_MainWindow


class PiprbookWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main(args):
    app = QApplication(args)
    window = PiprbookWindow()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    main(sys.argv)
