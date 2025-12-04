from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from Ui_YOLOSHOWUI import Ui_MainWindow

class Mywindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    window = Mywindow()
    window.show()
    app.exec()