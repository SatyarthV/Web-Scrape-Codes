# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup as Soup
from selenium import webdriver
import time
from urllib.request import urlopen as uReq
import urllib.request
import pandas as pd
from twilio.rest import Client


driver = webdriver.Chrome(executable_path = '/home/satyarthvaidya/Downloads/chromedriver')
# Your Account SID from twilio.com/console
#final=[]

for pg in range(23,29):

    try:
        final = []
#        
    
#        client = Client(account_sid, auth_token)
        print("DATE : " + str(pg) + " AUGUST" + "\n")
        my_Url = driver.get('https://www.makemytrip.com/air/search?tripType=O&itinerary=BOM-DXB-D-' +str(pg)+'Aug2017&paxType=A-1-C-0-I-0&cabinClass=E')
        #my_Url = driver.get('https://www.makemytrip.com/air/search?tripType=O&itinerary=BOM-DXB-D-19Aug2017&paxType=A-1-C-0-I-0&cabinClass=E')
    
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
               match=True
        
        my_Url = 'https://www.makemytrip.com/air/search?tripType=O&itinerary=BOM-DXB-D-19Aug2017&paxType=A-1-C-0-I-0&cabinClass=E'
        tmp = urllib.request.Request(my_Url)
        uClient = uReq(tmp)
        #time.sleep(120)
        page_html = uClient.read()
        uClient.close()
        
    #    page_soup_ = Soup(page_html,"html.parser")
        
        html_source = driver.page_source
        page_soup = Soup(html_source,"html.parser")    
        
        price =page_soup.findAll("div",{"class":"pull-left price"})
        airlines = page_soup.findAll("div",{"class":"pull-left airways-name-section"})
        depttime = page_soup.findAll("span",{"class":"dept-time"})
        
        #for l in price,airlines:
        for (l,a,d) in zip(airlines,price,depttime):
            sprice = a.findAll('span')
    #        print("AIRLINES : " + l.p.text + " - PRICE : " + sprice[2].text + " - TIME : " + d.text)
    #        final.append({})
            final.append({"AIRLINES":l.p.text,"PRICE:":sprice[2].text,"TIME":d.text})
        print(final[0])
#        message = client.messages.create(
#        to="+918369857961", 
#        from_="13072985798",
#        body=" " +  final[0]['AIRLINES'])
#
#    print("AIRLINES : " + l.p.text + " - PRICE : " + sprice[2].text + " - TIME : " + d.text)#    print(l.p.text + "\n")
#    print("\n")
    except Exception as e:
        print(str(e))
        pass
pd.DataFrame.from_dict(final).to_csv('Flights.csv')





