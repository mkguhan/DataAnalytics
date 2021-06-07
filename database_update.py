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
        try:
            self.conn = psycopg2.connect(self.DSN)
            self.cur = self.conn.cursor()
            sql = "INSERT INTO security (id, code, name, description, listed_date, series, isin_number, facevalue, paidup_value, market_lot) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.cur.execute(sql, values)
            self.conn.commit()
            print("Record inserted successfully")
        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into security table", error)
        finally:
            self.conn.close()

    @classmethod
    def get_security_id_list(self):
        try:
            self.conn = psycopg2.connect(self.DSN)
            self.cur = self.conn.cursor()
            sql = "Select id,code from security"
            self.cur.execute(sql)
            security_details = self.cur.fetchall()
            return security_details
        except (Exception, psycopg2.Error) as error:
            print("Failed get list of securites", error)


    def update_preopenmarket_date(self,data):
        pass