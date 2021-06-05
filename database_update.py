import psycopg2

class update_stock_data_db:
    __DBNAME = "stockdata"
    __USER = "trader"
    __PASS = "intraday"
    __HOST = "127.0.0.1"
    __PORT = "5432"


    def __init__(self):
        self.DSN = "dbname={} user={} password={} host={} port={}".format(self.__DBNAME,self.__USER,self.__PASS,self.__HOST,self.__PORT)


    def update_table(self, table, columns, values):
        self.conn = psycopg2.connect(self.DSN)
        self.cur = self.conn.cursor()
        columns = ",".join(columns)
        values = ",".join(values)
        self.cur.execute(
            "INSERT INTO {} ({}) VALUES ({})".format(table,columns,values));

        self.conn.commit()
        print("Record inserted successfully")
        self.conn.close()