import random
import math
from lag import Lag

class Kamp:
    def __init__(self, hjemmelag, bortelag, mål_hjemme=None, mål_borte=None):
        self._hjemmelag = hjemmelag
        self._bortelag = bortelag
        self._mål_hjemme = mål_hjemme
        self._mål_borte = mål_borte
        self._simulert = False # False om vi bruker ekte resultat, True om spill()-metoden har simulert et resultat

    def hjemmelag(self):
        return self._hjemmelag
    
    def bortelag(self):
        return self._bortelag

    def spill(self):
        # TODO: Endre metoden slik at kampen ikke ender 0-0, men
        #       får et tilfeldig resultat hver gang (se innleverings-
        #       oppgaven til Fredagsfordypning fra uke 7 for hint).
        #       Det er en fordel om du tar hensyn til hvor gode
        #       lagene er i angrep og forsvar, og gir hjemmelaget
        #       en fordel siden de spiller på hjemmebane.
        
        forventetmalhj = ((self._hjemmelag._angrep+self._bortelag._forsvar)/1.5)
        forventetmalbo = ((self._bortelag._angrep+(self._bortelag._forsvar))/2)


        mal_hjemme = random.gauss(forventetmalhj, 1)
        mal_borte = random.gauss(forventetmalbo, 1)
        
        while mal_borte < 0 or mal_hjemme < 0: 
            
            if mal_hjemme < 0 and mal_borte < 0: 
                   mal_hjemme = random.gauss(forventetmalhj, 1)
                   mal_borte = random.gauss(forventetmalbo, 1)
            
            elif mal_hjemme < 0 : 
                mal_hjemme = random.gauss(forventetmalhj, 1)
            
            else: 
                mal_borte = random.gauss(forventetmalbo, 1)
        
        if mal_hjemme != math.ceil(mal_hjemme): 
            if math.ceil(mal_hjemme) - mal_hjemme < 0.25:
                mal_hjemme = math.ceil(mal_hjemme)
            
            elif mal_hjemme-math.floor(mal_hjemme) < 0.5: 
                mal_hjemme = math.floor(mal_hjemme)
            else: 
                if random.randint(0, 1): 
                    mal_hjemme = math.ceil(mal_hjemme)
                
                else: 
                    mal_hjemme = math.floor(mal_hjemme)

       
        if mal_borte != math.ceil(mal_borte): 
            if math.ceil(mal_borte) - mal_borte < 0.25:
                mal_borte = math.ceil(mal_borte)
            
            elif mal_borte-math.floor(mal_borte) < 0.5: 
                mal_borte = math.floor(mal_borte)
            else: 
                #mal_borte = math.floor(mal_borte)                
                mal_borte = math.floor(mal_borte)
        
        self._mål_hjemme = mal_hjemme
        self._mål_borte = mal_borte

        self._simulert = True

    def mål_hjemme(self):
        return self._mål_hjemme

    def mål_borte(self):
        return self._mål_borte
    
    def ferdig(self):
        return (self.mål_hjemme() is not None) and (self.mål_borte() is not None)

    def __str__(self):
        # kampstr (en streng) inneholder først og fremst lagene som møtes
        # (se print_tabell for en forklaring av .ljust() og .rjust(), hvis du lurer)
        kampstr = (self._hjemmelag.navn() + " - " + self._bortelag.navn()).ljust(30)
        # legg til resultatet i kampstr dersom kampen er spilt og har et resultat
        if (self._mål_hjemme is not None) and (self._mål_borte is not None):
            kampstr += (str(self._mål_hjemme).rjust(2) + " - " + str(self._mål_borte).ljust(2))
        # simulerte kamper har * etter resultatet, ekte resultater har ikke det
        if self._simulert:
            kampstr += " *"
        return kampstr