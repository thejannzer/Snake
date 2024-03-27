#for-Schleifen

def Übungen():
    for zahl in 3,5,9:
        print(f"Zahl: {zahl}")

    for stadt in "London", "Berlin":
        print(f"Stadt: {stadt}")

    for zeichen in "Hello":
        print (zeichen)

    #continue führt zum abbruch des aktuellen Durchlaufs und überführt zum darauf folgenden
    for zahl in range (1,7):             #Zählt von 1 bis 6
        print (f"Zahl: {zahl}")
        if zahl*zahl < 20:
            continue
        else:
            print (zahl*zahl)

    #range()
    for i in range (4):                  #Zählt von 0 bis 3
        print (i)

    #range()
    #for i in range (Anfang des Bereiches, Ende des Bereiches+1, Schrittweite)
    for i in range (3,11,2):
        print (i)

#uebung_rechner
for i in range (15,41,5):
    print(f"Inch: {i} = {i*2.54}cm")




