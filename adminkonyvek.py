from tkinter import *
import tkinter as tk
from tkinter import ttk

def adminkonyvei():
        Adminkonyvek = Tk()
        Adminkonyvek.geometry("1600x600")
        Adminkonyvek.title("Lekérdezés")
        Adminkonyvek.configure(bg="#9A7E6F")
        proba = Label(Adminkonyvek, text="Könyvek", bg="#9A7E6F", fg="#493628",font=('sans', 70,'bold'),)
        proba.grid(row= 0, columnspan=1,pady=(10,10), padx=(550))
        def show():
                
            tempList = []
            tempList.sort(key=lambda e: e[1], reverse=True)

            for i, (name, title, borrowed) in enumerate(tempList, start=1):
                listBox.insert("", "end", values=(i, name, title, borrowed))
        # create Treeview with 3 columns
        cols = ('Sorszám', 'Cím', 'Kiadási dátum', 'Kiadó', 'Oldalszám', 'ISBN', 'Kölcsönzött-e?')
        listBox = ttk.Treeview(Adminkonyvek, columns=cols, show='headings')
        # set column headings
        for col in cols:
            listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)
        

        showScores = tk.Button(Adminkonyvek, text="Show tablazat", width=15, command=show).grid(row=4, column=0, padx=(200, 40))
        closeButton = tk.Button(Adminkonyvek, text="Close", width=15, command=exit).grid(row=4, column=0, padx=(40, 200))



        Adminkonyvek.mainloop()