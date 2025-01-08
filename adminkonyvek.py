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

    # Cím
    title_label = tk.Label(Adminkonyvek, text="Könyvek🎄", bg="#9A7E6F", fg="#493628", font=('sans', 40, 'bold'))
    title_label.grid(row=0, column=0, columnspan=2, pady=(10, 10), sticky="nsew")

    def beolvasas():
        """Beolvassa a könyveket a fájlból és tárolja őket a books listában."""
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
        """Frissíti a fájlt a books listában szereplő könyvekkel."""
        with open('könyvek.txt', 'w', encoding='utf-8') as fajl:
            for book in books:  # Minden könyvet végigírunk a fájlba
                fajl.write(f"{book.cim},{book.evszam},{book.kiado},{book.oldalszam},{book.isbn},{book.igennem}\n")

    def show():
        """Megjeleníti a könyveket a táblázatban."""
        # Törli az összes korábban megjelenített sort
        for item in listBox.get_children():
            listBox.delete(item)

        # Könyvek megjelenítése
        for i, book in enumerate(books, start=1):
            if i % 2 == 0:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.igennem),
                            tags=('even',))
            else:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.igennem))

        # Páros sorok színezése
        listBox.tag_configure('even', background='#AB886D')

    def delete_selected():
        """Törli a kijelölt könyveket a táblázatból és a fájlból."""
        global books  # Globális változó, amit frissíteni kell

        selected_items = listBox.selection()  # Kijelölt elemek
        to_delete = []  # Lista, amiben a törlendő könyveket tároljuk

        for item in selected_items:
            values = listBox.item(item, 'values')  # Kijelölt sor adatai
            listBox.delete(item)  # Könyv törlése a táblázatból
            to_delete.append(int(values[0]))  # Sorszámot hozzáadjuk a törlendők listájához

        # Frissítjük a books listát, eltávolítva a törölt könyveket
        books = [book for book in books if book.sorszam not in to_delete]
        
        # Frissítjük a fájlt is a módosított könyvlistával
        mentes()


    # Táblázat létrehozása
    cols = ('Sorszám', 'Cím', 'Kiadási dátum', 'Kiadó', 'Oldalszám', 'ISBN', 'Kölcsönzött-e?')
    listBox = ttk.Treeview(Adminkonyvek, columns=cols, show='headings', height=15)

    # Oszlopok beállítása
    for col in cols:
        listBox.heading(col, text=col)
        listBox.column(col, width=100)  # Oszlop szélesség

    # Scrollbar hozzáadása
    scrollbar = ttk.Scrollbar(Adminkonyvek, orient="vertical", command=listBox.yview)
    listBox.configure(yscroll=scrollbar.set)
    listBox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    scrollbar.grid(row=1, column=2, sticky="ns")

    # Gombok kerete
    button_frame = Frame(Adminkonyvek, bg="#9A7E6F")
    button_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")

    # Gombok
    show_button = tk.Button(button_frame, text="Adatok mutatása", fg="#493628", bg="#D6C0B3", font="sans 13 bold", 
                            width=30, height=2, command=show)
    show_button.pack(pady=5)

    delete_button = tk.Button(button_frame, text="Kijelölt mező törlése", fg="#493628", bg="#D6C0B3", font="sans 13 bold", 
                              width=30, height=2, command=delete_selected)
    delete_button.pack(pady=5)

    close_button = tk.Button(button_frame, text="Vissza", fg="#493628", bg="#FF8A8A", font="sans 13 bold", 
                             width=30, height=2, command=Adminkonyvek.destroy)
    close_button.pack(pady=5)

    # Könyvek beolvasása
    beolvasas()
    Adminkonyvek.mainloop()

adminkonyvei()
