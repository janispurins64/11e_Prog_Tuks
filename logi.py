from tkinter import *
from tkinter import messagebox
a = 0.
b = 0.
c = 0.
def fa_jauns():
    messagebox.showinfo("Info","Šeit jāapstrādā komanda")
def fa_autors():
    messagebox.showinfo("Autors","Vilis Vilītis"+"\n"+"12.VI")
def fa_datuievadsa():
    global a
    a = float(input("Ievadiet a:"))
def fa_datuievadsb():
    global b
    b = float(input("Ievadiet b:"))
def fa_datuievadsc():
    global c
    c = float(input("Ievadiet c:"))
def fa_rez():
    global a
    global b
    global c
    print("a=",a," b=",b," c=",c)
    label2 = Label(logs1, text = 'Rezultāts:'+str(a+b+c), fg = 'black',
                  bg = 'white', font = (None, 12), height = 2)
    label2.pack(side = BOTTOM)
# Izveidojam logu
logs1 = Tk()
logs1.title("Mana programma")
# šeit uzlikt logam fona krāsu
logs1.geometry("400x400")
menubar = Menu(logs1) # sagatavo izvēlņu joslu
# Izveido komandas 1
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Jauns", command=fa_jauns)
filemenu.add_command(label="Open", command=fa_jauns)
filemenu.add_command(label="Save", command=fa_jauns)
filemenu.add_command(label="Autors", command=fa_autors)
filemenu.add_separator()
filemenu.add_command(label="Close", command=fa_jauns)
# --- nākamās divas rindiņas ievieto izvēlņu joslā
# iepriekš sagatavoto kaskādi
menubar.add_cascade(label="File", menu=filemenu)
logs1.config(menu=menubar)
# Izveido komandas 2
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Mala a:", command=fa_datuievadsa)
editmenu.add_command(label="Mala b:", command=fa_datuievadsb)
editmenu.add_command(label="Mala c:", command=fa_datuievadsc)
editmenu.add_command(label="Rezultāts", command=fa_rez)
# --- nākamās divas rindiņas ievieto izvēlņu joslā
# iepriekš sagatavoto kaskādi
menubar.add_cascade(label="Edit", menu=editmenu)
logs1.config(menu=menubar)
#messagebox.showinfo("Info","Šī ir vienkāršā info") 
#messagebox.showwarning("Ūūū", "Šis ir brīdinājums")  
#messagebox.showerror("Alles kaput", "Fatāla kļūda")
label1 = Label(logs1, text = 'Mala a:', fg = 'black',
                  bg = 'white', font = (None, 12), height = 2)
label1.pack(side = TOP)


# Veidojam pogu
poguRamis = Frame(logs1, bg='white')
poga_a = Button(poguRamis, text = 'Mala a:', width = 25, height = 2, command=fa_datuievadsa)
poga_a.grid(row=0, column=0, pady = 10, padx = 25, sticky=W) 
poga_b = Button(poguRamis, text = 'Mala b:', width = 25, height = 2, command=fa_datuievadsb)
poga_b.grid(row=1, column=0, pady = 10, padx = 25, sticky=W) 
poga_c = Button(poguRamis, text = 'Mala c:', width = 25, height = 2, command=fa_datuievadsc)
poga_c.grid(row=2, column=0, pady = 10, padx = 25, sticky=W) 
poguRamis.pack(side=TOP) 
# ----- 
# Datu ievads
#ievadRamis = Frame(logs1, bg='white')
#ievadRamis.Label(logs1, text="First Name").grid(row=0)
#ievadRamis.Label(logs1, text="Last Name").grid(row=1)

#e1 = ievadRamis.Entry(logs1)
#e2 = ievadRamis.Entry(logs1)
#ievadRamis.pack(side=TOP) 
logs1.mainloop()