from  database_update import  update_stock_data_db

class preopenmarket_update:

    def __init__(self):
        pass


    def get_list_sec_id(self):
        list = update_stock_data_db.get_security_id_list()
        print(list)



if __name__ == "__main__":
    security_preopen = preopenmarket_update()
    security_preopen.get_list_sec_id()
