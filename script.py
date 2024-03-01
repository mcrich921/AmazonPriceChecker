import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

headers = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

url = 'https://www.amazon.com/Quest-Tortilla-Protein-Variety-Cheese/dp/B09GLBLPYG/ref=sr_1_6_pp?crid=8QNIVX5L74NP&dib=eyJ2IjoiMSJ9.jUMbpb71zQwn11sSe_fcd5oCNElnfPE-4cw1R_PYntyHnz21fnU-UFQ4tHRwEHDyFTTBdjeAFQ_3XsroRBcw4_YzsdrnehakzBfQzaeMU0X6dut2Fou8H2Ffss5QUK3iZyzclknsjvkNMw8ds49HaOJ5NS1_utJxkMh-zdkb3ZZSVOOwnce4-D94O6ahqE7rgyZvS41UVYGJPo9jG0RPDdrBdJFhYu8x6t2I9y87VWmZiDGjEJKzks9SZ5fwe2q8hze-X9UnlM2F7ZGbHIwIqoTWs9AXivf3ujNmIEWBb90.pA2B7N2aBejyzUGv5qOHVjYegZ_YHC1pynL8NmEwxj8&dib_tag=se&keywords=quest+chips&qid=1708290262&rdc=1&sprefix=quest+chips%2Caps%2C171&sr=8-6'
url2 = 'https://www.amazon.com/Quest-Nutrition-Tortilla-Protein-Cheese/dp/B07RRRV5CT/ref=sr_1_5_pp?crid=37SFU4JVWDZHX&dib=eyJ2IjoiMSJ9.jUMbpb71zQwn11sSe_fcd5oCNElnfPE-4cw1R_PYntyHnz21fnU-UFQ4tHRwEHDyFTTBdjeAFQ_3XsroRBcw4_YzsdrnehakzBfQzaeMU0X6dut2Fou8H2Ffss5QUK3iZyzclknsjvkNMw8ds49HaOJ5NS1_utJxkMh-zdkb3ZZ5Mbc3mugXlbMkyBZvIpOvgyZvS41UVYGJPo9jG0RPDdrBdJFhYu8x6t2I9y87VWmZiDGjEJKzks9SZ5fwe2q8hze-X9UnlM2F7ZGbHIwIqoTWs9AXivf3ujNmIEWBb90.Q03oBJC4mtkvsETF6KxTkPjtrcFxqlvomXwZ48wrj4Q&dib_tag=se&keywords=quest+chips&qid=1708291948&sprefix=quest+chip%2Caps%2C137&sr=8-5'

def getPrice():
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.content, "html.parser")
    price = soup.find('span', attrs={'class':'a-offscreen'}).get_text()[1:]

    print(price)

getPrice()