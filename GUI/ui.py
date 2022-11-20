from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtWidgets import QMainWindow, QDockWidget, QVBoxLayout, QTextEdit, QFrame, QHBoxLayout, QGroupBox, \
    QLabel, QComboBox, QPushButton, QCheckBox, QLineEdit, QWidget, QPlainTextEdit, QGridLayout, QSlider, QSpinBox


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
    def __init__(self, name, title, widget):
        super(DockInit, self).__init__()
        self.setObjectName(name)
        self.setTitleBarWidget(title)
        self.setWidget(widget)


class ButtonInit(QPushButton):
    def __init__(self, name, tips, width, height, color1, color2, color3):
        super(ButtonInit, self).__init__()
        self.setText(name)
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


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.frame_right = None
        self.frame_bot = None
        self.frame_left = None
        self.frame_top = None
        self.frame_center = None
        self.main_window()
        self.center()

    def main_window(self):
        # set main window title
        self.setWindowTitle("Bearing Seal Classification")
        self.setCorner(Qt.BottomLeftCorner, Qt.LeftDockWidgetArea)
        self.setCorner(Qt.BottomRightCorner, Qt.RightDockWidgetArea)

        # create layout for main window
        layout_mainWindow = QVBoxLayout()

        # call functions
        self.camera_show()
        self.quick_settings()
        self.general()
        self.log()
        self.details()
        self.makeup()

        # create dock inside main window
        dock_top = DockInit("Quick Settings", QWidget(None), self.frame_top)
        dock_top.setMinimumHeight(110)
        dock_top.setMaximumHeight(130)
        self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, dock_top)

        dock_left = DockInit("General", QWidget(None), self.frame_left)
        dock_left.setMinimumWidth(270)
        dock_left.setMaximumWidth(350)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock_left)

        dock_bot = DockInit("Logs", QWidget(None), self.frame_bot)
        dock_bot.setMinimumHeight(110)
        dock_bot.setMinimumHeight(200)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, dock_bot)

        dock_right = DockInit("Details", QWidget(None), self.frame_right)
        dock_right.setMinimumWidth(270)
        dock_right.setMaximumWidth(350)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock_right)

        # add components to main window
        layout_mainWindow.addWidget(QTextEdit())
        self.setCentralWidget(self.frame_center)

        # set layout for main window
        self.setLayout(layout_mainWindow)

        # display main window
        self.show()

    # Center widget
    def camera_show(self):
        self.frame_center = QFrame()
        layout_center = QVBoxLayout()
        layout_center.setContentsMargins(0, 0, 0, 0)
        self.frame_center.setLayout(layout_center)

        # create cam show group box
        groupbox_camShow = QGroupBox("Realtime Camera Display")

        # create cam show area layout
        layout_camShow = QVBoxLayout()
        groupbox_camShow.setLayout(layout_camShow)

        # create components inside cam show area
        holder_camShow = MediaHolder("./media/pic/800x600.jpg", 800, 600)

        # add components to cam show
        layout_camShow.addWidget(holder_camShow)
        layout_center.addWidget(groupbox_camShow)

    # Top dock
    def quick_settings(self):
        # create container for quick settings area
        self.frame_top = QFrame()
        # create layout for quick settings
        layout_top = QHBoxLayout()
        layout_top.setContentsMargins(15, 5, 15, 0)
        self.frame_top.setLayout(layout_top)

        groupbox_camSet = QGroupBox("Camera Settings")

        layout_camSet = QHBoxLayout()
        groupbox_camSet.setLayout(layout_camSet)

        label_camSet = QLabel("Select camera")

        combobox_camSet = QComboBox()
        combobox_camSet.setToolTip("Select camera to connect")
        combobox_camSet.addItem("Build-in camera")
        btn_camSet_connect = ButtonInit("Connect", "Connect to selected camera", 80, 35, "#fad4a6", "#fbe7ab",
                                        "#f8a57f")

        layout_camSet.addWidget(label_camSet)
        layout_camSet.addStretch()
        layout_camSet.addWidget(combobox_camSet)
        layout_camSet.addStretch()
        layout_camSet.addWidget(btn_camSet_connect)

        groupbox_portSet = QGroupBox("Serial Port Settings")

        layout_portSet = QHBoxLayout()
        groupbox_portSet.setLayout(layout_portSet)

        label_portSet = QLabel("Select serial port")
        combobox_portSet = QComboBox()
        combobox_portSet.setToolTip("Select COM port to connect")
        combobox_portSet.addItem("COM1")

        label_baudRateSet = QLabel("Select baudrate")
        combobox_baudRateSet = QComboBox()
        combobox_baudRateSet.setToolTip("Select baudrate of the COM port")
        combobox_baudRateSet.addItem("115200")

        btn_portSet_connect = ButtonInit("Connect", "Connect to selected COM port", 80, 35, "#fad4a6", "#fbe7ab",
                                         "#f8a57f")

        # add components to serial port settings
        layout_portSet.addWidget(label_portSet, )
        layout_portSet.addSpacing(20)
        layout_portSet.addWidget(combobox_portSet)
        layout_portSet.addStretch()
        layout_portSet.addWidget(label_baudRateSet)
        layout_portSet.addSpacing(20)
        layout_portSet.addWidget(combobox_baudRateSet)
        layout_portSet.addStretch()
        layout_portSet.addWidget(btn_portSet_connect)

        # create other settings group box
        groupbox_otherSet = QGroupBox("Other Settings")

        # create other settings layout
        layout_otherSet = QHBoxLayout()
        groupbox_otherSet.setLayout(layout_otherSet)

        # create components inside other settings
        checkbox_otherSet_showTab = QCheckBox("Hide Right Tab")
        checkbox_otherSet_showTab.setToolTip("Show/hide additions tab for detail settings")

        btn_otherSet_init = ButtonInit("Initialize System", "Set whole system to the initial working condition", 120,
                                       35, "#fad4a6", "#fbe7ab", "#f8a57f")

        # add components to other settings
        layout_otherSet.addWidget(checkbox_otherSet_showTab)
        layout_otherSet.addStretch()
        layout_otherSet.addWidget(btn_otherSet_init)

        ########################################
        # END CREATE QUICK SETTINGS COMPONENTS #
        ########################################

        # add group box to frame
        layout_top.addWidget(groupbox_camSet)
        layout_top.setSpacing(15)
        layout_top.addWidget(groupbox_portSet)
        layout_top.setSpacing(15)
        layout_top.addWidget(groupbox_otherSet)

        layout_top.setStretchFactor(groupbox_camSet, 2)
        layout_top.setStretchFactor(groupbox_portSet, 3)
        layout_top.setStretchFactor(groupbox_otherSet, 2)

    # Left dock
    def general(self):
        self.frame_left = QFrame()

        layout_left = QVBoxLayout()
        layout_left.setContentsMargins(15, 0, 15, 15)
        self.frame_left.setLayout(layout_left)

        groupbox_result = QGroupBox("Result")

        layout_result = QVBoxLayout()
        groupbox_result.setLayout(layout_result)

        holder_result = MediaHolder("./media/pic/200x200.png", 200, 200)

        label_result = QLabel("Result show here")
        label_result.setMinimumSize(180, 44)
        label_result.setStyleSheet(
            "QLabel{border-radius: 22px; background-color: #e8ecec; font-color: white; font-size: 20px;"
            "qproperty-alignment: 'AlignCenter';}")

        layout_result.addWidget(holder_result)
        layout_result.setStretchFactor(holder_result, 3)
        layout_result.addWidget(label_result, alignment=Qt.AlignCenter)
        layout_result.setStretchFactor(label_result, 1)

        groupbox_statistics = QGroupBox("Statistics")

        layout_statistics = QGridLayout()
        groupbox_statistics.setLayout(layout_statistics)
        layout_statistics.setColumnStretch(0, 1)
        layout_statistics.setColumnStretch(1, 1)

        label_totalNum = QLabel("Total Classified:")
        lineEdit_totalNum = StatisticsInit(0, 0, 110, 35, "#6695ED", "#1f3efa")

        layout_statistics.addWidget(label_totalNum, 0, 0)
        layout_statistics.addWidget(lineEdit_totalNum, 0, 1)

        label_passedNum = QLabel("Total Passed:")
        lineEdit_passedNum = StatisticsInit(0, 0, 110, 35, "#72fa93", "#40d872")

        layout_statistics.addWidget(label_passedNum, 1, 0)
        layout_statistics.addWidget(lineEdit_passedNum, 1, 1)

        label_failedNum = QLabel("Total Failed:")
        lineEdit_failedNum = StatisticsInit(0, 0, 110, 35, "#e36255", "#d31638")

        layout_statistics.addWidget(label_failedNum, 2, 0)
        layout_statistics.addWidget(lineEdit_failedNum, 2, 1)

        frame_split = QFrame()
        frame_split.setMaximumHeight(1)
        frame_split.setFrameShape(QFrame.StyledPanel)
        layout_statistics.addWidget(frame_split, 3, 0, 1, 2)

        label_passedPercent = QLabel("Passed percentage:")
        lineEdit_passedPercent = StatisticsInit(0, 0, 110, 35)
        layout_statistics.addWidget(label_passedPercent, 4, 0)
        layout_statistics.addWidget(lineEdit_passedPercent, 4, 1)

        label_failedPercent = QLabel("Failed percentage:")
        lineEdit_failedPercent = StatisticsInit(0, 0, 110, 35)
        layout_statistics.addWidget(label_failedPercent, 5, 0)
        layout_statistics.addWidget(lineEdit_failedPercent, 5, 1)

        groupbox_control = QGroupBox("Control")

        layout_control = QHBoxLayout()
        groupbox_control.setLayout(layout_control)

        btn_run = ButtonInit("Run", "Start system", 80, 35, "#72fa93", "#a8fcbd", "#34a871")
        btn_stop = ButtonInit("Stop", "Stop system", 80, 35, "#f2a298", "#f5d6d6", "#e45642")

        layout_control.addWidget(btn_run)
        layout_control.addWidget(btn_stop)

        layout_left.addWidget(groupbox_result)
        layout_left.addWidget(groupbox_statistics)
        layout_left.addWidget(groupbox_control)

        layout_left.setStretchFactor(groupbox_result, 3)
        layout_left.setStretchFactor(groupbox_statistics, 3)
        layout_left.setStretchFactor(groupbox_control, 1)

    # Bottom dock
    def log(self):
        self.frame_bot = QFrame()

        groupbox_log = QGroupBox("Log")

        layout_log = QHBoxLayout()
        groupbox_log.setLayout(layout_log)

        textEdit_log = QPlainTextEdit()

        btn_logClear = ButtonInit("Clear Log", "Clear all log entries history", 80, 35, '#9f8c86', '#f0eae7', '#895b4a')

        layout_log.addWidget(textEdit_log)
        layout_log.addWidget(btn_logClear)

        layout_bot = QVBoxLayout()
        layout_bot.setContentsMargins(0, 0, 0, 15)
        self.frame_bot.setLayout(layout_bot)

        layout_bot.addWidget(groupbox_log)

    # Right dock
    def details(self):
        self.frame_right = QFrame()

        layout_right = QVBoxLayout()
        layout_right.setContentsMargins(15, 0, 15, 15)
        self.frame_right.setLayout(layout_right)

        # Detail process
        groupbox_detailProcess = QGroupBox("Detail Process")
        layout_detailProcess = QVBoxLayout()
        # layout_detailProcess.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        groupbox_detailProcess.setLayout(layout_detailProcess)

        label_contour = QLabel("Contour Process")
        holder_contour = MediaHolder("./media/pic/150x150_1.png", 150, 150)

        label_hough = QLabel("Hough Circle Process")
        holder_hough = MediaHolder("./media/pic/150x150_2.png", 150, 150)

        label_yolo = QLabel("Yolo Process")
        holder_yolo = MediaHolder("./media/pic/150x150_3.png", 150, 150)

        layout_detailProcess.addWidget(label_contour, alignment=Qt.AlignCenter)
        layout_detailProcess.addWidget(holder_contour)
        layout_detailProcess.setStretchFactor(holder_contour, 2)
        layout_detailProcess.addWidget(label_hough, alignment=Qt.AlignCenter)
        layout_detailProcess.addWidget(holder_hough)
        layout_detailProcess.setStretchFactor(holder_hough, 2)
        layout_detailProcess.addWidget(label_yolo, alignment=Qt.AlignCenter)
        layout_detailProcess.addWidget(holder_yolo)
        layout_detailProcess.setStretchFactor(holder_yolo, 2)

        layout_right.addWidget(groupbox_detailProcess)

        # param setting
        groupbox_param = QGroupBox("Parameter Settings")
        layout_param = QVBoxLayout()
        groupbox_param.setLayout(layout_param)

        layout_paramCfg = QGridLayout()
        layout_param.addLayout(layout_paramCfg)

        label_errorThreshold = QLabel("Error Threshold")
        slider_errorThreshold = QSlider(Qt.Horizontal)
        slider_errorThreshold.setToolTip("Set the threshold for error percentage of the bearing seal size")
        spinbox_errorThreshold = QSpinBox()
        spinbox_errorThreshold.setToolTip("Set the threshold for error percentage of the bearing seal size")

        layout_paramCfg.addWidget(label_errorThreshold, 0, 0)
        layout_paramCfg.addWidget(slider_errorThreshold, 0, 1)
        layout_paramCfg.addWidget(spinbox_errorThreshold, 0, 2)

        layout_saveCfg = QHBoxLayout()
        layout_param.addLayout(layout_saveCfg)

        btn_defaultCfg = ButtonInit("Reset settings", "Reset all parameters to default value", 90, 35, "#a6c4d0",
                                    "#cadde4", "#88acbc")
        btn_saveCfg = ButtonInit("Save settings", "Save all parameters was set by user", 90, 35, "#a6c4d0", "#cadde4",
                                 "#88acbc")

        layout_saveCfg.addWidget(btn_defaultCfg)
        layout_saveCfg.addWidget(btn_saveCfg)

        layout_right.addWidget(groupbox_detailProcess)
        layout_right.addWidget(groupbox_param)

        layout_right.setStretchFactor(groupbox_detailProcess, 5)
        layout_right.setStretchFactor(groupbox_param, 2)

    def makeup(self):
        self.setStyleSheet("QMainWindow{background-color: #eff0f7;}"
                           "QGroupBox{border: 2px solid #ffffff; border-radius: 10px; margin-top: 0.5em; font-family: "
                           "'Segoe UI'; font-size: 14px; font-weight: regular; background-color: #ffffff;} "
                           "QGroupBox:title{subcontrol-origin: margin;left: 10px;}"
                           "QPushButton{border-radius: 10px; font-size: 14px;}"
                           "QLineEdit{border-radius: 10px;}"
                           "QPlainTextEdit{border-radius: 8px; background-color: #eff0f7;}"
                           "QPlainTextEdit:focus{border: 2px solid #9dbdba;}"
                           "QLabel,QCheckBox,QComboBox,QLineEdit,QPlainTextEdit{font-size: 14px;}")

    def center(self):
        frame_geometry = self.frameGeometry()
        center_point = self.screen().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())
