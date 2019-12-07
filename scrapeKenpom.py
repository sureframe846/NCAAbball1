
# coding: utf-8

# In[225]:


import numpy as np
import pandas as pandas
import requests
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
    columns = ['Rk','Team','Conf','W-L','AdjEM','AdjO','AdjO seed','AdjD','AdjD seed','AdjT','AdjT seed','Luck','Luck seed','AdjEM','AdjEM seed','OppO', 'OppO seed','OppD','OppD seed','AdjEM','AdjEM seed']
    df = pandas.DataFrame(data, columns = columns)
    return df
    
    
    
games2020 = getArray("https://kenpom.com/index.php")
mydf = makeDF(games2020)
print(mydf)

