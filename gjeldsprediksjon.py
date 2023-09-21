from pprint import pprint


class Bruker(): 
    def __init__(self, brukerid, alder, kjonn, sivilstatus, gjeld, betalingshistorikk, utdanning): 
        self.id = brukerid
        self.alder = alder 
        self.kjonn = kjonn
        self.sivilstatus = sivilstatus
        self.gjeld = gjeld
        self.historikk = betalingshistorikk
        self.utdanning = utdanning

    def prediksjon_med_historikk(self):
        svartliste = [23894, 29741, 10961, 22768, 22803, 11993, 24409, 9312, 29405, 6638, 738, 29964, 11967, 13443, 11534, 26228, 6867, 23027, 29137, 14084, 452, 15594, 22765, 25487]
        if self.id in svartliste: 
            return False
        else: 
            lonnsoversikt = {"ukjent": 300000, "grunnskole": 260000, "høyskole": 500000, "universitet": 700000}
            self.lonn = lonnsoversikt[self.utdanning]

            if self.lonn > (self.gjeld * 3) and self.kjonn == "mann": 
                return True
            
            elif (self.historikk).count("ikke_betalt") >= 2: 
                return False
            
            else: 
                return True

def test_min_prediksjon():

    antall_predikert = 0
    antall_riktig_predikert = 0
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0


    personregister = {}
    datafil = "individer1000.txt"
    fil = open(datafil)
    
    for linje in fil:
        data = linje.strip().split(",")
        brukerid = int(data[0])
        alder = int(data[1])
        kjonn = data[2]
        sivilstatus = data[3]
        gjeld = int(data[4])
        betalingshistorikk = []
        for i in range(0, 3):
            betalingshistorikk.append(data[5+i])

        utdanning = data[8].replace("oe", "ø")
        if data[9] == "vil betale": 
            fasit = True
        else:
            fasit = False
        
        personregister[brukerid] = [brukerid, alder, kjonn, sivilstatus, gjeld, betalingshistorikk, utdanning]
        objekt = Bruker(*personregister[brukerid])
        prediksjon = objekt.prediksjon_med_historikk()


        if prediksjon == fasit:
            antall_riktig_predikert += 1

        if fasit:
            if prediksjon:
                true_positive += 1
            else:
                false_negative += 1
        else:
            if prediksjon:
                true_negative += 1
            else:
                false_positive += 1

        antall_predikert += 1


    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)
    f1_score = 2 * (precision*recall) / (precision + recall)

    print(antall_riktig_predikert, "av", antall_predikert, "ble riktig predikert")
    print("Recall:", recall)
    print("Precision:", precision)
    print("F1 score:", f1_score)

test_min_prediksjon()



'''
def brukerdannelse(): 
    antallbrukere = int(input("Skriv inn antall brukere som skal lages: "))       
    brukere = []
    for i in range(antallbrukere):
        brukerinfo = ["alder", "kjonn", "sivilstatus", "gjeld"]
        bruker = []
        for i in brukerinfo:
            info = input(f"Skriv inn {i}: ")

            if info.isnumeric(): 
                bruker.append(int(info))
            else: 
                bruker.append(info)
        brukere.append(Bruker(*bruker))
    return brukere
'''
    #test1 = brukerdannelse()

    #test2 = test1[1]
    #test3 = test1[0]
    #pprint(vars(test2))
    #pprint(vars(test3))


'''
testing = Bruker(21, "mann", "gift", 120000)
test = Bruker(22, "mann", "gift", 0)
banan.prediksjon_med_historikk(); 
test.prediksjon_med_historikk(); 

pprint(vars(banan))
pprint(vars(test))
pprint(vars(banan))





    def enkelprediksjon(self): 
        if self.kjonn == "mann": 
            if (self.alder < 30) and (self.gjeld > 100000) and (self.sivilstatus == "singel"): 
                return False
            
            elif (self.alder < 25) and (self.gjeld > 200000): 
                return False
            else: 
                return True
          
        elif (self.alder < 28) and (self.gjeld > 300000): 
            return False
     
        else: 
            return True


'''




'''
def sorting(arr): 
    if len(arr) > 1: 
        leftArr = arr[:len(arr)//2]
        rightArr = arr[len(arr)//2:]
    
    sorting(leftArr)
    sorting(rightArr)

    i = 0 # left index
    j = 0 # right index 
    k = 0 # index for merged array
    while i < len(leftArr) and j < len(rightArr): 
        if leftArr(i) < rightArr[j]: 
            arr[k] = leftArr[i]
            i+=1
         
        else: 
            arr[k] = rightArr[j]
            j += 1
        k += 1
    while i < len(leftArr): 
        arr[k] = leftArr[i]
        i += 1
        k += 1
    while j < len(rightArr): 
        arr[k] = rightArr[j]
        j += 1
        k += 1
'''
