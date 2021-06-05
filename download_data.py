import requests
import pandas as pd

class download_data_nse:

    def __init__(self):
        self.url = "https://www.nseindia.com/"

    @staticmethod
    #download the data as Dataframe
    def _download_url_as_dataframe(filename):
        print("reading CSV with pandas")
        read_csv = pd.read_csv(filename)
        return read_csv


    @staticmethod
    def _download_url(url):
        print("Download url")
        req = requests.get(url)
        url_content = req.content
        csv_file = open('index_list.csv', 'wb')
        file_name = "index_list.csv"
        csv_file.write(url_content)
        csv_file.close()
        return file_name

