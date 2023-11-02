from lag import Lag
from kamp import Kamp
from lagliste import lagordbok

class Terminliste:
    def __init__(self, filename, lagordbok):
        fil = open(filename, encoding="utf-8")
        
        self._runder = {}
        
        # TODO: Les inn terminlisten
        malEn = None 
        malTo = None
        for linje in fil:
            
            if not linje.isalpha():
                if "Round" in linje: 
                    data = linje.strip().split()
                    midlertidig = data[1]
                    self._runder[midlertidig] = []
                    
                
                
                elif "-" in linje and len(linje.strip().split()) <= 6: 
                    data = linje.strip().split(" - ")
                    try: 
                        venstreDel = data[0]
                        hoyreDel = data[1]
                    except: 
                        continue
                    
                    if ":" in venstreDel.split()[0]: 
                        if len(venstreDel.split()) == 3: 
                            lagEn = f"{venstreDel.split()[1]} {venstreDel.split()[2]}"
                        else: 
                          
                            lagEn = venstreDel.split()[1]
                    

                    elif len(venstreDel.split()) == 2: 
                         
                        lagEn = f"{venstreDel.split()[0]} {venstreDel.split()[1]}"
                    else: 
                        lagEn = venstreDel

                    
                    if ("-" in hoyreDel) and len(hoyreDel.split()) == 3: 
                        lagTo = f"{hoyreDel.split()[0]} {hoyreDel.split()[1]}"
                        stilling = hoyreDel.split()[2].split("-")
                        malEn = stilling[0]
                        malTo = stilling[1]
                    
                    elif ("-" in hoyreDel) and len(hoyreDel.split()) == 2:
                        lagTo = hoyreDel.split()[0]
                        stilling = hoyreDel.split()[1].split("-")
                        malEn = int(stilling[0])
                        malTo = int(stilling[1])
                    
                    else: 
                        lagTo = hoyreDel
                        malEn = None 
                        malTo = None

                    hjemmelag = lagordbok[lagEn]
                    bortelag = lagordbok[lagTo]
                    kamp = Kamp(hjemmelag, bortelag, malEn, malTo)
                    self._runder[midlertidig].append(kamp)    
                
        
        fil.close()
        

    
    def runder(self):
        # Kopierer ordboken og i tillegg alle Kamp-objektene i den
        # slik at kampene blir forskjellige hver sesong,
        # ellers blir resultatene like i alle sesongene.
        #
        # På denne måten får hver Sesong en unike kopier av kamper fra
        # "moder-terminlisten" (som bare inneholder reelle resultater,
        # men ikke simulerte resultater).
        
        ny_ordbok = {}
        for rundenr in self._runder:
            ny_ordbok[rundenr] = []
            for kamp in self._runder[rundenr]:
                hlag = kamp.hjemmelag()
                blag = kamp.bortelag()
                hmål = kamp.mål_hjemme() # None hvis kampen ikke spilt
                bmål = kamp.mål_borte() # None hvis kampen ikke spilt
                ny_kamp = Kamp(hlag, blag, hmål, bmål)
                ny_ordbok[rundenr].append(ny_kamp)
        return ny_ordbok

if __name__ == "__main__":
    test = Terminliste("rsssf2023.dat", lagordbok) # hentes fra lagliste.py
    runder = test.runder()
    for runde in runder:
        print()
        print("Runde", runde)
        print()
        for kamp in runder[runde]:
            print(kamp)
    print()