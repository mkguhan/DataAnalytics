import requests
import pandas as pd

class download_data_nse:

    def __init__(self):
        self.url = ""

    @staticmethod
    #download the data as Dataframe
    def _download_url_as_dataframe(filename):
        print("reading CSV with pandas")
        read_csv = pd.read_csv(filename)
        return read_csv



