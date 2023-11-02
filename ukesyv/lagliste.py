from lag import Lag

# dette er listen over lag som skal spille (representert ved Lag-objekter)
# (brukes av klassen Tabell)
lagliste = []
lagliste.append(Lag("Bodø/Glimt", 2.6, 1.3))
lagliste.append(Lag("Brann", 1.8, 1.1))
lagliste.append(Lag("HamKam", 1.4, 2.2))
lagliste.append(Lag("Haugesund", 1.0, 1.4))
lagliste.append(Lag("Molde", 2.2, 1.2))
lagliste.append(Lag("Lillestrøm", 1.7, 1.5))
lagliste.append(Lag("Odd", 1.2, 1.4))
lagliste.append(Lag("Rosenborg", 1.3, 1.6))
lagliste.append(Lag("Sandefjord", 1.5, 2.0))
lagliste.append(Lag("Sarpsborg 08", 1.9, 1.6))
lagliste.append(Lag("Stabæk", 1.0, 1.5))
lagliste.append(Lag("Strømsgodset", 1.2, 1.3))
lagliste.append(Lag("Tromsø", 1.6, 1.1))
lagliste.append(Lag("Viking", 2.2, 1.5))
lagliste.append(Lag("Vålerenga", 1.3, 1.7))
lagliste.append(Lag("Aalesund", 0.8, 2.2))

# gjør den om til en ordbok for å kunne slå opp på lagnavn
# (brukes av klassen Terminliste)
lagordbok = {}
for lag in lagliste:
    lagordbok[lag.navn()] = lag