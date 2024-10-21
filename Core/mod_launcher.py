from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QSizeGrip
from Utils.qt_utility import displayMessageBox

class ModLauncher:
    def __init__(self, mainWindow, USING_MAINWINDOW):
        self.mainWindow = mainWindow

        if USING_MAINWINDOW:
            from Resources.UI.ui_main_window import Ui_MainWindow
            self.ui: Ui_MainWindow = self.mainWindow.ui
        else:
            from Resources.UI.ui_widget import Ui_Widget
            self.ui: Ui_Widget = self.mainWindow.ui

            self.moveGripper()

            self.resizeGripper()
    
    def moveGripper(self):
        self.ui.frame_4.mousePressEvent = self.frame_4_mousePressEvent
        self.ui.frame_4.mouseMoveEvent = lambda event, this=self.mainWindow: self.frame_4_mouseMoveEvent(event, this)

    def resizeGripper(self):
        frame = self.ui.frame_5

        # Layout to hold the QSizeGrip
        layout = QVBoxLayout(frame)

        # QSizeGrip to allow resizing
        size_grip = QSizeGrip(frame)
        layout.addWidget(size_grip, 0, Qt.AlignBottom | Qt.AlignRight)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        frame.setLayout(layout)

    def frame_4_mousePressEvent(self, event):
        self.frame_4_clickPosition = event.globalPos()
    
    def frame_4_mouseMoveEvent(self, event, this):
        self.mainWindow.move(self.mainWindow.pos() + event.globalPos() - self.frame_4_clickPosition)
        self.frame_4_clickPosition = event.globalPos()
        # event.accept()