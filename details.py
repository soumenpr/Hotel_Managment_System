from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime
class DeatalisRoom:
   def __init__(self, root):
    from tkinter import Label, Entry, Button, StringVar

    self.root = root
    self.root.title("Admin Login")
    self.root.geometry("500x300")  # Increase size as you wish

    # Clear any previous widgets
    for widget in self.root.winfo_children():
        widget.destroy()

    Label(self.root, text="Admin Username:", font=("Arial", 14)).pack(pady=15)
    username_var = StringVar()
    Entry(self.root, textvariable=username_var, font=("Arial", 14)).pack()

    Label(self.root, text="Admin Password:", font=("Arial", 14)).pack(pady=15)
    password_var = StringVar()
    Entry(self.root, textvariable=password_var, show="*", font=("Arial", 14)).pack()

    def check_login():
        if username_var.get() == "admin" and password_var.get() == "2005":
            # Clear login widgets
            for widget in self.root.winfo_children():
                widget.destroy()
            self.show_details_ui()  # Call your main UI setup
        else:
            messagebox.showerror("Access Denied", "You are not authorized to access this page.", parent=self.root)
            self.root.destroy()

    Button(self.root, text="Login", command=check_login, font=("Arial", 14), width=12).pack(pady=25)

    def show_details_ui(self):
           self.root.title("Details")
           self.root.geometry("1295x550+130+120")
    # ...rest of your existing UI code...
           self.root=root
           self.root.title("Details")
           self.root.geometry("1295x550+130+120")
      #*****Title*****
           bg_img = Image.open("IMAGE/taj.jpg")
           bg_img = bg_img.resize((1295, 500), Image.LANCZOS)
           self.bg = ImageTk.PhotoImage(bg_img)
           lblbg = Label(self.root, image=self.bg)
           lblbg.place(x=0, y=50, relwidth=1, relheight=1)
           lb1_title = Label(self.root, text="Room Booking", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
           lb1_title.place(x=0, y=0, width=1295, height=50)
           
           #******Logo****
           img2=Image.open(r"photo/logo.jpg")
           img2=img2.resize((100,40),Image.LANCZOS)
           self.photoimg2=ImageTk.PhotoImage(img2)
           lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
           lblimg.place(x=5,y=2,width=100,height=40)
           #******labelFrame****
           labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",bg="cyan",fg="green",font=("times new roman",23,"bold"),padx=2)
           labelframeleft.place(x=5,y=50,width=540,height=350)
           #****labels and entry****
           #floor
           lb1_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),bg="cyan",padx=2,pady=6)
           lb1_floor.grid(row=0,column=0,sticky=W)
           self.var_floor=StringVar()
           enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=29,font=("arial",13 ,"bold"))
           enty_floor.grid(row=0,column=1)
            #Room No
           lb1_room_no=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),bg="cyan",padx=2,pady=6)
           lb1_room_no.grid(row=1,column=0,sticky=W)
           self.var_roomNo=StringVar()
           enty_room_no=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,width=29,font=("arial",13 ,"bold"))
           enty_room_no.grid(row=1,column=1)
            #Room Type
           lb1_room_type=Label(labelframeleft,text="Room Type",bg="cyan",font=("arial",12,"bold"),padx=2,pady=6)
           lb1_room_type.grid(row=2,column=0,sticky=W)
           self.var_RoomType=StringVar()
           enty_room_type=ttk.Combobox(labelframeleft,textvariable=self.var_RoomType,width=27,font=("arial",13 ,"bold"),state="readonly")
           enty_room_type["value"]=("Single","Double","Luxary")
           enty_room_type.current(0)
           enty_room_type.grid(row=2,column=1)
            #btn
           btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
           btn_frame.place(x=0,y=200,height=40,width=312)

           btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",14,"bold"),bg="black",fg="gold",width=8)
           btnAdd.grid(row=0,column=0,padx=1)

           #btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",14,"bold"),bg="black",fg="gold",width=8)
           #btnUpdate.grid(row=0,column=1,padx=1)

           btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",14,"bold"),bg="black",fg="gold",width=8)
           btnDelete.grid(row=0,column=2,padx=1)

           btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",14,"bold"),bg="black",fg="gold",width=8)
           btnReset.grid(row=0,column=3,padx=1)
           #****table frame search system****
           table_frame=LabelFrame(self.root,relief=RIDGE,text="Show Room Details",font=("arial",20,"bold"),fg="red",padx=2)
           table_frame.place(x=600,y=55,width=600,height=350)

           scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
           scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
           self.room_table=ttk.Treeview(table_frame,column=("floor","roomno","roomType"),
            
           xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
           scroll_x.pack(side=BOTTOM,fill=X)
           scroll_y.pack(side=RIGHT,fill=Y)

           scroll_x.config(command=self.room_table.xview)
           scroll_y.config(command=self.room_table.yview)

           self.room_table.heading("floor",text="Floor")
           self.room_table.heading("roomno",text="Room No")
           self.room_table.heading("roomType",text="Room Type")
           
           self.room_table["show"]="headings"

           self.room_table.column("floor",width=100)
           self.room_table.column("roomno",width=100)
           self.room_table.column("roomType",width=100)
           
           self.room_table.pack(fill=BOTH,expand=1)
           self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
           self.fetch_data()
         #add
    def add_data(self):
            if self.var_floor.get() == "" or self.var_RoomType.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                  try:
                        conn = mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
                        my_cursor = conn.cursor()
            
                        my_cursor.execute("INSERT into details VALUES (%s, %s, %s)",(
                                                                           self.var_floor.get(),
                                                                           self.var_roomNo.get(),
                                                                           self.var_RoomType.get()
                                                                           ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "Room added Successfully", parent=self.root)
                  except Exception as es:
                       messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
    def fetch_data(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from details")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                  self.room_table.delete(*self.room_table.get_children())
                  for i in rows:
                        self.room_table.insert("",END,values=i)
                  conn.commit()
            conn.close()
    def get_cuersor(self,events=""):
            cusrson_rows=self.room_table.focus()
            content=self.room_table.item(cusrson_rows)
            row=content["values"]
            self.var_floor.set(row[0]),
            self.var_roomNo.set(row[1]),
            self.var_RoomType.set(row[2]),
            
            
    def update(self):
             if self.var_roomNo.get()=="":
                   messagebox.showerror("Error","Please enter valid Room No",parent=self.root)
             else:
                   conn= mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
                   my_cursor = conn.cursor()
                   my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                          self.var_floor.get(),
                                                                                          self.var_RoomType.get(),
                                                                                          self.var_roomNo.get(),
                                                                                    ))
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Update","Room Details has been updated seccessfully",parent=self.root)

    def delete(self):
            delete=messagebox.askyesno("Hotel Management system","Do you went delete this Room Details",parent=self.root)
            if delete>0:
                  conn= mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
                  my_cursor = conn.cursor()
                  query="delete from details where RoomNo=%s"
                  value=(self.var_roomNo.get(),)
                  my_cursor.execute(query,value)
            else:
                  if not delete:
                        return
            conn.commit()
            self.fetch_data()
            conn.close()
    def reset(self):
            self.var_floor.set(""),
            self.var_roomNo.set(""),
            self.var_RoomType.set("")

  