from tkinter import*
import felhasznaloi
import AdminKezdolap

master = Tk()
master.geometry("600x400")
master.title("Főoldal")
master.configure(bg="#9A7E6F")
def ujabblaknyitas():
     felhasznaloi.alap()
def adminablak():
    AdminKezdolap.adminegesz()

cím = Label(master, text="Kezdőoldal📖", fg="#493628",bg="#9A7E6F",font=('Times', 60,'bold'))
cím.grid(row= 1, columnspan=3,pady=(1,0), padx=60)
felhasznalonev = Label(master, text="Írja be a felhasználónevét: ", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
felhasznalonev.grid(row=2, columnspan=3, pady=4, padx=5)

username = Entry(master, width=20, bg="#D6C0B3")
username.grid(row=3, columnspan=3, pady=3, padx=5)

jelszoleiras = Label(master, text="Írja be a jelszavát: ", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
jelszoleiras.grid(row=4, columnspan=3, pady=4, padx=5)

jelszo = Entry(master, width=20, bg="#D6C0B3", show="*")
jelszo.grid(row=5, columnspan=3, pady=3, padx=5)


def ellenoriz():
        felhasznalonev = username.get()
        jelszom = jelszo.get()
        if felhasznalonev == "Felhasznalo" and jelszom == "Felhasznalo" :
            # Fő ablak bezárása sikeres bejelentkezés esetén
            ujabblaknyitas()
        if felhasznalonev == "Admin" and jelszom == "Admin":
            adminablak()
        else:
            rossz = Label(master, text="Rossz jelszó, próbáld újra", bg="#9A7E6F",fg="#493628", font=('Comic Sans', 11, 'bold'))
            rossz.grid(row=7, column=1, pady=10, padx=20) 
            def eltavolit():
                rossz.destroy()
            rossz.after(2000, eltavolit)
            

    # Ellenőrző gomb, amely hívja az ellenőrző függvényt
ellenorzo = Button(master, text="Ellenőrzés!", fg="#493628", bg="#D6C0B3", font="sans 13 bold", command=ellenoriz)
ellenorzo.grid(row=6, column=1, pady=10, padx=20)


mainloop()