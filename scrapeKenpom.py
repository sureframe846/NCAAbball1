
# coding: utf-8

# In[225]:


import numpy as np
import pandas as pandas
import requests
import sqlite3
from datetime import date

from bs4 import BeautifulSoup

def getArray(url): 
    page = requests.get(url)
    y = []
    soup1 = BeautifulSoup(page.content, 'html.parser')
    for tr in soup1.find_all('tr'):
        for td in tr.find_all('td'):
    
            y.append(td.get_text())
        
    games = np.array(y).reshape(int(len(y)/21),21)
    #print(games)
    return(games)
    

def makeDF(data):
    currentDate = date.today()
    columns = ['Rank','team','conf','w-l','adjEM','adjO','adjO_seed','adjD','adjD_seed','adjT','adjT_seed','luck','luck_seed','sched','sched_seed','OppO', 'OppO_seed','OppD','OppD_seed','ncadjEM','ncadjEM_seed']
    df = pandas.DataFrame(data, columns = columns)
    datevec = pandas.DataFrame([{'date': currentDate}] * len(df)) 
    df = df.join(datevec, how = 'left')
    return df


conn = sqlite3.connect('kenpom.db')
c = conn.cursor()
sqlcode = """
CREATE TABLE If NOT EXISTS STATS( 
    Rank int,
    team varchar(22),
    conf text,
    `w-l` text,
    adjEM real,
    adjO real,
    adjO_seed int,
    adjD real,
    adjD_seed int,
    adjT real,
    adjT_seed int,
    luck real,
    luck_seed int,
    sched real,
    sched_seed int,
    OppO real,
    OppO_seed int,
    OppD real,
    OppD_seed int,
    ncadjEM real,
    ncadjem_seed int,
    date date,
    PRIMARY KEY(team, date)
)
"""
#c.execute(sqlcode)    
    
games2020 = getArray("https://kenpom.com/index.php")
mydf = makeDF(games2020)
print(mydf)
mydf.to_sql('STATS', conn, if_exists = 'append', index = False)
mydf.to_csv('kenpom.csv', mode = 'a', header = False, index = False)