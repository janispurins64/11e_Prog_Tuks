from tkinter import *
from tkinter import messagebox
def fa_jauns():
    messagebox.showinfo("Info","Šeit atveram failu")

logs1 = Tk()
logs1.title("Mana programma")
logs1.geometry("400x400")
#messagebox.showinfo("Info","Šī ir vienkāršā info") 
#messagebox.showwarning("Ūūū", "Šis ir brīdinājums")  
#messagebox.showerror("Alles kaput", "Fatāla kļūda")
# Izvēlne ---------------------------
izvelne = Menu(logs1)
faili = Menu(izvelne)
paligs = Menu(izvelne)

izvelne.add_cascade(label="Faili",menu=faili)
izvelne.add_cascade(label="Help",menu=paligs)
faili.add_command(label="Jauns",command=fa_jauns)
# ----------------------------
logs1.mainloop()