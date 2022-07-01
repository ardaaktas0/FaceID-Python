from tkinter import *
import giris
import cikis
import fotosave
from tkinter import messagebox
from multiprocessing.connection import wait
from time import sleep
from turtle import speed
import cv2
from simple_facerec import SimpleFacerec
from datetime import datetime
from datetime import date

pencere = Tk()

pencere.title("Yüz Tanıma Sistemi")
pencere.geometry("700x400")

uygulama = Frame(pencere, padx = 100,pady = 100)
uygulama.grid(padx = 40, pady = 40)




def clik_me():
    giris.main()

def clik_me1():
    cikis.main()

def clik_me2():
    fotosave.main()





#button ekleme bölümü
button1 = Button(uygulama, text = " Giriş Yap " , command=clik_me)
button1.grid(row=0, column=1)

button2 = Button(uygulama, text = " Çıkış Yap " , command=clik_me1)
button2.grid(row=0, column=2)

button3 = Button(uygulama, text = " Kullanıcı Kaydet " , command=clik_me2)
button3.grid(row=0, column=3)

c = Button(pencere, text = "Uygulamayı Kapat", command = uygulama.quit)
c.grid(row=0, column=4)

pencere.mainloop()