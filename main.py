import tkinter as tk
from tkinter import messagebox
import pd_generator as jg
from pd_jelszokezelo import PdJelszoKezelo

class JELSZOapp:
    def __init__(self, root):
        self.root = root
        self.root.title("JELSZO - Jelszókezelő és generátor")

        self.jk = PdJelszoKezelo()

        # GUI elemek
        self.listbox = tk.Listbox(root, height=10, width=50)
        self.listbox.pack(padx=10, pady=10)

        self.btn_szamok = tk.Button(root, text="Jelszó generálás számokkal", command=self.btn_szamok_click)
        self.btn_szamok.pack(padx=10, pady=2)

        self.btn_karakterek = tk.Button(root, text="Jelszó generálás karakterekkel", command=self.btn_karakterek_click)
        self.btn_karakterek.pack(padx=10, pady=2)

        self.btn_komplex = tk.Button(root, text="Komplex jelszó generálás", command=self.btn_komplex_click)
        self.btn_komplex.pack(padx=10, pady=2)

        self.btn_hozzaad = tk.Button(root, text="Jelszó hozzáadása", command=self.btn_hozzaad_click)
        self.btn_hozzaad.pack(padx=10, pady=2)

        self.btn_torol = tk.Button(root, text="Kijelölt jelszó törlése", command=self.btn_torol_click)
        self.btn_torol.pack(padx=10, pady=2)

    def btn_szamok_click(self):
        jelszo = jg.pd_general_szamokkal()
        self.listbox.insert(tk.END, jelszo)

    def btn_karakterek_click(self):
        jelszo = jg.pd_general_karakterekkel()
        self.listbox.insert(tk.END, jelszo)

    def btn_komplex_click(self):
        jelszo = jg.pd_general_komplex()
        self.listbox.insert(tk.END, jelszo)

    def btn_hozzaad_click(self):
        try:
            index = self.listbox.curselection()[0]
            jelszo = self.listbox.get(index)
            self.jk.pd_hozzaad(jelszo)
            messagebox.showinfo("Siker", f"Jelszó hozzáadva a listához: {jelszo}")
        except IndexError:
            messagebox.showwarning("Figyelem", "Nincs kiválasztva jelszó hozzáadáshoz")

    def btn_torol_click(self):
        try:
            index = self.listbox.curselection()[0]
            jelszo = self.listbox.get(index)
            self.jk.pd_torles(index)
            self.listbox.delete(index)
            messagebox.showinfo("Siker", f"Jelszó törölve: {jelszo}")
        except IndexError:
            messagebox.showwarning("Figyelem", "Nincs kiválasztva jelszó törléshez")

if __name__ == '__main__':
    root = tk.Tk()
    app = JELSZOapp(root)
    root.mainloop()
