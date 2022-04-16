# thu vien mo rong
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
import mysql.connector as load_mySQL

timer = QTimer()

class show_chart(FigureCanvasQTAgg):
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)

        timer.timeout.connect(self.loop)
        timer.start(2000)

        plt.ion()
    def loop(self):
        db = load_mySQL.connect(user='root', password='1234',
                                     host='127.0.0.1', database='new_database')
        # lenh chay
        code_8 = 'SELECT name,km FROM distance'
        # lệnh chạy code
        mycursor = db.cursor()
        mycursor.execute(code_8)  # make database
        result = mycursor.fetchall()

        datas = (result[0][0], result[1][0], result[2][0], result[3][0], result[4][0])
        datas1 = (result[0][1], result[1][1], result[2][1], result[3][1], result[4][1])
        explode = (0.2, 0.1, 0, 0, 0)
        print("label: ", datas)
        print("data: ", datas1)

        self.ax.clear()
        self.ax.pie(datas1, labels=datas, autopct='%1.2f%%', explode=explode,
               shadow=True, startangle=90)  # , explode=explode