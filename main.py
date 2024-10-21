from PySide6.QtWidgets import QApplication
from Core.main_window import MainWindow
from Core.widget import Widget
from Core.mod_launcher import ModLauncher

USING_MAINWINDOW = True

class Entry:

    @classmethod
    def init(cls):
        
        if USING_MAINWINDOW:
            # Initialize main window
            cls.mainWindow = MainWindow()
            window = cls.mainWindow
        else:
            cls.Widget = Widget()
            window = cls.Widget

        # Initialize mod launcher
        cls.modLauncher = ModLauncher(window, USING_MAINWINDOW)

        if USING_MAINWINDOW:
            # Show main window
            cls.mainWindow.show()
        else:
            cls.Widget.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    entry = Entry()
    entry.init()
    sys.exit(app.exec())