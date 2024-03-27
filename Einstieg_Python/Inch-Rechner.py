print("Inch-Rechner")
zahl = input("Bitte gib den Wert in cm ein: ")
try:
    zahl = int (zahl)
except:
    print("Bitte gib eine ganze Zahl ein")

while zahl != 0:
    print (f"Der wert in Inch ist {zahl/2.54}")
    break



    
