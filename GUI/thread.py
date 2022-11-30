import cv2 as cv
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QImage


class Thread(QThread):
    center_frame = Signal(QImage)
    result_frame = Signal(QImage)
    cap_status = Signal(bool)

    def __init__(self):
        super(Thread, self).__init__(parent=None)
        self.status = 0
        self.cap = None
        self.cam_index = None

    def run(self):
        self.cap = cv.VideoCapture(self.cam_index, apiPreference=cv.CAP_DSHOW,
                                   params=[cv.CAP_PROP_FRAME_WIDTH, 800, cv.CAP_PROP_FRAME_HEIGHT, 600])
        if self.cap.isOpened():
            self.cap_status.emit(self.cap.isOpened())
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
        else:
            pass

    def disconnect_camera(self):
        self.cap_status.emit(False)
        self.cap.release()
        cv.destroyAllWindows()
