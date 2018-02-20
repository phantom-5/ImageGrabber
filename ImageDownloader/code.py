import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000000000)
    full_name = str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)

print("1:Enter next URL")
print("2:Stop")

while(True):
    q=int(input())
    if q is 1:
        s=input()
        download_web_image(s)
    else :
        break

