import requests
import bs4
import os

def dl_file(res, fname, ftype):
    file = open(fname + "." + ftype, "wb")
    for bundle in res.iter_content(100000):
        file.write(bundle)

def mkdir(dname):
    try:
        if not(os.path.isdir(dname)):
            os.makedirs(os.path.join(dname))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

path = input('Input Path (Default = C:/Temp) : ')
if path is "":
    path = "C:/Temp"

next_url = input('Input url (Default = http://wasabisyrup.com/archives/93) : ')
if next_url is "":
    next_url = "http://wasabisyrup.com/archives/93"

digit = input('Last Episode (Default = 999) : ')
if digit is "":
    digit = "999"

wasabi_domain = "http://wasabisyrup.com"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.100 Safari/537.36'}
wasabi_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.100 Safari/537.36', 'Referer' : 'http://wasabisyrup.com'}

page_url = ''

while next_url != page_url:
    os.chdir(path)
    page_url = next_url

    episode = requests.get(page_url, headers = headers)
    episode_html = bs4.BeautifulSoup(episode.text, "html.parser")

    title = episode_html.select('.title-subject')[0].text
    no = episode_html.select('.title-no')[0].text
    no = no.zfill(len(digit) + 1)

    mkdir(title)
    os.chdir('./' + title)

    mkdir(no)
    os.chdir('./' + no)
    img = episode_html.select('.gallery-template > img')
    print(title + " " + no, end = ' ', flush = True)
    for nth_img in range(len(img)):
        img_url = wasabi_domain + img[nth_img].get('data-src')
        img_res = requests.get(img_url, headers = wasabi_headers)
        fname = str(nth_img + 1).zfill(len(str(len(img))))
        dl_file(img_res, fname, ftype = 'jpg')

        if nth_img is 0:
            n_dot = 0
        for i in range(int(nth_img / len(img) * 10) - n_dot):
            print('.', end = '', flush = True)
            n_dot += int(nth_img / len(img) * 10)
    print('[Done]')

    url_path = episode_html.select('.nav-right > a')
    if url_path[0].get('href') != None:
        next_url = wasabi_domain + url_path[0].get('href')
