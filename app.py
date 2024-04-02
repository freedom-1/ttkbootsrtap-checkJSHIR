import tkinter as tk
import random 
import datetime
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from variable import themesDARK, themesLIGHT, oy_nomlari

class Application:
    def __init__(self, root):
        self.root = root
        self.name = tk.StringVar()
        self.compression = self.get_compression()
        self.create_widgets()

    def get_compression(self):
        x = int(datetime.datetime.now().strftime("%H"))
        return themesLIGHT[random.randrange(0,len(themesLIGHT))] if (x<19 and x>7) else themesDARK[random.randrange(0,len(themesDARK))]

    def check_jshir(self):
        try:
            a=self.name.get()
            if len(a)==14:
                jins = "Janob" if int(a[0])%2!=0 else "Honim"
                kun = int(a[1])*10+int(a[2])
                oy = oy_nomlari[int(a[3])*10+int(a[4])]
                yil = int("19"+a[5]+a[6]) if int(a[5]) !=0 else int("20"+a[5]+a[6])

                self.label.config(text=f"Assalomu alaykum {jins}. Siz {yil}-yil {kun}-{oy}da tug'ilgansiz.")
            else:
                self.label.config(text="JSHIR da belgilar soni 14 ta bo'lishi kerak")
        except Exception as e:
            self.label.config(text=f"Diqqat xatolik: {e}")

    def create_widgets(self):
        self.root.title("TTK Bootstrap")
        frame = ttk.Frame(self.root, padding="20")
        frame.grid(row=0, column=0)

        label1 = ttk.Label(frame, text="JSHIR ni kiriting")
        label1.grid(row=1, column=0)

        name_entry = ttk.Entry(frame, textvariable=self.name)
        name_entry.grid(row=2, column=0)

        hello_button = ttk.Button(frame, text="Hisoblash", command=self.check_jshir, bootstyle="success-outline")
        hello_button.grid(row=3, column=0)

        self.label = ttk.Label(frame, text="")
        self.label.grid(row=4, column=0)

root = tk.Tk()
app = Application(root)
root.mainloop()
