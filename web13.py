import requests

from bs4 import BeautifulSoup

imd='https://www.gittigidiyor.com/televizyon'

r=requests.get(imd)

print(r.status_code)


soup=BeautifulSoup(r.text,'lxml')
#print(soup)

vr1=soup.find_all('h3',{'class':'medium'})




#for i in vr1:

    #print(i.string)

vrm = soup.find_all('li',{'data-testid':'pagination-list-item'})
for i in vrm:
    
     print(i.find('a').get('href'))  
     imx= i.find('a').get('href')
     imx
     m=requests.get(imx)
     pge=BeautifulSoup(m.text,'lxml')  
     vr2=pge.find_all('h3',{'class':'medium'})

     for s in vr2:
         print(s.string)

for y in range(2,30):
    imm='https://www.gittigidiyor.com/televizyon?sf='+str(y)
    print(imm)
    m=requests.get(imx)
    pge=BeautifulSoup(m.text,'lxml')  
    vr2=pge.find_all('h3',{'class':'medium'})

    for s in vr2:
         print(s.string)
halt




