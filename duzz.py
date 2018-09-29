import requests
import bs4
import os

url = 'http://bf.nexon.com/News/Webtoon/View/6?cp=1'
res = requests.get(url)
html = bs4.BeautifulSoup(res.text, 'html.parser')

img = html.select('div > img')[1]

n = str(img).count('/>')
img = str(img).replace('/>', '>', n)
img = img.replace('</img></img></img>', '', 1)

tag = bs4.BeautifulSoup(img, 'html.parser')
print(tag.select('img')[0].get('src'))
