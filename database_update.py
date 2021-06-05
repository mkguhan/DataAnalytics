import psycopg2

class update_stock_data_db:
    __DBNAME = "stock_data"
    __USER = "trader"
    __PASS = "intraday"
    __HOST = "127.0.0.1"
    __PORT = "5432"


    def __init__(self):
        self.DSN = "dbname='stock_data',user='trader',password='intraday',host='127.0.0.1',port='5432'".format(self.__DBNAME,self.__USER,self.__PASS,self.__HOST,self.__PORT)


    def update_table(self, table, columns, values):
        self.conn = psycopg2.connect(self.DSN)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "INSERT INTO {} ({}) VALUES ({})".format(table,columns,values));

        self.conn.commit()
        print("Record inserted successfully")
        self.conn.close()