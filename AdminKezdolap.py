from tkinter import *
import adminkonyvek
import Lekerdezes
import ujkonyv
import modositas
def adminegesz():
    def LekerdezesNyitas():
        Lekerdezes.Lfuggveny()
    def ujnyitas():
        ujkonyv.ujfuggveny()
    def ModositasNyitas():
        modositas.mfugveny()
    
    def ADMINKONYV():
        adminkonyvek.adminkonyvei()

    Akezdo = Tk()
    Akezdo.geometry("1000x900")
    Akezdo.title("Főoldal")
    Akezdo.configure(bg="#9A7E6F")
    proba = Label(Akezdo, text="Adminisztrátor", bg="#9A7E6F", fg="#493628",font=('sans', 60,'bold'),)
    proba.grid(row= 0, columnspan=1,pady=(10,0), padx=200)
    konyvek = Button(Akezdo, text ="Könyvek - Törlése", bg="#D6C0B3", fg="#493628",font="sans 20 bold",  borderwidth=3, width= 40, height=3, command=ADMINKONYV).grid(row= 1, pady=4,padx=10)
    lekerdezes = Button(Akezdo, text ="Lekérdezés", bg="#D6C0B3", fg="#493628", font="sans 20 bold",  borderwidth=3, width= 40, height=3, command=LekerdezesNyitas).grid(row= 2, pady=4,padx=6)
    mdositas = Button(Akezdo, text ="Módosítás", bg="#D6C0B3", fg="#493628", font="sans 20 bold",  borderwidth=3, width= 40, height=3, command=ModositasNyitas).grid(row= 3, pady=4,padx=6)
    uj = Button(Akezdo, text ="Új könyv", bg="#D6C0B3",fg="#493628", font="sans 20 bold",  borderwidth=3, width= 40, height=3, command=ujnyitas).grid(row= 4, pady=4,padx=16)
    
    bezárás = Button(Akezdo, text ="Bezárás", bg="#FF8A8A", font="sans 16 bold",  borderwidth=10, command=Akezdo.destroy).grid(row= 6, pady=30,padx=200)
    
    Akezdo.mainloop()