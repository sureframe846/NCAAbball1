
# coding: utf-8

# In[144]:


import pandas as pandas
import numpy as np
from bs4 import BeautifulSoup
import requests

def getSchedule():
    url = "https://www.sports-reference.com/cbb/boxscores/index.cgi?month=12&day=6&year=2019"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    myList = []
    
    for tr in soup.find_all('tr'):
        for td in tr.find_all('td'):
            
            if(td.a):
                #print(td.a.string)
                myList.append(td.a.string)
                continue
            #print(td.contents[0])
            myList.append(td.contents[0])    
    
    while "Final" in myList:
        myList.remove("Final")
    while "" in myList:
        myList.remove("")
    while "\xa0\n\t\t\t" in myList:
        myList.remove("\xa0\n\t\t\t")
    
    #print(myList)
    
    todaysGames = np.array(myList).reshape(int(len(myList)/4), 4)
    #a = np.array(todaysGames[:,1] > todaysGames[:,3])
    winner = []
    for game in todaysGames:
        if(game[1] > game[3]):
            winner.append(game[0])
            continue
        winner.append(game[2])
    #print(winner)
    todaysGames = np.column_stack((todaysGames,np.array(winner)))
    print("[Team 1            Team 2             Winner]")
    print(todaysGames)
    
getSchedule()

