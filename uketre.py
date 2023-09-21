#Nederst i filen ligger første versjon av koden til programmet. Det gir sikkert litt mer mening med tanke på noen av if-else setningene. 

import random
def montystats(): 
    def monty(): 
        rekkefolge = random.sample(range(0,3), 3)
        dorer = {"Bil": rekkefolge[0], "Geiten": rekkefolge[1], "Geitto": rekkefolge[2]}

        forsok = random.randint(0,2)
        #forsok = int(input("Skriv inn dør: "))
        #forsok = 2
        #janei = ["ja", "nei"]
        #svar = random.sample(janei, 1)
        svar = "ja"
        #print(forsok)
        #print(dorer)

        if forsok == dorer["Bil"]: 
            #Har svar.lower fordi jeg først tok ja eller nei fra bruker. Gadd ikke å endre nå:p
            if svar.lower() == "ja": 
                print("feil")
                return 0 
            
            else: 
                print("riktig")
                return 1
        
        elif forsok == dorer["Geiten"]: 
            #Logikken bak svarene her er at jeg viser dør Geitto og spør om brukeren vil bytte.

            if svar.lower() == "ja": 
                print("riktig")
                return 1
           
            else: 
                print("feil") 
                return 0 
        else: 
            #Hvis brukervalgt dør ikke er Bil eller Geiten, blir det Geitto. Her også "åpner" jeg dør Geiten og spør om bruker vil bytte. 
            #Derfor blir det riktig hvis ja og feil ellers. 
            if svar.lower() == "ja": 
                print("riktig")
                return 1
                
            else:
                print("feil") 
                return 0 


    totalRuns = int(input("Antall runs som skal kjøres: ")) 
    counterriktig = 0
    counterfeil = 0 
    for i in range(totalRuns): 
        test = monty()
        if test == 1: 
            counterriktig+=1 
        else: 
            counterfeil+=1 
    print(f"Programmet har kjørt {totalRuns} ganger.")
    print(f"Antall seire med bytting av dør: {counterriktig}")
    print(f"Antall tap med bytting av dør: {counterfeil}")
    print(f"Når man bytter dør vinner man {100*(counterriktig/totalRuns)}% av gangene.")

#Denne la jeg inn bare for å leke litt med antallet kjøringer og se resultatene. 
inputtest = int(input("Antall kjøringer: "))
for i in range(inputtest): 
    montystats()












'''
def monty(): 
    rekkefolge = random.sample(range(0,3), 3)
    dorer = {"Bil": rekkefolge[0], "Geiten": rekkefolge[1], "Geitto": rekkefolge[2]}
    #dorer = {rekkefolge[0]: "Bil", rekkefolge[1]: "Geit", rekkefolge[2]: "Geit"}
    forsok = int(input("Skriv inn hvilken dør du tror det er:"))
    print(dorer)
    if forsok == dorer["Bil"]: 
        print("Bak dør " + str(dorer["Geiten"])+" står en geit")
        svar = input("Vil du bytte dør? ")
        if svar.lower() == "ja": 
            forsok == dorer["Geitto"]
            print("Du har byttet til en dør med en geit. Du har tapt.")
        else: 
            print("Du har valgt riktig dør, gratulerer.")
    elif forsok == dorer["Geiten"]: 
        print("Bak dør" + str(dorer["Geitto"])+ "står en geit")
        svar = input("Vil du bytte dør? ")
        if svar.lower() == "ja": 
            forsok == dorer["Bil"]
            print("Du har valgt riktig dør, gratulerer.")
        else: 
            print("Du har valgt feil dør.")
    else: 
        print("Bak dør " + str(dorer["Geiten"])+" står en geit")
        svar = input("Vil du bytte dør? ")
        if svar.lower() == "ja": 
            forsok == dorer["Geitto"]
            print("Du har byttet til en dør med en geit. Du har tapt.")
        else: 
            print("Du har valgt riktig dør, gratulerer.")

for i in range(10): 
    monty()
'''