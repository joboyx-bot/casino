from PyQt5 import QtWidgets
from PyQt5.QtGui import QScreen, QImage
from datetime import datetime
from PIL import Image
import sys
import numpy as np

class ScreenshotApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Screenshot App')
        self.setGeometry(100, 100, 200, 100)
        btn = QtWidgets.QPushButton('Take Screenshot', self)
        btn.clicked.connect(self.take_screenshot)
        btn.resize(btn.sizeHint())
        btn.move(50, 30)
        self.show()

    def take_screenshot(self):
        screen = QtWidgets.QApplication.primaryScreen()
        screenshot = screen.grabWindow(0)
        img = screenshot.toImage()
        img = img.convertToFormat(QImage.Format_RGBA8888)

        width = img.width()
        height = img.height()
        buffer = img.constBits()
        arr = np.array(buffer).reshape((height, width, 4))  # Copies the data
        pil_image = Image.fromarray(arr, 'RGBA')
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pil_image.save(f"screenshot_{timestamp}.png")
        print(f"Screenshot saved as screenshot_{timestamp}.png")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = ScreenshotApp()
    sys.exit(app.exec_())
