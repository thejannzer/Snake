import math
#beim importiern immer importierte libary mit angeben beim verwenden... siehe winkelf, oder auch RANDOM.randint(...)

#Typ ermitteln
def typ():
    a = 2
    b = "Hello_World"
    c = 2+4==6
    d = 3.454

    print (type(a))
    print (type(b))
    print (type(c))
    print (type(d))

#Exponentialisieren
def exponent():
    x = 5**3     # 5 hoch 3
    print(x)

#runden
def runden():
    x = 5/12
    print (x)
    print ("gerundet auf 3 Stellen: ", round(x,3))
    print ("gerundet auf eine Stelle: ", round(x,1))

#math
#import math
#Winkelfunktionen
def winkelf():
    x = 30
    print (math.sin(x))

#komplexe Zahlen
def komplex():
    a = 2-4j
    print ("a= ", a)
    print (f"Realteil: {a.real}")
    print (f"Imaginärteil: {a.imag}")
    print (f"Betrag von a: ", abs(a))

#binär
def binär():
    a = 4
    print (bin(a))

#suchen und ersetzen in Zeichenketten
