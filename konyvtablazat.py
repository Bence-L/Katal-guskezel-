from tkinter import*
import tkinter as tk
from tkinter import ttk
def tablazat():
    tablazat = Tk()
    tablazat.geometry("1000x800")
    tablazat.title("Táblázat")
    tablazat.configure(bg="#9A7E6F")
    

    

    def show():

        tempList = []
        tempList.sort(key=lambda e: e[1], reverse=True)

        for i, (name, title, borrowed) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(i, name, title, borrowed))

    label = tk.Label(tablazat, text="Könyvek", font=("Arial",30)).grid(row=0, columnspan=4)
    # create Treeview with 3 columns
    cols = ('Position', 'Író', 'Cím', 'Kölcsönzött-e')
    listBox = ttk.Treeview(tablazat, columns=cols, show='headings')
    # set column headings
    for col in cols:
        listBox.heading(col, text=col)    
    listBox.grid(row=1, column=0, columnspan=2)

    showScores = tk.Button(tablazat, text="Show tablazat", width=15, command=show).grid(row=4, column=0)
    closeButton = tk.Button(tablazat, text="Close", width=15, command=exit).grid(row=4, column=1)



    tablazat.mainloop()