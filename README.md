Pólya Dániel - D4JVTJ

Jelszógeneráló és jelszókezelő app.

Modulok
pd_generator.py
    pd_general_szamokkal(hossz=12)
    pd_general_karakterekkel(hossz=12)
    pd_general_komplex(hossz=12)

pd_jelszokezelo.py
    PdJelszoKezelo:
        pd_hozzaad(szolgaltatas, jelszo)
        pd_torles(index)
        pd_listazas()
        pd_mentes()
        pd_betolt()

main.py

Az adatok mentése és betöltése JSON formátumban történik a jelszavak.json fájlban.

Használt modulok
    "tkinter"
    "random" és "string"
    "json" és "os"
