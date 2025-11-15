import json
import os

class PdJelszoKezelo:
    def __init__(self, fajlnev='jelszavak.json'):
        self.fajlnev = fajlnev
        self.jelszo_adatok = []  # Lista: (szolgaltatas, jelszo) párok
        self.pd_betolt()

    def pd_hozzaad(self, szolgaltatas, jelszo):
        self.jelszo_adatok.append((szolgaltatas, jelszo))
        self.pd_mentes()

    def pd_torles(self, index):
        if 0 <= index < len(self.jelszo_adatok):
            del self.jelszo_adatok[index]
            self.pd_mentes()

    def pd_listazas(self):
        return self.jelszo_adatok

    def pd_mentes(self):
        with open(self.fajlnev, 'w', encoding='utf-8') as f:
            json.dump(self.jelszo_adatok, f, ensure_ascii=False, indent=4)

    def pd_betolt(self):
        if os.path.exists(self.fajlnev):
            with open(self.fajlnev, 'r', encoding='utf-8') as f:
                self.jelszo_adatok = json.load(f)
        else:
            self.jelszo_adatok = []
