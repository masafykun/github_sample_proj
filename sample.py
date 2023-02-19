import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def main():
    url = "https://news.yahoo.co.jp/" 
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    rs = soup.find_all(href=re.compile('news.yahoo.co.jp/pickup'))
    df = pd.DataFrame(index=[], columns=['text', 'link'])
    for i in rs:
        text = i.getText()
        link = i.attrs['href']
        index = pd.Series([text, link], index=df.columns)
        df = pd.concat([df, index.to_frame().T], ignore_index=True)
        #更新されていない？
    print(df)

if __name__=="__main__":
    main()
