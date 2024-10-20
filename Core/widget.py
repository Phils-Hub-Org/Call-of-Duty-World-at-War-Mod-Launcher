from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from Resources.UI.ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        # Hide window titlebar
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.ui = Ui_Widget()
        self.ui.setupUi(self)