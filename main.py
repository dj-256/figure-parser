from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPen, QPainter, QPainterPath, QBrush, QImage
from PySide6.QtWidgets import QWidget, QApplication, QGraphicsView, QGraphicsScene, QPushButton, QVBoxLayout, QLabel, \
    QHBoxLayout
import numpy as np

from image_checker import ImageChecker
from paint_view import PaintView


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.checker = ImageChecker()
        layout = QHBoxLayout()

        canva_layout = QVBoxLayout()
        view = PaintView()
        canva_layout.addWidget(view)
        button = QPushButton('Export')
        canva_layout.addWidget(button)
        layout.addLayout(canva_layout)

        output_layout = QVBoxLayout()
        output_layout.setAlignment(Qt.AlignTop)
        text = QLabel('You wrote the number:')
        number = QLabel()
        output_layout.addWidget(text)
        output_layout.addWidget(number)
        layout.addLayout(output_layout)

        self.setLayout(layout)

        def export_and_check_image():
            a = view.exportImage()
            res = self.checker.check_image(a)[0]
            print(res)
            number.setText(str(res))

        button.clicked.connect(export_and_check_image)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
