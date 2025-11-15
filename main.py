import tkinter as tk
from tkinter import messagebox
import pd_generator as jg
from pd_jelszokezelo import PdJelszoKezelo
#asd
class JELSZOapp:
    def __init__(self, root):
        self.root = root
        self.root.title("JELSZO - Jelszókezelő és generátor")

        self.pd = PdJelszoKezelo()

        self.label_szolg = tk.Label(root, text="Szolgáltatás (pl. gmail):")
        self.label_szolg.pack()
        self.entry_szolg = tk.Entry(root)
        self.entry_szolg.pack()

        self.listbox = tk.Listbox(root, height=12, width=70)
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

        self._frissit_lista()

    def _frissit_lista(self):
        self.listbox.delete(0, tk.END)
        for szol, jelszo in self.pd.pd_listazas():
            self.listbox.insert(tk.END, f"{szol}: {jelszo}")

    def btn_szamok_click(self):
        jelszo = jg.pd_general_szamokkal()
        self.listbox.insert(tk.END, f"Új generált jelszó: {jelszo}")

    def btn_karakterek_click(self):
        jelszo = jg.pd_general_karakterekkel()
        self.listbox.insert(tk.END, f"Új generált jelszó: {jelszo}")

    def btn_komplex_click(self):
        jelszo = jg.pd_general_komplex()
        self.listbox.insert(tk.END, f"Új generált jelszó: {jelszo}")

    def btn_hozzaad_click(self):
        szolgaltatas = self.entry_szolg.get().strip()
        if not szolgaltatas:
            messagebox.showwarning("Figyelem", "Add meg a szolgáltatás nevét!")
            return
        try:
            index = self.listbox.curselection()[0]
            sor = self.listbox.get(index)
            if sor.startswith("Új generált jelszó: "):
                jelszo = sor.replace("Új generált jelszó: ", "")
                self.pd.pd_hozzaad(szolgaltatas, jelszo)
                self._frissit_lista()
                self.entry_szolg.delete(0, tk.END)
                messagebox.showinfo("Siker", f"Jelszó hozzáadva a listához: {jelszo} ({szolgaltatas})")
            else:
                messagebox.showwarning("Figyelem", "Válassz egy generált jelszót a listából hozzáadáshoz!")
        except IndexError:
            messagebox.showwarning("Figyelem", "Nincs kiválasztva jelszó hozzáadáshoz")

    def btn_torol_click(self):
        try:
            index = self.listbox.curselection()[0]
            szol_jelszo = self.listbox.get(index)
            if ": " in szol_jelszo:
                self.pd.pd_torles(index)
                self._frissit_lista()
                messagebox.showinfo("Siker", f"Jelszó törölve: {szol_jelszo}")
            else:
                messagebox.showwarning("Figyelem", "Csak mentett jelszót lehet törölni!")
        except IndexError:
            messagebox.showwarning("Figyelem", "Nincs kiválasztva jelszó törléshez")

if __name__ == '__main__':
    root = tk.Tk()
    app = JELSZOapp(root)
    root.mainloop()
