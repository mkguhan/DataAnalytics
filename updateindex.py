from download_data import download_data_nse


class update_index_details:

    def __init__(self):
        self.index = True
        self.url = "https://www.nseindia.com/api/allIndices?csv=true"

    def _download_index_details(self, url):
        index_list = download_data_nse._download_url_as_dataframe(url)
        return index_list




if __name__ == "__main__":
    update_index = update_index_details()
    all_index_list = update_index._download_index_details(update_index.url)
    print(all_index_list)
