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

path = input('Input Path (Default = /home/lalaalal/Downloads) : ')
if path is "":
    path = "/home/lalaalal/Downloads"

list_url = input('Input url (Default = https://ani24joa.com/ani_list/109.html) : ')
if list_url is "":
    list_url = "https://ani24joa.com/ani_list/109.html"

os.chdir(path)

#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.100 Safari/537.36'}

url_head = ["http://vxzgfwfsafg.site/video0/id_", "http://aaazxvhrgwed.aaazxvhrgwed.life/video0/id_", "http://cbhegds.online/new/id_"]
url_tail = [".ewqta", ".dsgewy", ".png"]

res = requests.get(list_url)
html = bs4.BeautifulSoup(res.text, "html.parser")

page_list = html.select('.list_name > a')
title = html.select('h1')[0].text
print(title)

info = html.select(".ani_info_right_box > div > span")

n_epi = len(page_list)

mkdir(title)
os.chdir(title)
for i in range(n_epi):

    page_url = page_list[n_epi - 1 - i].get("href")
    no = str(i + 1).zfill(len(str(n_epi))) + "화"
    video_num = page_url[page_url.rfind('/') + 1:page_url.find('.html')]

    for j in range(len(url_head)):
        dl_url = url_head[j] + video_num + url_tail[j]

        print(dl_url)
        print(no, end = " . . . ",flush = True)

        video = requests.get(dl_url)
        print(video)
        if video.status_code != 404:
            break;

    fname = title + " " + no

    dl_file(video, fname, ftype = "mp4")
