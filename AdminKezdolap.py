from tkinter import *

Akezdo = Tk()
Akezdo.geometry("900x800")
Akezdo.title("Főoldal")
Akezdo.configure(bg="#B99470")
proba = Label(Akezdo, text="Próba", bg="#B99470",font=('Times', 60,'bold'))
proba.grid(row= 0, columnspan=3,pady=(10,0), padx=320)
#probalista = Label(Akezdo, text="1. 1984, 1949, Secker & Warburg, 328, 978-0451524935 \n 2. A kertészeti kézikönyv, 1996, Gulyás Kiadó, 400, 978-9632002336 \n  3. A mester és margarita, 1967, Harvill Press, 448, 978-0141180147 \n  4. To kill a mockingbird, 1960, J.B. Lippincott & Co., 281, 978-0061120084 \n  5. Harry potter és a bölcsek köve, 1997, Animus Kiadó, 320, 978-963-9700-57-7 \n  50. A nyugati világ vége, 2020, Tilos Az Á Kiadó, 301, 978-9634104216", bg="#B99470",font=('Times', 20,'bold'))
#probalista.grid(row= 1,pady=(10,0), padx=320)
mainloop()