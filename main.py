import requests 
import time 
 
def f(): 
    link="https://funpay.com/lots/raise" 
     
    headers = { 
        "Accept" : "application/json, text/javascript, */*; q=0.01", 
        "Accept-Encoding" : "gzip, deflate, br", 
        "Accept-Language" : "ru-RU,ru;q=0.9", 
        "Content-Length" : "64", 
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8", 
        "Cookie" : (
        "_ga=GA1.1.2134298177.1719245740; "
        "_ga_STVL2Q8BNQ=GS1.1.1728999348.114.1.1728999921.37.0.433156575; "
        "_gcl_au=1.1.18956329.1728999348; "
        "_ym_d=1719245733; "
        "_ym_isad=2; "
        "_ym_uid=1719245733282525695; "
        "fav_games=141-224-159-329-201-153-233-527-123-250; "
        "golden_key=be3x39urk8n1qpyjz0fotprh6kub7l7z; "
        "cookie_prefs=1; "
        "PHPSESSID=tva3ykDxRd4oMBtSkeLm%2CKRg3HwBxE6p"),
        "Origin" : "https://funpay.com", 
        "Referer" : "https://funpay.com/lots/401/trade", 
        "Sec-Ch-Ua" : '''"Google Chrome";v="110", "Chromium";v="110", "Not=A?Brand";v="24"''', 
        "Sec-Ch-Ua-Mobile" : "?0", 
        "Sec-Ch-Ua-Platform" : '''"Windows"''', 
        "Sec-Fetch-Dest" : "empty", 
        "Sec-Fetch-Mode" : "cors", 
        "Sec-Fetch-Site" : "same-origin", 
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", 
        "X-Requested-With" : "XMLHttpRequest" 
    } 
     
    data = { 
        "game_id" : "141", 
        "node_id" : "401", 
        "node_ids[]" : ["401", "925", "1155"]
    } 
     
    r = requests.post(link, data=data, headers=headers) 
      
    print(r.text) 
 
while(True): 
    f() 
    time.sleep(600)
