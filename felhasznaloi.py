from tkinter import*
from tkinter import messagebox
import tkinter as tk
import konyvtablazat
import kolcsonzottkonyvek
def alap():
    alap = Tk()
    alap.geometry("1000x800")
    alap.title("Felhasználó")
    alap.configure(bg="#9A7E6F")
    cím = Label(alap, text="Felhasználó", fg="#493628",bg="#9A7E6F",font=('Times', 60,'bold'))
    cím.grid(row= 1, columnspan=3,pady=(1,0), padx=320)
    
    def tablazaT():
        konyvtablazat.tablazat()
    tabla = Button(alap, text="Könyvek listája", fg="#493628", bg="#D6C0B3", font="sans 13 bold", command=tablazaT)
    tabla.grid(row=2, column=1, pady=10, padx=20)
    def kolcsonzott():
        kolcsonzottkonyvek.kolcson()
    kolcson = Button(alap, text="Kölcsönzött könyvek", fg="#493628", bg="#D6C0B3", font="sans 13 bold", command=kolcsonzott)
    kolcson.grid(row=3, column=1, pady=10, padx=20)
    alap.mainloop()