# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sim.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SimUI(object):
    def setupUi(self, SimUI):
        SimUI.setObjectName("SimUI")
        SimUI.resize(1131, 669)
        self.verticalLayout = QtWidgets.QVBoxLayout(SimUI)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hBox_top = QtWidgets.QHBoxLayout()
        self.hBox_top.setSpacing(3)
        self.hBox_top.setObjectName("hBox_top")
        self.cBox_view = QtWidgets.QComboBox(SimUI)
        self.cBox_view.setObjectName("cBox_view")
        self.cBox_view.addItem("")
        self.cBox_view.addItem("")
        self.hBox_top.addWidget(self.cBox_view)
        self.cBox_mode = QtWidgets.QComboBox(SimUI)
        self.cBox_mode.setObjectName("cBox_mode")
        self.cBox_mode.addItem("")
        self.cBox_mode.addItem("")
        self.hBox_top.addWidget(self.cBox_mode)
        self.cBox_FF = QtWidgets.QComboBox(SimUI)
        self.cBox_FF.setObjectName("cBox_FF")
        self.cBox_FF.addItem("")
        self.cBox_FF.addItem("")
        self.cBox_FF.addItem("")
        self.cBox_FF.addItem("")
        self.hBox_top.addWidget(self.cBox_FF)
        self.btn_load = QtWidgets.QPushButton(SimUI)
        self.btn_load.setIconSize(QtCore.QSize(20, 20))
        self.btn_load.setObjectName("btn_load")
        self.hBox_top.addWidget(self.btn_load)
        self.lab_data = QtWidgets.QLabel(SimUI)
        self.lab_data.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_data.setObjectName("lab_data")
        self.hBox_top.addWidget(self.lab_data)
        self.tBtn_start = QtWidgets.QToolButton(SimUI)
        self.tBtn_start.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Sim/images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tBtn_start.setIcon(icon)
        self.tBtn_start.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tBtn_start.setAutoRaise(True)
        self.tBtn_start.setObjectName("tBtn_start")
        self.hBox_top.addWidget(self.tBtn_start)
        self.tBtn_stop = QtWidgets.QToolButton(SimUI)
        self.tBtn_stop.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Sim/images/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tBtn_stop.setIcon(icon1)
        self.tBtn_stop.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tBtn_stop.setAutoRaise(True)
        self.tBtn_stop.setObjectName("tBtn_stop")
        self.hBox_top.addWidget(self.tBtn_stop)
        self.cBox_save = QtWidgets.QCheckBox(SimUI)
        self.cBox_save.setObjectName("cBox_save")
        self.hBox_top.addWidget(self.cBox_save)
        self.cBox_sim = QtWidgets.QCheckBox(SimUI)
        self.cBox_sim.setObjectName("cBox_sim")
        self.hBox_top.addWidget(self.cBox_sim)
        self.cBox_cam = QtWidgets.QCheckBox(SimUI)
        self.cBox_cam.setObjectName("cBox_cam")
        self.hBox_top.addWidget(self.cBox_cam)
        self.cBox_fov = QtWidgets.QCheckBox(SimUI)
        self.cBox_fov.setObjectName("cBox_fov")
        self.hBox_top.addWidget(self.cBox_fov)
        self.hBox_top.setStretch(0, 1)
        self.hBox_top.setStretch(1, 1)
        self.hBox_top.setStretch(2, 1)
        self.hBox_top.setStretch(3, 1)
        self.hBox_top.setStretch(4, 8)
        self.hBox_top.setStretch(5, 1)
        self.hBox_top.setStretch(6, 1)
        self.hBox_top.setStretch(8, 1)
        self.hBox_top.setStretch(10, 1)
        self.verticalLayout.addLayout(self.hBox_top)
        self.splitter_mid = QtWidgets.QSplitter(SimUI)
        self.splitter_mid.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_mid.setHandleWidth(3)
        self.splitter_mid.setObjectName("splitter_mid")
        self.radar_view_layout = GraphicsLayoutWidget(self.splitter_mid)
        self.radar_view_layout.setObjectName("radar_view_layout")
        self.splitter_table = QtWidgets.QSplitter(self.splitter_mid)
        self.splitter_table.setFrameShape(QtWidgets.QFrame.HLine)
        self.splitter_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.splitter_table.setOrientation(QtCore.Qt.Vertical)
        self.splitter_table.setHandleWidth(3)
        self.splitter_table.setObjectName("splitter_table")
        self.tabView_track = QtWidgets.QTableView(self.splitter_table)
        self.tabView_track.setObjectName("tabView_track")
        self.verticalLayout.addWidget(self.splitter_mid)
        self.gBox_bottom = QtWidgets.QGridLayout()
        self.gBox_bottom.setSpacing(6)
        self.gBox_bottom.setObjectName("gBox_bottom")
        self.verticalLayout.addLayout(self.gBox_bottom)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 20)
        self.verticalLayout.setStretch(2, 2)

        self.retranslateUi(SimUI)
        QtCore.QMetaObject.connectSlotsByName(SimUI)

    def retranslateUi(self, SimUI):
        _translate = QtCore.QCoreApplication.translate
        SimUI.setWindowTitle(_translate("SimUI", "Sim"))
        self.cBox_view.setItemText(0, _translate("SimUI", "Rear"))
        self.cBox_view.setItemText(1, _translate("SimUI", "Front"))
        self.cBox_mode.setItemText(0, _translate("SimUI", "offLine"))
        self.cBox_mode.setItemText(1, _translate("SimUI", "inLine"))
        self.cBox_FF.setItemText(0, _translate("SimUI", "Tail Door"))
        self.cBox_FF.setItemText(1, _translate("SimUI", "BSD"))
        self.cBox_FF.setItemText(2, _translate("SimUI", "LCA"))
        self.cBox_FF.setItemText(3, _translate("SimUI", "FCW"))
        self.btn_load.setText(_translate("SimUI", "LoadData"))
        self.lab_data.setText(_translate("SimUI", "Pls select a data source"))
        self.cBox_save.setText(_translate("SimUI", "Save"))
        self.cBox_sim.setText(_translate("SimUI", "Simultion"))
        self.cBox_cam.setText(_translate("SimUI", "Camera"))
        self.cBox_fov.setText(_translate("SimUI", "FOV"))
from pyqtgraph import GraphicsLayoutWidget
from . import sim_rc
