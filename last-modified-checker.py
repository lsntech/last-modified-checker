
#  Project: Webpage update checker
#  Version: 0.0.1
#  Description: This Script verify if a determined website has been modified.
#  Copyright(c) 2009-2020 Leandro Silva
#  License: GPL v3


import requests



url = 'https://www.saopaulo.sp.gov.br/ultimas-noticias/'


def saveLastModified(data):
    with open("last-modified.data", mode="w", encoding="utf-8") as f:
        f.write(data)


def readLastModified():
    with open("last-modified.data", mode="r" ,encoding="utf-8") as f:
        return f.read()



# This header verifies if-modified-since 
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36', 
            'If-modified-Since' : readLastModified() }

r = requests.get(url, headers=headers )


if r.status_code == 200:

    saveLastModified(r.headers["Last-Modified"] )
    print("Salvo: ", r.headers["Last-Modified"] )

else:
    print("[%d]: Not Modified" % r.status_code )   




