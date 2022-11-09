from PySide6 import QtCore
from PySide6.QtGui import QPixmap
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
        dock_left.setMaximumWidth(450)
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
        self.addDockWidget(QtCore.Qt.DockWidgetArea.RightDockWidgetArea, dock_right)

        # add components to main window
        layout_mainWindow.addWidget(QTextEdit())
        self.setCentralWidget(self.frame_center)

        # set layout for main window
        self.setLayout(layout_mainWindow)

        # display main window
        self.show()

    def camera_show(self):
        self.frame_center = QFrame()
        layout_center = QVBoxLayout()
        self.frame_center.setLayout(layout_center)
        # self.frame_center.setStyleSheet("background-color: blue;")

        # create cam show group box
        groupbox_camShow = QGroupBox("Realtime Camera Display")

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
        btn_portSet_connect = QPushButton("Connect")

        # add components to serial port settings
        layout_portSet.addWidget(label_portSet)
        layout_portSet.addStretch()
        layout_portSet.addWidget(combobox_portSet)
        layout_portSet.addStretch()
        layout_portSet.addWidget(btn_portSet_connect)

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

    def general(self):
        self.frame_left = QFrame()
        # self.frame_left.setStyleSheet("background-color: red;")

        ###################################
        # START CREATE GENERAL COMPONENTS #
        ###################################

        # create results group box
        groupbox_result = QGroupBox("Result")

        # create results area layout
        layout_result = QVBoxLayout()
        groupbox_result.setLayout(layout_result)

        # create components inside result group box
        # image_result = QPixmap("./media/icon/product.png")
        image_result = QLabel("Result")

        label_result = QLabel("Result")

        # add components to results group box
        layout_result.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        layout_result.addWidget(image_result)
        layout_result.addWidget(label_result)

        # create statistics group box
        groupbox_statistics = QGroupBox("Statistics")

        # create statistics layout
        layout_statistics = QVBoxLayout()
        groupbox_statistics.setLayout(layout_statistics)

        # create total layout
        layout_totalNum = QHBoxLayout()

        # create components inside total layout
        label_totalNum = QLabel("Total Classified:")
        lineEdit_totalNum = QLineEdit()

        # add components to total layout
        layout_totalNum.addWidget(label_totalNum)
        layout_totalNum.addStretch()
        layout_totalNum.addWidget(lineEdit_totalNum)

        # create passed layout
        layout_passedNum = QHBoxLayout()

        # create components inside passed layout
        label_passedNum = QLabel("Total Passed:")
        lineEdit_passedNum = QLineEdit()

        # add components to passed layout
        layout_passedNum.addWidget(label_passedNum)
        layout_passedNum.addStretch()
        layout_passedNum.addWidget(lineEdit_passedNum)

        # create failed layout
        layout_failedNum = QHBoxLayout()

        # create components inside failed layout
        label_failedNum = QLabel("Total Failed:")
        lineEdit_failedNum = QLineEdit()

        # add components to passed layout
        layout_failedNum.addWidget(label_failedNum)
        layout_failedNum.addStretch()
        layout_failedNum.addWidget(lineEdit_failedNum)

        # add 3 layout to statistics layout
        layout_statistics.addLayout(layout_totalNum)
        layout_statistics.addLayout(layout_passedNum)
        layout_statistics.addLayout(layout_failedNum)

        # create control group box
        groupbox_control = QGroupBox("Control")

        # create control layout
        layout_control = QHBoxLayout()
        groupbox_control.setLayout(layout_control)

        # create components inside control group box
        btn_run = QPushButton("Run")
        btn_stop = QPushButton("Stop")

        # add components to control group box
        layout_control.addWidget(btn_run)
        layout_control.addWidget(btn_stop)

        #################################
        # END CREATE GENERAL COMPONENTS #
        #################################

        # create layout for general
        layout_left = QVBoxLayout()
        self.frame_left.setLayout(layout_left)

        # add group box to frame
        layout_left.addWidget(groupbox_result)
        layout_left.addWidget(groupbox_statistics)
        layout_left.addWidget(groupbox_control)

        # set stretch layout for general
        layout_left.setStretchFactor(groupbox_result, 3)
        layout_left.setStretchFactor(groupbox_statistics, 2)
        layout_left.setStretchFactor(groupbox_control, 1)

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
        holder_contour.setPixmap(QPixmap("./media/pic/100x100.png"))
        holder_contour.setScaledContents(True)

        label_hough = QLabel("Hough Circle Process")

        holder_hough = QLabel()
        holder_hough.setMinimumSize(150, 150)
        holder_hough.setPixmap(QPixmap("./media/pic/100x100.png"))
        holder_hough.setScaledContents(True)

        label_yolo = QLabel("Yolo Process")

        holder_yolo = QLabel()
        holder_yolo.setMinimumSize(150, 150)
        holder_yolo.setPixmap(QPixmap("./media/pic/100x100.png"))
        holder_yolo.setScaledContents(True)

        layout_detailProcess.addWidget(label_contour, alignment=QtCore.Qt.AlignCenter)
        layout_detailProcess.addWidget(holder_contour)
        layout_detailProcess.addWidget(label_hough, alignment=QtCore.Qt.AlignCenter)
        layout_detailProcess.addWidget(holder_hough)
        layout_detailProcess.addWidget(label_yolo, alignment=QtCore.Qt.AlignCenter)
        layout_detailProcess.addWidget(holder_yolo)

        layout_right.addWidget(groupbox_detailProcess)

        # param setting
        groupbox_paramCfg = QGroupBox("Parameter Settings")
        layout_paramCfg = QGridLayout()
        groupbox_paramCfg.setLayout(layout_paramCfg)

        label_errorThreshold = QLabel("Error Threshold")
        slider_errorThreshold = QSlider(QtCore.Qt.Horizontal)
        spinbox_errorThreshold = QSpinBox()

        layout_paramCfg.addWidget(label_errorThreshold, 0, 0)
        layout_paramCfg.addWidget(slider_errorThreshold, 0, 1)
        layout_paramCfg.addWidget(spinbox_errorThreshold, 0, 2)

        layout_right.addWidget(groupbox_detailProcess)
        layout_right.addWidget(groupbox_paramCfg)
