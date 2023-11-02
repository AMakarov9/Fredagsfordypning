from kamp import Kamp

class Tabell:
    def __init__(self, lagliste):
        self._lagliste = lagliste

        # Tabellen er en ordbok med Lag-objekt som nøkler
        # Verdiene er ordbøker (med strenger som nøkler og tallene i tabellen som verdier)
        self._tabell = {}
        self._hjemme = {}
        self._borte = {}
        for lag in self._lagliste:
            self._tabell[lag] = {}
            self._tabell[lag]["navn"] = lag.navn()
            self._tabell[lag]["kamper"] = 0
            self._tabell[lag]["vunnet"] = 0
            self._tabell[lag]["uavgjort"] = 0
            self._tabell[lag]["tapt"] = 0
            self._tabell[lag]["mål for"] = 0
            self._tabell[lag]["mål mot"] = 0
            self._tabell[lag]["poeng"] = 0

            self._hjemme[lag] = []
            self._borte[lag] = []
        self._kampmål = []

        # Før noen kamper er spilt, sorterer vi bare lagene alfabetisk
        # (siden vi har implementert metodene __lt__ og __gt__ for klassen Lag)
        self._rangering = sorted(self._lagliste)

    def legg_til_resultat(self, kamp):
        # hent info om kampen - hvem spilte og hva ble resultatet?
        hjemmelag = kamp.hjemmelag()
        bortelag = kamp.bortelag()
        mål_hjemme = int(kamp.mål_hjemme())
        mål_borte = int(kamp.mål_borte())
        # Lagrer mål i lister til statistikk
        self._hjemme[hjemmelag].append(int(mål_hjemme) - int(mål_borte))
        self._borte[bortelag].append(int(mål_borte) - int(mål_hjemme))
        self._kampmål.append(int(mål_hjemme) + int(mål_borte))
        # oppdater antall spilte kamper
        self._tabell[hjemmelag]["kamper"] += 1
        self._tabell[bortelag]["kamper"] += 1
        # oppdater antall vunnet/uavgjort/tapt
        if mål_hjemme > mål_borte:      # hjemmelaget vant
            self._tabell[hjemmelag]["vunnet"] += 1
            self._tabell[bortelag]["tapt"] += 1
        elif mål_hjemme == mål_borte:   # uavgjort
            self._tabell[hjemmelag]["uavgjort"] += 1
            self._tabell[bortelag]["uavgjort"] += 1
        else:                           # bortelaget vant
            self._tabell[hjemmelag]["tapt"] += 1
            self._tabell[bortelag]["vunnet"] += 1
        # oppdater mål for begge lag
        self._tabell[hjemmelag]["mål for"] += mål_hjemme
        self._tabell[bortelag]["mål for"] += mål_borte
        # oppdater mål imot begge lag
        self._tabell[hjemmelag]["mål mot"] += mål_borte
        self._tabell[bortelag]["mål mot"] += mål_hjemme
        # oppdater poeng (3 for seier, 1 for uavgjort)
        self._tabell[hjemmelag]["poeng"] = 3*self._tabell[hjemmelag]["vunnet"] + self._tabell[hjemmelag]["uavgjort"]
        self._tabell[bortelag]["poeng"] = 3*self._tabell[bortelag]["vunnet"] + self._tabell[bortelag]["uavgjort"]

    # Denne metoden rangerer lagene på følgende måte:
    #
    # 1) Lag med mest poeng øverst
    # 2) Hvis likt antall poeng, lag med best målforskjell øverst
    # 3) Hvis både poeng og målforskjell likt, sorter alfabetisk på lagnavn
    #
    # Du trenger ikke forstå HVORDAN denne metoden virker (det er frivillig),
    # men du tregner å vite at den sorterer listen self._rangering
    # slik at lagene kommer i riktig tabell-rekkefølge
    def oppdater_rangering(self):
        gammel_rangering = self._rangering # kopi av rangering fra forrige runde
        self._rangering = []
        while len(gammel_rangering) > 0:   # så lenge det er lag igjen å rangere
            # let etter laget/lagene med mest poeng (av de som er igjen)
            maxpoeng = -1  # (foreløpig) største antall poeng vi har funnet
            beste_lag = [] # liste med alle lagene på max poeng
            for i in range(len(gammel_rangering)):
                lag = gammel_rangering[i]
                poeng = self._tabell[lag]["poeng"]
                if poeng == maxpoeng: # fant enda et lag med samme poengsum
                    beste_lag.append(i) # legg til i listen
                elif poeng > maxpoeng: # fant en ny og høyere poengsum
                    beste_lag = [i] # lag ny liste
                    maxpoeng = poeng # nå er dette den nye max-poengsummen

            # beste_lag inneholder bare indekser til lagene (i listen gammel_rangering)
            # beste_lagliste inneholder referanser til selve Lag-objektene
            beste_lagliste = []
            for j in beste_lag[::-1]:
                beste_lagliste.append(gammel_rangering.pop(j)) # fjerner lagene fra gammel_rangering

            # Blant lagene med max poengsum, gjenta prosessen over med målforskjell
            # (Var det bare ett lag, vil dette legges til i self._rangering)
            while len(beste_lagliste) > 0: # så lenge det er flere lag igjen med max poengsum
                maxmålforskjell = -9999 # (foreløpig) beste målforskjell vi har funnet
                aller_beste_lagliste = [] # liste med alle lagene på beste målforskjell
                for lag in beste_lagliste:
                    målforskjell = self._tabell[lag]["mål for"] - self._tabell[lag]["mål mot"]
                    if målforskjell == maxmålforskjell: # fant enda et lag med samme målforskjell
                        aller_beste_lagliste.append(lag) # legg til i listen
                    elif målforskjell > maxmålforskjell: # fant en ny og bedre målforskjell
                        aller_beste_lagliste = [lag] # lag ny liste
                        maxmålforskjell = målforskjell # nå er dette den nye beste målforskjellen
                
                # alfabetisk sortering på lagnavn hvis alt annet likt (derfor sorted)
                for lag in sorted(aller_beste_lagliste):
                    self._rangering.append(lag) # legger til laget i den nye rangeringen
                    beste_lagliste.remove(lag)  # må fjerne laget fra denne listen så løkken ikke går uendelig

    # Returnerer listen med lag i den rekkefølge de er i tabellen
    def hent_rangering(self):
        return self._rangering
    
    def gjennomsnitt_mål(self, desimaler=2):
        return round(sum(self._kampmål)/len(self._kampmål), desimaler)
    
    def standardavvik_mål(self, desimaler=2):
        avg = self.gjennomsnitt_mål()
        return round((sum([(x-avg)**2 for x in self._kampmål])/len(self._kampmål))**0.5, desimaler)
    
    # Skriver ut tabellen i et fint og leselig format
    # Skriver også ut gjennomsnittlig antall mål gjennom sesongen
    def print_tabell(self):
        print()
        print()
        mål = 0 # antall mål scoret
        kamper = 0 # antall kamper spilt
        for lag in self.hent_rangering():
            mål += self._tabell[lag]["mål for"] # målene dette laget har scoret
            kamper += self._tabell[lag]["kamper"] // 2 # hjemmekampene dette laget har spilt
            # (det er 2 lag per kamp, så vi teller kampene dobbelt hvis vi ikke deler på 2)

            # .ljust() og .rjust() gjør at tabellen ser fin ut
            # https://www.w3schools.com/python/ref_string_ljust.asp
            # https://www.w3schools.com/python/ref_string_rjust.asp
            print(self._tabell[lag]["navn"].ljust(14),
                  str(self._tabell[lag]["kamper"]).ljust(2),
                  str(self._tabell[lag]["vunnet"]).ljust(2),
                  str(self._tabell[lag]["uavgjort"]).ljust(2),
                  str(self._tabell[lag]["tapt"]).ljust(2),
                  str(self._tabell[lag]["mål for"]).rjust(3),
                  "-",
                  str(self._tabell[lag]["mål mot"]).ljust(3),
                  str(self._tabell[lag]["poeng"]).ljust(3)
            )
        print()
        print("Gjennomsnittlig antall mål:", self.gjennomsnitt_mål())
        print("Standardavvik antall mål:", self.standardavvik_mål())
        print()