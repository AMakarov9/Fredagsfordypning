class Statistikk:
    # lagliste er en liste med Lag-objekter
    def __init__(self, lagliste):
        self._plasseringer = {}         # ordbok med Lag-objekt som nøkkel og liste over
                                        # [ antall førsteplasser, antall andreplasser, ... , antall sisteplasser ]
                                        # for dette laget i løpet av de simulerte sesongene
        for lag in lagliste:
            # til å begynne med er listen [0, 0, 0, ..., 0]
            self._plasseringer[lag] = [0]*len(lagliste)

    # Lagrer rekkefølgen lagene kom i når en bestemt sesong er ferdig spilt
    def lagre_rangering(self, sesong):
        tabell = sesong.tabell()
        rangering = tabell.hent_rangering()
        # rangering er en liste over Lag-objekter (0 = 1. plass, 1 = 2. plass, osv.)
        for j in range(len(rangering)):     # for hver plassering:
            lag = rangering[j]                  # finn ut hvilket lag som fikk denne plasseringen
            self._plasseringer[lag][j] += 1     # registrer at dette laget fikk en slik plassering denne sesongen

    # Skriver ut antall plasseringer (1, 2, 3... osv.) for alle lagene (i alfabetisk rekkefølge)
    def print_plasseringer(self):
        print()
        for lag in self._plasseringer: # for hvert lag
            print()
            print(lag.navn())    # skriv ut lagets navn
            print("-"*len(lag.navn()))
            plasseringsliste = self._plasseringer[lag] # hent listen med plasseringer for dette laget
            # bruker indeksen j som løkkevariabel slik at vi også kan skrive ut
            # hvilken plass det er snakk om (0 = 1.plass, 1 = 2.plass, osv.)
            for j in range(len(plasseringsliste)):
                antall = plasseringsliste[j] # antall plasseringer av denne typen
                print(str(j + 1).ljust(2), str(antall).rjust(5))