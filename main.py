import datetime

class Test:
    def __init__(self):
        self.predmet = ("Všeobecné znalosti")
        datum = datetime.datetime.now()
        self.den = datum.strftime("%d") + "." + datum.strftime("%m") + "." + datum.strftime("%Y")
        self.spravne_odpovedi = ["Lisabon", "30", "144", "8", "Isaaca Asimova"]

    def typ_testu(self):
        print("T: Test")
        print("P: Přijímačky")
        self.typtestu=input("Typ zkoušky: ")

    def zapis(self):
        self.jmeno = str(input('Jméno a Příjmení: '))
        self.trida = str(input('Třída: '))
        print('Předmět:',self.predmet)
        print('Datum:',self.den)
        print('Jméno a Příjmení:',self.jmeno)
        print('Třída:',self.trida)
    
    def hodnoceni(self):
        self.znamka == ''
        if self.pocet_bodu == 5:
            self.znamka = 1
        elif self.pocet_bodu == 4:
            self.znamka = 2
        elif self.pocet_bodu == 3:
            self.znamka = 3
        elif self.pocet_bodu == 2:
            self.znamka = 4
        elif self.pocet_bodu == 1:
            self.znamka = 4
        elif self.pocet_bodu == 0:
            self.znamka = 5
        else:
            print('špatný počet bodů')

  print('počet bodů:', self.pocet_bodu)
  print('známka:', self.znamka)

class Prijmacky(Test):
    def __init__(self):
        Test.__init__(self)

test = Prijmacky()

test.typ_testu()
test.zapis()
