from PySide6.QtCore import Qt, QPoint, Slot, QIODeviceBase, QTimer
from PySide6.QtGui import QPixmap, QPainter, QImage
from PySide6.QtMultimedia import QMediaDevices
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtStateMachine import QStateMachine, QState
from PySide6.QtWidgets import QMainWindow, QDockWidget, QVBoxLayout, QFrame, QHBoxLayout, QGroupBox, QLabel, QComboBox, \
    QPushButton, QCheckBox, QLineEdit, QWidget, QPlainTextEdit, QGridLayout, QSlider, QSpinBox

from thread import Thread
import time


class MediaHolder(QLabel):
    def __init__(self, img, img_w, img_h):
        super(MediaHolder, self).__init__()
        self.pixmap = QPixmap(img)
        self.setMinimumSize(img_w, img_h)

    def paintEvent(self, event):
        holder_size = self.size()
        holder_painter = QPainter(self)
        holder_x = self.x()
        holder_y = self.y()
        holder_coordinates = QPoint(holder_x, holder_y)
        scaled_pixmap = self.pixmap.scaled(holder_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # start painting the label from left upper corner
        holder_coordinates.setX((holder_size.width() - scaled_pixmap.width()) / 2)
        holder_coordinates.setY((holder_size.height() - scaled_pixmap.height()) / 2)
        holder_painter.drawPixmap(holder_coordinates, scaled_pixmap)


class DockInit(QDockWidget):
    def __init__(self, title, widget, min_w=None, min_h=None, max_w=None, max_h=None):
        super(DockInit, self).__init__()
        self.setTitleBarWidget(title)
        self.setWidget(widget)

        if min_w is not None:
            self.setMinimumWidth(min_w)

        if min_h is not None:
            self.setMinimumHeight(min_h)

        if max_w is not None:
            self.setMaximumWidth(max_w)

        if max_h is not None:
            self.setMaximumHeight(max_h)


class ButtonInit(QPushButton):
    def __init__(self, name, tips, width, height, color1, color2, color3):
        super(ButtonInit, self).__init__()
        self.setText(name)
        self.setCheckable(True)
        self.setMinimumWidth(width)
        self.setMinimumHeight(height)
        self.setToolTip(tips)
        self.setStyleSheet("QPushButton{border: 2px solid %s; background-color: %s;}"
                           "QPushButton:hover{background-color: %s;}"
                           "QPushButton:pressed{border: 2px solid %s; background-color: %s;}" % (
                               color1, color2, color1, color3, color3))


class StatisticsInit(QLineEdit):
    def __init__(self, init_value, rw, min_w, min_h, color1=None, color2=None):
        super(StatisticsInit, self).__init__()
        self.setAlignment(Qt.AlignCenter)
        if rw == 1:
            self.setReadOnly(False)
        else:
            self.setReadOnly(True)
        self.setMinimumSize(min_w, min_h)
        if color1 and color2 is not None:
            self.setText(str(init_value))
            self.setStyleSheet("QLineEdit{background-color: %s;}"
                               "QLineEdit:focus{border: 2px solid %s;}" % (color1, color2))
        else:
            self.setText(str(init_value) + "%")


class CenterWgt(QFrame):
    def __init__(self):
        super(CenterWgt, self).__init__()
        self.frame_holder = None
        self.layout()
        self.func()

    def layout(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)

        # create cam show group box
        cont = QGroupBox("Realtime Camera Display")

        # create cam show area layout
        cont_layout = QVBoxLayout()
        cont.setLayout(cont_layout)

        # create components inside cam show area
        self.frame_holder = MediaHolder("./media/pic/800x600.jpg", 800, 600)
        self.frame_holder.setMinimumSize(800,600)

        # add components to cam show
        cont_layout.addWidget(self.frame_holder)
        main_layout.addWidget(cont)

    def func(self):
        pass


class TopWgt(QFrame):
    def __init__(self):
        super(TopWgt, self).__init__()

        self.cam_lst = None
        self.cam_set_btn = None
        self.port_lst = None
        self.baud_lst = None
        self.port_set_btn = None

        self.layout()

    def layout(self):
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(15, 5, 15, 0)
        self.setLayout(main_layout)

        # Camera Settings
        cam_set_cont = QGroupBox("Camera Settings")
        cam_set_layout = QHBoxLayout()
        cam_set_cont.setLayout(cam_set_layout)

        cam_set_label = QLabel("Select camera")

        self.cam_lst = QComboBox()
        self.cam_lst.setToolTip("Select camera to connect")
        self.cam_lst.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.cam_set_btn = ButtonInit("Connect", "Connect to selected camera", 80, 35, "#fad4a6", "#fbe7ab", "#f8a57f")

        cam_set_layout.addWidget(cam_set_label)
        cam_set_layout.addStretch()
        cam_set_layout.addWidget(self.cam_lst)
        cam_set_layout.addStretch()
        cam_set_layout.addWidget(self.cam_set_btn)

        # Port Settings
        port_set_cont = QGroupBox("Serial Port Settings")

        port_set_layout = QHBoxLayout()
        port_set_cont.setLayout(port_set_layout)

        port_set_label = QLabel("Select serial port")
        self.port_lst = QComboBox()
        self.port_lst.setToolTip("Select COM port to connect")
        self.port_lst.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        baud_label = QLabel("Select baudrate")
        self.baud_lst = QComboBox()
        self.baud_lst.addItem("9600", QSerialPort.Baud9600)
        self.baud_lst.addItem("19200", QSerialPort.Baud19200)
        self.baud_lst.addItem("38400", QSerialPort.Baud38400)
        self.baud_lst.addItem("115200", QSerialPort.Baud115200)
        self.baud_lst.setToolTip("Select baudrate of the COM port")
        self.baud_lst.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.port_set_btn = ButtonInit("Connect", "Connect to selected COM port", 80, 35, "#fad4a6", "#fbe7ab",
                                       "#f8a57f")

        port_set_layout.addWidget(port_set_label)
        port_set_layout.addSpacing(20)
        port_set_layout.addWidget(self.port_lst)
        port_set_layout.addStretch()
        port_set_layout.addWidget(baud_label)
        port_set_layout.addSpacing(20)
        port_set_layout.addWidget(self.baud_lst)
        port_set_layout.addStretch()
        port_set_layout.addWidget(self.port_set_btn)

        # Others
        others_cont = QGroupBox("Others")
        other_layout = QHBoxLayout()
        others_cont.setLayout(other_layout)

        img_save_cbox = QCheckBox("Save cropped image")
        img_save_cbox.setToolTip("Save cropped image for future model training")

        init_sys_btn = ButtonInit("Initialize System", "Set whole system to the initial working condition", 120, 35,
                                  "#fad4a6", "#fbe7ab", "#f8a57f")

        other_layout.addWidget(img_save_cbox)
        other_layout.addStretch()
        other_layout.addWidget(init_sys_btn)

        # add containers to main layout
        main_layout.addWidget(cam_set_cont)
        main_layout.setSpacing(15)
        main_layout.addWidget(port_set_cont)
        main_layout.setSpacing(15)
        main_layout.addWidget(others_cont)

        main_layout.setStretchFactor(cam_set_cont, 2)
        main_layout.setStretchFactor(port_set_cont, 3)
        main_layout.setStretchFactor(others_cont, 2)


class BotWgt(QFrame):
    def __init__(self):
        super(BotWgt, self).__init__()
        self.log_text = None
        self.log_clr_btn = None
        self.layout()
        self.connect_signal()

    def layout(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 15)
        self.setLayout(main_layout)

        log_cont = QGroupBox("Log")
        main_layout.addWidget(log_cont)

        cont_layout = QHBoxLayout()
        log_cont.setLayout(cont_layout)

        self.log_text = QPlainTextEdit()

        self.log_clr_btn = ButtonInit("Clear Log", "Clear all log entries history", 80, 35, '#9f8c86', '#f0eae7',
                                      '#895b4a')

        cont_layout.addWidget(self.log_text)
        cont_layout.addWidget(self.log_clr_btn)

    def connect_signal(self):
        self.log_clr_btn.clicked.connect(self.log_text.clear)

    @Slot(str)
    def send_log(self, message):
        self.log_text.appendPlainText(message)


class LeftWgt(QFrame):
    def __init__(self):
        super(LeftWgt, self).__init__()
        self.result_frame_holder = None
        self.final_result = None
        self.total_value = None
        self.passed_value = None
        self.failed_value = None
        self.passed_pct = None
        self.failed_pct = None
        self.run_btn = None
        self.stop_btn = None
        self.layout()
        self.connect_signal()

    def layout(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 0, 15, 15)
        self.setLayout(main_layout)

        # Result container
        result_cont = QGroupBox("Result")
        result_cont_layout = QVBoxLayout()
        result_cont.setLayout(result_cont_layout)

        self.result_frame_holder = MediaHolder("./media/pic/200x200.png", 200, 200)

        self.final_result = QLabel("Result show here")
        self.final_result.setMinimumSize(180, 44)
        self.final_result.setStyleSheet(
            "QLabel{border-radius: 22px; background-color: #e8ecec; font-color: white; font-size: 20px;"
            "qproperty-alignment: 'AlignCenter';}")

        result_cont_layout.addWidget(self.result_frame_holder)
        result_cont_layout.setStretchFactor(self.result_frame_holder, 3)
        result_cont_layout.addWidget(self.final_result, alignment=Qt.AlignCenter)
        result_cont_layout.setStretchFactor(self.final_result, 1)

        # Statistics container
        statistics_cont = QGroupBox("Statistics")
        statistics_layout = QGridLayout()
        statistics_cont.setLayout(statistics_layout)
        statistics_layout.setColumnStretch(0, 1)
        statistics_layout.setColumnStretch(1, 1)

        total_label = QLabel("Total Classified:")
        self.total_value = StatisticsInit(0, 0, 110, 35, "#6695ED", "#1f3efa")

        statistics_layout.addWidget(total_label, 0, 0)
        statistics_layout.addWidget(self.total_value, 0, 1)

        passed_label = QLabel("Total Passed:")
        self.passed_value = StatisticsInit(0, 0, 110, 35, "#72fa93", "#40d872")

        statistics_layout.addWidget(passed_label, 1, 0)
        statistics_layout.addWidget(self.passed_value, 1, 1)

        failed_label = QLabel("Total Failed:")
        self.failed_value = StatisticsInit(0, 0, 110, 35, "#e36255", "#d31638")

        statistics_layout.addWidget(failed_label, 2, 0)
        statistics_layout.addWidget(self.failed_value, 2, 1)

        split = QFrame()
        split.setMaximumHeight(1)
        split.setFrameShape(QFrame.StyledPanel)
        statistics_layout.addWidget(split, 3, 0, 1, 2)

        passed_pct_label = QLabel("Passed percentage:")
        self.passed_pct = StatisticsInit(0, 0, 110, 35)
        statistics_layout.addWidget(passed_pct_label, 4, 0)
        statistics_layout.addWidget(self.passed_pct, 4, 1)

        failed_pct_label = QLabel("Failed percentage:")
        self.failed_pct = StatisticsInit(0, 0, 110, 35)
        statistics_layout.addWidget(failed_pct_label, 5, 0)
        statistics_layout.addWidget(self.failed_pct, 5, 1)

        control_cnt = QGroupBox("Control")

        control_layout = QHBoxLayout()
        control_cnt.setLayout(control_layout)

        self.run_btn = ButtonInit("Run", "Start system", 80, 35, "#72fa93", "#a8fcbd", "#34a871")
        self.stop_btn = ButtonInit("Stop", "Stop system", 80, 35, "#f2a298", "#f5d6d6", "#e45642")

        control_layout.addWidget(self.run_btn)
        control_layout.addWidget(self.stop_btn)

        # Add containers to main layout
        main_layout.addWidget(result_cont)
        main_layout.addWidget(statistics_cont)
        main_layout.addWidget(control_cnt)

        main_layout.setStretchFactor(result_cont, 3)
        main_layout.setStretchFactor(statistics_cont, 3)
        main_layout.setStretchFactor(control_cnt, 1)

    def connect_signal(self):
        pass


class RightWgt(QFrame):
    def __init__(self):
        super(RightWgt, self).__init__()
        self.contour_holder = None
        self.hough_holder = None
        self.yolo_holder = None
        self.threshold_slider = None
        self.threshold_value = None
        self.default_cfg_btn = None
        self.save_cfg_btn = None
        self.layout()
        self.connect_signal()

    def layout(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 0, 15, 15)
        self.setLayout(main_layout)

        # Detail process
        detail_cont = QGroupBox("Detail Process")
        detail_layout = QVBoxLayout()
        detail_cont.setLayout(detail_layout)

        contour_label = QLabel("Contour Process")
        self.contour_holder = MediaHolder("./media/pic/150x150_1.png", 150, 150)

        hough_label = QLabel("Hough Circle Process")
        self.hough_holder = MediaHolder("./media/pic/150x150_2.png", 150, 150)

        yolo_label = QLabel("Yolo Process")
        self.yolo_holder = MediaHolder("./media/pic/150x150_3.png", 150, 150)

        detail_layout.addWidget(contour_label, alignment=Qt.AlignCenter)
        detail_layout.addWidget(self.contour_holder)
        detail_layout.setStretchFactor(self.contour_holder, 2)
        detail_layout.addWidget(hough_label, alignment=Qt.AlignCenter)
        detail_layout.addWidget(self.hough_holder)
        detail_layout.setStretchFactor(self.hough_holder, 2)
        detail_layout.addWidget(yolo_label, alignment=Qt.AlignCenter)
        detail_layout.addWidget(self.yolo_holder)
        detail_layout.setStretchFactor(self.yolo_holder, 2)

        main_layout.addWidget(detail_cont)

        # param setting
        param_cont = QGroupBox("Parameter Settings")
        param_layout = QVBoxLayout()
        param_cont.setLayout(param_layout)

        param_layout_child1 = QGridLayout()
        param_layout.addLayout(param_layout_child1)

        threshold_label = QLabel("Error Threshold")
        self.threshold_slider = QSlider(Qt.Horizontal)
        self.threshold_slider.setTickPosition(QSlider.TicksBelow)
        self.threshold_slider.setMaximum(10)
        self.threshold_slider.setTickInterval(1)
        self.threshold_slider.setToolTip("Set the threshold for error percentage of the bearing seal size")

        self.threshold_value = QSpinBox()
        self.threshold_value.setMaximum(10)
        self.threshold_value.setSuffix("%")
        self.threshold_value.setToolTip("Set the threshold for error percentage of the bearing seal size")

        param_layout_child1.addWidget(threshold_label, 0, 0)
        param_layout_child1.addWidget(self.threshold_slider, 0, 1)
        param_layout_child1.addWidget(self.threshold_value, 0, 2)

        param_layout_child2 = QHBoxLayout()
        param_layout.addLayout(param_layout_child2)

        self.default_cfg_btn = ButtonInit("Reset settings", "Reset all parameters to default value", 90, 35, "#a6c4d0",
                                          "#cadde4", "#88acbc")
        self.save_cfg_btn = ButtonInit("Save settings", "Save all parameters was set by user", 90, 35, "#a6c4d0",
                                       "#cadde4", "#88acbc")

        param_layout_child2.addWidget(self.default_cfg_btn)
        param_layout_child2.addWidget(self.save_cfg_btn)

        main_layout.addWidget(detail_cont)
        main_layout.addWidget(param_cont)

        main_layout.setStretchFactor(detail_cont, 5)
        main_layout.setStretchFactor(param_cont, 2)

    def connect_signal(self):
        self.threshold_slider.valueChanged.connect(self.threshold_value.setValue)
        self.threshold_value.valueChanged.connect(self.threshold_slider.setValue)


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.serial = QSerialPort()
        self.wgt_center = None
        self.wgt_top = None
        self.wgt_bot = None
        self.wgt_left = None
        self.wgt_right = None

        self.config_window()
        self.center_window()
        self.connect_signal()
        self.makeup()

        self.port_name = None
        self.baud_rate = None
        self.data_bits = QSerialPort.Data8
        self.parity = QSerialPort.NoParity
        self.stop_bits = QSerialPort.OneStop
        self.flow_control = QSerialPort.SoftwareControl

        self.init_num_port = 0
        self.init_num_cam = 0

        self.serial = QSerialPort(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.connected_devices_add())
        self.timer.start(200)

        self.th = Thread()

    def config_window(self):
        # set main window title
        self.setWindowTitle("Bearing Seal Classification")
        self.setCorner(Qt.BottomLeftCorner, Qt.LeftDockWidgetArea)
        self.setCorner(Qt.BottomRightCorner, Qt.RightDockWidgetArea)

        # create docks inside main window
        self.wgt_top = TopWgt()
        dock_top = DockInit(QWidget(None), self.wgt_top, None, 110, None, 130)
        self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, dock_top)

        self.wgt_bot = BotWgt()
        dock_bot = DockInit(QWidget(None), self.wgt_bot, None, 110, None, 200)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, dock_bot)

        self.wgt_left = LeftWgt()
        dock_left = DockInit(QWidget(None), self.wgt_left, 270, None, 350, None)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock_left)

        self.wgt_right = RightWgt()
        dock_right = DockInit(QWidget(None), self.wgt_right, 270, None, 350, None)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock_right)

        self.wgt_center = CenterWgt()
        self.setCentralWidget(self.wgt_center)

        # display main window
        self.show()

    def connect_signal(self):
        self.wgt_top.port_set_btn.clicked.connect(lambda: self.port_control())
        self.wgt_top.cam_set_btn.clicked.connect(lambda: self.cam_control())

        self.wgt_right.save_cfg_btn.clicked.connect(lambda: self.wgt_bot.send_log("Configuration Saved."))
        self.wgt_right.default_cfg_btn.clicked.connect(lambda: self.wgt_bot.send_log("Reset to default settings."))

    def center_window(self):
        frame_geometry = self.frameGeometry()
        center_point = self.screen().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def makeup(self):
        self.setStyleSheet("QMainWindow{background-color: #eff0f7;}"
                           "QGroupBox{border-radius: 10px; margin-top: 0.5em; font-family: 'Segoe UI'; font-size: 14px;"
                           "font-weight: regular; background-color: #ffffff;} "
                           "QGroupBox:title{subcontrol-origin: margin;left: 10px;}"
                           "QPushButton{border-radius: 10px; font-size: 14px;}"
                           "QLineEdit{border-radius: 10px;}"
                           "QPlainTextEdit{font-family: 'Cascadia Code'; border-radius: 8px; background-color: #eff0f7;}"
                           "QPlainTextEdit:focus{border: 2px solid #9dbdba;}"
                           "QLabel,QCheckBox,QComboBox,QLineEdit,QPlainTextEdit{font-size: 14px;}")

    @Slot()
    def connected_devices_add(self):
        port_index = 0
        cam_index = 0

        port_num = len(QSerialPortInfo().availablePorts())
        cam_num = len(QMediaDevices().videoInputs())

        # Check new COM port connected
        if port_num:
            if port_num != self.init_num_port:
                for port in QSerialPortInfo().availablePorts():
                    port_index += 1
                    self.wgt_top.port_lst.addItem(port.portName())
                self.init_num_port = port_num
            else:
                pass
        else:
            port_index = 0
            self.init_num_port = 0
            self.wgt_top.port_lst.clear()

        # Check new camera connected
        if cam_num:
            if cam_num != self.init_num_cam:
                for available_camera in QMediaDevices.videoInputs():
                    cam_index += 1
                    self.wgt_top.cam_lst.addItem(available_camera.description(), cam_index-1)
                self.init_num_cam = cam_num
            else:
                pass
        else:
            cam_index = 0
            self.init_num_cam = 0
            self.wgt_top.cam_lst.clear()

    @Slot()
    def port_control(self):
        if self.wgt_top.port_set_btn.text() == "Connect":
            self.port_name = self.wgt_top.port_lst.currentText()
            self.baud_rate = self.wgt_top.baud_lst.currentData()

            self.serial.setPortName(self.port_name)
            self.serial.setBaudRate(self.baud_rate, QSerialPort.AllDirections)
            self.serial.setDataBits(self.data_bits)
            self.serial.setParity(self.parity)
            self.serial.setStopBits(self.stop_bits)
            self.serial.setFlowControl(self.flow_control)

            if self.serial.open(QIODeviceBase.ReadWrite):
                self.wgt_top.port_set_btn.setText("Disconnect")
                self.wgt_bot.send_log("Connected to %s: %s, %s, %s, %s %s." % (
                    self.port_name, self.baud_rate, self.data_bits, self.parity, self.stop_bits, self.flow_control))
            else:
                self.wgt_bot.send_log("Connect failed.")
        else:
            if self.serial.isOpen():
                self.serial.close()
                self.wgt_top.port_set_btn.setText("Connect")
            self.wgt_bot.send_log("Port disconnected")

    @Slot(bytearray)
    def write_data(self, data):
        self.serial.write(data)


    @Slot()
    def read_data(self):
        data = self.serial.readAll()
        BotWgt.send_log("Serial Message:" + str(data))

    def cam_control(self):
        if self.wgt_top.cam_set_btn.text() == "Connect":
            self.th.connect_camera(self.wgt_top.cam_lst.currentData())
            self.th.center_frame.connect(self.set_center_holder)
            self.th.result_frame.connect(self.set_result_holder)
            self.th.start()
            self.wgt_top.cam_set_btn.setText("Disconnect")
        else:
            self.th.close_camera()
            self.wgt_top.cam_set_btn.setText("Connect")

    @Slot(QImage)
    def set_center_holder(self, image):
        self.wgt_center.frame_holder.pixmap = QPixmap(image)
        self.wgt_center.frame_holder.update()

    @Slot(QImage)
    def set_result_holder(self, image):
        self.wgt_left.result_frame_holder.pixmap = QPixmap(image)
        self.wgt_left.result_frame_holder.update()