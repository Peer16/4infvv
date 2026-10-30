getal1 = float(input("Geef een eerste getal: "))
bewerking = input("Welke bewerking? (+, -, *, /,**): ")
getal2 = float(input("Geef een tweede getal: "))

if bewerking == "+":
    resultaat = getal1 + getal2
    print(str(getal1) + " + " + str(getal2) + " = " + str(resultaat))
if bewerking == "-":
    resultaat = getal1 - getal2
    print(str(getal1) + " - " + str(getal2) + " = " + str(resultaat))
if bewerking == "*":
    resultaat = getal1 * getal2
    print(str(getal1) + " * " + str(getal2) + " = " + str(resultaat))
if bewerking == "/":
    resultaat = getal1 / getal2
    print(str(getal1) + " / " + str(getal2) + " = " + str(resultaat))
if bewerking == "**":
    resultaat = getal1 ** getal2
    print(str(getal1) + " ** " + str(getal2) + " = " + str(resultaat))
