import datetime

class Test:
    def __init__(self):
        self.predmet = ("Všeobecné znalosti")
        datum = datetime.datetime.now()
        self.den = datum.strftime("%d") + "." + datum.strftime("%m") + "." + datum.strftime("%Y")
        self.otazkyy = ["Hlavní město Portugalska?", "Jak dlouho trvala 30 letá válka?", "12 x 12?", "1 Byte = bitů?", "Autor díla Já, robot?"]
        self.odpovedi = []
        self.spravne_odpovedi = ["Lisabon", "30", "144", "8", "Isaaca Asimova"]
        self.pocet_bodu = 0


    def typ_testu(self):
        print("T: Test")
        print("P: Přijímačky")
        self.typtestu = input("Typ zkoušky: ")
        


    def txtretezec(self):
        if self.typtestu == "T" or self.typtestu == "t":
            print("Z A Č Á T E K   T E S T U . . .\n")
        elif self.typtestu == "P" or self.typtestu == "p":
            print("Z A Č Á T E K   P Ř I J Í M A Č E K . . .\n")


    def zapis(self):
        self.jmeno = str(input('\nJméno a Příjmení: '))
        self.trida = str(input('Třída: '))
        print('\nPředmět:',self.predmet)
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


    def otazky(self):
        for i in self.otazkyy:
            print(i)
            odpoved = input("Odpověd: ")
            self.odpovedi.append(odpoved)
            print()


    def kontrola(self):
        index = 0
        for i in self.odpovedi:
            if i == self.spravne_odpovedi[index]:
                self.pocet_bodu += 1

    
class Prijmacky(Test):
    def __init__(self):
        Test.__init__(self)


    def stav(self):
        if (znamka == 1) or (znamka == 2) or (znamka == 3):
            print('PŘIJAT')
        else:
            print('NEPŘIJAT')


    def __del__(self):
        print("\nHODNOCENÍ BYLO ULOŽENO")

test = Prijmacky()

test.typ_testu()
test.zapis()
test.txtretezec()
test.otazky()
test.kontrola()
if test.typtestu in "pP":
    test.stav(test.znamka)

del test
