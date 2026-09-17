from tkinter import *
from PIL import Image,ImageTk  
from customer import Cust_Win
from Room import roombooking
from details import DeatalisRoom
from aboutus import report
from tkinter import messagebox
from login import LoginWindow

class HotelManagementSystem:
      def __init__(self,root):
            self.root=root
            self.root.title("Hotel Managemant Sysrem")
            self.root.geometry('1900x1250+0+0')
            #******First image****
            img1=Image.open("IMAGE/hotel1.png")
            img1=img1.resize((1550,140),Image.LANCZOS)
            self.photoimg1=ImageTk.PhotoImage(img1)

            lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
            lblimg.place(x=0,y=0,width=1550,height=140)

            #******Logo****
            img2=Image.open("photo/logo.jpg")
            img2=img2.resize((230,140),Image.LANCZOS) 
            self.photoimg2=ImageTk.PhotoImage(img2)

            lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
            lblimg.place(x=0,y=0,width=230,height=140)
            #*****Title*****
            lb1_title=Label(self.root,text="SUNWAVE HOTEL",font=("times new roman",40,"bold"),bg="yellow",fg="black",bd=4,relief=RIDGE)
            lb1_title.place(x=0,y=140,width=1550,height=50)
            #*****Main Frame****
            main_frame=Frame(self.root,bd=4,relief=RIDGE)
            main_frame.place(x=0,y=190,width=1550,height=620)
            #****menu***
            lb1_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
            lb1_menu.place(x=0,y=0,width=230)
            #***bottom Frame***
            btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
            btn_frame.place(x=0,y=35,width=228,height=190)
            
            cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
            cust_btn.grid(row=0,column=0,pady=1)

            room_btn=Button(btn_frame,text="ROOM",command=self.room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
            room_btn.grid(row=1,column=0,pady=1)

            details_btn=Button(btn_frame,text="DETAILS",command=self.detailsroom,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
            details_btn.grid(row=2,column=0,pady=1)

            report_btn=Button(btn_frame,text="ABOUT US",command=self.report,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
            report_btn.grid(row=3,column=0,pady=1)

            logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
            logout_btn.grid(row=4,column=0,pady=1)
            #****right side image***
            img3=Image.open(r"photo/front.jpg")
            img3=img3.resize((1310,590),Image.LANCZOS)
            self.photoimg3=ImageTk.PhotoImage(img3)

            lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
            lblimg1.place(x=225,y=0,width=1310,height=590)
            #****down image****
            img4=Image.open(r"photo/side1.jpg")
            img4=img4.resize((230,210),Image.LANCZOS)
            self.photoimg4=ImageTk.PhotoImage(img4)

            lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
            lblimg1.place(x=0,y=225,width=230,height=100)

            img5=Image.open(r"IMAGE/khana.jpg")
            img5=img5.resize((230,190),Image.LANCZOS)
            self.photoimg5=ImageTk.PhotoImage(img5)

            lblimg1=Label(main_frame,image=self.photoimg5,bd=5,relief=RIDGE)
            lblimg1.place(x=0,y=325,width=230,height=190)




      def cust_details(self):
                 self.new_window=Toplevel(self.root)
                 self.app=Cust_Win(self.new_window)
      
      def room(self):
                 self.new_window=Toplevel(self.root)
                 self.app=roombooking(self.new_window)
      
      def detailsroom(self):
                 self.new_window=Toplevel(self.root)
                 self.app=DeatalisRoom(self.new_window)
      def report(self):
                 self.new_window=Toplevel(self.root)
                 self.app=report(self.new_window)
      def logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.root.destroy()

if __name__=='__main__':
    root=Tk()
    login = LoginWindow(root)
    root.mainloop()