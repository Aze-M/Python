def mwst():
    while True:
        try:
            value_text=input("Bitte Netto Betrag eingeben (leereingabe = Ende): ")
            if not value_text:
                print("Auf wiedersehen!")
                return
        
            value = float(value_text)
            print('Bruttopreis %.2f'%(value*1.19))
    
        except:       
            print(f"Bitte einen gueltigen Betrag eingeben")
#Main
mwst()