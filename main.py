class Dolgozo:
    ber_emeles = 1.035
    def __init__(self, veznev, kernev,  fizetes):
        self.kernev = kernev
        self.veznev = veznev
        self.email = str(self.veznev).lower() + "." + str(self.kernev).lower() + "@gmail.com"
        self.fizetes = fizetes

    def fizetes_emeles(self):
            self.fizetes = int(self.fizetes * self.ber_emeles)

    def TeljNev(self):
        return "{} {}".format(self.veznev, self.kernev)

class Tanar(Dolgozo):
    ber_emeles = 1.08

    def __init__(self, elotag, veznev, kernev,fizetes, tantargy):
        super().__init__(veznev, kernev, fizetes)
        self.elotag = elotag
        self.tantargy = tantargy
        self.email = "dr" + str(self.veznev).lower() + "." + str(self.kernev).lower() + "@pte.hu"

    def TeljNev(self):
        return "{} {} {}".format(self.elotag, self. veznev, self.kernev)

class Takarito(Dolgozo):
    ber_emeles = 1.04

    def __init__(self, veznev, kernev,  fizetes, emelet):
        super().__init__(veznev, kernev,  fizetes)
        self.emelet = emelet

class TanarFelugyelo(Dolgozo):
    ber_emeles = 1.10
    def __init__(self, veznev, kernev,  fizetes, tanar_lista=None):
        super().__init__(veznev, kernev,fizetes)
        if tanar_lista is None:
            self.tanar_lista = []
        else:
            self.tanar_lista = tanar_lista

    def tan_hozzaadas(self, tan):
        if tan not in self.tanar_lista:
            self.tanar_lista.append(tan)

    def tan_kivetel(self, tan):
        if tan in self.tanar_lista:
            self.tanar_lista.remove(tan)

    def lista_kiiras(self):
        for tan in self.tanar_lista:
            print("--" + tan.TeljNev())
        print("\n")




#kipróbálható dolgok listája (a ''' kitörlése után):

Tan = Tanar('Dr.', 'Kerekes', 'Kamilla', 370000, 'Linearis Algebra XIV.')
Dolg = Dolgozo("Gimer", "Dani", 300000)
TanFel = TanarFelugyelo("Nagy", "Bence", 460000, [Tan])
Tak = Takarito("Kiss", "Korinna", 270000, "3. Emelet")
ExtrTan = Tanar("Dr.", "Heller", "Szilvia", 385000, "Exponencializmus Elmélet")
'''
TanFel.lista_kiiras()
TanFel.tan_hozzaadas(ExtrTan)
TanFel.lista_kiiras()
TanFel.tan_kivetel(ExtrTan)
TanFel.lista_kiiras()
TanFel.tan_kivetel(Tan)
TanFel.lista_kiiras()
print(Dolg.fizetes)
Dolg.fizetes_emeles()
print(Dolg.fizetes)
print(TanFel.fizetes)
TanFel.fizetes_emeles()
print(TanFel.fizetes)
print(Tak.TeljNev())
print(Tak.email)
print(Tan.email)
print(Dolg.TeljNev())
Dolg.fizetes_emeles()
print(Tan.fizetes)
print(TanFel.TeljNev())
TanFel.fizetes_emeles()
print(TanFel.email)
print(Tak.emelet)
print(Tak.email)
print(Tan.email)
'''


