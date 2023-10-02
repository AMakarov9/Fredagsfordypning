import numpy as np
import wave
def lag_tone(antall_sekunder, antall_svingninger_i_sekundet):
    lyd = []
    for i in range(int(44100 * antall_sekunder)):
        lyd.append(16000 * (1 + np.sin(antall_svingninger_i_sekundet * i/44100 * 2 * np.pi)))
    return lyd

def skriv_lyd_til_fil(data, sample_rate, filnavn):
    # tatt fra https://stackoverflow.com/a/64376061
    audio = np.array([data, data]).T
    audio = audio.astype("<h")

    with wave.open(filnavn, "w") as f:
        f.setnchannels(2)
        f.setsampwidth(2)
        f.setframerate(sample_rate)
        f.writeframes(audio.tobytes())

#skriv_lyd_til_fil(lag_tone(10, 679), 44100, "filnavn.wav")

noter = {
    "A": 440,
    "G": 392,
    "F": 349,
    "E": 330,
    "D": 294,
    "B": 247,
    "C": 261,
    "-": 0
}
def les_sang_fra_fil(sangtekst, notes: dict): 
    fil = open(sangtekst)
    song = []
    for linje in fil: 
        data = linje.strip().split(" ")
        song.append([notes[data[0]], float(data[1])])

    return song

def lag_sang_fra_noter(noter): 
    lyd = []
    for i in range(len(noter)): 
        for j in range(int(44100 * noter[i][1])): 
            lyd.append(16000 * (1 + np.sin(noter[i][0] * j/44100 * 2 * np.pi)))
    print(len(lyd))
    return lyd



test = lag_sang_fra_noter(les_sang_fra_fil("sang.txt", noter))

def fade_ut(sang): 
    lengde = len(sang)
    refrence = lengde//10
    countIndex = 0
    volumeLevel = 10
    for i in range(0, lengde): 
        if i < (refrence*countIndex): 
            sang[i] = sang[i]*(volumeLevel/100)
              
        else: 
            countIndex += 1
            volumeLevel -= 1

    
    return sang 

def forenkle_lyd(lyd): 
    for i in range(0, len(lyd)): 
        if lyd[i] > 16000: 
            lyd[i] = 32000
        elif lyd[i] < 16000: 
            lyd[i] = 0
    return lyd 



skriv_lyd_til_fil(forenkle_lyd(test), 44100, "filnavn.wav")