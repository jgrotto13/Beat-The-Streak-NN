# -*- coding: utf-8 -*-
from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
#***************SCRAPING*********************
url = "https://www.rotowire.com/baseball/matchup.htm"
html = urlopen(url)
soup = BeautifulSoup(html)
type(soup)
column_headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
column_headers
data_rows = soup.findAll('tr')[2:27]
type(data_rows)
player_data = [[td.getText() for td in data_rows[i].findAll('td')]
            for i in range(len(data_rows))]
                
player_data_02 = []  #create an empty list to hold all the data

for i in range(len(data_rows)):  #for each table row
    player_row = []  #create an empty list for each matchup

    #for each table data element from each table row
    for td in data_rows[i].findAll('td'):
        #get the text content and append to the matchup_row 
        player_row.append(td.getText())

    #then append each matchup to the matchup_data matrix
    player_data_02.append(player_row)
    
player_data == player_data_02
df = pd.DataFrame(player_data, columns=column_headers)

#****************CLEANING********************
df[df['Batter'].isnull()]
df = df[df.Batter.notnull()]

df.drop('Pos', axis='columns', inplace=True)
df.drop('Team', axis='columns', inplace=True)
df.drop('Home?', axis='columns', inplace=True)
df.drop('Game Date', axis='columns', inplace=True)
df.drop('Opp', axis='columns', inplace=True)

df.to_csv("BatterMatchupData.csv")
#**********END TEST**************************
