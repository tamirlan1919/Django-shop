import requests
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today()
today = today.strftime('%d/%m/%Y')

payload = {'data_req':today}
print(today)
url = 'https://www.cbr.ru/scripts/XML_daily.asp?'
date = 'date_req=02/03/2002'
responce = requests.get(url,params=payload)

xml = BeautifulSoup(responce.content,'lxml')

def getCource(id):
    return xml.find('valute',{'id':id}).value.text

print(getCource('R01235'),'рублей за 1 dollar')
print(getCource('R01239'),'рублей за 1 euro')
print(getCource('R01010'),'рублей за 1 aud')