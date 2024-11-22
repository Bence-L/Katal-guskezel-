from tkinter import*
import felhasznaloi
import AdminKezdolap

master = Tk()
master.geometry("1000x800")
master.title("Főoldal")
master.configure(bg="black")
def ujabblaknyitas():
     felhasznaloi.alap()
def adminablak():
    AdminKezdolap.adminegesz()

cím = Label(master, text="Kezdooldal™", fg="#28e8fa",bg="black",font=('Times', 60,'bold'))
cím.grid(row= 1, columnspan=3,pady=(1,0), padx=320)
jelszo_bence = Label(master, text="Írja be a felhasználónevét: ", fg="#28e8fa", bg="black", font=('Comic Sans', 10, 'bold'))
jelszo_bence.grid(row=2, columnspan=3, pady=4, padx=5)

username = Entry(master, width=20, bg="#28e8fa")
username.grid(row=3, columnspan=3, pady=3, padx=5)
jelszo_bence = Label(master, text="Írja be a jelszavát: ", fg="#28e8fa", bg="black", font=('Comic Sans', 10, 'bold'))
jelszo_bence.grid(row=4, columnspan=3, pady=4, padx=5)
jelszo = Entry(master, width=20, bg="#28e8fa", show="*")
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
            rossz = Label(master, text="Rossz jelszó, próbáld újra", bg="black",fg="#28e8fa", font=('Comic Sans', 16, 'bold'))
            rossz.grid(row=7, column=1, pady=10, padx=20) 

    # Ellenőrző gomb, amely hívja az ellenőrző függvényt
ellenorzo = Button(master, text="Ellenőrzés!", fg="#28e8fa", bg="black", font="sans 13 bold", command=ellenoriz)
ellenorzo.grid(row=6, column=1, pady=10, padx=20)


mainloop()