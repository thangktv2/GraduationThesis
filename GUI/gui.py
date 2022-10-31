from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Bearing Seal Classification App"
        self.left = 100
        self.top = 100
        self.width = 1600
        self.height = 900

    def setup_ui(self):
        self.setWindowIcon(QIcon('product.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()
