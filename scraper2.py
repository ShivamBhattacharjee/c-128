import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(start_url)
#print(page)
time.sleep(10)
    
soup = BeautifulSoup(page.text , "html.parser")
starTable = soup.find_all("table")

#print(starTable)

temp_list = []
tableRows = starTable[3].find_all("tr")

for tr in tableRows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

starNames = []
distance = []
mass = []
radius = []

for i in range(1 , len(temp_list)):
    starNames.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][8])
    radius.append(temp_list[i][9])

df = pd.DataFrame(list(zip(starNames , distance , mass , radius)) , columns = ["Star Name" , "Distance" , "Mass" , "Radius"])

print(df)
df.to_csv("Stars2.csv")