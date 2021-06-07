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
            'authority': 'www.nseindia.com',
            'sec-ch-ua': '^\\^',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market',
            'accept-language': 'en-US,en;q=0.9,ta;q=0.8',
            'cookie': '_ga=GA1.2.2114335903.1623010131; nsit=LM_s5B5Pxxrhpxs5qQP5ZsBM; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTYyMzA5OTM0OSwiZXhwIjoxNjIzMTAyOTQ5fQ.SjVeKjVq774uQ0T_9oPR7jWdd4_z5Jd0ywpURGMF1P4; ak_bmsc=DBF3A76938627955CD7578214F179DFF17411D5CF8370000D687BE607DF9881E~pl57VphcJXelh6M8CBYukhH7RopCHtWDn10jD8CsHuPpkNmN4dcueAZ8xnzV/9vgucl2VSLyPXI+vnot1V9mtShFuJUwU6RrgmXr6jvD3yR1YEHZeA1Pt0KzIAR/pyyGpw6jg8E+2JZSniYKZrgBZxgG8xJyZSm2d+vgolSw+FTNIneC3+2ijDsuzLarhz/CgvWraAqU9iz0GYfEepfu8F95Gcnaarsb3ZaDtczBXlnvMF1uAmbFxemsn2qH/PCsa3; _gid=GA1.2.1826450012.1623099356; _gat_UA-143761337-1=1; bm_sv=9676BB37DE7EF72CAC8218FF9555A5DB~ilNPxfom/UIwybJih84yS4+g62kBkgHUplwjWlmfguOhK4e6gcWpLxUksmh3GA80YRzudLSdYNNDmYd0V8V/9eWPiM915OA0U9dEcZMEiCDDKc4GGRiOK7HNwfBYiHgccpl3iezsZvBgJaJSo7MSjof9cFOyOmmQl83MRZA6yBU=; RT=^\\^z=1&dm=nseindia.com&si=1af3cd12-c48e-4602-b30a-cb3412152702&ss=kpn3g31p&sl=0&tt=0&bcn=^%^2F^%^2F1737ad5c.akstat.io^%^2F&ld=1h48to&nu=ed8553192c8d124be55949cc1b2e99dc&cl=jhv^\\^',
        }

        params = (
            ('key', 'NIFTY'),
            ('csv', 'true'),
        )

        response = requests.get('https://www.nseindia.com/api/market-data-pre-open', headers=headers, params=params)
        print(response.text.splitlines()[10:])

if __name__ == "__main__":
    security_preopen = preopenmarket_update()
    security_preopen.get_list_sec_id()
    security_preopen.download_preopendata()
