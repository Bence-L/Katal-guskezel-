from tkinter import *

def Lfuggveny():
    Lekerdezes = Tk()
    Lekerdezes.geometry("600x600")
    Lekerdezes.title("Lekérdezés")
    Lekerdezes.configure(bg="#B99470")
    proba = Label(Lekerdezes, text="Lekérdezés", bg="#B99470", fg="#664343",font=('sans', 60,'bold'),)
    proba.grid(row= 0, columnspan=1,pady=(10,0), padx=200)