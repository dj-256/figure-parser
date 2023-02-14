from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QPainter, QPainterPath
from PySide6.QtWidgets import QWidget, QApplication


class PaintWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.path = None
        self.pen = QPen(Qt.black, 2, Qt.SolidLine)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.pen)
        if self.path is not None:
            painter.drawPath(self.path)

    def mousePressEvent(self, event):
        self.path = QPainterPath()
        self.path.moveTo(event.position())
        self.update()

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.position())
        self.update()

    def mouseReleaseEvent(self, event):
        self.path.lineTo(event.position())
        self.path = None
        # self.update()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    widget = PaintWidget()
    widget.show()
    sys.exit(app.exec())
