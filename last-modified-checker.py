
#  Project: Webpage update checker
#  Version: 0.0.1
#  Description: This Script verify if a determined webpage has been modified.
#  Copyright(c) 2009-2020 Leandro Silva
#  License: GPL v3


import requests



url = 'https://www.saopaulo.sp.gov.br/ultimas-noticias/'


def saveLastModified(data):
    try:
        with open("last-modified.data", mode="w", encoding="utf-8") as f:
            f.write(data)
    except PermissionError as e:
           print(e)


def readLastModified():
    try:
        with open("last-modified.data", mode="r" ,encoding="utf-8") as f:
           return f.read()
    except FileNotFoundError as e:
           print(e)
           return 'Sat, 1 Mar 2020 12:56:12 GMT' 
    
        
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36', 
            'If-modified-Since' : readLastModified() }

r = requests.get(url, headers=headers )


if r.status_code == 200:

    saveLastModified(r.headers["Last-Modified"] )
    print("Saved: ", r.headers["Last-Modified"] )

else:
    print("[%d]: %s" % (r.status_code , r.reason) )   




