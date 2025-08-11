
ponovi = True
seznamStrank = []
while (ponovi == True):
    odločitev=input("Vnesi 1 za DODAJANJE STRANK, vnesi 2 za IZPIS STRANK in 3 za IZHOD iz programa.")
    if (odločitev=="1"):
        ime = input("Vnesi ime stranke: ")
        seznamStrank.append(ime)
    elif (odločitev=="2"):
        print(seznamStrank)
    elif (odločitev=="3"):
        ponovi=False
        print(seznamStrank)
        print("Hvala da si uporabil naš program.")
    else:
        input("Vnesel si neveljavno vrednost poskusi ponovno. Za nadaljevanje pritisni ENTER.")
        

   
      
    

