import requests
import pandas as pd

class download_data_nse:

    def __init__(self):
        self.url = "https://www.nseindia.com/"

    @staticmethod
    #download the data as Dataframe
    def _download_url_as_dataframe(url):
        read_csv = pd.read_csv(url)
        return read_csv

