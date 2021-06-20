age = int(input("Életkora: "))
drink = input("Milyen italt kér? ")

if age < 18 and (drink == "sör" or drink == "kóla"):
    if drink == "sör":
        print("Sajnos kiskorúakat nem szolgálhatunk ki alkohollal!")
    else:
        print("Parancsoljon,a kólája.")
elif 60 < age and (drink == "sör" or drink == "kóla"):
    if drink == "kóla":
        print("A koffein megemelheti a vérnyomását")
    else:
        print("Parancsoljon, a söre.")
else:
    print("Csak sört és kólát tudunk adni!")
