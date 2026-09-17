from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime
class roombooking:
      def __init__(self,root):
           self.root=root
           self.root.title("Room")
           self.root.geometry("1295x550+130+120")
           self.root.config(bg="light blue")
           #variables
           self.var_conatct=StringVar()
           self.var_chechin=StringVar()
           self.var_chechout=StringVar()
           self.var_roomtype=StringVar()
           self.var_roomavailable=StringVar()
           self.var_meal=StringVar()
           meal_options = [
                        "Breakfast",
                        "Lunch",
                        "Dinner",
                        "Breakfast + Lunch",
                        "Lunch + Dinner",
                        "Breakfast + Dinner",
                        "Breakfast + Lunch + Dinner"
                        ]
           self.var_noofdays=StringVar()
           self.var_paidtax=StringVar()
           self.var_actualtotal=StringVar()
           self.var_total=StringVar()
      
           #*****Title*****
           lb1_title=Label(self.root,text="Room Booking",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
           lb1_title.place(x=0,y=0,width=1295,height=50)
           
           #******Logo****
           img2=Image.open(r"photo/logo.jpg")
           img2=img2.resize((100,40),Image.LANCZOS)
           self.photoimg2=ImageTk.PhotoImage(img2)
           lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
           lblimg.place(x=5,y=2,width=100,height=40)
           #******labelFrame****
           labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking",font=("times new roman",12,"bold"),bg="teal",padx=2)
           labelframeleft.place(x=5,y=50,width=425,height=490)
           #****labels and entry****
           #customer contact
           lb1_cust_contact=Label(labelframeleft,text="Customer Contact:",font=("arial",12,"bold"),bg="teal",padx=2,pady=6)
           lb1_cust_contact.grid(row=0,column=0,sticky=W)
           enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_conatct,width=29,font=("arial",13 ,"bold"))
           enty_contact.grid(row=0,column=1)
           #fatch data button
           btnfatch=Button(labelframeleft,command=self.fatch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
           btnfatch.place(x=347,y=4)
           #check in date
           check_in_Date=Label(labelframeleft,text="Check in Date:",font=("arial",12,"bold"),bg="teal",padx=2,pady=6)
           check_in_Date.grid(row=1,column=0,sticky=W)
           check_in_Date=ttk.Entry(labelframeleft,textvariable=self.var_chechin,width=29,font=("arial",13 ,"bold"))
           check_in_Date.grid(row=1,column=1)
           #check out date
           check_out_Date=Label(labelframeleft,text="Check out Date:",font=("arial",12,"bold"),bg="teal",padx=2,pady=6)
           check_out_Date.grid(row=2,column=0,sticky=W)
           check_out_Date=ttk.Entry(labelframeleft,textvariable=self.var_chechout,width=29,font=("arial",13 ,"bold"))
           check_out_Date.grid(row=2,column=1)
           #Room type
           roomtype=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),bg="teal",padx=2,pady=6)
           roomtype.grid(row=3,column=0,sticky=W)
           try:
              conn = mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
              my_cursor = conn.cursor()
              my_cursor.execute("select distinct RoomType from details")
              rows1=my_cursor.fetchall()
              conn.close()
           except Exception as e:
                 messagebox.showerror("Error", f"Database connection error: {str(e)}", parent=self.root)
                 row1=[]
           combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,width=27,font=("arial",13 ,"bold"),state="readonly")
           combo_roomtype["value"]=rows1
           combo_roomtype.current(0)
           combo_roomtype.grid(row=3,column=1)
           # Available Room
           room_available=Label(labelframeleft,text="roomavailable",font=("arial",12,"bold"),bg="teal",padx=2,pady=6)
           room_available.grid(row=4,column=0,sticky=W)

           self.combo_roomavailable=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,width=27,font=("arial",13 ,"bold"),state="readonly")
           self.combo_roomavailable.grid(row=4,column=1)

           def update_room_numbers(event=None):
                room_type = self.var_roomtype.get()
                conn = mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("select RoomNo from details where RoomType=%s and RoomNo not in(select roomavailable from room)""", (room_type,))
                rows = my_cursor.fetchall()
                conn.close()
                room_nos = [row[0] for row in rows]
                self.combo_roomavailable["values"] = room_nos
                if room_nos:
                    self.combo_roomavailable.current(0)
                else:
                    self.combo_roomavailable.set('')

            # Bind the update function to the room type combobox
           combo_roomtype.bind("<<ComboboxSelected>>", update_room_numbers)
           update_room_numbers()
            #Meal
           meal=Label(labelframeleft,text="Meal:",font=("arial",12,"bold"),bg="teal",padx=2,pady=6)
           meal.grid(row=5,column=0,sticky=W)
           meal_combo = ttk.Combobox(labelframeleft,textvariable=self.var_meal,width=27,values=meal_options,font=("arial",13 ,"bold"),state="readonly")
           meal_combo.grid(row=5, column=1, padx=10, pady=10)
           meal_combo.current(0)
           #No of Days
           noofday=Label(labelframeleft,text="No Of Days:",font=("arial",12,"bold"),bg="teal",padx=2,pady=6)
           noofday.grid(row=6,column=0,sticky=W)
           txt_noofday=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=29,font=("arial",13 ,"bold"))
           txt_noofday.grid(row=6,column=1)
           #Paid tax
           paid_tax=Label(labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),bg="teal",padx=2,pady=6)
           paid_tax.grid(row=7,column=0,sticky=W)
           txt_paidtax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("arial",13 ,"bold"))
           txt_paidtax.grid(row=7,column=1)
           #Sub Total
           subtotal=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),bg="teal",padx=2,pady=6)
           subtotal.grid(row=8,column=0,sticky=W)
           txt_subtotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("arial",13 ,"bold"))
           txt_subtotal.grid(row=8,column=1)
           #Total cost
           total_cost=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),bg="teal",padx=2,pady=6)
           total_cost.grid(row=9,column=0,sticky=W)
           txt_totalcost=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("arial",13 ,"bold"))
           txt_totalcost.grid(row=9,column=1)
           #bil button
           btnbil=Button(labelframeleft,text="Bil",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
           btnbil.grid(row=10,column=0,padx=1,sticky=W)
           #btn
           btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
           btn_frame.place(x=0,y=400,height=40,width=412)

           btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",15,"bold"),bg="black",fg="gold",width=8)
           btnAdd.grid(row=0,column=0,padx=1)

           btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",15,"bold"),bg="black",fg="gold",width=8)
           btnUpdate.grid(row=0,column=1,padx=1)

           btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",15,"bold"),bg="black",fg="gold",width=8)
           btnDelete.grid(row=0,column=2,padx=1)

           btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",15,"bold"),bg="black",fg="gold",width=8)
           btnReset.grid(row=0,column=3,padx=1)

           #right dide image
           img3=Image.open(r"photo/bed.jpg")
           img3=img3.resize((520,300),Image.LANCZOS)
           self.photoimg3=ImageTk.PhotoImage(img3)
           lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
           lblimg.place(x=760,y=55,width=520,height=200)

           #****table frame search system****
           table_frame=LabelFrame(self.root,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
           table_frame.place(x=435,y=288,width=860,height=260)
  
           lb1searchBy=Label(table_frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
           lb1searchBy.grid(row=0,column=0,sticky=W,padx=2)
           
           self.search_var=StringVar()
           combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,width=24,font=("arial",13 ,"bold"),state="readonly")
           combo_search["value"]=("Contact","roomavailable")
           combo_search.current(0)
           combo_search.grid(row=0,column=1,padx=2)

           self.txt_search=StringVar()
           txtsearch=ttk.Entry(table_frame,textvariable=self.txt_search,width=24,font=("arial",13 ,"bold"))
           txtsearch.grid(row=0,column=2,padx=2)

           btnSearch=Button(table_frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
           btnSearch.grid(row=0,column=3,padx=1)

           btnShowall=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
           btnShowall.grid(row=0,column=4,padx=1)
           ######show data table####
           details_table=Frame(table_frame,bd=2,relief=RIDGE)
           details_table.place(x=0,y=50,width=860,height=180)

           scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
           scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
           self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype",
                                                                     "roomavailable","meal","noOfdays",),
                                                                     xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
           scroll_x.pack(side=BOTTOM,fill=X)
           scroll_y.pack(side=RIGHT,fill=Y)

           scroll_x.config(command=self.room_table.xview)
           scroll_y.config(command=self.room_table.yview)
           
           self.room_table.heading("contact",text="Contact")
           self.room_table.heading("checkin",text="Checkin")
           self.room_table.heading("checkout",text="Checkout")
           self.room_table.heading("roomtype",text="Room Type")
           self.room_table.heading("roomavailable",text="Room No")
           self.room_table.heading("meal",text="Meal")
           self.room_table.heading("noOfdays",text="NoOfDays")
           

           self.room_table["show"]="headings"

           self.room_table.column("contact",width=100)
           self.room_table.column("checkin",width=100)
           self.room_table.column("checkout",width=100)
           self.room_table.column("roomtype",width=100)
           self.room_table.column("roomavailable",width=100)
           self.room_table.column("meal",width=100)
           self.room_table.column("noOfdays",width=100)
           self.room_table.pack(fill=BOTH,expand=1)
           self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
           self.fetch_data()
           #add
      def add_data(self):
            if self.var_conatct.get() == "" or self.var_chechin.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                  try:
                        conn = mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
                        my_cursor = conn.cursor()
            
                        my_cursor.execute("INSERT into room VALUES (%s, %s, %s, %s, %s, %s, %s)",(
                                                                                                            self.var_conatct.get(),
                                                                                                            self.var_chechin.get(),
                                                                                                            self.var_chechout.get(),
                                                                                                            self.var_roomtype.get(),
                                                                                                            self.var_roomavailable.get(),
                                                                                                            self.var_meal.get(),
                                                                                                            self.var_noofdays.get()
                                                                                                            
                                                                                                       ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "Room has been added", parent=self.root)
                  except Exception as es:
                       messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
      def fetch_data(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from room")
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
            self.var_conatct.set(row[0]),
            self.var_chechin.set(row[1]),
            self.var_chechout.set(row[2]),
            self.var_roomtype.set(row[3]),
            self.var_roomavailable.set(row[4]),
            self.var_meal.set(row[5]),
            self.var_noofdays.set(row[6])
            
      # def update(self):
      #        if self.var_conatct.get()=="":
      #              messagebox.showerror("Error","Please enter mobile number",parent=self.root)
      #        else:
      #              conn= mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
      #              my_cursor = conn.cursor()
      #              my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
      #                                                                                                                                                 self.var_chechin.get(),
      #                                                                                                                                                 self.var_chechout.get(),
      #                                                                                                                                                 self.var_roomtype.get(),
      #                                                                                                                                                 self.var_roomavailable.get(),
      #                                                                                                                                                 self.var_meal.get(),
      #                                                                                                                                                 self.var_noofdays.get(),
      #                                                                                                                                                 self.var_conatct.get()                                                                    
      #                                                                                                                                            ))
      #              conn.commit()
      #              self.fetch_data()
      #              conn.close()
      #              messagebox.showinfo("Update","Room Details has been updated seccessfully",parent=self.root)
      def update(self):
            if self.var_conatct.get() == "":
                  messagebox.showerror("Error", "Please select a record or enter a mobile number", parent=self.root)
                  return
            try:
                  conn = mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
                  my_cursor = conn.cursor()
                  my_cursor.execute(
                              "update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",
                              (
                              self.var_chechin.get(),
                              self.var_chechout.get(),
                              self.var_roomtype.get(),
                              self.var_roomavailable.get(),
                              self.var_meal.get(),
                              self.var_noofdays.get(),
                              self.var_conatct.get()
                              )
                        )
                  conn.commit()
                  if my_cursor.rowcount == 0:
                        messagebox.showerror("Error", "No record found with this contact number.", parent=self.root)
                  else:
                        self.fetch_data()
                  messagebox.showinfo("Update", "Room Details has been updated successfully", parent=self.root)
                  conn.close()
            except Exception as e:
             messagebox.showerror("Error", f"Update failed: {e}", parent=self.root)
      def delete(self):
            delete=messagebox.askyesno("Hotel Management system","Do you went delete this Room Details",parent=self.root)
            if delete>0:
                  conn= mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
                  my_cursor = conn.cursor()
                  query="delete from room where Contact=%s"
                  value=(self.var_conatct.get(),)
                  my_cursor.execute(query,value)
            else:
                  if not delete:
                        return
            conn.commit()
            self.fetch_data()
            conn.close()
      def reset(self):
            self.var_conatct.set(""),
            self.var_chechin.set(""),
            self.var_chechout.set(""),
           # self.var_roomtype.set(""),
            self.var_roomavailable.set(""),
            self.var_meal.set(""),
            self.var_noofdays.set("")
            self.var_paidtax.set("")
            self.var_actualtotal.set("")
            self.var_total.set("")
      
           #all data fatch
      def fatch_contact(self):
            if self.var_conatct.get()=="":
                  messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
            else:
                  conn= mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
                  my_cursor = conn.cursor()
                  query="select Name from customer where Mobile=%s"
                  value=(self.var_conatct.get(),)
                  my_cursor.execute(query,value)
                  row=my_cursor.fetchone()
                  if row:
                        name=row[0].replace("{","").replace("}","")
                  else:
                        name="Not Found"
                  
                  if row==None:
                        messagebox.showerror("Errow","This number not found",parent=self.root)
                  else:
                        conn.commit()
                        conn.close()

                        showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                        showDataframe.place(x=450,y=55,width=300,height=180)

                        lb1Name=Label(showDataframe,text="Name",font=("arial",12,"bold"))
                        lb1Name.place(x=0,y=0)

                        lb1=Label(showDataframe,text=f"{name}",font=("arial",12,"bold"))
                        lb1.place(x=90,y=0)
                  
                        #gender
                        conn= mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
                        my_cursor = conn.cursor()
                        query=("select Gender from customer where Mobile=%s")
                        value=(self.var_conatct.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        lb1gender=Label(showDataframe,text="Gender",font=("arial",12,"bold"))
                        lb1gender.place(x=0,y=30)

                        lb2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lb2.place(x=90,y=30)

                        #email
                        conn= mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
                        my_cursor = conn.cursor()
                        query=("select Email from customer where Mobile=%s")
                        value=(self.var_conatct.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        lb1gender=Label(showDataframe,text="Email",font=("arial",12,"bold"))
                        lb1gender.place(x=0,y=60)

                        lb2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lb2.place(x=90,y=60)

                        #nationality
                        conn= mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
                        my_cursor = conn.cursor()
                        query=("select Nationality from customer where Mobile=%s")
                        value=(self.var_conatct.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        lb1gender=Label(showDataframe,text="Nationality",font=("arial",12,"bold"))
                        lb1gender.place(x=0,y=90)

                        lb2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lb2.place(x=90,y=90)

                        #address
                        conn= mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
                        my_cursor = conn.cursor()
                        query="select Address from customer where Mobile=%s"
                        value=(self.var_conatct.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        lb1gender=Label(showDataframe,text="Address",font=("arial",12,"bold"))
                        lb1gender.place(x=0,y=120)

                        lb2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lb2.place(x=90,y=120)
        #search system
      def search(self):
             conn= mysql.connector.connect(host="localhost", username="root", password="2005", database="management")
             my_cursor = conn.cursor()
             my_cursor.execute("select * from room where "+str(self.search_var.get())
                                +" like '%"+str(self.txt_search.get())+"%'")
             rows=my_cursor.fetchall()
             if len(rows)!=0:
                   self.room_table.delete(*self.room_table.get_children())
                   for i in rows:
                         self.room_table.insert("",END,values=i)
                   conn.commit()
             conn.close()
      
      def total(self):
            inDate = self.var_chechin.get()
            outDate = self.var_chechout.get()
            inDate = datetime.strptime(inDate, "%d/%m/%Y")
            outDate = datetime.strptime(outDate, "%d/%m/%Y")
            self.var_noofdays.set(abs((outDate - inDate).days))

                  # Prices
            Breakfast = 200.0
            Lunch = 400.0
            Dinner = 500.0
            Single = 400.0
            Double=600.0
            Luxary=1000.0
            num_days = float(self.var_noofdays.get())

            total_per_day = 0

            if self.var_roomtype.get() == "Single":
                  if self.var_meal.get() == "Breakfast":
                        total_per_day = Single + Breakfast
                  elif self.var_meal.get() == "Lunch":
                        total_per_day = Single + Lunch
                  elif self.var_meal.get() == "Dinner":
                        total_per_day = Single + Dinner
                  elif self.var_meal.get() == "Breakfast + Lunch":
                        total_per_day = Single + Breakfast + Lunch
                  elif self.var_meal.get() == "Lunch + Dinner":
                        total_per_day = Single + Lunch + Dinner
                  elif self.var_meal.get() == "Breakfast + Dinner":
                        total_per_day = Single + Breakfast + Dinner
                  elif self.var_meal.get() == "Breakfast + Lunch + Dinner":
                        total_per_day = Single + Breakfast + Lunch + Dinner
            if self.var_roomtype.get() == "Double":
                  if self.var_meal.get() == "Breakfast":
                        total_per_day = Double + Breakfast
                  elif self.var_meal.get() == "Lunch":
                        total_per_day =Double + Lunch
                  elif self.var_meal.get() == "Dinner":
                        total_per_day = Double + Dinner
                  elif self.var_meal.get() == "Breakfast + Lunch":
                        total_per_day =Double + Breakfast + Lunch
                  elif self.var_meal.get() == "Lunch + Dinner":
                        total_per_day =Double + Lunch + Dinner
                  elif self.var_meal.get() == "Breakfast + Dinner":
                        total_per_day =Double + Breakfast + Dinner
                  elif self.var_meal.get() == "Breakfast + Lunch + Dinner":
                        total_per_day =Double + Breakfast + Lunch + Dinner
            if self.var_roomtype.get() == "Luxary":
                  if self.var_meal.get() == "Breakfast":
                        total_per_day = Luxary + Breakfast
                  elif self.var_meal.get() == "Lunch":
                        total_per_day =Luxary + Lunch
                  elif self.var_meal.get() == "Dinner":
                        total_per_day = Luxary + Dinner
                  elif self.var_meal.get() == "Breakfast + Lunch":
                        total_per_day =Luxary + Breakfast + Lunch
                  elif self.var_meal.get() == "Lunch + Dinner":
                        total_per_day =Luxary + Lunch + Dinner
                  elif self.var_meal.get() == "Breakfast + Dinner":
                        total_per_day =Luxary + Breakfast + Dinner
                  elif self.var_meal.get() == "Breakfast + Lunch + Dinner":
                        total_per_day =Luxary + Breakfast + Lunch + Dinner
        

            subtotal = num_days * total_per_day
            tax = subtotal * 0.09
            total = subtotal + tax
            self.var_paidtax.set("Rs." + str("%.2f" % tax))
            self.var_actualtotal.set("Rs." + str("%.2f" % subtotal))
            self.var_total.set("Rs." + str("%.2f" % total))

      





            



            

           
           
           






if __name__=="__main__":
      root=Tk()
      obj=roombooking(root)
      root.mainloop()
