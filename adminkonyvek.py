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

def adminkonyvei():
    Adminkonyvek = tk.Tk()
    Adminkonyvek.geometry("1600x600")
    Adminkonyvek.title("Lekérdezés")
    Adminkonyvek.configure(bg="#9A7E6F")
    
    proba = tk.Label(Adminkonyvek, text="Könyvek", bg="#9A7E6F", fg="#493628", font=('sans', 70, 'bold'))
    proba.grid(row=0, columnspan=1, pady=(10, 10), padx=(400))

    def beolvasas():
        global books
        books = []
        with open('könyvek.txt', 'r', encoding='utf-8') as fajl:
            for i, sor in enumerate(fajl, start=1):  # Az enumerate segítségével a könyvek sorszámot kapnak
                adat = sor.strip().split(',')  # A könyvek adatait vesszővel elválasztva olvassuk
                cim = adat[0].strip()  # A cím tisztítása (ha van fölösleges szóköz)
                evszam = adat[1].strip()
                kiado = adat[2].strip()
                oldalszam = adat[3].strip()
                isbn = adat[4].strip()
                book = Objektum(i, cim, evszam, kiado, oldalszam, isbn)  # A sorszámot az enumerate biztosítja
                books.append(book)

    def show():
        # Töröljük a meglévő adatokat a táblázatból
        for item in listBox.get_children():
            listBox.delete(item)
        
        # Könyvek sorbarendezése a sorszámok szerint
        sorted_books = sorted(books, key=lambda book: book.sorszam)  # Az sorszam alapján rendezzük

        # Könyvek adatainak kiírása a táblázatba
        for i, book in enumerate(sorted_books, start=1):
            listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.kolcsonzott))

    cols = ('Sorszám', 'Cím', 'Kiadási dátum', 'Kiadó', 'Oldalszám', 'ISBN', 'Kölcsönzött-e?')
    listBox = ttk.Treeview(Adminkonyvek, columns=cols, show='headings')

    # Fejléc beállítása
    for col in cols:
        listBox.heading(col, text=col)
    
    # A Treeview elhelyezése a főablakban
    listBox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Gomb, amellyel a táblázatot megjeleníthetjük
    showScores = tk.Button(Adminkonyvek, text="Show tablazat", width=15, command=show)
    showScores.grid(row=4, column=0, padx=(200, 40))

    # Gomb, amellyel az ablakot bezárhatjuk
    closeButton = tk.Button(Adminkonyvek, text="Close", width=15, command=Adminkonyvek.quit)
    closeButton.grid(row=4, column=1, padx=(40, 200))

    # Könyvek beolvasása a fájlból
    beolvasas()

    # Az ablak futtatása
    Adminkonyvek.mainloop()

# A függvény meghívása
adminkonyvei()

