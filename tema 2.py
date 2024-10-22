#metoda care separa cele sirul in 2 siruri
def separare(sir):
    sir1=sir[0:len(sir)//2]
    if len(sir)%2==0:
        sir2=sir[len(sir)//2:]
    else:
        sir2 =sir[len(sir) // 2 +1:]
    return sir1, sir2
#transforma toate literele in majuscule
def maj(sir1):
    return sir1.upper()
#elimina toate spatiile goale de la inceputul si finalul sirului
def capete(sir1):
    return sir1.strip(" ")
#inverseaza ordinea caracterelor
def inv(sir2):
    return "".join(reversed(sir2))
#transforma prima litera in majuscula
def litmare(sir2):
    return sir2.capitalize()
#elimina toate caracterele de puncuatie
def eliminare(sir2):
    sir2 = sir2.replace(".", "")
    sir2 = sir2.replace(",", "")
    sir2 = sir2.replace("?", "")
    sir2 = sir2.replace("!", "")
    sir2 = sir2.replace("(", "")
    sir2 = sir2.replace(")", "")
    sir2 = sir2.replace("-", "")
    return sir2
#combina si afiseaza rezultatul
def comb(sir):
    sir=sir1+sir2
    print(sir)
sir="Scuderia Ferrari a reuşit dubla în Marele Premiu de Formula 1 al Statelor Unite, dominat de piloţii echipei italiene, monegascul Charles Leclerc şi spaniolul Carlos Sainz Jr, care au ocupat primele două locuri în clasamentul final, devansându-l pe campionul mondial en titre, olandezul Max Verstappen (Red Bull), clasat pe ultima treaptă a podiumului."
sir1, sir2=separare(sir)
sir1=maj(sir1)
sir1=capete(sir1)
sir2=inv(sir2)
sir2=litmare(sir2)
sir2=eliminare(sir2)
comb(sir)
