from tkinter import *
import tkinter as tk
from tkinter import ttk

class Objektum:
    def __init__(self, sorszam, cim, evszam, kiado, oldalszam, isbn, igennem):
        self.sorszam = sorszam
        self.cim = cim
        self.evszam = evszam
        self.kiado = kiado
        self.oldalszam = oldalszam
        self.isbn = isbn
        self.igennem = igennem

def adminkonyvei():
    Adminkonyvek = tk.Tk()
    Adminkonyvek.geometry("1420x600")
    Adminkonyvek.title("Könyvek")
    Adminkonyvek.configure(bg="#9A7E6F")
    
    proba = tk.Label(Adminkonyvek, text="Könyvek🎄", bg="#9A7E6F", fg="#493628", font=('sans', 70, 'bold'))
    proba.grid(row=0, columnspan=1, pady=(10, 10), padx=(450,100))

    def beolvasas():
        global books
        books = []
        with open('könyvek.txt', 'r', encoding='utf-8') as fajl:
            for i, sor in enumerate(fajl, start=1):
                adat = sor.strip().split(',')  
                cim = adat[0].strip()  
                evszam = adat[1].strip()
                kiado = adat[2].strip()
                oldalszam = adat[3].strip()
                isbn = adat[4].strip()
                igennem = adat[5].strip()
                book = Objektum(i, cim, evszam, kiado, oldalszam, isbn, igennem)  
                books.append(book)

    def show():
        for item in listBox.get_children():
            listBox.delete(item)
        
        sorted_books = sorted(books, key=lambda book: book.sorszam) 

        for i, book in enumerate(sorted_books, start=1):
            if i % 2 == 0:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.igennem),
                               tags=('even'))
            else:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.igennem))

        listBox.tag_configure('even', background='#AB886D') 
    


    cols = ('Sorszám', 'Cím', 'Kiadási dátum', 'Kiadó', 'Oldalszám', 'ISBN', 'Kölcsönzött-e?')
    listBox = ttk.Treeview(Adminkonyvek, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col)

    listBox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    showScores = tk.Button(Adminkonyvek, text="Adatok mutatása",  fg="#493628", bg="#D6C0B3", font="sans 13 bold", width="30", height="3", command=show)
    showScores.grid(row=4, column=0, padx=(480, 100))

    torlogomb = tk.Button(Adminkonyvek, text="Kijelölt mező törlése", fg="#493628", bg="#D6C0B3", font="sans 13 bold", width="30", height="3")
    torlogomb.grid(row=5, column=0 , pady=10, padx=(480, 100))

    closeButton = tk.Button(Adminkonyvek, text="Vissza", fg="#493628", bg="#FF8A8A", font="sans 13 bold", command=Adminkonyvek.destroy)
    closeButton.grid(row=6, column=0 , pady=20, padx=(480, 100))

    beolvasas()
    Adminkonyvek.mainloop()


