from tkinter import *
from tkinter import ttk


class Konyv:
    def __init__(self, sorszam, cim, evszam, kiado, oldalszam, isbn, kolcsonzott):
        self.sorszam = sorszam
        self.cim = cim
        self.evszam = evszam
        self.kiado = kiado
        self.oldalszam = oldalszam
        self.isbn = isbn
        self.kolcsonzott = kolcsonzott


def konyv_modositas():
    ablak = Tk()
    ablak.geometry("1450x750")
    ablak.title("Lekérdezés")
    ablak.configure(bg="#9A7E6F")

    #Cím
    cimke = Label(ablak, text="Módosítás🧪", bg="#9A7E6F", fg="#493628", font=('sans', 40, 'bold'))
    cimke.grid(row=0, columnspan=3, pady=(10, 10))

    global konyvek
    konyvek = []

    #Beolvasás
    def beolvasas():
        global konyvek
        konyvek = []
        with open('könyvek.txt', 'r', encoding='utf-8') as fajl:
            for i, sor in enumerate(fajl, start=1):
                adatok = sor.strip().split(',')
                konyv = Konyv(i, *[adat.strip() for adat in adatok])
                konyvek.append(konyv)

    #Megjelenítés
    def megjelenites():
        tabla.delete(*tabla.get_children())
        for konyv in konyvek:
            tabla.insert("", "end", values=(konyv.sorszam, konyv.cim, konyv.evszam, konyv.kiado, konyv.oldalszam, konyv.isbn, konyv.kolcsonzott))

    #Betöltés
    def betoltes():
        kivalasztott = tabla.selection()
        if kivalasztott:
            ertekek = tabla.item(kivalasztott[0], 'values')
            for konyv in konyvek:
                if str(konyv.sorszam) == ertekek[0]:
                    kitoltes(konyv)

    #Az entryk feltöltése adatokkal
    def kitoltes(konyv):
        sorszam_mezo.delete(0, END)
        cim_mezo.delete(0, END)
        evszam_mezo.delete(0, END)
        kiado_mezo.delete(0, END)
        oldalszam_mezo.delete(0, END)
        isbn_mezo.delete(0, END)
        kolcsonzott_mezo.delete(0, END)

        sorszam_mezo.insert(0, konyv.sorszam)
        cim_mezo.insert(0, konyv.cim)
        evszam_mezo.insert(0, konyv.evszam)
        kiado_mezo.insert(0, konyv.kiado)
        oldalszam_mezo.insert(0, konyv.oldalszam)
        isbn_mezo.insert(0, konyv.isbn)
        kolcsonzott_mezo.insert(0, konyv.kolcsonzott)

    #Mentés
    def mentes():
        kivalasztott = tabla.selection()
        if kivalasztott:
            ertekek = tabla.item(kivalasztott[0], 'values')
            for konyv in konyvek:
                if str(konyv.sorszam) == ertekek[0]:
                    konyv.sorszam = sorszam_mezo.get()
                    konyv.cim = cim_mezo.get()
                    konyv.evszam = evszam_mezo.get()
                    konyv.kiado = kiado_mezo.get()
                    konyv.oldalszam = oldalszam_mezo.get()
                    konyv.isbn = isbn_mezo.get()
                    konyv.kolcsonzott = kolcsonzott_mezo.get()

            with open('könyvek.txt', 'w', encoding='utf-8') as fajl:
                for konyv in konyvek:
                    fajl.write(f"{konyv.cim},{konyv.evszam},{konyv.kiado},{konyv.oldalszam},{konyv.isbn},{konyv.kolcsonzott}\n")

            megjelenites()

    oszlopok = ('Sorszám', 'Cím', 'Kiadási dátum', 'Kiadó', 'Oldalszám', 'ISBN', 'Kölcsönzött-e?')
    tabla = ttk.Treeview(ablak, columns=oszlopok, show='headings', height=8)

    for oszlop in oszlopok:
        tabla.heading(oszlop, text=oszlop)

    #Scrollbar
    gorgeto = Scrollbar(ablak, orient=VERTICAL, command=tabla.yview)
    tabla.configure(yscrollcommand=gorgeto.set)

    gorgeto.grid(row=1, column=2, sticky="ns", padx=(0, 10))
    tabla.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    #Adatok megmutatása gomb
    adat_gomb = Button(ablak, text="Adatok mutatása", fg="#493628", bg="#D6C0B3", font="sans 16 bold", command=lambda: [beolvasas(), megjelenites()])
    adat_gomb.grid(row=2, column=0, columnspan=2, pady=10)

    #A kiválasztott sor adatainak betöltése
    betolt_gomb = Button(ablak, text="Lekérdezés", fg="#493628", bg="#D6C0B3", font="sans 13 bold", width=20, height=2, command=betoltes)
    betolt_gomb.grid(row=3, column=0, columnspan=2, pady=10)

    cimkek = ["Sorszám:", "Cím:", "Kiadási dátum:", "Kiadó:", "Oldalszám:", "ISBN:", "Kölcsönzött-e?"]
    mezok = []


    for i, cimke_szoveg in enumerate(cimkek):
        cimke = Label(ablak, text=cimke_szoveg, bg="#9A7E6F", fg="#493628", font=('Comic Sans', 10, 'bold'))
        cimke.grid(row=4 + i, column=0, sticky="e", pady=5)

        mezo = Entry(ablak, width=30, bg="#D6C0B3")
        mezo.grid(row=4 + i, column=1, sticky="w", pady=5)
        mezok.append(mezo)

    sorszam_mezo, cim_mezo, evszam_mezo, kiado_mezo, oldalszam_mezo, isbn_mezo, kolcsonzott_mezo = mezok

    #Mentő és bezáró gomb
    mentes_gomb = Button(ablak, text="Mentés", fg="#493628", bg="#D6C0B3", font="sans 13 bold", command=mentes)
    mentes_gomb.grid(row=11, column=0, columnspan=2, pady=10)
    bezar_gomb = Button(ablak, text="Bezárás", fg="#493628", bg="#FF8A8A", font="sans 13 bold", command=ablak.destroy)
    bezar_gomb.grid(row=12, column=0, columnspan=2, pady=10)

    ablak.mainloop()


konyv_modositas()
