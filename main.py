import os
import random
import tkinter as tk
from PIL import Image, ImageTk

class self(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Imagine by DanyB0")
        self.master.geometry("700x400")
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.grid()
        self.rando()
        self.img_sfondo = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\" + str(self.rando()) + ".png"))
        self.img_sfondo_2 = self.img_sfondo
        #self.master.configure(bg=self.img_sfondo)
        self.master.wm_attributes("-topmost", True)
        self.master.wm_attributes("-transparentcolor", "green")
        self.master.iconbitmap(os.getcwd() + r"\logo.ICO")
        self.widgets()

    def widgets(self):
        self.sfondo = tk.Label(self, image=self.img_sfondo, bg="green")
        self.sfondo.grid(row=0, column=0)
        #self.btn = tk.Button(self, image=self.img_btn, bd=0, command=self.cambia_imm)
        #self.btn.grid(row=0, column=0, pady=2, sticky="swe")
        self.master.bind( "<Button-1>", self.pressed )
        self.master.bind( "<B1-Motion>", self.mouseDragged)
    
    def rando(self):
        file = os.listdir()
        rand = random.randint(0,len(file)-2)
        return rand

    def pressed(self, event):
        self.x = event.x
        self.y = event.y

    def mouseDragged(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        newX = self.master.winfo_x() + deltax
        newY = self.master.winfo_y() + deltay
        self.master.geometry("+%d+%d"% (newX, newY))

def main():
    w = self()
    w.mainloop()

main()