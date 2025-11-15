class PdJelszoKezelo:
    def __init__(self):
        self.jelszavak = []

    def pd_hozzaad(self, jelszo):
        self.jelszavak.append(jelszo)

    def pd_torles(self, index):
        if 0 <= index < len(self.jelszavak):
            del self.jelszavak[index]

    def pd_listazas(self):
        return self.jelszavak
