# this is a simple digital clock using tkinter and datetime module.

from tkinter import *
clock = Tk()
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    am = time.strftime("%p")
    lab_hr.config(text = hr)
    lab_min.config(text = min)
    lab_sec.config(text = sec)
    lab_am.config(text = am)
    lab_hr.after(200, date_time)

clock.title("***DIGITAL CLOCK***")
clock.geometry("950x500")
clock.config(bg="grey")

lab_hr = Label(clock,text="00",
               font=("Time New Roman",60,"bold"),
                bg="red",
                fg="white")

lab_hr.place(x=50, y=40,
               height=110,
               width=100)


lab_min = Label(clock,text="00",
               font=("Time New Roman",60,"bold"),
                bg="red",
                fg="white")

lab_min.place(x=300, y=40,
               height=110,
               width=100)

lab_sec = Label(clock,text="00",
               font=("Time New Roman",60,"bold"),
                bg="red",
                fg="white")

lab_sec.place(x=550, y=40,
               height=110,
               width=100)

lab_am = Label(clock,text="00",
               font=("Time New Roman",40,"bold"),
                bg="red",
                fg="white")

lab_am.place(x=800, y=40,
               height=110,
               width=100)

date_time()
clock.mainloop()
