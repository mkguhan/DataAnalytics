from download_data import download_data_nse


class update_index_details:

    def __init__(self):
        self.index_file_path = "files/EQUITY_L.csv"

    def _download_index_details(self):
        index_list = download_data_nse._download_url_as_dataframe(self.index_file_path)
        return index_list



if __name__ == "__main__":
    update_index = update_index_details()
    print("Getting the list of stocks")
    all_index_list = update_index._download_index_details()
    print(all_index_list)
