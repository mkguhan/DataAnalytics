import psycopg2

class update_stock_data_db:
    __DBNAME = "stockdata"
    __USER = "trader"
    __PASS = "intraday"
    __HOST = "127.0.0.1"
    __PORT = "5432"


    def __init__(self):
        self.DSN = "dbname={} user={} password={} host={} port={}".format(self.__DBNAME,self.__USER,self.__PASS,self.__HOST,self.__PORT)


    def update_security_table(self, table, columns, values):
        self.conn = psycopg2.connect(self.DSN)
        self.cur = self.conn.cursor()
        self.cur.execute("INSERT INTO security ('id', 'code', 'name', 'description', 'listed_date', 'series', 'isin_number', 'facevalue', 'paidup_value', 'market_lot') VALUES (values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8])");

        self.conn.commit()
        print("Record inserted successfully")
        self.conn.close()