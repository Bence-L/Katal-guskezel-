from tkinter import *
import adminkonyvek
import Lekerdezes
import ujkonyv
def adminegesz():
    def LekerdezesNyitas():
        Lekerdezes.Lfuggveny()
    def ujnyitas():
        ujkonyv.ujfuggveny()
    #     Modositas.Mfuggveny()
    # def HozzaadasNyitas():
    #     Hozzaadas.Hfuggveny()
    # def TorlesNyitas():
    #     Torles.Tfuggveny()
    def ADMINKONYV():
        adminkonyvek.adminkonyvei()

    Akezdo = Tk()
    Akezdo.geometry("1000x900")
    Akezdo.title("Főoldal")
    Akezdo.configure(bg="#9A7E6F")
    proba = Label(Akezdo, text="Adminisztrátor", bg="#9A7E6F", fg="#493628",font=('sans', 60,'bold'),)
    proba.grid(row= 0, columnspan=1,pady=(10,0), padx=200)
    konyvek = Button(Akezdo, text ="Könyvek - Törlése", bg="#D6C0B3", fg="#493628",font="sans 20 bold",  borderwidth=3, width= 40, height=3, command=ADMINKONYV).grid(row= 1, pady=4,padx=10)
    lekerdezes = Button(Akezdo, text ="Lekérdezés - Módosítás", bg="#D6C0B3", fg="#493628", font="sans 20 bold",  borderwidth=3, width= 40, height=3, command=LekerdezesNyitas).grid(row= 2, pady=4,padx=6)
    uj = Button(Akezdo, text ="Új könyv", bg="#D6C0B3",fg="#493628", font="sans 20 bold",  borderwidth=3, width= 40, height=3, command=ujnyitas).grid(row= 3, pady=4,padx=16)
    # hozzáadás = Button(Akezdo, text ="Hozzáadás", bg="#D6C0B3", fg="#493628",font="sans 20 bold",  borderwidth=3, width= 40, height=3, command=HozzaadasNyitas).grid(row= 4, pady=4,padx=6)
    
    bezárás = Button(Akezdo, text ="Bezárás", bg="#FF8A8A", font="sans 16 bold",  borderwidth=10, command=Akezdo.destroy).grid(row= 6, pady=30,padx=200)
    #probalista = Label(Akezdo, text="1. 1984, 1949, Secker & Warburg, 328, 978-0451524935 \n 2. A kertészeti kézikönyv, 1996, Gulyás Kiadó, 400, 978-9632002336 \n  3. A mester és margarita, 1967, Harvill Press, 448, 978-0141180147 \n  4. To kill a mockingbird, 1960, J.B. Lippincott & Co., 281, 978-0061120084 \n  5. Harry potter és a bölcsek köve, 1997, Animus Kiadó, 320, 978-963-9700-57-7 \n  50. A nyugati világ vége, 2020, Tilos Az Á Kiadó, 301, 978-9634104216", bg="#B99470",font=('Times', 20,'bold'))
    #probalista.grid(row= 1,pady=(10,0), padx=320)
    Akezdo.mainloop()