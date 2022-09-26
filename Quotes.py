import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

all_quotes = []
for i in range(1, 11):
    url = f'https://quotes.toscrape.com/'
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text

        single_quote = [text, author]
        all_quotes.append(single_quote)

df = pd.DataFrame(all_quotes, columns=['quote', 'author'])
df.to_csv('quotes.csv', index=False)
