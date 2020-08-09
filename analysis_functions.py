#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



    

data = pd.read_excel('Data/A_new.xlsx')

data.dropna(inplace = True)

def __init__(self,window):
    self.box=Entry(window)
    self.button=Button(window,text="check",command=self.plot)
    self.box.pack()
    self.button.pack()

#A
def getTotalAreaSoldVsLeased(year):
    year_data = data[data['Year'] == year]
    owned = data[data['Year']==year ]
    owned = owned[owned['Tenure'] == 'Owned']
    area_owned = sum(owned['Area'])
    leased = data[data['Year']==year ]
    leased = leased[leased['Tenure'] == 'Leased']
    area_leased = sum(leased['Area'])
    sns.countplot(x='Tenure',data=year_data,palette='Set1')
    
    return area_owned, area_leased
    plt.show()
    plt.gcf().canvas.draw()
    fig=plt.figure()
    canvas=FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=1,column=24)
    canvas.draw()

# own_area, leas_area = getTotalAreaSoldVsLeased(2019)
#
# print('The total property area sold in Sq-M is ',own_area)
# print('The total property area leased in Sq-M is ',leas_area)

#B
def yeargotmaximumleasedareainCAandWScountries(year):
    leased_data = data[data["Tenure"] == "Leased"]
    CA = leased_data[leased_data["Country"] == "CA"]
    WS = leased_data[leased_data["Country"] == "WS"]
    CA_YEAR = CA[CA["Year"] == year]
    WS_YEAR = WS[WS["Year"] == year]
    ca_max_leased_area = sum(CA_YEAR["Area"])
    ws_max_leased_area = sum(WS_YEAR["Area"])
    return ("CA",ca_max_leased_area),("WS", ws_max_leased_area)
   


#year = int(input("Enter the year: "))
#country1,country2 = yeargotmaximumleasedareainCAandWScountries(year)
#print(country1, "has the maximum leased area in the",year)
#print(country2, "has the maximum leased area in the",year)
# data["Agent"].value_counts().to_dict()
# data[data["Tenure"] == "Leased" and data["Year"] == 2017]

#C
def agentcode(year):
    agent_data = data[data["Tenure"] == "Owned"]
    agent_data = agent_data[agent_data["Year"] == year]
    return agent_data["Identifier"].unique().tolist(), agent_data["Agent"].unique().tolist()

# year = int(input("Enter the year: "))
# identifier, agents = agentcode(year)
# print("Identifiers = ", identifier)
# print("Agents = ", agents)

#D
def maxleasedagent(year):
    leased_data = data[data["Tenure"] == "Leased"]
    leased_data = leased_data[leased_data["Year"] == year]
    leased_data = leased_data[leased_data["City"] == "Chilliwack"]
    agent_dict = leased_data["Agent"].value_counts().to_dict()
#     print(agent_dict)
    required_agent = max(agent_dict, key=agent_dict.get)
    return required_agent

# year = int(input("Enter the year: "))
# agent = maxleasedagent(year)
# print(agent,"agent has got the maximum deals in leased form. ")

# leased_data = data[data["Tenure"] == "Leased"]
# leased_data = leased_data[leased_data["Year"] == 2018]
# leased_data = leased_data[leased_data["City"] == "Chilliwack"]
    
#E
    
agent_list_dict = data['Agent'].value_counts().to_dict()
    
agent_list = []
for k in agent_list_dict:
    agent_list.append(k)
agent_list

def get_agent(year):
    area_owned_agent={}
    area_leased_agent={}
    year_data = data[data['Year']==year]
    for agent in agent_list:
        agent_data = year_data[year_data['Agent']==agent]
        owned_area_data = agent_data[agent_data['Tenure'] == 'Owned']
        leased_area_data = agent_data[agent_data['Tenure'] == 'Leased']
        area_owned_agent[agent] = round(sum(owned_area_data['Area']),2)
        area_leased_agent[agent] = round(sum(leased_area_data['Area']),2)
    return area_owned_agent, area_leased_agent

#owned_agent_list, leased_agent_list = get_agent(2017)
# plt.hist(owned_agent_list.keys(), owned_agent_list.values(), color='g', label = "Real distribution")
# plt.show()
#print(owned_agent_list)
#print(leased_agent_list)
#keys = owned_agent_list.keys()
#vals = owned_agent_list.values()
#plt.figure(figsize=(14, 6), dpi= 80, facecolor='w', edgecolor='k')
#plt.bar(keys, vals, label="Distrinution")

#plt.ylim(0,max(vals))
#plt.ylabel ('Area Sold (sq.meter)')
#plt.xlabel ('Agents')
#plt.xticks(list(keys))
#plt.legend (bbox_to_anchor=(1, 1), loc="upper right", borderaxespad=0.)

#F
def propertysoldforjuly():
    
    owned =data[data["Tenure"] == "Owned"]
    area_owned = sum(owned['Area'])
    return area_owned

#year = int(input("Enter the year: "))
#propertyareasold= propertysoldforjuly()
#print("The amount of property area sold for the month of july is",propertyareasold,"sq.m in the year",year)
    
#G
#x=data[['Year']]
#datatoplot=data[['Area']]
#plt.plot(x,datatoplot)
