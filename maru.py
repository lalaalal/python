import requests
import bs4
import os

def dl_file(res, fname, ftype):
    file = open(fname + ftype, "wb")
    for bundle in res.iter_content(100000):
        file.write(bundle)
    
title = '우마루_'

wasabi_domain = "http://wasabisyrup.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.100 Safari/537.36', 'Referer' : 'http://wasabisyrup.com'}
wasabi_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.100 Safari/537.36', 'Referer' : 'http://wasabisyrup.com'}
next_url = "http://wasabisyrup.com/archives/93"

page_url = ''
#for i in range(5):
while next_url != page_url:
    page_url = next_url
    
    episode = requests.get(page_url, headers = headers)
    episode_html = bs4.BeautifulSoup(episode.text, "html.parser")

    title = episode_html.select('.title-subject')
    no = episode_html.select('.title-no')
    print(title[0].text + "_" + no[0].text)

    img = episode_html.select('.gallery-template > img')
    for nth_img in range(len(img)):
        img_url = wasabi_domain + img[nth_img].get('src')
        img_res = requests.get(img_url, headers = wasabi_headers)
        print(img_res)

    url_path = episode_html.select('.nav-right > a')
    if url_path[0].get('href') != None:
        next_url = wasabi_domain + url_path[0].get('href')
        
