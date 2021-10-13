from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
headers = {
    "Accept" : "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
}

shIT = requests.get(url, headers=headers)
soup = BeautifulSoup(shIT.text, 'html.parser')
print(soup)

crypto_code = soup.find('table', class_='h7vnx2-2').find('tbody').find('tr').find('td').find('p', class_='sc-16r8icm-0 iworPT')
print(crypto_code)
