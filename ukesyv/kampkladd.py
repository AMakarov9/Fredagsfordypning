from lag import Lag
import random
import math
class Kamp(): 
    def __init__(self, hjemmelag: Lag, bortelag: Lag, mal_hjemme = None, mal_borte=None):
        self.hjemmelag = hjemmelag
        self.bortelag = bortelag
        self._mal_hjemme = mal_hjemme
        self._mal_borte = mal_borte
        self.simulert = False
        self.seier_hjemme = 0
        self.seier_borte = 0 
        self.uavgjort = 0
        self.kampnr = 0 
        self.kamperoverfem = {}
        self.kamperoverfemteller = 0
        self.totalmalhj = 0 
        self.totalmalbo = 0
        self.totalkamper = 0


    def spill(self):
        self.kampnr += 1 
        forventetmalhj = ((self.hjemmelag._angrep+self.bortelag._forsvar)/1.5)
        forventetmalbo = ((self.bortelag._angrep+(self.bortelag._forsvar))/2)


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
                
        self.mal_hjemme = mal_hjemme
        self.mal_borte = mal_borte
        self.totalmalhj += mal_hjemme
        self.totalmalbo += mal_borte
        if mal_hjemme < mal_borte: 
            self.seier_borte += 1
        elif mal_hjemme > mal_borte: 
            self.seier_hjemme += 1 
        else: 
            self.uavgjort += 1 

        if mal_hjemme + mal_borte > 5: 
            self.kamperoverfemteller += 1 
            self.kamperoverfem[f"{self.kampnr}"] = [mal_hjemme, mal_borte]
    
    def spillbo(self):
        self.kampnr += 1 

        forventetmalhj = ((self.hjemmelag._angrep+(self.hjemmelag._forsvar))/2)
        forventetmalbo = ((self.bortelag._angrep+(self.bortelag._forsvar))/1.5)
  

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
            if math.ceil(mal_hjemme) - mal_hjemme < 0.20:
                mal_hjemme = math.ceil(mal_hjemme)
            
            elif mal_hjemme-math.floor(mal_hjemme) < 0.5: 
                mal_hjemme = math.floor(mal_hjemme)
            else: 
                mal_hjemme = math.floor(mal_hjemme)

                
                '''
                if self.hjemmelag.angrep > self.bortelag.forsvar: 
                    mal_hjemme = math.ceil(mal_hjemme)
                
                else: 
                    mal_hjemme = math.floor(mal_hjemme)
                '''
        
        '''
        if mal_hjemme < 0 or mal_borte < 0: 
            if mal_hjemme < 0 and mal_borte < 0: 
                mal_hjemme = abs(mal_hjemme) 
                mal_borte = abs(mal_borte)
            elif mal_hjemme == 0: 
                mal_hjemme = abs(mal_hjemme) 
            else: 
                mal_borte = abs(mal_borte)

        '''
       
        if mal_borte != math.ceil(mal_borte): 
            if math.ceil(mal_borte) - mal_borte < 0.25:
                mal_borte = math.ceil(mal_borte)
            
            elif mal_borte-math.floor(mal_borte) < 0.5: 
                mal_borte = math.floor(mal_borte)
            else: 
                if random.randint(0, 1): 
                    mal_borte = math.ceil(mal_borte)
                else: 
                    mal_borte = math.floor(mal_borte)
            
        self.mal_hjemme = mal_hjemme
        self.mal_borte = mal_borte
        self.totalmalhj += mal_hjemme
        self.totalmalbo += mal_borte
        if mal_hjemme < mal_borte: 
            self.seier_borte += 1
        elif mal_hjemme > mal_borte: 
            self.seier_hjemme += 1 
        else: 
            self.uavgjort += 1 

        if mal_hjemme + mal_borte > 5: 
            self.kamperoverfemteller += 1 
            self.kamperoverfem[f"{self.kampnr}"] = [mal_hjemme, mal_borte]
        
    def mål_hjemme(self): 
        return self.mal_hjemme
        print(self.mal_hjemme)
        
    def mål_borte(self): 
        return self.mal_borte
        print(self.mal_borte)

    def statistikk(self): 

        print(f"\n Statistikk for {self.hjemmelag._navn} mot et gjennomsnittelig lag:\n")
        print(f"Gjennomsnittelig angrep: {self.totalmalhj/self.kampnr}, forsvar: {self.totalmalbo/self.kampnr}")
        print(f"seire hjemmelag: {self.seier_hjemme}, bortelag: {self.seier_borte}, uavgjort: {self.uavgjort}, kamper med over fem mål: {self.kamperoverfemteller}")
        #print(self.kamperoverfem)
        print(f"Prosentvis hjemmeseier: {self.seier_hjemme/(self.kampnr)}")
        print(f"Gjennomsnittelig mål per kamp: {(self.totalmalbo+self.totalmalhj)/self.kampnr}")
        


