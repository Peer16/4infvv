aantal_personen = int(input("Hoeveel personen zijn er aanwezig? "))

if aantal_personen > 0:
    snoepjes_per_persoon = 250 // aantal_personen
    overgebleven_snoepjes = 250 % aantal_personen

    print("Elke persoon krijgt", snoepjes_per_persoon, "snoepjes.")
    print("Er blijven", overgebleven_snoepjes, "snoepjes over.")
else:
    print("Er moet minstens 1 persoon aanwezig zijn.")
