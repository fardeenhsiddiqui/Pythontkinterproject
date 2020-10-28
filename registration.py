from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Windows")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #=======Image=============
        im1=Image.open("E:\\python3.8\\Gallery\\bokeh-png.png")
        self.bg1= ImageTk.PhotoImage(im1.resize((1100,700), Image.ANTIALIAS))
        bg1_lbl=Label(self.root,image=self.bg1,bd=0).place(x=200,y=0,relwidth=1,relheight=1)

        #=========leftimage=======
        im2=Image.open("E:\\python3.8\\Gallery\\moti (1).jpg")
        self.bg2= ImageTk.PhotoImage(im2.resize((400,500), Image.ANTIALIAS))
        bg2_lbl=Label(self.root,image=self.bg2,bd=0).place(x=70,y=100)


        #==========Registration frame========
        frame1=Frame(self.root,bg="white")
        frame1.place(x=470,y=100,width=700,height=500)

        #===========title
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        #==========Row1 ============username,password============
        #self.var_fname=StringVar()
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        #==========Row2 ============
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

        #==========Row3 ============
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cmb_ques=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_ques['value']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_ques.place(x=50,y=270,width=250)
        self.cmb_ques.current(0)
        


        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)

        #=======================================
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)



        #============Term condition
        self.var_chk=IntVar()
        chk = Checkbutton(frame1,text="I Agree The Term & Condition",bg="white",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",12)).place(x=50,y=380)

        self.btn_regiter=Button(frame1,text="REGISTER NOW ->",font=("times new roman",15,"bold"),bg="green",bd=0,
                   activebackground="green",activeforeground="#00759E",command=self.register_data).place(x=50,y=420,width=250)

        btn_login=Button(self.root,text="Sign In",font=("times new roman",20,"bold"),command=self.login_window,bg="white",cursor='hand2').place(x=80,y=390,width=130)

        #==========================



    def login_window(self):
        self.root.destroy()
        import login


        
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.cmb_ques.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" or self.txt_contact.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)

        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm password should be same",parent=self.root)

        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our terms & Condition",parent=self.root)
        else:

            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="loginpage")
                cur=con.cursor()
                cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                            (self.txt_fname.get(),
                             self.txt_lname.get(),
                             self.txt_contact.get(),
                             self.txt_email.get(),
                             self.cmb_ques.get(),
                             self.txt_answer.get(),
                             self.txt_password.get()
                             ) )
                con.commit()
                con.close()
                messagebox.showinfo("success","Register Successful",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
            
            
              

        

        
        
                           



root=Tk()
obj=Register(root)
root.mainloop()
