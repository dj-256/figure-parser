from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPen, QPainter, QPainterPath, QBrush, QImage
from PySide6.QtWidgets import QWidget, QApplication, QGraphicsView, QGraphicsScene, QPushButton, QVBoxLayout
import numpy as np

from paint_view import PaintView


class Main(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        view = PaintView()
        layout.addWidget(view)
        button = QPushButton('Export')
        layout.addWidget(button)
        self.setLayout(layout)
        button.clicked.connect(view.exportImage)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
