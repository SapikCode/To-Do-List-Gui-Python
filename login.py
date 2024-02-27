import tkinter
from tkinter import *  
from tkinter import messagebox
from tkinter import simpledialog
from subprocess import call

root = tkinter.Tk() 
root.geometry("550x300")
root.title("Login to DO List")

user=["tiara","ridho","angger","adel","shafwan","dewa"]



def button_function():
    cek = inputs.get().lower()
    pas = inputp.get()
    allt = all(cek in my_list for my_list in [user])
    if allt:
        labelc["text"]="Username ada,password salah"
        inputs.delete(0,"end")
        inputp.delete(0,"end")
        if pas == "admin":
            labelc["text"]="Berhasil Masuk"
            buttonh["text"]="Ke Beranda"
            buttonh.place(relx=0.5,rely=0.9,anchor=tkinter.CENTER)
    else:
        labelc["text"]="Username tidak ada"
        inputs.delete(0,"end")
        inputp.delete(0,"end")
    
def buka():
    root.withdraw()
    call(["python","tiketbaru.py"])
            




   


image = PhotoImage(file="bglog.png")
labelm = tkinter.Label(root,image=image)
labelm.pack()



inputs = tkinter.Entry(root)
inputp = tkinter.Entry(root)
labelc = tkinter.Label(root,text="",bg="#6772D1",fg="white")
button = tkinter.Button(root,text="Login",command=button_function,width=10,bg="#6772D1",fg="white")
buttonh = tkinter.Button(root,text="",bg="#6772D1",fg="white",command=buka)
button.place(relx=0.49, rely=0.7,anchor=tkinter.CENTER)
inputs.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)
inputp.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)
labelc.place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)
buttonh.place(relx=0,rely=20,anchor=tkinter.CENTER)





root.mainloop()