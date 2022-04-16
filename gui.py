# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 400))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tableWidget.setFont(font)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(300, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.screen = QtWidgets.QVBoxLayout()
        self.screen.setObjectName("screen")
        self.gridLayout_2.addLayout(self.screen, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Button_load_data = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_load_data.sizePolicy().hasHeightForWidth())
        self.Button_load_data.setSizePolicy(sizePolicy)
        self.Button_load_data.setMinimumSize(QtCore.QSize(0, 50))
        self.Button_load_data.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_load_data.setFont(font)
        self.Button_load_data.setObjectName("Button_load_data")
        self.gridLayout.addWidget(self.Button_load_data, 0, 0, 1, 1)
        self.Button_update = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_update.sizePolicy().hasHeightForWidth())
        self.Button_update.setSizePolicy(sizePolicy)
        self.Button_update.setMinimumSize(QtCore.QSize(0, 50))
        self.Button_update.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_update.setFont(font)
        self.Button_update.setObjectName("Button_update")
        self.gridLayout.addWidget(self.Button_update, 0, 1, 1, 1)
        self.Button_start_chart = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_start_chart.sizePolicy().hasHeightForWidth())
        self.Button_start_chart.setSizePolicy(sizePolicy)
        self.Button_start_chart.setMinimumSize(QtCore.QSize(0, 50))
        self.Button_start_chart.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_start_chart.setFont(font)
        self.Button_start_chart.setObjectName("Button_start_chart")
        self.gridLayout.addWidget(self.Button_start_chart, 0, 2, 1, 1)
        self.Button_stop_chart = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_stop_chart.sizePolicy().hasHeightForWidth())
        self.Button_stop_chart.setSizePolicy(sizePolicy)
        self.Button_stop_chart.setMinimumSize(QtCore.QSize(0, 50))
        self.Button_stop_chart.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_stop_chart.setFont(font)
        self.Button_stop_chart.setObjectName("Button_stop_chart")
        self.gridLayout.addWidget(self.Button_stop_chart, 0, 3, 1, 1)
        self.comboBox_chosse_database = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_chosse_database.sizePolicy().hasHeightForWidth())
        self.comboBox_chosse_database.setSizePolicy(sizePolicy)
        self.comboBox_chosse_database.setMinimumSize(QtCore.QSize(0, 50))
        self.comboBox_chosse_database.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_chosse_database.setFont(font)
        self.comboBox_chosse_database.setObjectName("comboBox_chosse_database")
        self.comboBox_chosse_database.addItem("")
        self.comboBox_chosse_database.addItem("")
        self.gridLayout.addWidget(self.comboBox_chosse_database, 1, 0, 1, 1)
        self.comboBox_choose_table = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_choose_table.sizePolicy().hasHeightForWidth())
        self.comboBox_choose_table.setSizePolicy(sizePolicy)
        self.comboBox_choose_table.setMinimumSize(QtCore.QSize(0, 50))
        self.comboBox_choose_table.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_choose_table.setFont(font)
        self.comboBox_choose_table.setObjectName("comboBox_choose_table")
        self.comboBox_choose_table.addItem("")
        self.comboBox_choose_table.addItem("")
        self.comboBox_choose_table.addItem("")
        self.comboBox_choose_table.addItem("")
        self.gridLayout.addWidget(self.comboBox_choose_table, 1, 1, 1, 1)
        self.textEdit_data = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_data.setMinimumSize(QtCore.QSize(0, 50))
        self.textEdit_data.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textEdit_data.setFont(font)
        self.textEdit_data.setObjectName("textEdit_data")
        self.gridLayout.addWidget(self.textEdit_data, 1, 2, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_load_data.setText(_translate("MainWindow", "Load Data"))
        self.Button_update.setText(_translate("MainWindow", "update"))
        self.Button_start_chart.setText(_translate("MainWindow", "Start Chart"))
        self.Button_stop_chart.setText(_translate("MainWindow", "Stop Chart"))
        self.comboBox_chosse_database.setItemText(0, _translate("MainWindow", "new_database"))
        self.comboBox_chosse_database.setItemText(1, _translate("MainWindow", "new_database_1"))
        self.comboBox_choose_table.setItemText(0, _translate("MainWindow", "customer"))
        self.comboBox_choose_table.setItemText(1, _translate("MainWindow", "distance"))
        self.comboBox_choose_table.setItemText(2, _translate("MainWindow", "food"))
        self.comboBox_choose_table.setItemText(3, _translate("MainWindow", "food_t1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
