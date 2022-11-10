from PySide6 import QtCore
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import QMainWindow, QDockWidget, QVBoxLayout, QTextEdit, QFrame, QHBoxLayout, QGroupBox, QLabel, \
    QComboBox, QPushButton, QCheckBox, QLineEdit, QWidget, QPlainTextEdit, QGridLayout, QSlider, QSpinBox


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.main_window()

    def main_window(self):
        # set main window title
        self.setWindowTitle("Bearing Seal Classification")

        # create layout for main window
        layout_mainWindow = QVBoxLayout()

        # call functions
        self.camera_show()
        self.quick_settings()
        self.general()
        self.log()
        self.details()

        # create dock inside main window
        dock_top = QDockWidget("Quick Settings", self)
        dock_top.setTitleBarWidget(QWidget(None))
        dock_top.setWidget(self.frame_top)
        dock_top.setMaximumHeight(120)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.TopDockWidgetArea, dock_top)

        dock_left = QDockWidget("General", self)
        dock_left.setTitleBarWidget(QWidget(None))
        self.setCorner(QtCore.Qt.BottomLeftCorner, QtCore.Qt.LeftDockWidgetArea)
        dock_left.setWidget(self.frame_left)
        dock_left.setMinimumWidth(270)
        dock_left.setMaximumWidth(350)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea, dock_left)

        dock_bot = QDockWidget("Log", self)
        dock_bot.setTitleBarWidget(QWidget(None))
        dock_bot.setWidget(self.frame_bot)
        dock_bot.setMinimumHeight(150)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.BottomDockWidgetArea, dock_bot)

        dock_right = QDockWidget("Detail", self)
        dock_right.setTitleBarWidget(QWidget(None))
        self.setCorner(QtCore.Qt.BottomRightCorner, QtCore.Qt.RightDockWidgetArea)
        dock_right.setWidget(self.frame_right)
        dock_right.setMinimumWidth(250)
        dock_right.setMaximumWidth(350)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.RightDockWidgetArea, dock_right)

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
        self.frame_center.setLayout(layout_center)
        # self.frame_center.setStyleSheet("background-color: blue;")

        # create cam show group box
        groupbox_camShow = QGroupBox("Realtime Camera Display")
        groupbox_camShow.setFont(QFont("Arial", 12, weight=QFont.Bold))

        # create cam show area layout
        layout_camShow = QVBoxLayout()
        groupbox_camShow.setLayout(layout_camShow)

        # create components inside cam show area
        holder_camShow = QLabel()
        holder_camShow.setMinimumSize(800, 600)
        holder_camShow.setPixmap(QPixmap("./media/pic/800x600.jpg"))
        holder_camShow.setScaledContents(True)

        # add components to cam show
        layout_camShow.addWidget(holder_camShow)

        layout_center.addWidget(groupbox_camShow)

    # Top dock
    def quick_settings(self):
        # create container for quick settings area
        self.frame_top = QFrame()

        ##########################################
        # START CREATE QUICK SETTINGS COMPONENTS #
        ##########################################

        # create camera settings group box
        groupbox_camSet = QGroupBox("Camera Settings")

        # create camera settings area layout
        layout_camSet = QHBoxLayout()
        groupbox_camSet.setLayout(layout_camSet)

        # create components inside camera settings area
        label_camSet = QLabel("Select camera")
        combobox_camSet = QComboBox()
        combobox_camSet.addItem("Build-in camera")
        btn_camSet_connect = QPushButton("Connect")

        # add components to quick settings
        layout_camSet.addWidget(label_camSet)
        layout_camSet.addStretch()
        layout_camSet.addWidget(combobox_camSet)
        layout_camSet.addStretch()
        layout_camSet.addWidget(btn_camSet_connect)

        # create serial port settings group box
        groupbox_portSet = QGroupBox("Serial Port Settings")

        # create serial port settings layout
        layout_portSet = QHBoxLayout()
        groupbox_portSet.setLayout(layout_portSet)

        # create components inside serial port settings
        label_portSet = QLabel("Select serial port")
        combobox_portSet = QComboBox()
        combobox_portSet.addItem("COM1")
        btn_portSet_connect = QPushButton("Connect")

        # add components to serial port settings
        layout_portSet.addWidget(label_portSet, )
        layout_portSet.addStretch()
        layout_portSet.addWidget(combobox_portSet, 1.5, QtCore.Qt.AlignmentFlag.AlignLeft)
        layout_portSet.addStretch()
        layout_portSet.addWidget(btn_portSet_connect, 0.5)

        # create other settings group box
        groupbox_otherSet = QGroupBox("Other Settings")

        # create other settings layout
        layout_otherSet = QHBoxLayout()
        groupbox_otherSet.setLayout(layout_otherSet)

        # create components inside other settings
        btn_otherSet_init = QPushButton("Initialize System")
        checkbox_otherSet_showTab = QCheckBox("Show Right Tab")

        # add components to other settings
        layout_otherSet.addWidget(btn_otherSet_init)
        layout_otherSet.addStretch()
        layout_otherSet.addWidget(checkbox_otherSet_showTab)

        ########################################
        # END CREATE QUICK SETTINGS COMPONENTS #
        ########################################

        # create layout for quick settings
        layout_top = QHBoxLayout()
        self.frame_top.setLayout(layout_top)

        # add group box to frame
        layout_top.addWidget(groupbox_camSet)
        layout_top.addWidget(groupbox_portSet)
        layout_top.addWidget(groupbox_otherSet)

    # Left dock
    def general(self):
        self.frame_left = QFrame()
        # self.frame_left.setStyleSheet("background-color: red;")

        layout_left = QVBoxLayout()
        self.frame_left.setLayout(layout_left)

        groupbox_result = QGroupBox("Result")

        layout_result = QVBoxLayout()
        groupbox_result.setLayout(layout_result)

        holder_result = QLabel()
        holder_result.setMinimumSize(200, 200)
        holder_result.setPixmap(QPixmap("./media/pic/200x200.png"))
        holder_result.setScaledContents(True)

        label_result = QLabel("Result show here")

        layout_result.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        layout_result.addWidget(holder_result)
        layout_result.addWidget(label_result, alignment=QtCore.Qt.AlignCenter)

        groupbox_statistics = QGroupBox("Statistics")

        layout_statistics = QGridLayout()
        groupbox_statistics.setLayout(layout_statistics)
        layout_statistics.setColumnStretch(0, 1)
        layout_statistics.setColumnStretch(1, 1)

        label_totalNum = QLabel("Total Classified:")
        lineEdit_totalNum = QLineEdit()
        layout_statistics.addWidget(label_totalNum, 0, 0)
        layout_statistics.addWidget(lineEdit_totalNum, 0, 1)

        label_passedNum = QLabel("Total Passed:")
        lineEdit_passedNum = QLineEdit()
        layout_statistics.addWidget(label_passedNum, 1, 0)
        layout_statistics.addWidget(lineEdit_passedNum, 1, 1)

        label_failedNum = QLabel("Total Failed:")
        lineEdit_failedNum = QLineEdit()
        layout_statistics.addWidget(label_failedNum, 2, 0)
        layout_statistics.addWidget(lineEdit_failedNum, 2, 1)

        frame_split = QFrame()
        frame_split.setMaximumHeight(1)
        frame_split.setFrameShape(QFrame.StyledPanel)
        layout_statistics.addWidget(frame_split, 3, 0, 1, 2)

        label_passedPercent = QLabel("Passed percentage:")
        lineEdit_passedPercent = QLineEdit()
        layout_statistics.addWidget(label_passedPercent, 4, 0)
        layout_statistics.addWidget(lineEdit_passedPercent, 4, 1)

        label_failedPercent = QLabel("Failed percentage:")
        lineEdit_failedPercent = QLineEdit()
        layout_statistics.addWidget(label_failedPercent, 5, 0)
        layout_statistics.addWidget(lineEdit_failedPercent, 5, 1)

        groupbox_control = QGroupBox("Control")

        layout_control = QHBoxLayout()
        groupbox_control.setLayout(layout_control)

        btn_run = QPushButton("Run")
        btn_stop = QPushButton("Stop")

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
        btn_logClear = QPushButton("Clear Log")

        layout_log.addWidget(textEdit_log)
        layout_log.addWidget(btn_logClear)

        layout_bot = QVBoxLayout()
        self.frame_bot.setLayout(layout_bot)

        layout_bot.addWidget(groupbox_log)

    # Right dock
    def details(self):
        self.frame_right = QFrame()
        layout_right = QVBoxLayout()
        self.frame_right.setLayout(layout_right)

        # Detail process
        groupbox_detailProcess = QGroupBox("Detail Process")
        layout_detailProcess = QVBoxLayout()
        layout_detailProcess.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        groupbox_detailProcess.setLayout(layout_detailProcess)

        label_contour = QLabel("Contour Process")

        holder_contour = QLabel()
        holder_contour.setMinimumSize(150, 150)
        holder_contour.setPixmap(QPixmap("./media/pic/150x150_1.png"))
        holder_contour.setScaledContents(True)

        label_hough = QLabel("Hough Circle Process")

        holder_hough = QLabel()
        holder_hough.setMinimumSize(150, 150)
        holder_hough.setPixmap(QPixmap("./media/pic/150x150_2.png"))
        holder_hough.setScaledContents(True)

        label_yolo = QLabel("Yolo Process")

        holder_yolo = QLabel()
        holder_yolo.setMinimumSize(150, 150)
        holder_yolo.setPixmap(QPixmap("./media/pic/150x150_3.png"))
        holder_yolo.setScaledContents(True)

        layout_detailProcess.addWidget(label_contour, alignment=QtCore.Qt.AlignCenter)
        layout_detailProcess.addWidget(holder_contour)
        layout_detailProcess.addWidget(label_hough, alignment=QtCore.Qt.AlignCenter)
        layout_detailProcess.addWidget(holder_hough)
        layout_detailProcess.addWidget(label_yolo, alignment=QtCore.Qt.AlignCenter)
        layout_detailProcess.addWidget(holder_yolo)

        layout_right.addWidget(groupbox_detailProcess)

        # param setting
        groupbox_param = QGroupBox("Parameter Settings")
        layout_param = QVBoxLayout()
        groupbox_param.setLayout(layout_param)

        layout_paramCfg = QGridLayout()
        layout_param.addLayout(layout_paramCfg)

        label_errorThreshold = QLabel("Error Threshold")
        label_errorThreshold.setToolTip("Set the threshold for error percentage of the bearing seal size")
        slider_errorThreshold = QSlider(QtCore.Qt.Horizontal)
        spinbox_errorThreshold = QSpinBox()

        layout_paramCfg.addWidget(label_errorThreshold, 0, 0)
        layout_paramCfg.addWidget(slider_errorThreshold, 0, 1)
        layout_paramCfg.addWidget(spinbox_errorThreshold, 0, 2)

        layout_saveCfg = QHBoxLayout()
        layout_param.addLayout(layout_saveCfg)

        btn_defaultCfg = QPushButton("Reset settings")
        btn_defaultCfg.setToolTip("Reset all parameters to default value")

        btn_saveCfg = QPushButton("Save settings")
        btn_saveCfg.setToolTip("Save all parameters was set by user")

        layout_saveCfg.addWidget(btn_defaultCfg)
        layout_saveCfg.addWidget(btn_saveCfg)

        layout_right.addWidget(groupbox_detailProcess)
        layout_right.addWidget(groupbox_param)
