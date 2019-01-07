import requests
import bs4
import os
import re

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

path = input("PATH: ")
if path is "":
    path = "/home/lalaalal/Videos"

title = input("Title: ")
head = input("Head: ")
tail = input("Tail: ")

mkdir(path + '/' + title)
os.chdir(path + '/' + title)

m = input("First: ")
n = input("Last : ")

for i in range(int(m), int(n) + 1):
    req_url = head + "%02d"%i + tail
    print("[%02d] "%i + title, end = ' ', flush = True)
    res = requests.get(req_url)
    print(res.status_code)

    if (res.status_code != 200) and (int(n) == i):
        req_url = head + "%02d"%i + " END" + tail
        print("[%02d]"%i + title)
        res = requests.get(req_url)

    dl_file(res, "[%02d] "%i + title, ftype = "mp4")

print("Checking OVA...")
req_url = head + "OVA" + tail
res = requests.get(req_url)
if res.status_code == 200:
    print("[OVA]" + title, end = ' ', flush = True)
    dl_file(res, "[OVA] " + title, ftype = "mp4")

i = 1
print("[OVA %d] "%i + title, end = ' ', flush = True)
req_url = head + "OVA%d"%i + tail
res = requests.get(req_url)
print(res.status_code)

while res.status_code == 200:
    print(res.status_code)
    dl_file(res, "[OVA %d] "%i + title, ftype = "mp4")

    i += 1

    print("[OVA %d] "%i + title, end = ' ', flush = True)
    req_url = head + "OVA%d"%i + tail
    res = requests.get(req_url)

print("\nDone!")
