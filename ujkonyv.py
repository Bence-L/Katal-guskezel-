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

def ujfuggveny():
    ujkonyvek = tk.Tk()
    ujkonyvek.geometry("750x1300")
    ujkonyvek.title("Könyvek📖")
    ujkonyvek.configure(bg="#9A7E6F")

    proba = Label(ujkonyvek, text="Hozzáadás", bg="#9A7E6F", fg="#493628", font=('sans', 60, 'bold'))
    proba.grid(row=0, column=0, columnspan=2, pady=(10, 10), sticky="nsew")
    def beolvasas():
        #Beolvasas
        global books
        books = []  # Üres lista a könyvek tárolásához
        with open('könyvek.txt', 'r', encoding='utf-8') as fajl:
            for i, sor in enumerate(fajl, start=1):  # Fájl sorainak beolvasása
                adat = sor.strip().split(',')  # Sor adatainak szétválasztása
                cim = adat[0].strip()  # Könyv címe
                evszam = adat[1].strip()  # Kiadás éve
                kiado = adat[2].strip()  # Kiadó
                oldalszam = adat[3].strip()  # Oldalszám
                isbn = adat[4].strip()  # ISBN
                igennem = adat[5].strip()  # Kölcsönzés állapota
                book = Objektum(i, cim, evszam, kiado, oldalszam, isbn, igennem)  # Objektum létrehozása
                books.append(book)  # Könyv hozzáadása a listához

    def mentes():
        #Frissítés
        with open('könyvek.txt', 'w', encoding='utf-8') as fajl:
            for book in books:  # Minden könyvet végigírunk a fájlba
                fajl.write(f"{book.cim},{book.evszam},{book.kiado},{book.oldalszam},{book.isbn},{book.igennem}\n")

    def show():
        #Mutatás
        #Törli az összes korábban megjelenített sort
        for item in listBox.get_children():
            listBox.delete(item)

        #Könyvek megjelenítése
        for i, book in enumerate(books, start=1):
            if i % 2 == 0:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.igennem),
                            tags=('even',))
            else:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.igennem))

        # Páros sorok színezése
        listBox.tag_configure('even', background='#AB886D')

    cols = ('Sorszám', 'Cím', 'Kiadási dátum', 'Kiadó', 'Oldalszám', 'ISBN', 'Kölcsönzött-e?')
    listBox = ttk.Treeview(ujkonyvek, columns=cols, show='headings', height=15)

    # Oszlopok beállítása
    for col in cols:
        listBox.heading(col, text=col)
        listBox.column(col, width=100)  # Oszlop szélesség

    # Scrollbar hozzáadása
    gorgeto = ttk.Scrollbar(ujkonyvek, orient="vertical", command=listBox.yview)
    listBox.configure(yscroll=gorgeto.set)
    listBox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    gorgeto.grid(row=1, column=2, sticky="ns")

    # Gombok kerete
    gomb_keret = Frame(ujkonyvek, bg="#9A7E6F")
    gomb_keret.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")
    kilepo_keret = Frame(ujkonyvek, bg="#9A7E6F")
    kilepo_keret.grid(row=16, column=0, columnspan=2, pady=10, sticky="nsew")
    hozzaado_keret = Frame(ujkonyvek, bg="#9A7E6F")
    hozzaado_keret.grid(row=15, column=0, columnspan=2, pady=10, sticky="nsew")
    

    show_button = tk.Button(gomb_keret, text="Adatok mutatása", fg="#493628", bg="#D6C0B3", font="sans 13 bold", 
                            width=30, height=2, command=show)
    show_button.pack(pady=5)

    cime = Label(ujkonyvek, text="Írja be a címet ", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    cime.grid(row=5, column=0, columnspan=2, pady=(5, 5), sticky="nsew")

    Cím = Entry(ujkonyvek, width=20, bg="#D6C0B3" )
    Cím.grid(row=6, column=0, columnspan=2, pady=(0, 5))

    datuma = Label(ujkonyvek, text="Írja be a kiadasi dátumot:", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    datuma.grid(row=7, column=0, columnspan=2, pady=(5, 5), sticky="nsew")

    datum = Entry(ujkonyvek, width=20, bg="#D6C0B3")
    datum.grid(row=8, column=0, columnspan=2, pady=(0, 5))

    kiadoja = Label(ujkonyvek, text="Írja be a Kiadót: ", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    kiadoja.grid(row=9, column=0, columnspan=2, pady=(5, 5), sticky="nsew")

    kiado = Entry(ujkonyvek, width=20, bg="#D6C0B3")
    kiado.grid(row=10, column=0, columnspan=2, pady=(0, 5))
    
    oldalszama = Label(ujkonyvek, text="Írja be az Oldalszámot: ", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    oldalszama.grid(row=11, column=0, columnspan=2, pady=(5, 5), sticky="nsew")

    oldalszam = Entry(ujkonyvek, width=20, bg="#D6C0B3")
    oldalszam.grid(row=12, column=0, columnspan=2, pady=(0, 5))

    isbne = Label(ujkonyvek, text="Írja be az ISBN-t: ", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    isbne.grid(row=13, column=0, columnspan=2, pady=(5, 5), sticky="nsew")

    isbn = Entry(ujkonyvek, width=20, bg="#D6C0B3")
    isbn.grid(row=14, column=0, columnspan=2, pady=(0, 5))

    hozzaadas_button = tk.Button(hozzaado_keret, text="Hozzáadás", fg="#493628", bg="#D6C0B3", font="sans 13 bold", 
                             width=20, height=2)
    hozzaadas_button.pack(pady=10)

    close_button = tk.Button(kilepo_keret, text="Vissza", fg="#493628", bg="#FF8A8A", font="sans 13 bold", 
                             width=30, height=2, command=ujkonyvek.destroy)
    close_button.pack(pady=(0,10))
    beolvasas()
    ujkonyvek.mainloop()

ujfuggveny()