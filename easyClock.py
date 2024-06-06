#this program is made by harshit grewal if you find this source code please thank to him
# email1: chhtsg101@hotmail.com
# email2: chhtsg8.1@hotmail.com
# this program's source is free for everyone as all rights are given to editor.
'''                       No Cost Is greator than a Thanks                   '''
from tkinter import*
import time
import datetime
#=======================================Window Design ====================================
root=Tk()
root.title("Easy Clock   by Harshit Grewal")
root.configure(background='sky blue')
root.geometry("500x630")
#=======================================IST===============================================
lb1=Label(root, text=time.strftime("%Z") , font=('calibri', 20 ), bd=1, bg='black', fg='white')
lb1.pack(fill= BOTH, expand=0)
#=======================================Time Code ========================================
Head1=Label(root, text="Current Time is :", font=('calibri', 40 ), bg='sky blue')
Head1.pack(side=TOP)
t=''
clock =Label(root, font=('segoe script', 50 , 'bold'), bg="light green")
clock.pack(fill= BOTH, expand=0)
def tiktik():
    global t
    t2= time.strftime('%X')
    if t2!=t:
        t=t2
        clock.config(text=t2)
    clock.after(2, tiktik)
tiktik()
#=======================================Greetings ========================================
greet=Label(root, font=('segoe print', 25 ), bg='red')
greet.pack(fill=BOTH, expand=0)
def greetings():
    current= datetime.datetime.now()
    today7am  = current.replace(hour=7, minute=0, second=0, microsecond=0)
    today9pm  = current.replace(hour=21, minute=0, second=0, microsecond=0)
    today12pm = current.replace(hour=12, minute=0, second=0, microsecond=0)
    today5pm  = current.replace(hour=17, minute=0, second=0, microsecond=0)
    today12am = current.replace(hour=0, minute=0, second=0, microsecond=0)
    if (current>=today7am and current<today12pm):
        a="Goodmorning!! "   
    elif(current==today12pm and current<=today5pm):
        a="Goodafternoon!! " 
    elif(current>=today5pm and current<=today9pm):
        a="Goodevening!!   "
    elif(current<=today9pm and current==today12am):
        a="GoodNight....time to take rest. ;-)"
    else:
        a="You Should be sleeping now!!"
    
    greet.config(text=a)
    greet.after(200, greetings)
greetings()
#=======================================Date Code ========================================
Head2=Label(root, text="Current Date is :", font=('calibri', 40 ), bg='sky blue')
Head2.pack(side=TOP)
d=''
date=Label(root, font=('calibri', 50 , 'bold'), bg="yellow")
date.pack(fill= BOTH, expand=0)
def day():
    global d
    d2= time.strftime("%D")
    if d2!=d:
        d=d2
        date.config(text=d2)
    date.after(200, day)
day()
#=======================================Dayname Code =====================================
Head3=Label(root, text="Today is :", font=('calibri', 40 ), bg='sky blue')
Head3.pack(side=TOP)
f=''
name=Label(root, font=('aerial', 50 , 'bold'), bg="orange")
name.pack(fill= BOTH, expand=0)
def dayname():
    global f
    f2= time.strftime("%A")
    if f2!=f:
        f=f2
        name.config(text=f2)
    name.after(200, dayname)
dayname()
#=======================================Quit Button ======================================
btn1=Button(root, text= "Quit", font=('calibri', 20 ), bd=1, bg='black', fg='white', command=quit)
btn1.pack(side=BOTTOM)
#=======================================Final Window Loop=================================
root.mainloop()
