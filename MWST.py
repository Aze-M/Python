while True:
    try:
        in_price = float(input("Preis eingeben: "))
        break
    except ValueError:
        print("Eingang kein valider Preis.")

print(f"Brutto Preis: {float(in_price) * 1.19}")