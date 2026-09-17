from tkinter import *
from PIL import Image,ImageTk  
class report:
      def __init__(self,root):
            self.root=root
            self.root.title("About us")
            self.root.geometry("1295x550+230+220")
            self.root.config(bg="light blue")
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
            lb1_title=Label(self.root,text="About Us",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
            lb1_title.place(x=0,y=140,width=1550,height=50) 
            #******labelFrame meal details****
            labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Meal Details",fg="blue",bg="cyan",font=("times new roman",25,"bold"),padx=2)
            labelframeleft.place(x=50,y=200,width=800,height=300)
            #brakefast Frame
            brakefast=LabelFrame(labelframeleft,bd=2,relief=RIDGE,text="Brakefast",fg="purple",bg="light green",font=("times new roman",15,"bold"),padx=2)
            brakefast.place(x=5,y=5,width=310,height=250)
            item1=Label(brakefast,text="1.Upma  2.Masala Dosa",font=("times new roman",12,"bold"),fg="black",bg="light green",padx=2,pady=6)
            item1.grid(row=0,column=0)
            item2=Label(brakefast,text="3.Phoa    4.Poori",font=("times new roman",12,"bold"),bg="light green",padx=2,pady=6)
            item2.grid(row=1,column=0)            
            item3=Label(brakefast,text="5.Idli Sambar  6.Cheese Dosa",font=("times new roman",12,"bold"),bg="light green",padx=2,pady=6)
            item3.grid(row=3,column=0)
            item4=Label(brakefast,text="7.Paneer Bhuji  8.Palak Paratha",font=("times new roman",12,"bold"),bg="light green",padx=2,pady=6)
            item4.grid(row=4,column=0)
            item5=Label(brakefast,text="9.Wheat Dosa 10.Pesarattu",font=("times new roman",12,"bold"),bg="light green",padx=2,pady=6)
            item5.grid(row=5,column=0)
            item6=Label(brakefast,text="11.Paniyaram 12.Mooli Paratha",font=("times new roman",12,"bold"),bg="light green",padx=2,pady=6)
            item6.grid(row=6,column=0)
           
            #lunch Frame
            lunch=LabelFrame(labelframeleft,bd=2,relief=RIDGE,text="Lunch",font=("times new roman",15,"bold"),bg="salmon",padx=2)
            lunch.place(x=250,y=5,width=310,height=250)
            item1=Label(lunch,text="1.Malai Kofta  2.Navaratna Kurma",font=("times new roman",12,"bold"),bg="salmon",padx=2,pady=6)
            item1.grid(row=0,column=0)
            item2=Label(lunch,text="3.Carrot Halwa   4.Cobb Salad",font=("times new roman",12,"bold"),bg="salmon",padx=2,pady=6)
            item2.grid(row=1,column=0)
            item3=Label(lunch,text="5.Dal Makhani  6.Kulcha",font=("times new roman",12,"bold"),bg="salmon",padx=2,pady=6)
            item3.grid(row=2,column=0)
            item4=Label(lunch,text="9.Bhindi Masala  8.Avocado Salad",font=("times new roman",12,"bold"),bg="salmon",padx=2,pady=6)
            item4.grid(row=3,column=0)
            item5=Label(lunch,text="9.Butter Chapati  10.Garlic Naan",font=("times new roman",12,"bold"),bg="salmon",padx=2,pady=6)
            item5.grid(row=4,column=0)
            item6=Label(lunch,text="11.Veggie Stir - Fry",font=("times new roman",12,"bold"),bg="salmon",padx=2,pady=6)
            item6.grid(row=5,column=0)
            #Dinner Frame
            dinner=LabelFrame(labelframeleft,bd=2,relief=RIDGE,text="Dinner",font=("times new roman",12,"bold"),bg="sky blue",padx=2)
            dinner.place(x=500,y=5,width=280,height=250)
            item1=Label(dinner,text="1.Tofu and Vetetable stir-fry",font=("times new roman",12,"bold"),bg="sky blue",padx=2,pady=6)
            item1.grid(row=0,column=0)
            item2=Label(dinner,text="2.Brown Rice Pliaf with Vegetables",font=("times new roman",12,"bold"),bg="sky blue",padx=2,pady=6)
            item2.grid(row=1,column=0)
            item3=Label(dinner,text="3.Vegetarian Sushi Grain Bowl",font=("times new roman",12,"bold"),bg="sky blue",padx=2,pady=6)
            item3.grid(row=2,column=0)
            item4=Label(dinner,text="4.Mixed Vegetable Curry with Quinoa",font=("times new roman",12,"bold"),bg="sky blue",padx=2,pady=6)
            item4.grid(row=3,column=0)
            item5=Label(dinner,text="5.Vegetable-Loaded Frittatas",font=("times new roman",12,"bold"),bg="sky blue",padx=2,pady=6)
            item5.grid(row=4,column=0)
            item6=Label(dinner,text="6.Simple Moong Dal Khichdi",font=("times new roman",12,"bold"),bg="sky blue",padx=2,pady=6)
            item6.grid(row=5,column=0)
            #******labelFrame room details****
            labelframeleft2=LabelFrame(self.root,bd=2,relief=RIDGE,text="Hotel Protocol",fg="green", font=("times new roman",25,"bold"),bg="silver",padx=2)
            labelframeleft2.place(x=900,y=200,width=350,height=300)
            item1=Label(labelframeleft2,text="1. Guest Safety and Security",font=("times new roman",15,"bold"),bg="silver",padx=2,pady=6)
            item1.grid(row=0,column=0)
            item2=Label(labelframeleft2,text="2. Positive Guest Experience",font=("times new roman",15,"bold"),bg="silver",padx=2,pady=6)
            item2.grid(row=1,column=0)
            item3=Label(labelframeleft2,text="3. Guest Verification and Registration",font=("times new roman",15,"bold"),bg="silver",padx=2,pady=6)
            item3.grid(row=2,column=0)
            item4=Label(labelframeleft2,text="4. Secure Parking Facilities",font=("times new roman",15,"bold"),bg="silver",padx=2,pady=6)
            item4.grid(row=3,column=0)
            item5=Label(labelframeleft2,text="5. Emergency Response Plan",font=("times new roman",15,"bold"),bg="silver",padx=2,pady=6)
            item5.grid(row=4,column=0)
            item4=Label(labelframeleft2,text="6. Collaboration with Local Authorities",font=("times new roman",15,"bold"),bg="silver",padx=2,pady=6)
            item4.grid(row=5,column=0)
            #******labelFrame conect us****
            labelframeleft3=LabelFrame(self.root,bd=2,relief=RIDGE,text="Connect Us",font=("times new roman",12,"bold"),bg="lime green",padx=2)
            labelframeleft3.place(x=50,y=500,width=1000,height=100)
            item1=Label(labelframeleft3,text="Mobile No:6297723751",font=("times new roman",15,"bold"),bg="lime Green",padx=2,pady=6)
            item1.grid(row=0,column=0)
            item2=Label(labelframeleft3,text="Email ID:sunwave@gmail.com        Address:CONTAI    PURBA MEDINIPUR",font=("times new roman",15,"bold"),bg="lime green",padx=2,pady=6)
            item2.grid(row=1,column=0)
            



if __name__=='__main__':
      root=Tk()
      obj=report(root)
      root.mainloop()