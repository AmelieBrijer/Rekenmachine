import math

resultaat = float(input("Eerste getal? "))

while True:
    invoer = input("Operator ('+', '-', '*', '/', 'sqrt', '^') of 'nieuw' om opnieuw te beginnen: ").strip().lower()

    if invoer == 'nieuw':
        resultaat = float(input("Nieuw getal? "))
        print("Resultaat opnieuw ingesteld op:", resultaat)
        continue

    operator = invoer

    if operator == 'sqrt':
        if resultaat < 0:
            print("Kan geen wortel nemen van een negatief getal.")
            continue
        resultaat = math.sqrt(resultaat)
    else:
        getal_2 = float(input("Volgend getal? "))

        if operator == '+':
            resultaat += getal_2
        elif operator == '-':
            resultaat -= getal_2
        elif operator == '*':
            resultaat *= getal_2
        elif operator == '/':
            if getal_2 == 0:
                print("Je kunt niet delen door 0.")
                continue
            resultaat /= getal_2
        elif operator == '^' or operator == '**':
            resultaat **= getal_2
        else:
            print("Ongeldige operator.")
            continue

    print("Resultaat:", resultaat)


