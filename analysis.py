from tkinter import *
from tkinter import ttk
import os
from analysis_functions import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Analysis():
    def __init__(self,root):
        self.root=root
        self.root.title("Analysis")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="sky blue")
        self.question_number = StringVar()
        self.year = StringVar()
        self.y1 = StringVar()
        self.A1 = StringVar()
        self.A2 = StringVar()
        
        
        self.title=Label(self.root,text="WELCOME TO Analysis SECTION",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="white",fg="Navy Blue")
        self.title.pack(side=TOP,fill=X)
        
        Label(self.root,text="Choose Question",font=("times new roman",18,"bold"),fg="Green").pack(pady=20)
        self.questions = ttk.Combobox(self.root, width = 130, textvariable = self.question_number)
        self.questions['values'] = ( "A) The total property area sold vs total property are leased in Sq-M only.",
    "B) Of the years 2017,2018,2019- which year got maximum leased area in CA and WS countries",
    "C) What are the Agent codes of all the agents who have got deals in ‘OWNED’ categories across the years",
    "D) For the city of chillwalk, which agent hs got the maximum deals in leased form.",
    "E) Compare the performance of all agents based on the area leased and owned for the years 2017,2018 and 2019.Who has been the best performer?",
    "F) What is the amount of property area sold for the month of july for all the years.")
    
        self.questions.pack(pady=20)
        
        
        self.yearlabel=Label(self.root,text="Choose Year",font=("times new roman",20,"bold"),fg="green").pack(pady=20)
        self.select_year = ttk.Combobox(self.root, width = 50, textvariable = self.year)
        self.select_year['values'] = ('2017','2018','2019','2020')
        self.select_year.pack(pady=20)
        self.but = Button(self.root, text="Continue", bg = "#747437", fg="white",font=("times new roman",20,"bold"),command=self.dest).pack(pady=20)
        self.menubtn=Button(self.root,text="<Back to Menu",bg = "#747437", fg="white",font=("times new roman",15,"bold"),cursor="hand2",command=self.Menu_window).place(x=20,y=100)
        self.y = Label(self.root,textvariable=self.y1,font=("times new roman",20,"bold"),fg="Green",bg="sky blue").pack(pady=20)
        self.a1 = Label(self.root,textvariable=self.A1,font=("times new roman",15,"bold"),bg="sky blue").pack(pady=20)
        self.a2 = Label(self.root,textvariable=self.A2,font=("times new roman",15,"bold"),bg="sky blue").pack(pady=20)
    
    def Menu_window(self):
        self.root.destroy()
        import kh
        
    def dest(self):
        global Q, Y, question_number,year, y, a1, a2
        
        Y = int(self.year.get())
        Q = str(self.question_number.get())
        print(Q, Y)
        if self.question_number.get()=="A) The total property area sold vs total property are leased in Sq-M only.":
            area_owned, area_leased = getTotalAreaSoldVsLeased(Y)
            self.y1.set("Your Answer")
            self.A1.set("The total property area sold in Sq-M is "+str(area_owned))
            self.A2.set("The total property area leased in Sq-M is "+str(area_leased))
            
            
            
            
            
        elif self.question_number.get()=="B) Of the years 2017,2018,2019- which year got maximum leased area in CA and WS countries":   
            country1,country2 = yeargotmaximumleasedareainCAandWScountries(Y)
            self.y1.set("Your Answer")
            self.A1.set((str(country1))+"has the maximum leased area in the "+str(Y))
            self.A2.set((str(country2))+"has the maximum leased area in the "+str(Y))
            
        elif self.question_number.get()=="C) What are the Agent codes of all the agents who have got deals in ‘OWNED’ categories across the years":
            identifier, agents = agentcode(Y)
            self.y1.set("Your Answer")
            self.A1.set("Identifiers = "+str(identifier))
            self.A2.set("Agents = "+str(agents))
           
        
        elif self.question_number.get()=="D) For the city of chillwalk, which agent hs got the maximum deals in leased form.":
            agent = maxleasedagent(Y)
            self.y1.set("Your Answer")
            self.A1.set(str(agent)+" agent has got the maximum deals in leased form.")
            self.A2.set("")
            leased_data = data[data["Tenure"] == "Leased"]
            leased_data = leased_data[leased_data["Year"] == 2018]
            leased_data = leased_data[leased_data["City"] == "Chilliwack"]
        elif self.question_number.get()=="E) Compare the performance of all agents based on the area leased and owned for the years 2017,2018 and 2019.Who has been the best performer?":
            owned_agent_list, leased_agent_list = get_agent(Y)
            self.y1.set("Your Answer")
            self.A1.set("The best performer for owned area is "+max(owned_agent_list,key=owned_agent_list.get))
            self.A2.set("The best performer for leased area is "+max(leased_agent_list,key=leased_agent_list.get))
        # plt.hist(owned_agent_list.keys(), owned_agent_list.values(), color='g', label = "Real distribution")
        # plt.show()
            keys = owned_agent_list.keys()
            vals = owned_agent_list.values()
            plt.figure(figsize=(14, 6), dpi= 80, facecolor='w', edgecolor='k')
            plt.bar(keys, vals, label="Distrinution")

            plt.ylim(0,max(vals))
            plt.ylabel ('Area Sold (sq.meter)')
            plt.xlabel ('Agents')
            plt.xticks(list(keys))
            plt.legend (bbox_to_anchor=(1, 1), loc="upper right", borderaxespad=0.)
            
        elif self.question_number.get()=="F) What is the amount of property area sold for the month of july for all the years.":
            propertyareasold= propertysoldforjuly()
            self.y1.set("Your Answer")
            self.A1.set("The amount of property area sold for the month of july is "+str(propertyareasold)+"sq.m in the year"+str(Y))
            self.A2.set("")
            
        
        else:
            messagebox.showerror("Error","Please fill all details")





root=Tk()
# while True:
obj=Analysis(root)
root.mainloop()        