import random
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