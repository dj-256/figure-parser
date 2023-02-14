import numpy as np
from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPen, QPainter, QPainterPath, QBrush, QImage
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from skimage.transform import resize
from skimage.util import invert

class PaintView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setScene(QGraphicsScene())
        self.setFixedSize(300, 300)
        self.setRenderHint(QPainter.Antialiasing)
        self.pen = QPen(Qt.black, 20, Qt.SolidLine)
        self.brush = QBrush(Qt.SolidPattern)
        self.path = None
        self.current_item = None
        self.setSceneRect(QRectF(0, 0, 280, 280))

    def mousePressEvent(self, event):
        pos = self.mapToScene(event.pos())
        self.path = QPainterPath()
        self.path.moveTo(pos)
        self.current_item = self.scene().addPath(self.path, self.pen)

    def mouseMoveEvent(self, event):
        if self.current_item is not None:
            pos = self.mapToScene(event.pos())
            self.path.lineTo(pos)
            self.current_item.setPath(self.path)

    def mouseReleaseEvent(self, event):
        self.path = None
        self.current_item = None

    def exportImage(self):
        image = QImage(280, 280, QImage.Format.Format_ARGB32)
        image.fill(Qt.white)
        painter = QPainter(image)
        self.scene().render(painter, QRectF(0, 0, 280, 280), QRectF(0, 0, 280, 280))
        painter.end()
        image.save('image.png')

        # Create a numpy array from the image data
        data = image.bits()
        arr = np.frombuffer(data, np.uint8).reshape((image.height(), image.width(), 4))
        arr = resize(arr, (28, 28), preserve_range=True)
        # Convert the ARGB format to grayscale and normalize to [0, 1]
        arr = arr[..., 0]  # Select only the alpha channel (grayscale)
        # arr = invert(arr)
        arr = 255 - arr.astype(np.uint8)
        print(arr)
        self.scene().clear()
        self.update()
        return arr
