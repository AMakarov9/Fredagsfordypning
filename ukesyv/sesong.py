from kamp import Kamp
from terminliste import Terminliste
from tabell import Tabell
from lagliste import lagliste, lagordbok

class Sesong:
    def __init__(self, lagliste, terminliste):
        self._runder = {}
        self._tabell = Tabell(lagliste)
        self._runder = terminliste.runder()

    def tabell(self):

        

        return self._tabell

    # Denne metoden simulerer en sesong
    # Alle kampene spilles, og tabellen oppdateres etter hver kamp
    def simuler(self):
        # self._runder er en ordbok med rundenummer som nøkkel
        # og en liste med Kamp-objekter som verdi for hver runde
        for i in self._runder.values(): 
            for j in i:
                if not j.ferdig():
                    j.spill()
                self._tabell.legg_til_resultat(j)   
            self._tabell.oppdater_rangering()  
            
    def print_runder(self):
        # self._runder er en orbok med rundenummer som nøkler
        # verdiene er lister med Kamp-objekter
        for rundenr in self._runder:
            print()
            print("Runde", str(rundenr).rjust(2))
            print("--------")
            print()
            kamper = self._runder[rundenr] # liste med Kamp-objekter
            for kamp in kamper:
                print(kamp)
        
# Testkode (kjøres ikke når klassen importeres, kun når sesong.py kjøres)
if __name__=="__main__":
    # sett opp sesongen
    terminliste = Terminliste("rsssf2023.dat", lagordbok)
    testsesong = Sesong(lagliste, terminliste)  # lagene hentes fra lagliste.py
    testsesong.simuler()                        # spill alle kampene
    testsesong.print_runder()                   # print alle rundene (med resultater)
    testsesong.tabell().print_tabell()          # skriv ut tabellen etter siste runde