from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Weather App")
win.config(bg="#0a0808")
win.geometry("400x400")

name_label = Label(win,text = "Weather App", font =("Helevetica", 20,"bold"))
name_label.place(x=24,y=49,height=40,width=430)

list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

com  = ttk.Combobox(win,text="Weather App",values=list_name,
                    font=("Helvetica",20,"bold"))
com.place(x=20,y=100,height=40,width=430)

button = Button(win,text="Done",
                font=("Comic Sans MS",30,"bold"))
button.place(x=190,y=150,height=50,width=99)


w_label =Label(win,text="Climate",
               font=("Comic Sans MS",20,"bold"))
w_label.place(x=20,y=215,height=47,width=99)

w_label1 =Label(win,text="",
               font=("Comic Sans MS",20,"bold"))
w_label1.place(x=200,y=215,height=47,width=99)


wb_label = Label (win,text="Description",
                  font=("Comic Sans MS",12,"bold"))
wb_label.place(x=20,y=265,height=47,width=99)

wb_label1 = Label (win,text="",
                  font=("Comic Sans MS",20,"bold"))
wb_label1.place(x=200,y=265,height=47,width=99)


temp_label = Label(win,text="Temperature",
                   font=("Helvetica",12,"bold"))
temp_label.place(x=20,y=315,height=47,width=99)

temp_label1 = Label(win,text="",
                   font=("Comic Sans MS",20,"bold"))
temp_label1.place(x=200,y=315,height=47,width=99)


per_label =Label(win,text="Pressure",
                 font=("Helvetica",12,"bold"))
per_label.place(x=20,y=365,height=47,width=99)

per_label1 =Label(win,text="",
                 font=("Comic Sans MS",20,"bold"))
per_label1.place(x=200,y=365,height=47,width=99)


win.mainloop()