from download_data import download_data_nse
from database_update import update_stock_data_db
from datetime import datetime


class update_index_details:
    #self.index_column = ['id','code','name','description','listed_date','series','isin_number','facevalue','paidup_value','market_lot']
    def __init__(self):
        self.index_file_path = "files/EQUITY_L.csv"
        self.index_column = ['id', 'code', 'name', 'description', 'listed_date', 'series', 'isin_number', 'facevalue',
                             'paidup_value', 'market_lot']

    def _download_index_details(self):
        index_list = download_data_nse._download_url_as_dataframe(self.index_file_path)
        return index_list



if __name__ == "__main__":
    update_index = update_index_details()
    print("Getting the list of stocks")
    all_index_list = update_index._download_index_details()
    all_index_list = all_index_list.to_datetime(all_index_list['DATE OF LISTING'], format='%d-%m-%Y')
    all_index_list.index = all_index_list.index + 1
    all_index_list.columns = all_index_list.columns.str.replace(' ','_')
    all_index_list.columns = all_index_list.columns.str.lstrip('_')
    for row in all_index_list.iterrows():
        values = [row[0], row[1].SYMBOL, row[1].NAME_OF_COMPANY,' ',row[1].DATE_OF_LISTING.strftime("%d-%m-%Y"),row[1].SERIES,row[1].ISIN_NUMBER,row[1].FACE_VALUE,row[1].PAID_UP_VALUE,row[1].MARKET_LOT]
        print(update_index.index_column)
        print(values)
