Code = input("Wat wil je vertalen?")
while True:#Checkt of stappen een cijfer is.
    Stappen = input("Met hoeveel stappen wil je het vertalen?")
    try:
        Stappen =  int(Stappen)
        break; 
    except ValueError:
        print('Type een heel getal getal.')
def Ceasarrotation(Woord , Hoeveelheid ):#Ceasarrotation 
    Aantalstappen = Hoeveelheid % 26 #Deelt jouw input door 26 en neemt het overige
    ApparteLettersTuple = (*Woord.upper(),)#Haalt het woord uit elkaar en uppercase in een tuple
    VertaaldeLetters = [] #Legelijst voor eindproduct
    for Letter in ApparteLettersTuple:#Gaat door de tuple heen
        if ord(Letter) < 91 and ord(Letter) > 64: #Checkt of het een letter is
            VertaaldeLetters.append(chr((ord(Letter) - 65 + Aantalstappen) % 26 + 65)) #Vertaald de letter
        elif ord(Letter) == 32:  #Checkt of het een spatie is
            VertaaldeLetters.append(Letter) #Behoudt de spatie
    VertaaldeLetters = "".join(VertaaldeLetters)#Zet alles bij elkaar
    return VertaaldeLetters#spreekt voor zich
print("Dit is je vertaalde tekst:", Ceasarrotation(Code , Stappen))# Spreekt voor zich