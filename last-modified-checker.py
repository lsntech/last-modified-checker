import requests


url = 'https://www.saopaulo.sp.gov.br/ultimas-noticias/'


# refatorar e criar o arquivo .data caso nao exista.

def salveLastModified(data):
    with open("last-modified.data", mode="w", encoding="utf-8") as f:
        f.write(data)


def readLastModified():
    with open("last-modified.data", mode="r" ,encoding="utf-8") as f:
         return f.read()
     

print("lido: " , readLastModified())



headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36', 
            'If-modified-Since' : readLastModified()}

r = requests.get(url, headers=headers)


if r.status_code == 200:
    lastm = r.headers["Last-Modified"]
    salveLastModified(lastm)
    print("Salvo: ", lastm)

else:
    print("[%d]: Not Modified" % r.status_code)   




