import requests
from bs4 import BeautifulSoup

url = 'https://www.mtu.edu/cs/graduate/computer-science/'

def getandsave(url,path):
    r= requests.get(url)
    with open(path,'w')as f:
        f.write(r.text)
        
getandsave(url,'data/index.html')

with open ('data/index.html','r')as f:
        doc = f.read()
    
soup = BeautifulSoup (doc,'html.parser')

print(soup.title.get_text())

data = soup.get_text()

print(type(data))

print(data)

with open('hello.txt' , 'w') as f:
    f.write(data)

