import requests
import bs4
import os

domain = "http://www.hani.co.kr"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
next_url = "http://www.hani.co.kr/arti/cartoon/hanicartoon/home01.html=361102"

for i in range(5):
    url = next_url
    
    res = requests.get(url,headers=headers)
    html = bs4.BeautifulSoup(res.text, "html.parser")

    #next url
    next_url = html.select('div.paginate > a')
    next_url = domain + next_url[len(next_url) - 1].get('href')

    print(next_url)

    article = html.select(".article-photo img")
    print(len(article))
    #article
    for n in range(len(article)):
        fname = article[n].get('title')
        img_src = article[n].get('src')
        print(fname)

    res = requests.get(img_src)
    
    imageFile = open(fname + ".jpg", "wb")
    for j in res.iter_content(100000):
        imageFile.write(j)
    imageFile.close()
