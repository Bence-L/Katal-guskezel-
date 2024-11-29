from tkinter import *
import tkinter as tk
from tkinter import ttk
from konyvekhero import Objektum

def adminkonyvei():
        Adminkonyvek = Tk()
        Adminkonyvek.geometry("1600x600")
        Adminkonyvek.title("Lekérdezés")
        Adminkonyvek.configure(bg="#9A7E6F")
        proba = Label(Adminkonyvek, text="Könyvek", bg="#9A7E6F", fg="#493628",font=('sans', 70,'bold'),)
        proba.grid(row= 0, columnspan=1,pady=(10,10), padx=(550))
        
        def beolvasas():
            global books
            global adat
            global adat2
            books = []
            with open('könyvek.txt', 'r', encoding='utf-8') as fajl:
                for sor in fajl:
                    adat = sor.strip().split(',')
                    # print(adat) 
                    adat2 = Objektum(adat[0], adat[1], adat[2], adat[3], adat[4], adat[5],)
        beolvasas()
        
        def show():
            for i in books:
                tempList = [[adat2.sorszam,adat2.cim,adat2.evszam,adat2.kiado,adat2.oldalszam,adat2.isbn,adat2.kolcsonzott, ]]
                tempList.sort(key=lambda e: e[1], reverse=True)

                for i, (i, cim, kiadasidatum, kiado, oldalszam, isbn, kolcsonzott) in enumerate(tempList, start=1):
                    listBox.insert("", "end", values=( i, cim, kiadasidatum, kiado, oldalszam, isbn, kolcsonzott))
        cols = ('Sorszám', 'Cím', 'Kiadási dátum', 'Kiadó', 'Oldalszám', 'ISBN', 'Kölcsönzött-e?')
        listBox = ttk.Treeview(Adminkonyvek, columns=cols, show='headings')
        # set column headings
        for col in cols:
            listBox.heading(col, text=col)    
        listBox.grid(row=3, column=0, columnspan=2)
        

        showScores = tk.Button(Adminkonyvek, text="Show tablazat", width=15, command=show).grid(row=4, column=0, padx=(200, 40))
        closeButton = tk.Button(Adminkonyvek, text="Close", width=15, command=exit).grid(row=4, column=0, padx=(40, 200))



        Adminkonyvek.mainloop()