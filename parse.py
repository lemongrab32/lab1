from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

ua = UserAgent()

headers = {
    "User-Agent": ua.chrome,
    
}

def parse():
    url = 'https://auto.drom.ru/'
    page = requests.get(url, headers=headers)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")

    block = soup.find_all('div', class_="css-17lk78h e3f4v4l2")
    description = []
    for data in block:
        if data.find_all("span"):
            description.append(data.text)

    #print(block[0])


    f = open('auto.txt', 'w')
    for a in description:
        f.write(a)
        f.write("\n")
    f.close()