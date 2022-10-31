import sys

from PySide6.QtWidgets import QApplication

from gui import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.setup_ui()
    sys.exit(app.exec())
