import tkinter
from tkinter import *
root=tkinter.Tk()
root.configure(background="light green")
root.geometry("250x110")
def shutdown():
    import os;
    os.system("shutdown /s /t 1");
s1=tkinter.Button(root, text="Shutdown", command=shutdown, bd=5)
s1.pack()
def restart():
    import os;
    os.system("shutdown /r /t 1");
s2=tkinter.Button(root, text="Restart", command=restart, bd=5)
s2.pack()
def hibernate():
    import os;
    os.system("shutdown.exe /h")
s3=tkinter.Button(root, text="Hibernate", command=hibernate, bd=5)
s3.pack()

root.mainloop()
