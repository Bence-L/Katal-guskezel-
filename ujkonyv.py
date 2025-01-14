from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
    
    #Címsor
    proba = Label(ujkonyvek, text="Hozzáadás", bg="#9A7E6F", fg="#493628", font=('sans', 40, 'bold'))
    proba.grid(row=0, column=0, columnspan=2, pady=(10, 10), sticky="nsew")

    #Beolvasás
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

    #Mentés
    def mentes():
        with open('könyvek.txt', 'w', encoding='utf-8') as fajl:
            for book in books:
                fajl.write(f"{book.cim},{book.evszam},{book.kiado},{book.oldalszam},{book.isbn},{book.igennem}\n")

    #Adatok megjelenítése a táblázatban
    def megjelenit():
        for item in listBox.get_children():
            listBox.delete(item)

        for i, book in enumerate(books, start=1):
            if i % 2 == 0:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.igennem),
                               tags=('even',))
            else:
                listBox.insert("", "end", values=(book.sorszam, book.cim, book.evszam, book.kiado, book.oldalszam, book.isbn, book.igennem))
        listBox.tag_configure('even', background='#AB886D')

    #Az új könyv hozzáadása a táblázathoz és a txthez is.
    def hozzaadas():
        # Mezők értékeinek kiolvasása
        cim = Cím.get().strip()
        evszam = datum.get().strip()
        kiado = kiado_mezo.get().strip()
        oldalszam = oldalszam_mezo.get().strip()
        isbn = isbn_mezo.get().strip()

        #A mezők listája
        mezok = [cim, evszam, kiado, oldalszam, isbn]
        
        #Megnézi hogy van e üres mező
        ures_mezo_talalva = False
        for mezo in mezok:
            if mezo == "":
                ures_mezo_talalva = True
                break

        # Ha talál üres mezőt, felugrik egy üzenet ami figyelmeztet
        if ures_mezo_talalva:
            messagebox.showwarning("Hiányzó adatok", "Kérlek tölts ki minden mezőt!")
            return

        #Új objektum készítése
        sorszam = len(books) + 1
        uj_konyv = Objektum(sorszam, cim, evszam, kiado, oldalszam, isbn, "Nem")
        books.append(uj_konyv)

        #Táblázat frissítése
        listBox.insert("", "end", values=(sorszam, cim, evszam, kiado, oldalszam, isbn, "Nem"))

        #könyvek.txt frissítése
        with open('könyvek.txt', 'a', encoding='utf-8') as fajl:
            fajl.write(f"{cim},{evszam},{kiado},{oldalszam},{isbn},Nem\n")

        #Mezők ürítése a beküldés után hogy megint lehessen hozzáadni
        Cím.delete(0, tk.END)
        datum.delete(0, tk.END)
        kiado_mezo.delete(0, tk.END)
        oldalszam_mezo.delete(0, tk.END)
        isbn_mezo.delete(0, tk.END)

    cols = ('Sorszám', 'Cím', 'Kiadási dátum', 'Kiadó', 'Oldalszám', 'ISBN', 'Kölcsönzött-e?')
    listBox = ttk.Treeview(ujkonyvek, columns=cols, show='headings', height=11)
    for col in cols:
        listBox.heading(col, text=col)
        listBox.column(col, width=100)
    
    #Táblázathoz görgetés.
    gorgeto = ttk.Scrollbar(ujkonyvek, orient="vertical", command=listBox.yview)
    listBox.configure(yscroll=gorgeto.set)
    listBox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    gorgeto.grid(row=1, column=2, sticky="ns")

    #gomb stílusai és elhelyezkedés helye
    gomb_keret = Frame(ujkonyvek, bg="#9A7E6F")
    gomb_keret.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")
    kilepo_keret = Frame(ujkonyvek, bg="#9A7E6F")
    kilepo_keret.grid(row=16, column=0, columnspan=2, pady=10, sticky="nsew")
    hozzaado_keret = Frame(ujkonyvek, bg="#9A7E6F")
    hozzaado_keret.grid(row=15, column=0, columnspan=2, pady=10, sticky="nsew")

    #gomb ami megjeleníti az adatokat
    adatok_megjelenitese = tk.Button(gomb_keret, text="Adatok mutatása", fg="#493628", bg="#D6C0B3", font="sans 13 bold", width=30, height=2, command=megjelenit)
    adatok_megjelenitese.pack(pady=3)

    #Az entry mezők és a hozzájuk tartozó leírások
    cime = Label(ujkonyvek, text="Írja be a címet ", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    cime.grid(row=5, column=0, columnspan=2, pady=(2, 2), sticky="nsew")

    Cím = Entry(ujkonyvek, width=20, bg="#D6C0B3")
    Cím.grid(row=6, column=0, columnspan=2, pady=(0, 3))

    datuma = Label(ujkonyvek, text="Írja be a kiadasi dátumot:", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    datuma.grid(row=7, column=0, columnspan=2, pady=(2, 2), sticky="nsew")

    datum = Entry(ujkonyvek, width=20, bg="#D6C0B3")
    datum.grid(row=8, column=0, columnspan=2, pady=(0, 3))

    kiadoja = Label(ujkonyvek, text="Írja be a Kiadót: ", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    kiadoja.grid(row=9, column=0, columnspan=2, pady=(2, 2), sticky="nsew")

    kiado_mezo = Entry(ujkonyvek, width=20, bg="#D6C0B3")
    kiado_mezo.grid(row=10, column=0, columnspan=2, pady=(0, 3))

    oldalszama = Label(ujkonyvek, text="Írja be az Oldalszámot: ", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    oldalszama.grid(row=11, column=0, columnspan=2, pady=(2, 2), sticky="nsew")

    oldalszam_mezo = Entry(ujkonyvek, width=20, bg="#D6C0B3")
    oldalszam_mezo.grid(row=12, column=0, columnspan=2, pady=(0, 3))

    isbne = Label(ujkonyvek, text="Írja be az ISBN-t: ", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    isbne.grid(row=13, column=0, columnspan=2, pady=(2, 2), sticky="nsew")

    isbn_mezo = Entry(ujkonyvek, width=20, bg="#D6C0B3")
    isbn_mezo.grid(row=14, column=0, columnspan=2, pady=(0, 3))

    #Hozzáadó gomb és a bezáró gomb
    hozzaadas_button = tk.Button(hozzaado_keret, text="Hozzáadás", fg="#493628", bg="#D6C0B3", font="sans 13 bold", width=30, height=2, command=hozzaadas)
    hozzaadas_button.pack(pady=10)

    close_button = tk.Button(kilepo_keret, text="Vissza", fg="#493628", bg="#FF8A8A", font="sans 13 bold", width=30, height=2, command=ujkonyvek.destroy)
    close_button.pack(pady=(0,10))

    beolvasas()
    ujkonyvek.mainloop()

