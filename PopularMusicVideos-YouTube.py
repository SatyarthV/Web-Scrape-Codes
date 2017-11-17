#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 23:00:27 2017

@author: satyarthvaidya
"""

from bs4 import BeautifulSoup as Soup
from selenium import webdriver
import time
from urllib.request import urlopen as uReq
import urllib.request
import pandas as pd

driver = webdriver.Chrome(executable_path = '/home/satyarthvaidya/Downloads/chromedriver')

my_Url = driver.get('https://www.youtube.com/watch?v=3tmd-ClpJxA&list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI')

my_Url = "https://www.youtube.com/watch?v=3tmd-ClpJxA&list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI"
tmp = urllib.request.Request(my_Url)
uClient = uReq(tmp)
#time.sleep(120)
page_html = uClient.read()
uClient.close()


html_source = driver.page_source
page_soup = Soup(html_source,"html.parser")    

link = page_soup.findAll("a",{"class":"style-scope ytd-playlist-panel-video-renderer"})

for i in len(link):
    print(link[i]['href'])
    
    
    
    
#price =page_soup.findAll("div",{"class":"pull-left price"})
#airlines = page_soup.findAll("div",{"class":"pull-left airways-name-section"})
#depttime = page_soup.findAll("span",{"class":"dept-time"})









##RANDOM CRAP BELOW


<a is="yt-endpoint" class="style-scope ytd-playlist-panel-video-renderer" href="/watch?v=3tmd-ClpJxA&amp;index=1&amp;list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI">
      <div id="container" class="style-scope ytd-playlist-panel-video-renderer">
        <span id="index" class="style-scope ytd-playlist-panel-video-renderer">▶</span>
        <div id="thumbnail-container" class="style-scope ytd-playlist-panel-video-renderer">
          <yt-img-shadow width="100" class="style-scope ytd-playlist-panel-video-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" width="100" src="https://i.ytimg.com/vi/3tmd-ClpJxA/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&amp;rs=AOn4CLAdFrZi975hkMaE-j1Eti6N4kQbsg"></yt-img-shadow>
        </div>
        <div id="meta" class="style-scope ytd-playlist-panel-video-renderer">
          <yt-formatted-string id="unplayableText" no-endpoints="" class="style-scope ytd-playlist-panel-video-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string>
          <h4 class="style-scope ytd-playlist-panel-video-renderer">
            <ytd-badge-supported-renderer class="style-scope ytd-playlist-panel-video-renderer" disable-upgrade="">
            </ytd-badge-supported-renderer>
            <span id="video-title" class="style-scope ytd-playlist-panel-video-renderer" title="Taylor Swift - Look What You Made Me Do">
              Taylor Swift - Look What You Made Me Do
            </span>
          </h4>
          <div id="byline-containerz" class="style-scope ytd-playlist-panel-video-renderer">
            <span id="byline" class="style-scope ytd-playlist-panel-video-renderer">TaylorSwiftVEVO</span>
            <ytd-badge-supported-renderer class="style-scope ytd-playlist-panel-video-renderer" disable-upgrade="">
            </ytd-badge-supported-renderer>
          </div>
        </div>
      </div>
    </a>






















