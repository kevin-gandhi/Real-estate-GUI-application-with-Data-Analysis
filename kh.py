from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox  #combobox
import pymysql,re
import os
from analysis_functions import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


#+++++++++++++++++++++<<<<<<<<<<AGENT RECORD>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def Agent():
    
    global screen4,AGENT_CODE_var,AGENT_NAME_var,WORKING_AREA_var,COMMISSION_var,PHONE_NO_var,COUNTRY_var,Search_by,Search_txt,Agent_table
    
    screen4=Toplevel(screen)
    screen4.title("Agent Record")
    screen4.geometry("1350x700+0+0")
    screen4.focus_force()
    screen4.grab_set()
     
    
    
    
    title=Label(screen4,text="Agent Details",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
    title.pack(side=TOP,fill=X)
    
    #_____Variables______
    AGENT_CODE_var=StringVar()
    AGENT_NAME_var=StringVar()
    WORKING_AREA_var=StringVar()
    COMMISSION_var=StringVar()
    PHONE_NO_var=StringVar()
    COUNTRY_var=StringVar()
    
    Search_by=StringVar()
    Search_txt=StringVar()
    
    
    
    
    # ++++++++++Manage Frame++++++++++
    Manage_Frame=Frame(screen4,bd=4,relief=RIDGE,bg="light pink")
    Manage_Frame.place(x=20,y=100,width=520,height=560)
    
    m_title=Label(Manage_Frame,text="Manage Agents",bg="light pink",fg="green",font=("times new roman",30,"bold"))
    m_title.grid(row=0,columnspan=2,pady=20)
    
    lbl_AGENT_CODE=Label(Manage_Frame,text="Agent Code",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    lbl_AGENT_CODE.grid(row=1,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_AGENT_CODE=Entry(Manage_Frame,textvariable=AGENT_CODE_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_AGENT_CODE.grid(row=1,column=1,pady=10,padx=20,sticky="w")
    
    
    lbl_AGENT_NAME=Label(Manage_Frame,text="Agent Name",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    lbl_AGENT_NAME.grid(row=2,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_AGENT_NAME=Entry(Manage_Frame,textvariable=AGENT_NAME_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_AGENT_NAME.grid(row=2,column=1,pady=10,padx=20,sticky="w")
    
    
    lbl_WORKING_AREA=Label(Manage_Frame,text="Working Area",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    lbl_WORKING_AREA.grid(row=3,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_WORKING_AREA=Entry(Manage_Frame,textvariable=WORKING_AREA_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_WORKING_AREA.grid(row=3,column=1,pady=10,padx=20,sticky="w")
    
    lbl_COMMISSION=Label(Manage_Frame,text="Commission",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    lbl_COMMISSION.grid(row=4,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_COMMISSION=Entry(Manage_Frame,textvariable=COMMISSION_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_COMMISSION.grid(row=4,column=1,pady=10,padx=20,sticky="w")
    
    lbl_PHONE_NO=Label(Manage_Frame,text="Contact No",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    lbl_PHONE_NO.grid(row=5,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_PHONE_NO=Entry(Manage_Frame,textvariable=PHONE_NO_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_PHONE_NO.grid(row=5,column=1,pady=10,padx=20,sticky="w")
    
    
    lbl_COUNTRY=Label(Manage_Frame,text="Country",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    lbl_COUNTRY.grid(row=6,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_COUNTRY=Entry(Manage_Frame,textvariable=COUNTRY_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_COUNTRY.grid(row=6,column=1,pady=10,padx=20,sticky="w")
    
    
    #+++++++++++++++BUTTON FRAME+++++++++++++++
    btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="light pink")
    btn_Frame.place(x=10,y=450,width=495)
    
    Addbtn=Button(btn_Frame,text="Add",width=10,cursor="hand2",command=add_agent).grid(row=0,column=0,padx=10,pady=10)
    Updatebtn=Button(btn_Frame,text="Update",width=10,cursor="hand2",command=update_data).grid(row=0,column=1,padx=10,pady=10)
    Deletbtn=Button(btn_Frame,text="Delete",width=10,cursor="hand2",command=delete_data).grid(row=0,column=2,padx=10,pady=10)
    clearbtn=Button(btn_Frame,text="Clear",width=10,cursor="hand2",command=Aclear).grid(row=0,column=3,padx=10,pady=10)
    menubtn=Button(btn_Frame,text="Menu",width=10,cursor="hand2",command=screen4.destroy).grid(row=0,column=4,padx=10,pady=10)
    
    #+++++++++++++Detail Frame+++++++++++++++
    Detail_Frame=Frame(screen4,bd=4,relief=RIDGE,bg="light pink")
    Detail_Frame.place(x=530,y=100,width=800,height=560)
    
    lbl_Search=Label(Detail_Frame,text="Search By",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    lbl_Search.grid(row=0,column=0,pady=0,padx=20,sticky="w")
    
    combo_Search=ttk.Combobox(Detail_Frame,textvariable=Search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
    combo_Search['values']=("Agent_Code","Agent_Name")
    combo_Search.grid(row=0,column=1,padx=0,pady=10)
    
    txt_Search=Entry(Detail_Frame,textvariable=Search_txt,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
    txt_Search.grid(row=0,column=2,pady=10,padx=8,sticky="w")
    
    searchbtn=Button(Detail_Frame,text="Search",width=10,command=search_data).grid(row=0,column=3,padx=10,pady=10)
    showallbtn=Button(Detail_Frame,text="Show All",width=10,command=fetch_data).grid(row=0,column=4,padx=10,pady=10)
    
    
    #++++++Table Frame++++++++++++++
    Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="light pink")
    Table_Frame.place(x=10,y=70,width=760,height=480)
    
    
    scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
   
    Agent_table=ttk.Treeview(Table_Frame,columns=("AGENT_CODE","AGENT_NAME","WORKING_AREA","COMMISSION","PHONE_NO","COUNTRY"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=Agent_table.xview)
    scroll_y.config(command=Agent_table.yview)
    Agent_table.heading("AGENT_CODE",text="AGENT_CODE")
    Agent_table.heading("AGENT_NAME",text="AGENT_NAME")
    Agent_table.heading("WORKING_AREA",text="WORKING_AREA")
    Agent_table.heading("COMMISSION",text="COMMISSION")
    Agent_table.heading("PHONE_NO",text="PHONE_NO")
    Agent_table.heading("COUNTRY",text="COUNTRY")
    Agent_table['show']='headings'
    Agent_table.column("AGENT_CODE",width=150)
    Agent_table.column("AGENT_NAME",width=150)
    Agent_table.column("WORKING_AREA",width=150)
    Agent_table.column("COMMISSION",width=150)
    Agent_table.column("PHONE_NO",width=150)
    Agent_table.column("COUNTRY",width=150)
    Agent_table.pack(fill=BOTH,expand=1)
    Agent_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_data()




    
    

def add_agent():
    if AGENT_CODE_var.get()=="" or AGENT_NAME_var.get()=="" or WORKING_AREA_var.get()=="" or COMMISSION_var.get()=="" or PHONE_NO_var.get()=="" or COUNTRY_var.get()=="":
        messagebox.showerror("Error","All fields are required!!!",parent=screen4)
    elif not re.match("^((\+)?(\d{3}[-])?(\d{10}){1})?(\d{11}){0,1}?$",PHONE_NO_var.get()):
        messagebox.showerror("Error","Please Enter Valid Phone No",parent=screen4)
   
    elif not re.match("^[0-9]*(\.[0-9]{0,2})?$",COMMISSION_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty")
    elif not re.match("(^[A]?\d{2,5})$",AGENT_CODE_var.get()):
        messagebox.showerror("Error","Please Enter Valid Agent Code")
    else:
        con=pymysql.connect(host="localhost",user="root",password="",database="sales")
        cur=con.cursor()
        cur.execute("insert into agents (AGENT_CODE,AGENT_NAME,WORKING_AREA,COMMISSION,PHONE_NO,COUNTRY) values(%s,%s,%s,%s,%s,%s)",(AGENT_CODE_var.get(),
                                                                AGENT_NAME_var.get().capitalize(),
                                                                WORKING_AREA_var.get().capitalize(),
                                                                COMMISSION_var.get(),
                                                                PHONE_NO_var.get(),
                                                                COUNTRY_var.get().capitalize()
                                                                ))
        con.commit()
        fetch_data()
        Aclear()
        con.close()
        messagebox.showinfo("Success","Record has been inserted")

def fetch_data():
    con=pymysql.connect(host="localhost",user="root",password="",database="sales")
    cur=con.cursor()
    cur.execute("select * from agents")
    rows=cur.fetchall()
    if len(rows)!=0:
        Agent_table.delete(*Agent_table.get_children())
        for row in rows:
            Agent_table.insert('',END,values=row)
        con.commit()
    con.close()
    
def Aclear():
    AGENT_CODE_var.set("")
    AGENT_NAME_var.set("")
    WORKING_AREA_var.set("")
    COMMISSION_var.set("")
    PHONE_NO_var.set("")
    COUNTRY_var.set("")
 

#________Selected data from table will display in the fields_______
def get_cursor(ev):
    cursor_row=Agent_table.focus()
    contents=Agent_table.item(cursor_row)
    row=contents['values']
    AGENT_CODE_var.set(row[0])
    AGENT_NAME_var.set(row[1])
    WORKING_AREA_var.set(row[2])
    COMMISSION_var.set(row[3])
    PHONE_NO_var.set(row[4])
    COUNTRY_var.set(row[5])
    
def update_data():
    if not re.match("(^((\+)?(\d{3}[-])?(\d{10}){1})?(\d{11}){0,1}?$)",PHONE_NO_var.get()):
        messagebox.showerror("Error","Please Enter Valid Phone No",parent=screen4)
    elif not re.match("^[0-9]*(\.[0-9]{0,2})?$",COMMISSION_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty")
    
    else:
        con=pymysql.connect(host="localhost",user="root",password="",database="sales")
        cur=con.cursor()
        cur.execute("update agents set AGENT_NAME=%s,WORKING_AREA=%s,COMMISSION=%s,PHONE_NO=%s,COUNTRY=%s where AGENT_CODE=%s",(
                                                                    AGENT_NAME_var.get().capitalize(),
                                                                    WORKING_AREA_var.get().capitalize(),
                                                                    COMMISSION_var.get(),
                                                                    PHONE_NO_var.get(),
                                                                    COUNTRY_var.get().capitalize(),
                                                                    AGENT_CODE_var.get()
                                                                    ))
        con.commit()
        fetch_data()
        Aclear()
        con.close()
        messagebox.showinfo("Success","Record has been Updated")

    
def delete_data():
    con=pymysql.connect(host="localhost",user="root",password="",database="sales")
    cur=con.cursor()
    cur.execute("delete from agents where AGENT_CODE=%s",AGENT_CODE_var.get())
    con.commit()
    con.close()
    fetch_data()
    Aclear()
    messagebox.showinfo("Success","Record has been deleted")

    
def search_data():
    con=pymysql.connect(host="localhost",user="root",password="",database="sales")
    cur=con.cursor()
    cur.execute("select * from agents where "+str(Search_by.get()) +"=%s",(str(Search_txt.get())))
    rows=cur.fetchall()
    if len(rows)!=0:
        Agent_table.delete(*Agent_table.get_children())
        for row in rows:
            Agent_table.insert('',END,values=row)
    else:
            messagebox.showinfo("Error","No Such Record")
    con.commit()
    con.close()    



#+++++++++++++++++++<<<<<<<<<<<<<<<<<<<<Customer Record>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



def Customer():
    global screen1,Search_by,Search_txt,CUST_CODE_var,CUST_NAME_var,CUST_CITY_var,WORKING_AREA_var,CUST_COUNTRY_var,GRADE_var,OPENING_AMT_var,RECEIVE_AMT_var,OUTSTANDING_AMT_var,PAYMENT_AMT_var, PHONE_NO_var,AGENT_CODE_var,Search_by_var,Search_txt_var,Customer_table
    screen1=Toplevel(screen)
    
    screen1.title("Customer Record")
    screen1.geometry("1350x700+0+0")
    
    
    title=Label(screen1,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
    title.pack(side=TOP,fill=X)
    
     #_____Variables______
    CUST_CODE_var=StringVar()
    CUST_NAME_var=StringVar()
    CUST_CITY_var=StringVar()
    WORKING_AREA_var=StringVar()
    CUST_COUNTRY_var=StringVar()
    GRADE_var=StringVar()
    OPENING_AMT_var=StringVar()
    RECEIVE_AMT_var=StringVar()
    OUTSTANDING_AMT_var=StringVar()
    PAYMENT_AMT_var=StringVar()
    PHONE_NO_var=StringVar()
    AGENT_CODE_var=StringVar()
    Search_by=StringVar()
    Search_txt=StringVar()
    
    
    
    
    
    
    # ++++++++++Manage Frame++++++++++
    Manage_Frame=Frame(screen1,bd=4,relief=RIDGE,bg="light pink")
    Manage_Frame.place(x=20,y=100,width=800,height=580)
    
    m_title=Label(Manage_Frame,text="Manage Customer",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    m_title.grid(row=0,columnspan=4,pady=20)
    
    lbl_CUST_CODE=Label(Manage_Frame,text="Customer Code",bg="light pink",fg="green",font=("times new roman",15,"bold"))
    lbl_CUST_CODE.grid(row=1,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_CUST_CODE=Entry(Manage_Frame,textvariable=CUST_CODE_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
    txt_CUST_CODE.grid(row=1,column=1,pady=10,padx=20,sticky="w")
    
    
    lbl_CUST_NAME=Label(Manage_Frame,text="Customer Name",bg="light pink",fg="green",font=("times new roman",15,"bold"))
    lbl_CUST_NAME.grid(row=1,column=2,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_CUST_NAME=Entry(Manage_Frame,textvariable=CUST_NAME_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
    txt_CUST_NAME.grid(row=1,column=3,pady=10,padx=20,sticky="w")
    
    
    lbl_PAYMENT_AMT=Label(Manage_Frame,text="Payment Amount",bg="light pink",fg="green",font=("times new roman",15,"bold"))
    lbl_PAYMENT_AMT.grid(row=2,column=2,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_PAYMENT_AMT=Entry(Manage_Frame,textvariable=PAYMENT_AMT_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
    txt_PAYMENT_AMT.grid(row=2,column=3,pady=10,padx=20,sticky="w")
    
    
    lbl_CUST_CITY=Label(Manage_Frame,text="Customer City",bg="light pink",fg="green",font=("times new roman",15,"bold"))
    lbl_CUST_CITY.grid(row=2,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_CUST_CITY=Entry(Manage_Frame,textvariable=CUST_CITY_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
    txt_CUST_CITY.grid(row=2,column=1,pady=10,padx=20,sticky="w")


    lbl_WORKING_AREA=Label(Manage_Frame,text="Working Area",bg="light pink",fg="green",font=("times new roman",15,"bold"))
    lbl_WORKING_AREA.grid(row=3,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_WORKING_AREA=Entry(Manage_Frame,textvariable=WORKING_AREA_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
    txt_WORKING_AREA.grid(row=3,column=1,pady=10,padx=20,sticky="w")
    
    lbl_OUTSTANDING_AMT=Label(Manage_Frame,text="Outstanding Amount",bg="light pink",fg="green",font=("times new roman",15,"bold"))
    lbl_OUTSTANDING_AMT.grid(row=3,column=2,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_OUTSTANDING_AMT=Entry(Manage_Frame,textvariable=OUTSTANDING_AMT_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
    txt_OUTSTANDING_AMT.grid(row=3,column=3,pady=10,padx=20,sticky="w")
    
    lbl_CUST_COUNTRY=Label(Manage_Frame,text="Customer Country",bg="light pink",fg="green",font=("times new roman",15,"bold"))
    lbl_CUST_COUNTRY.grid(row=4,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_CUST_COUNTRY=Entry(Manage_Frame,textvariable=CUST_COUNTRY_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
    txt_CUST_COUNTRY.grid(row=4,column=1,pady=10,padx=20,sticky="w")
    
    lbl_PHONE_NO=Label(Manage_Frame,text="Phone No",bg="light pink",fg="green",font=("times new roman",15,"bold"))
    lbl_PHONE_NO.grid(row=4,column=2,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_PHONE_NO=Entry(Manage_Frame,textvariable=PHONE_NO_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
    txt_PHONE_NO.grid(row=4,column=3,pady=10,padx=20,sticky="w")
    
    lbl_GRADE=Label(Manage_Frame,text="Grade",bg="light pink",fg="green",font=("times new roman",15,"bold"))
    lbl_GRADE.grid(row=5,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_GRADE=Entry(Manage_Frame,textvariable=GRADE_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
    txt_GRADE.grid(row=5,column=1,pady=10,padx=20,sticky="w")
    
    lbl_AGENT_CODE=Label(Manage_Frame,text="Agent Code",bg="light pink",fg="green",font=("times new roman",15,"bold"))
    lbl_AGENT_CODE.grid(row=5,column=2,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_AGENT_CODE=Entry(Manage_Frame,textvariable=AGENT_CODE_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
    txt_AGENT_CODE.grid(row=5,column=3,pady=10,padx=20,sticky="w")
    
    
    lbl_OPENING_AMT=Label(Manage_Frame,text="Opening Amount",bg="light pink",fg="green",font=("times new roman",15,"bold"))
    lbl_OPENING_AMT.grid(row=6,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_OPENING_AMT=Entry(Manage_Frame,textvariable=OPENING_AMT_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
    txt_OPENING_AMT.grid(row=6,column=1,pady=10,padx=20,sticky="w")
    
    lbl_RECEIVE_AMT=Label(Manage_Frame,text="Receive Amount",bg="light pink",fg="green",font=("times new roman",15,"bold"))
    lbl_RECEIVE_AMT.grid(row=6,column=2,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_RECEIVE_AMT=Entry(Manage_Frame,textvariable=RECEIVE_AMT_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
    txt_RECEIVE_AMT.grid(row=6,column=3,pady=10,padx=20,sticky="w")
    
    
    
    #+++++++++++++++BUTTON FRAME+++++++++++++++
    btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="light pink")
    btn_Frame.place(x=15,y=450,width=720)
    
    Addbtn=Button(btn_Frame,text="Add",width=15,cursor="hand2",command=Cadd_cust).grid(row=0,column=0,padx=10,pady=10)
    Updatebtn=Button(btn_Frame,text="Update",width=15,cursor="hand2",command=Cupdate_data).grid(row=0,column=1,padx=10,pady=10)
    Deletbtn=Button(btn_Frame,text="Delete",width=15,cursor="hand2",command=Cdelete_data).grid(row=0,column=2,padx=10,pady=10)
    clearbtn=Button(btn_Frame,text="Clear",width=15,cursor="hand2",command=Cclear).grid(row=0,column=3,padx=10,pady=10)
    showallbtn=Button(btn_Frame,text="Show All",width=15,cursor="hand2",command=Cfetch_data).grid(row=0,column=4,padx=10,pady=10)
    menubtn=Button(btn_Frame,text="Menu",width=15,cursor="hand2",command=screen1.destroy).grid(row=0,column=4,padx=10,pady=10)
    
    
    
    #+++++++++++++Detail Frame+++++++++++++++
    Detail_Frame=Frame(screen1,bd=4,relief=RIDGE,bg="light pink")
    Detail_Frame.place(x=830,y=100,width=500,height=580)
    
    lbl_Search=Label(Detail_Frame,text="Search By",bg="light pink",fg="green",font=("times new roman",15,"bold"))
    lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
    
    combo_Search=ttk.Combobox(Detail_Frame,textvariable=Search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
    combo_Search['values']=("Cust_Code","Cust_Name","Agent_Code")
    combo_Search.grid(row=0,column=1,padx=10,pady=10)
    
    txt_Search=Entry(Detail_Frame,textvariable=Search_txt,width=15,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
    txt_Search.grid(row=0,column=2,pady=10,padx=10,sticky="w")
    
    searchbtn=Button(Detail_Frame,text="Search",width=10,command=Csearch_data).grid(row=0,column=3,padx=10,pady=10)
    
    #_________Table Frame_______________
    Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="light pink")
    Table_Frame.place(x=10,y=70,width=470,height=480)
    
    scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
   
    Customer_table=ttk.Treeview(Table_Frame,columns=("CUST_CODE","CUST_NAME","CUST_CITY","WORKING_AREA","CUST_COUNTRY","GRADE","OPENING_AMT","RECEIVE_AMT","PAYMENT_AMT","OUTSTANDING_AMT","PHONE_NO","AGENT_CODE"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=Customer_table.xview)
    scroll_y.config(command=Customer_table.yview)
    Customer_table.heading("CUST_CODE",text="CUST_CODE")
    Customer_table.heading("CUST_NAME",text="CUST_NAME")
    Customer_table.heading("CUST_CITY",text="CUST_CITY")
    Customer_table.heading("WORKING_AREA",text="WORKING_AREA")
    Customer_table.heading("CUST_COUNTRY",text="CUST_COUNTRY")
    Customer_table.heading("GRADE",text="GRADE")
    Customer_table.heading("OPENING_AMT",text="OPENING_AMT")
    Customer_table.heading("RECEIVE_AMT",text="RECEIVE_AMT")
    Customer_table.heading("PAYMENT_AMT",text="PAYMENT_AMT")
    Customer_table.heading("OUTSTANDING_AMT",text="OUTSTANDING_AMT")
    Customer_table.heading("PHONE_NO",text="PHONE_NO")
    Customer_table.heading("AGENT_CODE",text="AGENT_CODE")
   
    Customer_table['show']='headings'
    Customer_table.column("CUST_CODE",width=150)
    Customer_table.column("CUST_NAME",width=150)
    Customer_table.column("CUST_CITY",width=150)
    Customer_table.column("WORKING_AREA",width=150)
    Customer_table.column("CUST_COUNTRY",width=150)
    Customer_table.column("GRADE",width=150)
    Customer_table.column("OPENING_AMT",width=150)
    Customer_table.column("RECEIVE_AMT",width=150)
    Customer_table.column("PAYMENT_AMT",width=150)
    Customer_table.column("OUTSTANDING_AMT",width=150)
    Customer_table.column("PHONE_NO",width=150)
    Customer_table.column("AGENT_CODE",width=150)
    Customer_table.pack(fill=BOTH,expand=1)
    Customer_table.bind("<ButtonRelease-1>",Cget_cursor)
    Cfetch_data()
 


def Cadd_cust():
    if CUST_CODE_var.get()=="" or CUST_NAME_var.get()=="" or CUST_CITY_var.get()=="" or WORKING_AREA_var.get()=="" or CUST_COUNTRY_var.get()=="" or  GRADE_var.get()=="" or OPENING_AMT_var.get()=="" or RECEIVE_AMT_var.get()=="" or PAYMENT_AMT_var.get()=="" or OUTSTANDING_AMT_var.get()=="" or PHONE_NO_var.get()=="" or AGENT_CODE_var.get()=="":
        messagebox.showerror("Error","All fields are required!!!")
    elif not re.match("^((\+)?(\d{3}[-])?(\d{10}){1})?(\d{11}){0,1}?$",PHONE_NO_var.get()):
        messagebox.showerror("Error","Please Enter Valid Phone No",parent=screen1)
    elif not re.match("^[0-9]*(\.[0-9]{0,0})?$",GRADE_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty For Grade",parent=screen1)
    elif not re.match("(^[A]?\d{2,5})$",AGENT_CODE_var.get()):
        messagebox.showerror("Error","Please Enter Valid Agent Code",parent=screen1)
    elif not re.match("(^[C]?\d{2,5})$",CUST_CODE_var.get()):
        messagebox.showerror("Error","Please Enter Valid Customer Code",parent=screen1)
    elif not re.match("^[0-9]*(\.[0-9]{0,2})?$",OPENING_AMT_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty for Opening Amount",parent=screen1)
    elif not re.match("^[0-9]*(\.[0-9]{0,2})?$",RECEIVE_AMT_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty for Receive Amount",parent=screen1)    
    elif not re.match("^[0-9]*(\.[0-9]{0,2})?$",PAYMENT_AMT_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty for Payment Amount",parent=screen1)    
    elif not re.match("^[0-9]*(\.[0-9]{0,2})?$",OUTSTANDING_AMT_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty for Outstanding Amount",parent=screen1)    
    
    else:
        con=pymysql.connect(host="localhost",user="root",password="",database="sales")
        cur=con.cursor()
        cur.execute("insert into customer (CUST_CODE,CUST_NAME,CUST_CITY,WORKING_AREA,CUST_COUNTRY,GRADE,OPENING_AMT,RECEIVE_AMT,PAYMENT_AMT,OUTSTANDING_AMT,PHONE_NO,AGENT_CODE) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(CUST_CODE_var.get(),
                                                                CUST_NAME_var.get().capitalize(),
                                                                CUST_CITY_var.get().capitalize(),
                                                                WORKING_AREA_var.get().capitalize(),
                                                                CUST_COUNTRY_var.get().capitalize(),
                                                                GRADE_var.get(),
                                                                OPENING_AMT_var.get(),
                                                                RECEIVE_AMT_var.get(),
                                                                PAYMENT_AMT_var.get(),
                                                                OUTSTANDING_AMT_var.get(),
                                                                PHONE_NO_var.get(),
                                                                AGENT_CODE_var.get()
                                                               
                                                                ))
        con.commit()
        Cfetch_data()
        Cclear()
        con.close()
        messagebox.showinfo("Success","Record has been inserted")

def Cfetch_data():
    con=pymysql.connect(host="localhost",user="root",password="",database="sales")
    cur=con.cursor()
    cur.execute("select * from customer")
    rows=cur.fetchall()
    if len(rows)!=0:
        Customer_table.delete(*Customer_table.get_children())
        for row in rows:
            Customer_table.insert('',END,values=row)
        con.commit()
    con.close()
    
def Cclear():
    CUST_CODE_var.set("")
    CUST_NAME_var.set("")
    CUST_CITY_var.set("")
    WORKING_AREA_var.set("")
    CUST_COUNTRY_var.set("")
    GRADE_var.set("")
    OPENING_AMT_var.set("")
    RECEIVE_AMT_var.set("")
    PAYMENT_AMT_var.set("")
    OUTSTANDING_AMT_var.set("")
    PHONE_NO_var.set("")
    AGENT_CODE_var.set("")
    
#________Selected data from table will display in the fields_______
def Cget_cursor(ev):
    cursor_row=Customer_table.focus()
    contents=Customer_table.item(cursor_row)
    row=contents['values']
    CUST_CODE_var.set(row[0])
    CUST_NAME_var.set(row[1])
    CUST_CITY_var.set(row[2])
    WORKING_AREA_var.set(row[3])
    CUST_COUNTRY_var.set(row[4])
    GRADE_var.set(row[5])
    OPENING_AMT_var.set(row[6])
    RECEIVE_AMT_var.set(row[7])
    PAYMENT_AMT_var.set(row[8])
    OUTSTANDING_AMT_var.set(row[9])
    PHONE_NO_var.set(row[10])
    AGENT_CODE_var.set(row[11])
    
    
def Cupdate_data():
    if not re.match("^((\+)?(\d{3}[-])?(\d{10}){1})?(\d{11}){0,1}?$",PHONE_NO_var.get()):
        messagebox.showerror("Error","Please Enter Valid Phone No",parent=screen1)
    elif not re.match("^[0-9]*(\.[0-9]{0,0})?$",GRADE_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty",parent=screen1)
    elif not re.match("(^[A]?\d{2,5})$",AGENT_CODE_var.get()):
        messagebox.showerror("Error","Please Enter Valid Agent Code",parent=screen1)
    elif not re.match("(^[C]?\d{2,5})$",CUST_CODE_var.get()):
        messagebox.showerror("Error","Please Enter Valid Customer Code",parent=screen1)
    elif not re.match("^[0-9]*(\.[0-9]{0,2})?$",OPENING_AMT_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty for Opening Amount",parent=screen1)
    elif not re.match("^[0-9]*(\.[0-9]{0,2})?$",RECEIVE_AMT_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty for Receive Amount",parent=screen1)    
    elif not re.match("^[0-9]*(\.[0-9]{0,2})?$",PAYMENT_AMT_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty for Payment Amount",parent=screen1)    
    elif not re.match("^[0-9]*(\.[0-9]{0,2})?$",OUTSTANDING_AMT_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty for Outstanding Amount",parent=screen1)    
    
    else:
        con=pymysql.connect(host="localhost",user="root",password="",database="sales")
        cur=con.cursor()
        cur.execute("update customer set CUST_NAME=%s,CUST_CITY=%s,WORKING_AREA=%s,CUST_COUNTRY=%s,GRADE=%s,OPENING_AMT=%s,RECEIVE_AMT=%s,PAYMENT_AMT=%s,OUTSTANDING_AMT=%s,PHONE_NO=%s,AGENT_CODE=%s where CUST_CODE=%s",(
                                                                    CUST_NAME_var.get().capitalize(),
                                                                    CUST_CITY_var.get().capitalize(),
                                                                    WORKING_AREA_var.get().capitalize(),
                                                                    CUST_COUNTRY_var.get().capitalize(),
                                                                    GRADE_var.get(),
                                                                    OPENING_AMT_var.get(),
                                                                    RECEIVE_AMT_var.get(),
                                                                    PAYMENT_AMT_var.get(),
                                                                    OUTSTANDING_AMT_var.get(),
                                                                    PHONE_NO_var.get(),
                                                                    AGENT_CODE_var.get(),
                                                                    CUST_CODE_var.get()
                                                                    ))
        con.commit()
        Cfetch_data()
        Cclear()
        con.close()
        messagebox.showinfo("Success","Record has been updated")
    
      
def Cdelete_data():
    con=pymysql.connect(host="localhost",user="root",password="",database="sales")
    cur=con.cursor()
    cur.execute("delete from customer where CUST_CODE=%s",CUST_CODE_var.get())
    con.commit()
    con.close()
    Cfetch_data()
    Cclear()
    messagebox.showinfo("Success","Record has been deleted")

    
    
def Csearch_data():
    con=pymysql.connect(host="localhost",user="root",password="",database="sales")
    cur=con.cursor()
    cur.execute("select * from customer where "+str(Search_by.get()) +"=%s",(str(Search_txt.get())))
    rows=cur.fetchall()
    if len(rows)!=0:
        Customer_table.delete(*Customer_table.get_children())
        for row in rows:
            Customer_table.insert('',END,values=row)
    else:
        messagebox.showinfo("Error","No Such Record")

    con.commit()
    con.close()    


        

#++++++++++++++<<<<<<<<<<<<<<<<<<<<<<<<<<ORDER DATA>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



def Order():
    global screen2,Order_table,ORD_NUM_var,ORD_AMOUNT_var,ADVANCE_AMOUNT_var,ORD_DATE_var,CUST_CODE_var,AGENT_CODE_var,ORD_DESCRIPTION_var,Search_by,Search_txt
    screen2=Toplevel(screen)
    screen2.title("Order Record")
    screen2.geometry("1350x700+0+0")
    
    
    
    title=Label(screen2,text="Order Details",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
    title.pack(side=TOP,fill=X)
    
    #_____Variables______
    ORD_NUM_var=StringVar()
    ORD_AMOUNT_var=StringVar()
    ADVANCE_AMOUNT_var=StringVar()
    ORD_DATE_var=StringVar()
    CUST_CODE_var=StringVar()
    AGENT_CODE_var=StringVar()
    ORD_DESCRIPTION_var=StringVar()
    
    Search_by=StringVar()
    Search_txt=StringVar()
    
    
    
    
    # ++++++++++Manage Frame++++++++++
    Manage_Frame=Frame(screen2,bd=4,relief=RIDGE,bg="light pink")
    Manage_Frame.place(x=20,y=100,width=500,height=590)
    
    m_title=Label(Manage_Frame,text="Manage Orders",bg="light pink",fg="green",font=("times new roman",30,"bold"))
    m_title.grid(row=0,columnspan=2,pady=20)
    
    lbl_ORD_NUM=Label(Manage_Frame,text="Order No.",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    lbl_ORD_NUM.grid(row=1,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_ORD_NUM=Entry(Manage_Frame,textvariable=ORD_NUM_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_ORD_NUM.grid(row=1,column=1,pady=10,padx=20,sticky="w")
    
    
    
    lbl_ORD_AMOUNT=Label(Manage_Frame,text="Order Amount",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    lbl_ORD_AMOUNT.grid(row=2,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_ORD_AMOUNT=Entry(Manage_Frame,textvariable=ORD_AMOUNT_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_ORD_AMOUNT.grid(row=2,column=1,pady=10,padx=20,sticky="w")
    
    
    lbl_ADVANCE_AMOUNT=Label(Manage_Frame,text="Advance Amount",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    lbl_ADVANCE_AMOUNT.grid(row=3,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_ADVANCE_AMOUNT=Entry(Manage_Frame,textvariable=ADVANCE_AMOUNT_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_ADVANCE_AMOUNT.grid(row=3,column=1,pady=10,padx=20,sticky="w")
    
    lbl_ORD_DATE=Label(Manage_Frame,text="Order Date",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    lbl_ORD_DATE.grid(row=4,column=0,pady=10,padx=20,sticky="w")
    lbl=Label(Manage_Frame,text="*Enter Date AS (YY-MM-DD)",bg="light pink",fg="Red",font=("times new roman",10,"bold"))
    lbl.place(x=15,y=310)
    #>>>>>>>>>Entry field>>>>>>>>
    txt_ORD_DATE=Entry(Manage_Frame,textvariable=ORD_DATE_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_ORD_DATE.grid(row=4,column=1,pady=10,padx=20,sticky="w")
    
    lbl_CUST_CODE=Label(Manage_Frame,text="Customer Code",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    lbl_CUST_CODE.grid(row=5,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_CUST_CODE=Entry(Manage_Frame,textvariable=CUST_CODE_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_CUST_CODE.grid(row=5,column=1,pady=10,padx=20,sticky="w")
    
    
    lbl_AGENT_CODE=Label(Manage_Frame,text="Agent Code",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    lbl_AGENT_CODE.grid(row=6,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_AGENT_CODE=Entry(Manage_Frame,textvariable=AGENT_CODE_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_AGENT_CODE.grid(row=6,column=1,pady=10,padx=20,sticky="w")
    
    lbl_ORD_DESCRIPTION=Label(Manage_Frame,text="Order Description",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    lbl_ORD_DESCRIPTION.grid(row=7,column=0,pady=10,padx=20,sticky="w")
    
    #>>>>>>>>>Entry field>>>>>>>>
    txt_ORD_DESCRIPTION=Entry(Manage_Frame,textvariable=ORD_DESCRIPTION_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_ORD_DESCRIPTION.grid(row=7,column=1,pady=10,padx=20,sticky="w")
    
    
    #+++++++++++++++BUTTON FRAME+++++++++++++++
    btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="light pink")
    btn_Frame.place(x=6,y=500,width=484)
    
    Addbtn=Button(btn_Frame,text="Add",width=10,command=Oadd_order,cursor="hand2").grid(row=0,column=0,padx=10,pady=10)
    Updatebtn=Button(btn_Frame,text="Update",width=10,command=Oupdate_data,cursor="hand2").grid(row=0,column=1,padx=10,pady=10)
    Deletbtn=Button(btn_Frame,text="Delete",width=10,command=Odelete_data,cursor="hand2").grid(row=0,column=2,padx=10,pady=10)
    clearbtn=Button(btn_Frame,text="Clear",width=10,command= Oclear,cursor="hand2").grid(row=0,column=3,padx=10,pady=10)
    menubtn=Button(btn_Frame,text="Menu",width=10,cursor="hand2",command=screen2.destroy).grid(row=0,column=4,padx=10,pady=10)
    
    
    
    #+++++++++++++Detail Frame+++++++++++++++
    Detail_Frame=Frame(screen2,bd=4,relief=RIDGE,bg="light pink")
    Detail_Frame.place(x=530,y=100,width=800,height=590)
    
    lbl_Search=Label(Detail_Frame,text="Search By",bg="light pink",fg="green",font=("times new roman",20,"bold"))
    lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
    
    combo_Search=ttk.Combobox(Detail_Frame,textvariable=Search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
    combo_Search['values']=("ORD_NUM","ORD_DATE","CUST_CODE")
    combo_Search.grid(row=0,column=1,padx=20,pady=10)
    
    txt_Search=Entry(Detail_Frame,textvariable=Search_txt,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
    txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
    
    searchbtn=Button(Detail_Frame,text="Search",width=10,command=Osearch_data,cursor="hand2").grid(row=0,column=3,padx=10,pady=10)
    showallbtn=Button(Detail_Frame,text="Show All",width=10,command=Ofetch_data,cursor="hand2").grid(row=0,column=4,padx=10,pady=10)
    
    
    #++++++Table Frame++++++++++++++
    Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="light pink")
    Table_Frame.place(x=10,y=70,width=760,height=480)
    
    
    scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
   
    Order_table=ttk.Treeview(Table_Frame,columns=("ORD_NUM","ORD_AMOUNT","ADVANCE_AMOUNT","ORD_DATE","CUST_CODE","AGENT_CODE","ORD_DESCRIPTION"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=Order_table.xview)
    scroll_y.config(command=Order_table.yview)
    Order_table.heading("ORD_NUM",text="ORD_NUM")
    Order_table.heading("ORD_AMOUNT",text="ORD_AMOUNT")
    Order_table.heading("ADVANCE_AMOUNT",text="ADVANCE_AMOUNT")
    Order_table.heading("ORD_DATE",text="ORD_DATE")
    Order_table.heading("CUST_CODE",text="CUST_CODE")
    Order_table.heading("AGENT_CODE",text="AGENT_CODE")
    Order_table.heading("ORD_DESCRIPTION",text="ORD_DESCRIPTION")
    Order_table['show']='headings'
    Order_table.column("ORD_NUM",width=150)
    Order_table.column("ORD_AMOUNT",width=150)
    Order_table.column("ADVANCE_AMOUNT",width=150)
    Order_table.column("ORD_DATE",width=150)
    Order_table.column("CUST_CODE",width=150)
    Order_table.column("AGENT_CODE",width=150)
    Order_table.column("ORD_DESCRIPTION",width=150)
    Order_table.pack(fill=BOTH,expand=1)
    Order_table.bind("<ButtonRelease-1>",Oget_cursor)
    Ofetch_data()


    
def Oadd_order():
    if CUST_CODE_var.get()=="" or ORD_NUM_var.get()=="" or ORD_AMOUNT_var.get()=="" or ADVANCE_AMOUNT_var.get()=="" or ORD_DATE_var.get()=="" or AGENT_CODE_var.get()=="" or ORD_DESCRIPTION_var.get()=="":
        messagebox.showerror("Error","All fields are required!!!",parent=screen2)
    elif not re.match("(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])", ORD_DATE_var.get()): # validating the date
        messagebox.showerror("Error","Please enter valid date",parent=screen2)
    elif not re.match("(^\d{2,6})$",ORD_NUM_var.get()):
        messagebox.showerror("Error","Please Enter Valid Order Number",parent=screen2)
    elif not re.match("(^[C]?\d{2,5})$",CUST_CODE_var.get()):
        messagebox.showerror("Error","Please Enter Valid Customer Code",parent=screen2)
    elif not re.match("(^[A]?\d{2,5})$",AGENT_CODE_var.get()):
        messagebox.showerror("Error","Please Enter Valid Agent Code",parent=screen2)
    elif not re.match("^[0-9]*(\.[0-9]{0,2})?$",ORD_AMOUNT_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty for Order Amount",parent=screen2)
       
    elif not re.match("^[0-9]*(\.[0-9]{0,2})?$",ADVANCE_AMOUNT_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty for Advance Amount",parent=screen2)
             
    else:
        con=pymysql.connect(host="localhost",user="root",password="",database="sales")
        cur=con.cursor()
        cur.execute("insert into orders (ORD_NUM,ORD_AMOUNT,ADVANCE_AMOUNT,ORD_DATE,CUST_CODE,AGENT_CODE,ORD_DESCRIPTION) values(%s,%s,%s,%s,%s,%s,%s)",(ORD_NUM_var.get(),
                                                                ORD_AMOUNT_var.get(),
                                                                ADVANCE_AMOUNT_var.get(),
                                                                ORD_DATE_var.get(),
                                                                CUST_CODE_var.get(),
                                                                AGENT_CODE_var.get(),
                                                                ORD_DESCRIPTION_var.get()
                                                                ))
       
        con.commit()
        Ofetch_data()
        Oclear()
        con.close()
        messagebox.showinfo("Success","Record has been inserted")

def Ofetch_data():
    con=pymysql.connect(host="localhost",user="root",password="",database="sales")
    cur=con.cursor()
    cur.execute("select * from orders")
    rows=cur.fetchall()
    if len(rows)!=0:
        Order_table.delete(*Order_table.get_children())
        for row in rows:
            Order_table.insert('',END,values=row)
        con.commit()
    con.close()
    
def Oclear():
    ORD_NUM_var.set("")
    ORD_AMOUNT_var.set("")
    ADVANCE_AMOUNT_var.set("")
    ORD_DATE_var.set("")
    CUST_CODE_var.set("")
    AGENT_CODE_var.set("")
    ORD_DESCRIPTION_var.set("")
 

#________Selected data from table will display in the fields_______
def Oget_cursor(ev):
    cursor_row=Order_table.focus()
    contents=Order_table.item(cursor_row)
    row=contents['values']
    ORD_NUM_var.set(row[0])
    ORD_AMOUNT_var.set(row[1])
    ADVANCE_AMOUNT_var.set(row[2])
    ORD_DATE_var.set(row[3])
    CUST_CODE_var.set(row[4])
    AGENT_CODE_var.set(row[5])
    ORD_DESCRIPTION_var.set(row[6])
    
def Oupdate_data():
    if not re.match("(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])", ORD_DATE_var.get()): # validating the date
        messagebox.showerror("Error","Please enter valid date",parent=screen2)
    elif not re.match("(^\d{2,6})$",ORD_NUM_var.get()):
        messagebox.showerror("Error","Please Enter Valid Order Number",parent=screen2)
    elif not re.match("(^[C]?\d{2,5})$",CUST_CODE_var.get()):
        messagebox.showerror("Error","Please Enter Valid Customer Code",parent=screen2)
    elif not re.match("(^[A]?\d{2,5})$",AGENT_CODE_var.get()):
        messagebox.showerror("Error","Please Enter Valid Agent Code",parent=screen2)
    elif not re.match("^[0-9]*(\.[0-9]{0,2})?$",ORD_AMOUNT_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty for Order Amount",parent=screen2)
       
    elif not re.match("^[0-9]*(\.[0-9]{0,2})?$",ADVANCE_AMOUNT_var.get()):
        messagebox.showerror("Error","Please Check Your Enrty for Advance Amount",parent=screen2)
    else:
        con=pymysql.connect(host="localhost",user="root",password="",database="sales")
        cur=con.cursor()
        cur.execute("update orders set ORD_AMOUNT=%s,ADVANCE_AMOUNT=%s,ORD_DATE=%s,CUST_CODE=%s,AGENT_CODE=%s,ORD_DESCRIPTION=%s where ORD_NUM=%s",(
                                                                    ORD_AMOUNT_var.get(),
                                                                    ADVANCE_AMOUNT_var.get(),
                                                                    ORD_DATE_var.get(),
                                                                    CUST_CODE_var.get(),
                                                                    AGENT_CODE_var.get(),
                                                                    ORD_DESCRIPTION_var.get(),
                                                                    ORD_NUM_var.get()
                                                                    ))
        con.commit()
        Ofetch_data()
        Oclear()
        con.close()
        messagebox.showinfo("Success","Record has been Updated")
    
        
def Odelete_data():
    con=pymysql.connect(host="localhost",user="root",password="",database="sales")
    cur=con.cursor()
    cur.execute("delete from orders where ORD_NUM=%s",ORD_NUM_var.get())
    con.commit()
    con.close()
    Ofetch_data()
    Oclear()
    messagebox.showinfo("Success","Record has been Deleted")

    
def Osearch_data():
    con=pymysql.connect(host="localhost",user="root",password="",database="sales")
    cur=con.cursor()
    cur.execute("select * from orders where "+str(Search_by.get()) +"=%s",(str(Search_txt.get())))
    rows=cur.fetchall()
    if len(rows)!=0:
        Order_table.delete(*Order_table.get_children())
        for row in rows:
            Order_table.insert('',END,values=row)
    else:
        messagebox.showinfo("Error","No Such Record")

    con.commit()
    con.close()    



#+++++++++++++++++++++<<<<<<<<<<<<<<<<<<<<<REPORT >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



def Report():
    global screen3,Search_by,Search_txt,Agent_table
    screen3=Toplevel(screen)
    screen3.title("Report")
    screen3.geometry("1350x700+0+0")
    Search_by=StringVar()
    Search_txt=StringVar()
    screen3.configure(background="sky blue")
    
    
    
    
    
    
    title=Label(screen3,text="WELCOME TO REPORT SECTION",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="white",fg="Navy Blue")
    title.pack(side=TOP,fill=X)
    
    lbl_Search=Label(screen3,text="Search By",width=10,bg="white",fg="green",font=("times new roman",20,"bold")).place(x=50,y=100)
    
    combo_Search=ttk.Combobox(screen3,textvariable=Search_by,width=50,font=("times new roman",13,"bold"),state='readonly')
    combo_Search['values']=("Balance Amount Of Orders","Country With maximum no. of register Customer")
    combo_Search.place(x=230,y=100)
    
    continuehbtn=Button(screen3,text="Continue",width=7,command=balance_amt,font=("times new roman",20,"bold"),fg="green",bg="white",cursor="hand2").place(x=720,y=100)
    menuhbtn=Button(screen3,text="Back To Menu",width=10,command=screen3.destroy,font=("times new roman",20,"bold"),fg="green",bg="white",cursor="hand2").place(x=850,y=100)


    
def balance_amt():
    if Search_by.get()=="Balance Amount Of Orders":
        Table_Frame=Frame(screen3,bd=4,relief=RIDGE,bg="light pink")
        Table_Frame.place(x=30,y=170,width=1300,height=500)
    
    
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
   
        Agent_table=ttk.Treeview(Table_Frame,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Agent_table.xview)
        scroll_y.config(command=Agent_table.yview)
        Agent_table.heading(1,text="Cust_code")
        Agent_table.heading(2,text="Cust_name")
        Agent_table.heading(3,text="Cust_city")
        Agent_table.heading(4,text="Working_area")
        Agent_table.heading(5,text="Cust_country")
        Agent_table.heading(6,text="Grade")
        Agent_table.heading(7,text="Opening_amt")
        Agent_table.heading(8,text="Receive_amt")
        Agent_table.heading(9,text="Payment_amt")
        Agent_table.heading(10,text="Outsanding_amt")
        Agent_table.heading(11,text="Phone_no")
        Agent_table.heading(12,text="Agent_code")
        Agent_table.heading(13,text="Agent_name")
        Agent_table['show']='headings'
        Agent_table.column(1,width=150)
        Agent_table.column(2,width=150)
        Agent_table.column(3,width=150)
        Agent_table.column(4,width=150)
        Agent_table.column(5,width=150)
        Agent_table.column(6,width=150)
        Agent_table.column(7,width=150)
        Agent_table.column(8,width=150)
        Agent_table.column(9,width=150)
        Agent_table.column(10,width=150)
        Agent_table.column(11,width=150)
        Agent_table.column(12,width=150)
        Agent_table.column(13,width=150)
    
        Agent_table.pack(fill=BOTH,expand=1)
    
        con=pymysql.connect(user="root",password="",database="sales",host="localhost")
        cur=con.cursor()
        cur.execute("SELECT * FROM customer,agents ORDER BY OUTSTANDING_AMT DESC")
        
        rows=cur.fetchall()
        if len(rows)!=0:
            Agent_table.delete(*Agent_table.get_children())
            for row in rows:
                Agent_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    elif Search_by.get()=="Country With maximum no. of register Customer":
        Table_Frame=Frame(screen3,bd=4,relief=RIDGE,bg="light pink")
        Table_Frame.place(x=30,y=170,width=1300,height=500)
    
    
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
   
        Agent_table=ttk.Treeview(Table_Frame,columns=(1,2,3),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Agent_table.xview)
        scroll_y.config(command=Agent_table.yview)
        Agent_table.heading(1,text="Cust_country")
        Agent_table.heading(2,text="Payment_amt")
        Agent_table.heading(3,text="Outsanding_amt")
        Agent_table['show']='headings'
        Agent_table.column(1,width=150)
        Agent_table.column(2,width=150)
        Agent_table.column(3,width=150)

        Agent_table.pack(fill=BOTH,expand=1)
    
        con=pymysql.connect(user="root",password="",database="sales",host="localhost")
        cur=con.cursor()
        cur.execute("SELECT  CUST_COUNTRY,SUM(PAYMENT_AMT),SUM(OUTSTANDING_AMT) FROM customer GROUP BY (CUST_COUNTRY) DESC")
        
        rows=cur.fetchall()
        if len(rows)!=0:
            Agent_table.delete(*Agent_table.get_children())
            for row in rows:
                Agent_table.insert('',END,values=row)
            con.commit()
        con.close()
        
    
    else:
       messagebox.showerror("Error","Please select One option")
    
    
    


#function to open Analysis Window

def Analysis_window():
    screen.destroy()
    import analysis


# function to open login window

def tm_window():
    screen.destroy()
    import analysis2
    
def login_window():
    screen.destroy()
    import ILogin    


#++++++++++++++++++++++++++<<<<<<<<<<<<<<<<<<<<<<<<<MENU PAGE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def Sunville():
    global screen
    screen=Tk()

    screen.title("Sunville Window")
    screen.geometry("1350x700+0+0")
    screen.config(bg="white")
    agent_icon=PhotoImage(file="C:\\python-junaid sir\\Internship analysis and gui\\agent.png")
    customer_icon=PhotoImage(file="C:\\python-junaid sir\\Internship analysis and gui\\cust.png")
    order_icon=PhotoImage(file="C:\\python-junaid sir\\Internship analysis and gui\\order.png")
    report_icon=PhotoImage(file="C:\\python-junaid sir\\Internship analysis and gui\\report.png")
    analysis_icon=PhotoImage(file="C:\\python-junaid sir\\Internship analysis and gui\\analysis.png")
    bg_icon=ImageTk.PhotoImage(Image.open("C:\\python-junaid sir\\Internship analysis and gui\\background.jpeg"))
    signout_icon=ImageTk.PhotoImage(Image.open("C:\\python-junaid sir\\Internship analysis and gui\\sign_out.png"))
    
    
    title=Label(screen,text="Welcome To Sunville Property",font=("times new roman",40,"bold"),bg="white",fg="Navy blue",bd=10,relief=GROOVE)
    title.place(x=0,y=0,relwidth=1)
    
    
    bg_lbl=Label(screen,image=bg_icon).place(x=0,y=90)
    
    
    #left image
    left_image=ImageTk.PhotoImage(file="C:\\python-junaid sir\\Internship analysis and gui\\side (1).png")
    left=Label(screen,image=left_image).place(x=80,y=130,width=400,height=540)
    left_image.image=left_image
    
    #register frame
    frame1=Frame(screen,bg="light pink")
    frame1.place(x=480,y=130,width=700,height=540)
    
    title=Label(frame1,text="Menu",font=("times new roman",20,"bold"),bg="light pink",fg="green").place(x=0,y=30,width=700)
    
    agentbtn=Button(frame1,text="Agent Record",width=250,cursor="hand2",image=agent_icon,compound=LEFT,command=Agent,font=("times new roman",15,"bold")).place(x=200,y=80)
    
   
    customerbtn=Button(frame1,text="Customer Record",width=250,cursor="hand2",image=customer_icon,compound=LEFT,command=Customer,font=("times new roman",15,"bold")).place(x=200,y=160)
    orderbtn=Button(frame1,text="Order Record",width=250,cursor="hand2",image=order_icon,compound=LEFT,command=Order,font=("times new roman",15,"bold")).place(x=200,y=240)
    reporbtn=Button(frame1,text="Report",width=250,cursor="hand2",image=report_icon,compound=LEFT,command=Report,font=("times new roman",15,"bold")).place(x=200,y=320)
    analysisbtn=Button(frame1,text="Analysis",width=250,cursor="hand2",image=analysis_icon,compound=LEFT,command=Analysis_window,font=("times new roman",15,"bold")).place(x=200,y=400)
    analysis1btn=Button(frame1,text="Time Series Analysis",width=250,cursor="hand2",image=analysis_icon,compound=LEFT,command=tm_window,font=("times new roman",15,"bold")).place(x=200,y=480)
    signoutbtn=Button(frame1,text="Sign out",width=180,height=50,cursor="hand2",image=signout_icon,compound=LEFT,command=login_window,font=("times new roman",15,"bold")).place(x=500,y=0)
    
    screen.mainloop()
    
Sunville()

