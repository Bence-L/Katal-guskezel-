from tkinter import *
import tkinter as tk
from tkinter import ttk


def ujfuggveny():
    ujkonyvek = tk.Tk()
    ujkonyvek.geometry("1420x600")
    ujkonyvek.title("Könyvek")
    ujkonyvek.configure(bg="#9A7E6F")

    proba = Label(ujkonyvek, text="Hozzáadás", bg="#9A7E6F", fg="#493628", font=('sans', 60, 'bold'))
    proba.grid(row=0, pady=(10, 10), padx=(480,100))


    cime = Label(ujkonyvek, text="Írja be a címet ", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    cime.grid(row=1, pady=3, padx=(0, 150))

    Cím = Entry(ujkonyvek, width=20, bg="#D6C0B3")
    Cím.grid(row=2, pady=3, padx=(0, 150))

    isbne = Label(ujkonyvek, text="Írja be az ISBN-t: ", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    isbne.grid(row=1, pady=3, padx=(0,300))

    isbn = Entry(ujkonyvek, width=20, bg="#D6C0B3")
    isbn.grid(row=2, pady=3, padx=(0,300))

    datuma = Label(ujkonyvek, text="Írja be a kiadasi dátumot:", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    datuma.grid(row=1, pady=3, padx=(0, 450))

    datum = Entry(ujkonyvek, width=20, bg="#D6C0B3")
    datum.grid(row=2, pady=3, padx=(0, 450))

    kiadoja = Label(ujkonyvek, text="Írja be az Kiadót: ", fg="#493628", bg="#9A7E6F", font=('Comic Sans', 10, 'bold'))
    kiadoja.grid(row=1, pady=3, padx=(0,600))

    kiado = Entry(ujkonyvek, width=20, bg="#D6C0B3")
    kiado.grid(row=2, pady=3, padx=(0,600))