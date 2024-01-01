from PySide6.QtWidgets import QMainWindow
from ui.output import Ui_Form

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
