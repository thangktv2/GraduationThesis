from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QDockWidget, QVBoxLayout, QTextEdit, QFrame, QHBoxLayout, QGroupBox, QLabel, \
    QComboBox, QPushButton, QCheckBox, QLineEdit


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
        self.quick_settings()
        self.general()

        # create dock inside main window
        dock_top = QDockWidget('Quick Settings', self)
        dock_top.setWidget(self.frame_top)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.TopDockWidgetArea, dock_top)

        dock_left = QDockWidget('General', self)
        dock_left.setWidget(self.frame_left)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea, dock_left)

        # add components to main window
        layout_mainWindow.addWidget(QTextEdit())
        self.setCentralWidget(QTextEdit())

        # set layout for main window
        self.setLayout(layout_mainWindow)

        # display main window
        self.show()

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
        layout_camSet.addWidget(combobox_camSet)
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
        layout_portSet.addWidget(combobox_portSet)
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
        layout_otherSet.addWidget(checkbox_otherSet_showTab)

        ########################################
        # END CREATE QUICK SETTINGS COMPONENTS #
        ########################################

        # create layout for quick settings
        layout_quickSet = QHBoxLayout()
        self.frame_top.setLayout(layout_quickSet)

        # add group box to frame
        layout_quickSet.addWidget(groupbox_camSet)
        layout_quickSet.addWidget(groupbox_portSet)
        layout_quickSet.addWidget(groupbox_otherSet)

    def general(self):
        self.frame_left = QFrame()

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
        layout_result.addWidget(image_result)
        layout_result.addWidget(label_result)

        # create statistics group box
        groupbox_statistics = QGroupBox("Statistics")

        # create statistics layout
        layout_statistics = QVBoxLayout()
        groupbox_statistics.setLayout(layout_statistics)

        # create total layout
        layout_totalNum = QVBoxLayout()

        # create components inside total layout
        label_totalNum = QLabel("Total Classified:")
        lineEdit_totalNum = QLineEdit()

        # add components to total layout
        layout_totalNum.addWidget(label_totalNum)
        layout_totalNum.addWidget(lineEdit_totalNum)

        # create passed layout
        layout_passedNum = QHBoxLayout()

        # create components inside passed layout
        label_passedNum = QLabel("Total Passed:")
        lineEdit_passedNum = QLineEdit()

        # add components to passed layout
        layout_totalNum.addWidget(label_passedNum)
        layout_totalNum.addWidget(lineEdit_passedNum)

        # create failed layout
        layout_failedNum = QHBoxLayout()

        # create components inside failed layout
        label_failedNum = QLabel("Total Failed:")
        lineEdit_failedNum = QLineEdit()

        # add components to passed layout
        layout_totalNum.addWidget(label_failedNum)
        layout_totalNum.addWidget(lineEdit_failedNum)

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
        layout_general = QVBoxLayout()
        self.frame_left.setLayout(layout_general)

        # add group box to frame
        layout_general.addWidget(groupbox_result)
        layout_general.addWidget(groupbox_statistics)
        layout_general.addWidget(groupbox_control)
