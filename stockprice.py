import requests
from bs4 import BeautifulSoup
import csv

def parseprice():
    req=requests.get('https://in.finance.yahoo.com/quote/%5EBSESN?p=^BSESN')
    soup=BeautifulSoup(req.text,'lxml')
    price=soup.find('div',{'class':'D(ib) Mend(20px)'}).findAll('span')
    return price[0].text 

while True:
    print('th current price: '+str(parseprice()))   

file=csv.writer(open("output.csv","w"))
file.writerow([parseprice])