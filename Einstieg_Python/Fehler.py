#Fehlerbehandlung

#einmalige ausführung
zahl = input ("Bitte gib eine zahl ein: ")

try:
    zahl = int(zahl)
    print("Super, alles richtig")
except:
    print ("Bitte gib eine Zahl ein")

#mehrfache ausführung wegen unendlicher Schleife (while True), ende bei richtiger Eingabe
while True:
    zahl2 = input ("Bitte gib die zweite Zahl ein: ")
    try:
        zahl2 = int(zahl2)
        print("Auch hier alles richitg")
        break
    except:
        print("Bitte eine Zahl eingeben")
        




        