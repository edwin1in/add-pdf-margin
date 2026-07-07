from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QComboBox,
    QLabel,
)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("app")

        app_layout = QVBoxLayout()
        input_layout = QHBoxLayout()

        labels = ["Left margin", "Right margin", "Top margin", "Bottom margin"]
        margins = [QSpinBox() for _ in range(0, 4)]

        self.lmargin, self.rmargin, self.tmargin, self.bmargin = margins

        for label, margin in zip(labels, margins):
            input_layout.addWidget(QLabel(label))
            input_layout.addWidget(margin)
        app_layout.addLayout(input_layout)
        units = ["px", "in", "cm", "mm"]
        self.unit = QComboBox()
        self.unit.addItems(units)
        input_layout.addWidget(QLabel("Units"))
        input_layout.addWidget(self.unit)

        self.button = QPushButton("Add margin(s)")
        app_layout.addWidget(self.button)

        widget = QWidget()
        widget.setLayout(app_layout)
        self.setCentralWidget(widget)
