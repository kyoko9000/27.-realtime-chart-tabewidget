import mysql.connector
from PyQt5.QtCore import QThread, pyqtSignal


class show_data(QThread):
    signal = pyqtSignal(list)

    def __init__(self, index=0, database=0, table=0):
        super(show_data, self).__init__()
        self.a = index
        self.b = database
        self.c = table
        print("start threading", self.a)

    def run(self):
        try:
            # connect to mysql*********************
            db = mysql.connector.connect(user='root', password='1234',
                                         host='127.0.0.1', database=self.b)

            # command to choose table custom
            code_8 = 'SELECT * FROM {}'.format(self.c)
            mycursor = db.cursor()  # create mycoursor
            mycursor.execute(code_8)  # execute command
            result = mycursor.fetchall()  # result
            print(result)

            self.signal.emit(result)
        except:
            # main = MainWindow()
            # main.uic.textEdit_data.setText("no data")
            print("no data")
