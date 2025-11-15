class PdJelszoKezelo:
    def __init__(self):
        self.jelszo_adatok = []

    def pd_hozzaad(self, szolgaltatas, jelszo):
        self.jelszo_adatok.append((szolgaltatas, jelszo))

    def pd_torles(self, index):
        if 0 <= index < len(self.jelszo_adatok):
            del self.jelszo_adatok[index]

    def pd_listazas(self):
        return self.jelszo_adatok
