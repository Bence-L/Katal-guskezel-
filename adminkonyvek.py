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

    def save_to_file():
        """Frissíti a fájlt a listából."""
        with open('könyvek.txt', 'w', encoding='utf-8') as fajl:
            for book in books:
                fajl.write(f"{book.cim},{book.evszam},{book.kiado},{book.oldalszam},{book.isbn},{book.igennem}\n")

    def show():
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

        listBox.tag_configure('even', background='#AB886D')  # Páros sorok színezése

    def delete_selected():
        """Törli a kijelölt könyveket a táblázatból és a fájlból."""
        global books
        selected_items = listBox.selection()  # Kijelölt elemek
        to_delete = []

        for item in selected_items:
            values = listBox.item(item, 'values')  # Kijelölt sor adatai
            listBox.delete(item)  # Törlés a Treeview-ból
            to_delete.append(int(values[0]))  # Sorszám alapú azonosítás

        # Könyvek szűrése a törléshez
        books = [book for book in books if book.sorszam not in to_delete]
        save_to_file()  # Frissítés a fájlban

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
