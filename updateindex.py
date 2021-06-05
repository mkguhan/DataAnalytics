from download_data import download_data_nse


class update_index_details:

    def __init__(self):
        self.index = True
        self.url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"

    def _download_index_details(self, url):
        download_csv = download_data_nse._download_url(url)
        index_list = download_data_nse._download_url_as_dataframe(download_csv)
        return index_list




if __name__ == "__main__":
    update_index = update_index_details()
    print("Getting the list of stocks")
    all_index_list = update_index._download_index_details(update_index.url)
    print(all_index_list)
