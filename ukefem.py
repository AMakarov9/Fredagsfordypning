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