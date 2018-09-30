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

list_url = input('Input url (Default = https://ani24joa.com/ani_list/109.html) : ')
if list_url is "":
    list_url = "https://ani24joa.com/ani_list/109.html"

digit = input('Last Episode (Default = 999) : ')
if digit is "":
    digit = "999"

os.chdir(path)

url_head = "http://vxzgfwfsafg.site/video0/id_"
url_tail = ".ewqta"

list_url = "https://ani24joa.com/ani_list/109.html"

res = requests.get(list_url)
html = bs4.BeautifulSoup(res.text, "html.parser")

page_list = html.select('.list_name > a')
title = html.select('h1')[0].text
print(title)

mkdir(title)
os.chdir(title)
for i in range(len(page_list)):

    page_url = page_list[11 - i].get("href")
    no = str(i + 1).zfill(len(digit)) + "화"
    print(no, end = " . . . ",flush = True)

    video_num = page_url[page_url.rfind('/') + 1:page_url.find('.html')]
    dl_url = url_head + video_num + url_tail

    video = requests.get(dl_url)
    print(video)

    fname = title + " " + no

    dl_file(video, fname, ftype = "mp4")
