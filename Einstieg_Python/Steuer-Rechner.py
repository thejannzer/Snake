def steuer(x):
    if x > 2500:
        print (f"es sind {x*0.22} Euro Steuern zu zahlen")
    else:
        print (f"es sind {x*0.18} Euro Steuern zu zahlen")

steuer(1800)
steuer(2200)
steuer(2500)
steuer(2900)

print ("----------------------------------")

def steuer_2():
    for i in range (1500, 3600, 500):
        if i == 2500:
            print (f"Es sind {i*0.22} Euro Steuern zu zahlen")
        elif i >= 3000:
            print (f"Es sind {i*0.33} Euro Steuern zu zahlen")
        else:
            print (f"Es sind {i*0.18} Euro Steuern zu zahlen")

steuer_2()



    