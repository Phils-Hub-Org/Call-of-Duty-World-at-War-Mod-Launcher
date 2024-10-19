from PySide6.QtWidgets import QApplication
from Core.main_window import MainWindow
from Core.mod_launcher import ModLauncher

class Entry:

    @classmethod
    def init(cls):
        
        # Initialize main window
        cls.mainWindow = MainWindow()

        # Initialize mod launcher
        cls.modLauncher = ModLauncher(cls.mainWindow)

        # Show main window
        cls.mainWindow.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    entry = Entry()
    entry.init()
    sys.exit(app.exec())