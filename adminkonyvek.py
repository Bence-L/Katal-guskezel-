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
    Adminkonyvek.geometry("750x700")
    Adminkonyvek.title("Könyvek")
    Adminkonyvek.configure(bg="#9A7E6F")

    #Cím
    title_label = tk.Label(Adminkonyvek, text="Könyvek🎄", bg="#9A7E6F", fg="#493628", font=('sans', 40, 'bold'))
    title_label.grid(row=0, column=0, columnspan=2, pady=(10, 10), sticky="nsew")

    #Beolvasás
    def beolvasas():
        global books
        #Üres lista könyveknek
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

    #Frissítés
    def mentes():
        with open('könyvek.txt', 'w', encoding='utf-8') as fajl:
            for book in books:
                fajl.write(f"{book.cim},{book.evszam},{book.kiado},{book.oldalszam},{book.isbn},{book.igennem}\n")

    #Mutatás
    def show():
        for item in listBox.get_children():
            listBox.delete(item)

        #Könyvek megjelenítése
        for i, book in enumerate(books, start=1):
            #Páros sorok kiválasztása
            if i % 2 == 0:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.igennem),
                            tags=('even',))
            else:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.igennem))

        #Szinezés 
        listBox.tag_configure('even', background='#AB886D')

    #Törlés
    def kijelolt_torleses():
        global books  
        kijelolt_konyvek = listBox.selection()
        to_delete = []
        for item in kijelolt_konyvek:
            #Sor adatainak kijelölése
            values = listBox.item(item, 'values')  
            listBox.delete(item)
            to_delete.append(int(values[0]))

        #Frissítjük a books listát
        books = [book for book in books if book.sorszam not in to_delete] 
        #Frissítjük a fájlt
        mentes()


    #Táblázat létrehozása
    cols = ('Sorszám', 'Cím', 'Kiadási dátum', 'Kiadó', 'Oldalszám', 'ISBN', 'Kölcsönzött-e?')
    listBox = ttk.Treeview(Adminkonyvek, columns=cols, show='headings', height=15)

    #Oszlopok beállítása
    for col in cols:
        listBox.heading(col, text=col)
        listBox.column(col, width=100) 

    #Scrollbar hozzáadása
    gorgeto = ttk.Scrollbar(Adminkonyvek, orient="vertical", command=listBox.yview)
    listBox.configure(yscroll=gorgeto.set)
    listBox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    gorgeto.grid(row=1, column=2, sticky="ns")

    #Gombok kerete
    gomb_keret = Frame(Adminkonyvek, bg="#9A7E6F")
    gomb_keret.grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")

    #Gombok
    show_button = tk.Button(gomb_keret, text="Adatok mutatása", fg="#493628", bg="#D6C0B3", font="sans 13 bold", width=30, height=2, command=show)
    show_button.pack(pady=5)

    delete_button = tk.Button(gomb_keret, text="Kijelölt mező törlése", fg="#493628", bg="#D6C0B3", font="sans 13 bold", width=30, height=2, command=kijelolt_torleses)
    delete_button.pack(pady=5)

    close_button = tk.Button(gomb_keret, text="Vissza", fg="#493628", bg="#FF8A8A", font="sans 13 bold", width=30, height=2, command=Adminkonyvek.destroy)
    close_button.pack(pady=5)

    #Könyvek beolvasása
    beolvasas()
    Adminkonyvek.mainloop()


