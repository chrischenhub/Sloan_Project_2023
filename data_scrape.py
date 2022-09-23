# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:51:05 2022

@author: Chris
"""

'''This is the example scraping process in our dataframe, more data will be updated
when all data are sracped
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "https://www.basketball-reference.com/players/d/duranke01.html#all_per_game-playoffs_per_game"
html = urlopen(url)
soup = BeautifulSoup(html, features="lxml")
headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
rows = soup.findAll('tr')[2:]
rows_data = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]

print(rows_data)

url1 = "https://www.basketball-reference.com/leagues/NBA_2022_per_game.html"
html1 = urlopen(url1)
soup1 = BeautifulSoup(html1, features="lxml")
headers1 = [th.getText() for th in soup1.findAll('tr', limit=2)[0].findAll('th')]
rows1 = soup1.findAll('tr')[1:]
rows_data1 = [[td.getText() for td in rows1[i].findAll('td')] for i in range(len(rows1))]
season = pd.DataFrame(rows_data1, columns = headers1[1:])
season.head()
pts = season['PTS']
print(pts)

pts.describe()

#drop none
ptsd = []
for val in pts:
    if val != None :
        ptsd.append(val)

#convert str to float
new_list = [float(i) for i in ptsd]

#finish the cleaning and put it in the final dataframe
newdf = pd.DataFrame(data=new_list)
                     
            
     
