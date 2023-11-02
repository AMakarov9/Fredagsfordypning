class Lag:
    def __init__(self, navn, angrep, forsvar):
        self._navn = navn
        self._angrep = angrep
        self._forsvar = forsvar

    # Navnet til laget
    def navn(self):
        return self._navn
    
    # Antall mål laget scorer mot et gjennomsnittlig lag (høyere = bedre for dette laget)
    def angrep(self):
        return self._angrep
    
    # Antall mål laget slipper inn mot et gjennomsnittlig lag (lavere = bedre for dette laget)
    def forsvar(self):
        return self._forsvar
    
    # Magisk metode som gjør at lagene kan sorteres alfabetisk etter navn (gjøres av Tabell)
    def __gt__(self, other):
        return self._navn > other._navn
    
    # Magisk metode som gjør at lagene kan sorteres alfabetisk etter navn (gjøres av Tabell)
    def __lt__(self, other):
        return self._navn < other._navn