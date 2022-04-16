import mysql.connector

class save_data_handle():
    def __init__(self, row_po=0, row_val=0, column=0):
        super(save_data_handle, self).__init__()

        db = mysql.connector.connect(user='root', password='1234',
                                     host='127.0.0.1', database="new_database")

        if column == 1:
            sql = "UPDATE `distance` SET `name`= %s WHERE `ID` = %s"
            val = (row_val, row_po)
            mycursor = db.cursor()  # run command
            mycursor.execute(sql, val)
            db.commit()
            print(mycursor.rowcount, "record(s) affected")

        elif column == 2:
            sql = "UPDATE `distance` SET `km`= %s WHERE `ID` = %s"
            val = (row_val, row_po)
            mycursor = db.cursor()  # run command
            mycursor.execute(sql, val)
            db.commit()
            print(mycursor.rowcount, "record(s) affected")