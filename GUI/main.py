import sys

from PySide6.QtWidgets import QApplication

from ui import Ui

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec())
