from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Sunville Property")
        self.root.geometry("1030x600+100+50")
        self.root.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file = "C:\\python-junaid sir\\Internship analysis and gui\\intern.jpeg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        
        Frame_login=Frame(self.root,bg="White")
        Frame_login.place(x=150,y=150,height=340,width=500)
        
        
        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Employee Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)
        
        email=Label(Frame_login,text="Email Address",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=90,y=140)
        self.txt_email=Entry(Frame_login,font=("times new roman",15),bg="light gray")
        self.txt_email.place(x=90,y=170,width=350,height=35)
        
        
        lbl_password=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_password=Entry(Frame_login,show='*',font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=90,y=240,width=350,height=35)
        
        
        forget_btn=Button(Frame_login,text="Forget Password?",cursor="hand2",command=self.forget_window,bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)
        Login_btn=Button(self.root,command=self.login_function,cursor="hand2",text="Login",fg="white",bg="#d77337",font=("times new roman",20)).place(x=300,y=470,width=180,height=40)
        
        
        NewRegister_btn=Button(Frame_login,text="New Registration",cursor="hand2",command=self.register_window,bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=220,y=280)
    
    def forget_pass(self):
        if self.cmb_quest.get()=="Select" or self.txt_ans.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="sales")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and question=%s and ans=%s",(self.txt_email.get(),self.cmb_quest.get(),self.txt_ans.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select the correct Security Question/ Enter Answer",parent=self.root2)
                    
                else:
                    cur.execute("Update employee set password=%s  where email=%s ",(self.txt_new_pass.get(),self.txt_email.get()))
                    
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your Password has been Reset, Please Login with new Password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                 messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
      
                
    
    def forget_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please Enter Email Id to reset Your Password",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="sales")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",(self.txt_email.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Enter Valid Email Id To reset your Password",parent=self.root)
                    
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+350+230")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
                
                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").pack()
                
                    question=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
                
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                    self.cmb_quest['values']=("select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)
                
                
                    ans=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
                    self.txt_ans=Entry(self.root2,font=("times new roman",15),bg="light gray")
                    self.txt_ans.place(x=50,y=210,width=270)
                    
                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
                    self.txt_new_pass=Entry(self.root2,show='*',font=("times new roman",15),bg="light gray")
                    self.txt_new_pass.place(x=50,y=290,width=270)
                    
                    btn_change_password=Button(self.root2,text="Reset Password",bg="green",fg="white",command=self.forget_pass,font=("times new roman",15,"bold")).place(x=90,y=340)
                
                    
                
        
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
      
        
    #Reset Forget Pass window    
    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_ans.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)
            
         
    
    def register_window(self):
        self.root.destroy()
        import Register
    
    def login_function(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="sales")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Usename/Password",parent=self.root)
                    
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    import kh
                    
                    
                con.close()
        
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
      
                
root=Tk()
obj=Login(root)
root.mainloop()