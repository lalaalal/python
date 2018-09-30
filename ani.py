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

url_head = "http://vxzgfwfsafg.site/video0/id_"
url_tail = ".ewqta"

url = "https://ani24joa.com/ani_view/1872.html"

res = requests.get(url)
video_num = url[url.rfind('/') + 1:url.find('.html')]
dl_url = url_head + video_num + url_tail
print(dl_url)

video = requests.get(dl_url)
print(video)

os.chdir("/home/lalaalal/Downloads")

dl_file(video, fname = "umr", ftype = ".mp4")
