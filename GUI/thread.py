import sys
import time

import cv2 as cv
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QImage


class Thread(QThread):
    center_frame = Signal(QImage)
    result_frame = Signal(QImage)

    def __init__(self):
        super(Thread, self).__init__(parent=None)
        self.status = 0
        self.cap = None

    def run(self):
        print(self.status)
        while self.status:
            ret, frame = self.cap.read()
            if not ret:
                continue

            # Reading the image in RGB to display it
            color_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

            # Creating and scaling QImage
            h, w, ch = color_frame.shape
            img = QImage(color_frame.data, w, h, ch * w, QImage.Format_RGB888)
            scaled_img = img.scaled(800, 600, Qt.KeepAspectRatio)
            scaled_img2 = img.scaled(300, 300)

            # Emit signal
            self.center_frame.emit(scaled_img)
            self.result_frame.emit(scaled_img2)
        sys.exit(-1)

    def connect_camera(self, index):
        print("Camera index " + str(index))
        self.cap = cv.VideoCapture(index, apiPreference=cv.CAP_ANY,
                                   params=[cv.CAP_PROP_FRAME_WIDTH, 800, cv.CAP_PROP_FRAME_HEIGHT, 600])
        self.status = 1

    def close_camera(self):
        self.cap.release()
        cv.destroyAllWindows()
        time.sleep(1)
        self.status = 0
        self.finished.connect(self.quit())
