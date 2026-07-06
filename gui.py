from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QHBoxLayout, QWidget

# TODO: check out QStackedLayout https://www.pythonguis.com/tutorials/pyqt6-layouts/

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("app")

        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)
