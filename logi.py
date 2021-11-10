from tkinter import *
from tkinter import messagebox
def fa_jauns():
    messagebox.showinfo("Info","Šeit atveram failu")
# Izveidojam logu
logs1 = Tk()
logs1.title("Mana programma")
logs1.geometry("400x400")
menubar = Menu(logs1) # sagatavo izvēlņu joslu
# Izveido
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=fa_jauns)
filemenu.add_command(label="Open", command=fa_jauns)
filemenu.add_command(label="Save", command=fa_jauns)
filemenu.add_command(label="Save as...", command=fa_jauns)
filemenu.add_separator()
filemenu.add_command(label="Close", command=fa_jauns)
# --- nākamās divas rindiņas ievieto izvēlņu joslā
# iepriekš sagatavoto kaskādi
menubar.add_cascade(label="File", menu=filemenu)
logs1.config(menu=menubar)

#messagebox.showinfo("Info","Šī ir vienkāršā info") 
#messagebox.showwarning("Ūūū", "Šis ir brīdinājums")  
#messagebox.showerror("Alles kaput", "Fatāla kļūda")
# Izvēlne ---------------------------
#izvelne = Menu(logs1)
##faili = Menu(izvelne, tearoff=0)
#paligs = Menu(izvelne)

#faili.add_cascade(label="Faili",menu=faili)
#izvelne.add_cascade(label="Help",menu=paligs)
#faili.add_command(label="Jauns",command=fa_jauns)
# ----------------------------
logs1.mainloop()