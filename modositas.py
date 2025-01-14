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

def mfugveny():
    Modositas = Tk()
    Modositas.geometry("1420x750")
    Modositas.title("Lekérdezés")
    Modositas.configure(bg="#9A7E6F")

    proba = Label(Modositas, text="Lekérdezés🎁", bg="#9A7E6F", fg="#493628", font=('sans', 60, 'bold'))
    proba.grid(row=0, columnspan=2, pady=(10, 10))

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
        for item in listBox.get_children():
            listBox.delete(item)

        sorted_books = sorted(books, key=lambda book: book.sorszam)
        for i, book in enumerate(sorted_books, start=1):
            if i % 2 == 0:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.igennem),
                            tags=('even',))
            else:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.igennem))

        listBox.tag_configure('even', background='#AB886D')

    def on_select(event):
        """Kiválasztott könyv adatainak betöltése az Entry mezőkbe."""
        selected_item = listBox.selection()
        if selected_item:
            values = listBox.item(selected_item[0], 'values')
            for book in books:
                if str(book.sorszam) == values[0]:
                    populate_entries(book)

    def populate_entries(book):
        """Kitölti az Entry mezőket a könyv adataival."""
        sorszam_entry.delete(0, END)
        cim_entry.delete(0, END)
        evszam_entry.delete(0, END)
        kiado_entry.delete(0, END)
        oldalszam_entry.delete(0, END)
        isbn_entry.delete(0, END)
        igennem_entry.delete(0, END)

        sorszam_entry.insert(0, book.sorszam)
        cim_entry.insert(0, book.cim)
        evszam_entry.insert(0, book.evszam)
        kiado_entry.insert(0, book.kiado)
        oldalszam_entry.insert(0, book.oldalszam)
        isbn_entry.insert(0, book.isbn)
        igennem_entry.insert(0, book.igennem)

    def save_changes():
        """Mentés gomb megnyomására frissíti a könyv adatait."""
        selected_item = listBox.selection()
        if selected_item:
            values = listBox.item(selected_item[0], 'values')
            for book in books:
                if str(book.sorszam) == values[0]:
                    book.sorszam = sorszam_entry.get()
                    book.cim = cim_entry.get()
                    book.evszam = evszam_entry.get()
                    book.kiado = kiado_entry.get()
                    book.oldalszam = oldalszam_entry.get()
                    book.isbn = isbn_entry.get()
                    book.igennem = igennem_entry.get()
                    show()

    cols = ('Sorszám', 'Cím', 'Kiadási dátum', 'Kiadó', 'Oldalszám', 'ISBN', 'Kölcsönzött-e?')
    listBox = ttk.Treeview(Modositas, columns=cols, show='headings', height=15)

    for col in cols:
        listBox.heading(col, text=col)

    listBox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    listBox.bind('<<TreeviewSelect>>', on_select)

    adat = Button(Modositas, text="Adatok mutatása", fg="#493628", bg="#D6C0B3", font="sans 16 bold", command=show)
    adat.grid(row=2, column=0, columnspan=2, pady=10)

    labels = ["Sorszám:", "Cím:", "Kiadási dátum:", "Kiadó:", "Oldalszám:", "ISBN:", "Kölcsönzött-e:"]
    entries = []

    for i, label_text in enumerate(labels):
        label = Label(Modositas, text=label_text, bg="#9A7E6F", fg="#493628", font=('Comic Sans', 10, 'bold'))
        label.grid(row=3 + i, column=0, sticky="e", pady=5)

        entry = Entry(Modositas, width=30, bg="#D6C0B3")
        entry.grid(row=3 + i, column=1, sticky="w", pady=5)
        entries.append(entry)

    sorszam_entry, cim_entry, evszam_entry, kiado_entry, oldalszam_entry, isbn_entry, igennem_entry = entries

    save_button = Button(Modositas, text="Mentés", fg="#493628", bg="#D6C0B3", font="sans 13 bold", command=save_changes)
    save_button.grid(row=10, column=0, columnspan=2, pady=10)

    beolvasas()
    show()
    Modositas.mainloop()

mfugveny()
