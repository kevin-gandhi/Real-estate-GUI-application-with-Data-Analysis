from tkinter import *
#import tkinter as tk
import pymysql
from datetime import datetime, timedelta
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd


def Menu_window():
    screen.destroy()
    import kh

def moduleg1():
    #screen.destroy()
    global screen27
    screen27 = Toplevel(screen)
    screen27.title("Time series for orders in database")
    Label(screen27, text="", bg='#dddddd',width='500', height='50').place(x=0, y=70)
    Label(screen27, text="Time series for orders in database", width="500", height="2",font=("Calibri", 22, 'bold'), fg='black', bg='#77d8d8').pack()
    #adjustWindow(screen27)
    
    connection = pymysql.connect(host="localhost",user="root",passwd="", database="sales") # database connection
    cursor = connection.cursor()
    select_query =  "SELECT ORD_DATE FROM orders ;" # queries for retrieving values 
    cursor.execute(select_query) # executing the queries 
    date = cursor.fetchall()
    date_list = []
    
    for i in range(len(date)):       
        date_list.append(date[i][0])
        date_list.sort(key = lambda date: datetime.strptime(str(date), '%Y-%m-%d')) 
        fdate = {}
        
        for i in range(len(date_list)):
            if date_list[i] in fdate:
                fdate[date_list[i]] = fdate[date_list[i]] + 1
            else:
                fdate[date_list[i]] = 1
     

    df = pd.DataFrame.from_dict(fdate,orient='index')
    
    figure = plt.Figure(figsize=(10,6.1), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, screen27)
    chart_type.get_tk_widget().pack()
    df.plot(rot=90,ax=ax)
    ax.set_ylabel("Number of orders")
    ax.set_title('Time series for orders in database')
    
    
def moduleg2():
    global screen28
    screen28 = Toplevel(screen)
    screen28.title("Time series for Area leased or owned")
    Label(screen28, text="", bg='#dddddd',width='500', height='50').place(x=0, y=70)
    Label(screen28, text="Time series for Area leased or owned", width="500", height="2",font=("Calibri", 22, 'bold'), fg='white', bg='#77d8d8').pack()
    #adjustWindow(screen28)
    data = pd.read_excel("A_new.xlsx",header = 8)
    data = data[:-1]
    data.loc[data.UoM == "HA", "Area"] = data.Area*10000
    data=data.replace('HA','SQ-M')
    q7a = dict(data.groupby('Year').count()['Prov'])
    q7ad = pd.DataFrame({'Year':list(q7a.keys()),'Number of orders':list(q7a.values())})
    figure = plt.Figure(figsize=(10,6.1), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, screen28)
    chart_type.get_tk_widget().pack()
    q7ad.plot(ax=ax,x='Year')
    ax.set_ylabel("Number of orders")
    ax.set_title('Time series for Area leased or owned')

    
def main_screen():
    global screen
    screen=Tk()
    screen.title("Time Series Analysis")
    screen.geometry("1030x600+100+50")
    screen.configure(background="sky blue")
    lbl=Label(screen,text="Time Series Analysis For Order Date VS Order Amount",font=("times new roman",20,"bold"),fg="green")
    lbl.place(x=250,y=120)
    
    lbl=Label(screen,text="Time Series Analysis For Order Date VS Advance Amount",font=("times new roman",20,"bold"),fg="green")
    lbl.place(x=250,y=300)

    but = Button(screen, text="VIEW GRAPH", bg = "#747437", fg="white",font=("times new roman",20,"bold"),cursor="hand2",command=moduleg1)
        
    but.place(x=440,y=180)
    menubtn=Button(screen,text="<Back to Menu",bg = "#747437", fg="white",font=("times new roman",15,"bold"),cursor="hand2",command=Menu_window).place(x=20,y=60)
     
    
    but = Button(screen, text="VIEW GRAPH", bg = "#747437", fg="white",font=("times new roman",20,"bold"),cursor="hand2",command=moduleg2)
            
    but.place(x=440,y=360)
    screen.mainloop()
    
main_screen()
 
