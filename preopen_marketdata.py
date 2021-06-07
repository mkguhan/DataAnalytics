from  database_update import  update_stock_data_db
import  requests

class preopenmarket_update:

    def __init__(self):
        pass


    def get_list_sec_id(self):
        list = update_stock_data_db.get_security_id_list()
        print(list)

    def download_preopendata(self):
        url = "https://www.nseindia.com/api/market-data-pre-open?key=NIFTY&csv=true"
        headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,ta;q=0.8",
            "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-requested-with": "XMLHttpRequest",
            "referrer": "https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market",
            "referrerPolicy": "strict-origin-when-cross-origin",
            "method": "GET",
            "mode": "cors",
            "credentials": "include"
        }
        data = requests.get(url, headers=headers)
        print(data)




if __name__ == "__main__":
    security_preopen = preopenmarket_update()
    security_preopen.get_list_sec_id()
    security_preopen.download_preopendata()
