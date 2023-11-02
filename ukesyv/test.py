from lag import Lag
from kamp import Kamp

lagEn = Lag("Juve", 1.52, 1.52)
lagTo = Lag("Gjennomsnittslag", 1.52, 1.52)
kampEn = Kamp(lagEn, lagEn)
'''
lagliste = []
lagliste.append(Lag("Bodø/Glimt  ", 2.6, 1.2))
lagliste.append(Lag("Brann       ", 1.8, 1.1))
lagliste.append(Lag("HamKam      ", 1.4, 2.1))
lagliste.append(Lag("Haugesund   ", 0.9, 1.4))
lagliste.append(Lag("Molde       ", 2.2, 1.1))
lagliste.append(Lag("Lillestrøm  ", 1.7, 1.5))
lagliste.append(Lag("Odd         ", 1.2, 1.3))
lagliste.append(Lag("Rosenborg   ", 1.3, 1.7))
lagliste.append(Lag("Sandefjord  ", 1.5, 1.9))
lagliste.append(Lag("Sarpsborg 08", 1.9, 1.6))
lagliste.append(Lag("Stabæk      ", 1.0, 1.5))
lagliste.append(Lag("Strømsgodset", 1.1, 1.3))
lagliste.append(Lag("Tromsø      ", 1.5, 1.0))
lagliste.append(Lag("Viking      ", 2.1, 1.4))
lagliste.append(Lag("Vålerenga   ", 1.4, 1.7))
lagliste.append(Lag("Aalesund    ", 0.8, 2.2))

kamplister = []

for i in lagliste: 
    kamplister.append(Kamp(i, lagTo))


for i in kamplister: 
    for j in range(10000):
        i.spillhj()
        i.spillbo()
 
    i.statistikk()

    
'''
for i in range(1000000): 
    kampEn.spill()

    

kampEn.statistikk()


    #print(f"hjemmelag: {kampEn.malhjemme()}, bortelag: {kampEn.malborte()}")

