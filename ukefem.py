def beregnScore(valg_spiller1, valg_spiller2): 
    if valg_spiller1 == "samarbeid":
        if valg_spiller2 == "samarbeid": 
            return [3, 3]
        else: 
            return [0, 5]
    else: 
        if valg_spiller2 == "samarbeid": 
            return [5, 0]
        else: 
            return [1, 1]
        
def spill_snilt(valg: list) -> str:
    count = 0
    if len(valg) == 0:
         return "samarbeid"
    else: 
        for i in valg: 
            if i == "svik": 
                count += 1
        if count > (len(valg)//2): 
            return "svik"
        else: 
            return "samarbeid"


def spill_slemt(valg): 
    if len(valg) >= 5: 
        return "svik"
    else: 
        return "samarbeid"    

def utfor_spill(): 
    valgSnill = []
    valgSlem = []
    scoreSnill = 0
    scoreSlem = 0
    for i in range(1000): 
        snill = spill_snilt(valgSlem)
        slem = spill_slemt(valgSlem)
        score = beregnScore(snill, slem)
        scoreSnill += score[0]
        scoreSlem += score[1]
        valgSlem.append(slem)
        valgSnill.append(snill)

    print(f"Score snill: {scoreSnill}")
    print(f"Score slem: {scoreSlem}")

def utfor_spill_uendelig(): 
        valgSnill = []
        valgSlem = []
        scoreSnill = 0
        scoreSlem = 0
        while True: 
            finput = input("Skriv inn om programmet skal kjøre eller ikke: ")
            if finput == "ja": 
                snill = spill_snilt(valgSlem)
                slem = spill_slemt(valgSlem)
                score = beregnScore(snill, slem)
                scoreSnill += score[0]
                scoreSlem += score[1]
                valgSlem.append(slem)
                valgSnill.append(snill)
                print(f"Score snill: {scoreSnill}")
                print(f"Score slem: {scoreSlem}")
            else: 
                print(f"Score snill: {scoreSnill}")
                print(f"Score slem: {scoreSlem}")
                break

utfor_spill_uendelig()
