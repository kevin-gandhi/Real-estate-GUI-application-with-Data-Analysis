from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox  #combobox
import pymysql,re

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        
        #bg image
        self.bg=ImageTk.PhotoImage(file="C:\\python-junaid sir\\Internship analysis and gui\\background.jpeg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        #left image
        self.left=ImageTk.PhotoImage(file="C:\\python-junaid sir\\Internship analysis and gui\\side.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        
        #register frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        
        title=Label(frame1,text="Register Here",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        
        
        #_____Row1
       
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_fname.place(x=50,y=130,width=250)
        
        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_lname.place(x=370,y=130,width=250)
         
        #______________Row2
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_email.place(x=370,y=200,width=250)
         
        #_____________________Row3
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
        
        
        ans=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_ans=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_ans.place(x=370,y=270,width=270)
         
        #_______Row4
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,show='*',font=("times new roman",15),bg="light gray")
        self.txt_password.place(x=50,y=340,width=250)
        
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,show='*',font=("times new roman",15),bg="light gray")
        self.txt_cpassword.place(x=370,y=340,width=250)
        
        
        #__________Terms
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree Terms and Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
        self.btn_register=Button(frame1,text="Register Now",font=("times new roman",15,"bold"),bg="green",fg="white",bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
        
        btn_login=Button(frame1,text="Sign In",font=("times new roman",15,"bold"),command=self.login_window,bg="green",fg="white",bd=0,cursor="hand2").place(x=200,y=420)
        
    def login_window(self):
        self.root.destroy()
        import ILogin
    
    
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.txt_ans.delete(0,END)
        self.cmb_quest.current(0)
        self.var_chk.set(0)
        
        
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="select" or  self.txt_ans.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" or self.txt_contact.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif not re.match("^((\+)?(\d{3}[-])?(\d{10}){1})?(\d{11}){0,1}?$",self.txt_contact.get()):
            messagebox.showerror("Error","Please Enter Valid Phone No",parent=self.root)
        elif not re.match("^[a-zA-Z]*$",self.txt_fname.get()):
            messagebox.showerror("Error","Please Enter Valid Name",parent=self.root)
        elif not re.match("^[a-zA-Z]*$",self.txt_lname.get()):
            messagebox.showerror("Error","Please Enter Valid Name",parent=self.root)
        
        elif self.txt_password.get()!= self.txt_cpassword.get():
             messagebox.showerror("Error","Password and Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
             messagebox.showerror("Error","Please Agree our Terms And Condition",parent=self.root)
        elif not re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", self.txt_email.get()): # validating the email 
             messagebox.showerror("Error","Please enter valid email",parent=self.root)
              
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="sales")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",self.txt_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                     messagebox.showerror("Error","User already Exist,Please try with another email",parent=self.root)
                
                else:
                    cur.execute("insert into employee (f_name,l_name,contact,email,question,ans,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                   (self.txt_fname.get().capitalize(),
                                    self.txt_lname.get().capitalize(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.cmb_quest.get(),
                                    self.txt_ans.get(),
                                    self.txt_password.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successful",parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
            
            
            
            
            
            
              
              
    
    
    
root=Tk()
obj=Register(root)
root.mainloop()