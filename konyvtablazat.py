from tkinter import*
import tkinter as tk
from tkinter import ttk

class Objektum:
    def __init__(self, sorszam, cim, evszam, kiado, oldalszam, isbn):
        self.sorszam = sorszam
        self.cim = cim
        self.evszam = evszam
        self.kiado = kiado
        self.oldalszam = oldalszam
        self.isbn = isbn
        self.kolcsonzott = '❌'


def tablazat():
    tablazat = Tk()
    tablazat.geometry("1000x800")
    tablazat.title("Táblázat")
    tablazat.configure(bg="#9A7E6F")
    

    

    proba = tk.Label(tablazat, text="Könyvek", bg="#9A7E6F", fg="#493628", font=('sans', 70, 'bold'))
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
                book = Objektum(i, cim, evszam, kiado, oldalszam, isbn)  
                books.append(book)

    def show():
        for item in listBox.get_children():
            listBox.delete(item)
        
        sorted_books = sorted(books, key=lambda book: book.sorszam) 

        for i, book in enumerate(sorted_books, start=1):
            if i % 2 == 0:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.kolcsonzott),
                               tags=('even'))
            else:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.kolcsonzott))

        listBox.tag_configure('even', background='#AB886D') 

    cols = ('Sorszám', 'Cím', 'Kiadási dátum', 'Kiadó', 'Oldalszám', 'ISBN', 'Kölcsönzött-e?')
    listBox = ttk.Treeview(tablazat, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col)

    listBox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    showScores = tk.Button(tablazat, text="Adatok mutatása",  fg="#493628", bg="#D6C0B3", font="sans 13 bold", command=show)
    showScores.grid(row=4, column=0, padx=(480, 100))

    closeButton = tk.Button(tablazat, text="Vissza", fg="#493628", bg="#FF8A8A", font="sans 13 bold", command=tablazat.destroy)
    closeButton.grid(row=5, column=0 , pady=50, padx=(480, 100))

    beolvasas()
    tablazat.mainloop()