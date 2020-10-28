from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


ima1 = Image.open("E:\\python3.8\\Gallery\\MYPIC.jpg")
ima1 = ima1.resize((500,650), Image.ANTIALIAS)
ima2 = Image.open("E:\\python3.8\\Gallery\\far.jpg")
ima2 = ima2.resize((500,750), Image.ANTIALIAS)
ima3 = Image.open("E:\\python3.8\\Gallery\\fardeen.jpg")
ima3 = ima3.resize((500,750), Image.ANTIALIAS)


class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #====image===
        image = Image.open("E:\\python3.8\\Gallery\\phone.png")
        image = image.resize((500,750), Image.ANTIALIAS)
        self.phone_image=ImageTk.PhotoImage(image)
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=20)


        #=====LoginFrame=====
        login_frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=720,y=120,width=350,height=460)

        title_frame =Label(login_frame,text="Login System",font="Elephant 30 bold",bg="white").place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Username",font="Andalus 15",bg="white",fg="#767171").place(x=50,y=100)
        self.username=StringVar()
        self.password=StringVar()
        txt_username=Entry(login_frame,textvariable=self.username,font=("times new roman", 15),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_pass=Label(login_frame,text="Password",font="Andalus 15",bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,font=("times new roman", 15),bg="#ECECEC",show="*").place(x=50,y=240,width=250)

        btn_login = Button(login_frame,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",
                           activebackground="#00B0F0",activeforeground="white",cursor="hand2",command=self.login).place(x=50,y=300,width=250,height=35)

        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)

        or_=Label(login_frame,text="OR",fg="lightgray",bg="white",font=("times new roman", 15,"bold")).place(x=150,y=355)

        btn_forget=Button(login_frame,text="Forget Password?",font=("times new roman", 13,"bold"),bg="white",fg="#00759E",bd=0,
                          activebackground="white",activeforeground="#00759E").place(x=100,y=390)

        #=====Frame2=========
        register_frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=720,y=600,width=350,height=60)

        lbl_reg=Label(register_frame,text="Don't have an account?",font=("times new roman", 13),bg="white").place(x=40,y=15)
        btn_snp =Button(register_frame,text="Sign Up",font=("times new roman", 13,"bold"),bd=0,fg="#00759E",bg="white",command=self.register_window,
                        activebackground="white",activeforeground="#00759E").place(x=210,y=13)





        #=====Animation======
        self.im1=ImageTk.PhotoImage(ima1)
        self.im2=ImageTk.PhotoImage(ima2)
        self.im3=ImageTk.PhotoImage(ima3)

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=456,y=134,width=235,height=519)

        self.animate()


    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)



    def register_window(self):
        self.root.destroy()
        import registration
        


    def login(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All Fields are required")
        
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="loginpage")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.username.get(),self.password.get()))
                r=cur.fetchone()
                if r==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD")
                else:
                    messagebox.showinfo("Success","Welcome")
                    self.root.destroy()
                    import snake
                con.close()
                    
                    
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to:{self(es)}")
            #messagebox.showinfo("Information",f"Welcome :{self.username.get()}\nYour Password: {self.password.get()}")



root = Tk()
obj = Login_System(root)
root.mainloop
