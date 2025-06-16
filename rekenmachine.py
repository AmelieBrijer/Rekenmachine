resultaat = float(input("Eerste getal? "))

while True:
    invoer = input("Operator of 'nieuw' om opnieuw te beginnen: ").strip().lower()

    if invoer == 'nieuw':
        resultaat = float(input("Nieuw getal? "))
        print("Resultaat opnieuw ingesteld op:", resultaat)
        continue

    operator = invoer
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
    else:
        print("Ongeldige operator.")
        continue

    print("Resultaat:", resultaat)

