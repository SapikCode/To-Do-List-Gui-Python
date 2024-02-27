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
        if pas == "yttaaa":
            labelc["text"]="Berhasil Masuk"
            buttonh["text"]="Ke Beranda"
            buttonh.place(relx=0.5,rely=0.9,anchor=tkinter.CENTER)
    else:
        labelc["text"]="Username tidak ada"
        inputs.delete(0,"end")
        inputp.delete(0,"end")
    
def buka():
    root.withdraw()
    call(["python","tampilan.py"])
            




   


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


import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import csv

def update_listbox():
    clear_listbox()
    for tugas, deadline in tasks.items():
        listbox.insert("end", tugas)
        listboxd.insert("end", deadline)

def clear_listbox():
    listbox.delete(0, "end")
    listboxd.delete(0, "end")


tasks = {}

lines = {}


def tambah_tugas():
    tugas = entry1.get()
    line = isian.get()

    if tugas != "":
        tasks[tugas] = line
        update_listbox()
    else:
        messagebox.showwarning("Isi")
    entry1.delete(0, "end")
    isian.delete(0, "end")
    

def hapus_tugas():
    hapusdl()
    try:
        selected_tugas = listbox.get(listbox.curselection())
        del tasks[selected_tugas]
        update_listbox()
    except IndexError:
        pass

def hapusdl():
    try:
        selected_index = listboxd.curselection()[0]
        listboxd.delete(selected_index)
    except IndexError:
        pass



def hapus_semua_tugas():
    listbox.delete(0, tk.END)

def cari():
    query = carian.get().lower()
    listbox_hasil.delete(0, tk.END)
    for i in (tasks):
        if query in i.lower():
            listbox_hasil.insert(tk.END,i)

def jumlah():
    num_tasks = len(tasks)
    msg = "Ada {} Tugas".format(num_tasks)
    labelt["text"]=msg

def simpan():
    namaf = simpledialog.askstring("input","Masukan Nama File")+(".txt")
    data = listboxd.get(0,"end")
    hasil=[tasks,data]
    with open(namaf,'w',newline='') as csvfile:
        csv_writer = csv.writer(csvfile,delimiter=',')
        csv_writer.writerow(["Tugas","Deadline"])
        for i in zip(*hasil):
            csv_writer.writerow(i)
        print("data berhasil disimpan dengan nama ",namaf)






root = tk.Tk()
root.title("Aplikasi To-Do List dengan Deadline")
root.geometry("550x300")
root.configure(bg="#1C1A29")

image = PhotoImage(file="background.png")


labelm = tk.Label(root,image=image)
labelm.pack()




entry1 = tk.Entry(root,bg="white")
entry1.pack()


isian = tk.Entry(root)
isian.pack()


tambah_button = tk.Button(root, text="Tambah Tugas", command=tambah_tugas,bg="#6772D1",fg="white")
tambah_button.pack(pady=5)



carian = tk.Entry(root)
carian.pack()

caributton = tk.Button(root,text="Cari",command=cari,bg="#6772D1",fg="white")
caributton.pack(pady=5)


tugas_label = tk.Label(root, text='Tugas :')
deadline_label = tk.Label(root, text='Deadline :')

listbox = tk.Listbox(root,bg="#414FCD",width=20,height=10,fg="white")
listbox.pack()

listboxd = tk.Listbox(root,bg="#414FCD",width=20,height=10,fg="white")
listboxd.pack()

labelt = tk.Label(root, text="",bg="#6772D1",fg="white")
labelt.pack(pady=10)

totalt = tk.Button(root,text="Cek Jumlah Tugas",command=jumlah,bg="#6772D1",fg="white")
totalt.pack(pady=5)

listbox_hasil = tk.Listbox(root,bg="#414FCD",width=20,height=6,fg="white")
listbox_hasil.pack()


hapus_button = tk.Button(root, text="Hapus Tugas", command=hapus_tugas,bg="#6772D1",fg="white")
hapus_button.pack(pady=5)


hapus_semua_button = tk.Button(root, text="Hapus Semua Tugas", command=hapus_semua_tugas,bg="#6772D1",fg="white")
hapus_semua_button.pack()


simpand = tk.Button(root, text="Simpan Data Ke Database",command=simpan,bg="#6772D1",fg="white")
simpand.pack()




entry1.place(x=10,y=60)
isian.place(x=10,y=120)
tambah_button.place(x=29,y=160)
carian.place(x=405,y=40)
caributton.place(x=405,y=70)
listbox.place(x=150,y=80)
listboxd.place(x=270,y=80)
listbox_hasil.place(x=400,y=130)
hapus_button.place(x=33,y=190)
hapus_semua_button.place(x=10,y=220)
labelt.place(x=150,y=275)
totalt.place(x=15,y=250)
tugas_label.place(x=150,y=60)
deadline_label.place(x=270,y=60)
simpand.place(x=150,y=250)


root.mainloop()