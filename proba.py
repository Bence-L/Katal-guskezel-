import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Treeview demo')
root.geometry('620x200')

# define columns
columns = ('Sorszám', 'Cím', 'Kiadási dátum', 'Kiadó', 'Oldalszám', 'ISBN', 'Kölcsönzött-e?')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('Sorszám', text='First Name')
tree.heading('Cím', text='Cím')
tree.heading('Kiadási dátum', text='Kiadási dátum')
tree.heading('Kiadó', text='Kiadó')
tree.heading('Oldalszám', text='Oldalszám ')
tree.heading('ISBN', text='ISBN')
tree.heading('Kölcsönzött-e?', text=' Kölcsönzött-e?')

class Objektum:
    def __init__(self, sorszam, cim, evszam, kiado, oldalszam, isbn, igennem):
        self.sorszam = sorszam
        self.cim = cim
        self.evszam = evszam
        self.kiado = kiado
        self.oldalszam = oldalszam
        self.isbn = isbn
        self.igennem = igennem


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
# generate sample data

# add data to the treeview
for i in books:
    tree.insert('', tk.END, values=books)


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
root.mainloop()