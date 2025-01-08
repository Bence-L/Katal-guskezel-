from tkinter import *
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

def Lfuggveny():
    Lekerdezes = Tk()
    Lekerdezes.geometry("1420x750")
    Lekerdezes.title("Lekérdezés")
    Lekerdezes.configure(bg="#9A7E6F")

    # Cím
    proba = Label(Lekerdezes, text="Lekérdezés🎁", bg="#9A7E6F", fg="#493628", font=('sans', 60, 'bold'))
    proba.grid(row=0, columnspan=2, pady=(10, 10))

    # Globális könyvek lista
    global books
    books = []

    def beolvasas():
        """Beolvassa a könyveket a fájlból."""
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
        """Megjeleníti a könyveket a táblázatban."""
        # Törli az összes sort a táblázatból
        for item in listBox.get_children():
            listBox.delete(item)

        # Rendezett könyvek megjelenítése
        sorted_books = sorted(books, key=lambda book: book.sorszam)
        for i, book in enumerate(sorted_books, start=1):
            if i % 2 == 0:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.igennem),
                            tags=('even',))
            else:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.igennem))

        # Páros sorok színezése
        listBox.tag_configure('even', background='#AB886D')


    def search():
        """Keresés cím vagy ISBN alapján."""
        keresett_cim = Cím.get().strip().lower()
        keresett_isbn = isbn.get().strip().lower()

        # Hibaüzenet alaphelyzetbe
        error_label.config(text="")

        # Ellenőrizzük, hogy van-e megadott keresési feltétel
        if keresett_cim == "" and keresett_isbn == "":
            error_label.config(text="Adjon meg egy címet vagy ISBN-t a kereséshez!", fg="red")
            return

        # Keresés a táblázatban
        found = False
        for item in listBox.get_children():
            values = listBox.item(item, 'values')

            # Cím egyezés ellenőrzése
            cim_egyezes = False
            if keresett_cim != "":
                if keresett_cim in values[1].lower():
                    cim_egyezes = True

            # ISBN egyezés ellenőrzése
            isbn_egyezes = False
            if keresett_isbn != "":
                if keresett_isbn in values[5].lower():
                    isbn_egyezes = True

            # Ha van egyezés, kijelöljük az elemet
            if cim_egyezes or isbn_egyezes:
                listBox.selection_add(item)
                listBox.see(item)
                found = True

        # Hibaüzenet, ha nincs találat
        if found == False:
            error_label.config(text="Ilyen könyv nincs a kínálatunkban.", fg="red")



    # Táblázat létrehozása
    cols = ('Sorszám', 'Cím', 'Kiadási dátum', 'Kiadó', 'Oldalszám', 'ISBN', 'Kölcsönzött-e?')
    listBox = ttk.Treeview(Lekerdezes, columns=cols, show='headings', height=15)

    for col in cols:
        listBox.heading(col, text=col)

    listBox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Adatok mutatása gomb
    adat = Button(Lekerdezes, text="Adatok mutatása", fg="#493628", bg="#D6C0B3", font="sans 16 bold", command=show)
    adat.grid(row=2, column=0, columnspan=2, pady=10)

    # Cím keresési mező
    cime = Label(Lekerdezes, text="Írja be a címet:", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    cime.grid(row=3, column=0, pady=3, sticky="e")

    Cím = Entry(Lekerdezes, width=30, bg="#D6C0B3")
    Cím.grid(row=3, column=1, pady=3, sticky="w")

    # ISBN keresési mező
    isbne = Label(Lekerdezes, text="Írja be az ISBN-t:", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    isbne.grid(row=4, column=0, pady=3, sticky="e")

    isbn = Entry(Lekerdezes, width=30, bg="#D6C0B3")
    isbn.grid(row=4, column=1, pady=3, sticky="w")

    # Keresés gomb
    keres_gomb = Button(Lekerdezes, text="KERESÉS", fg="#493628", bg="#D6C0B3", font="sans 13 bold", command=search)
    keres_gomb.grid(row=5, column=0, columnspan=2, pady=10)

    # Hibaüzenet
    error_label = Label(Lekerdezes, text="", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    error_label.grid(row=6, column=0, columnspan=2, pady=5)

    # Vissza gomb
    bezaras = Button(Lekerdezes, text="Vissza", fg="#493628", bg="#FF8A8A", font="sans 13 bold", command=Lekerdezes.destroy)
    bezaras.grid(row=7, column=0, columnspan=2, pady=20)

    # Könyvek beolvasása
    beolvasas()
    Lekerdezes.mainloop()

Lfuggveny()
