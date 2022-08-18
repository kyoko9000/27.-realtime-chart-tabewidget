import sys
# pip install pyqt5
import mysql.connector
from PyQt5.QtCore import QTimer, Qt, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

# just change the name
from draw_chart import show_chart
from gui import Ui_MainWindow
from save_data_to_mySQL import save_data_handle
from show_data_form_mySQL import show_data

timer = QTimer()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.thread = {}

        # khai bao button *****************************************
        self.uic.Button_load_data.clicked.connect(self.show_data_1)
        self.uic.Button_update.clicked.connect(self.save_data)

        self.uic.Button_start_chart.clicked.connect(self.show_diagram)
        self.uic.Button_stop_chart.clicked.connect(self.stop_update)


    def show_data_1(self):
        # clear error on the screen
        self.uic.textEdit_data.setText('')
        # read text from combobox database
        choose_database = self.uic.comboBox_chosse_database.currentText()
        print(choose_database)

        # read text from combobox table
        choose_table = self.uic.comboBox_choose_table.currentText()
        print(choose_table)

        self.thread[1] = show_data(index=1, database=choose_database, table=choose_table)
        self.thread[1].start()
        self.thread[1].signal.connect(self.show_chart)

    def show_chart(self, result):
        # load du lieu lên tablewidget ************
        a = 0
        for row in result:
            a = len(row)
        self.uic.tableWidget.setRowCount(len(result))  # tao so row
        self.uic.tableWidget.setColumnCount(a)  # tao so column

        # fill data to tablewidget
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                self.uic.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def closeEvent(self, event):
        print("close update")
        self.stop_update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            print("enter press")
            self.save_data()

    def stop_update(self):
        timer.stop()

    def show_diagram(self):
        if self.uic.screen.isEmpty():
            self.uic.screen.addWidget(show_chart())
        elif self.uic.screen is not None:
            timer.start(2000)

    def save_data(self):
        # tim ra toa doa cua item can thay the
        currentItems = 0
        for currentItems in self.uic.tableWidget.selectedItems():
            print('row: ', currentItems.row())
            print("column: ", currentItems.column())
            print("value: ", currentItems.text())
        try:

            ID_value = self.uic.tableWidget.item(currentItems.row(), 0).text()
            print("ID: ", ID_value)
            # take value
            row_val = currentItems.text()
            row_po = ID_value

            save_data_handle(row_po=row_po, row_val=row_val, column=currentItems.column())

        except:
            print("no data")


if __name__ == "__main__":
    # run app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
