import requests
import os
import re

FTYPE = "mp4"

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

path    = input("PATH   : ")
title   = input("Title  : ")
head    = input("Head   : ")
tail    = input("Tail   : ")
m       = input("First  : ")
n       = input("Last   : ")
more    = input("More   : ")
option  = input("Option : ")

if path == "":
    path = "/home/lalaalal/Videos"

if tail == "":
    tail = ".moe"

mkdir(path + '/' + title)
os.chdir(path + '/' + title)

print("\n[Start Downloading]\n")
for i in range(int(m), int(n) + 1):
    if option.find("z") == 0:
        req_url = head + i + tail
    else:
        req_url = head + "%02d"%i + tail

    print("[%02d] "%i + title, end = ' ', flush = True)
    res = requests.get(req_url)
    print("<%d>"%res.status_code)

    if (res.status_code != 200) and (int(n) == i):
        req_url = head + "%02d"%i + " END" + tail
        print("[%02d]"%i + title)
        res = requests.get(req_url)

    dl_file(res, "[%02d] "%i + title, FTYPE)

addition = re.findall("([a-zA-Z]+);", more)

for i in addition:
    print("\n[Checking %s]\n"%i)

    print("[%s]"%i + title, end = ' ', flush = True)
    req_url = head + i + tail
    res = requests.get(req_url)
    print("<%d>\n"%res.status_code)

    if res.status_code == 200:
        dl_file(res, "[%s] "%i + title, FTYPE)
        continue

    j = 1
    while True:
        print("[%s %d] "%(i, j) + title, end = ' ', flush = True)
        req_url = head + "%s%d"%(i, j) + tail
        res = requests.get(req_url)
        print("<%d>"%res.status_code)

        if res.status_code != 200:
            break
        else:
            dl_file(res, "[%s %d] "%(i, j) + title, FTYPE)

        j += 1

print("\nDone!")
