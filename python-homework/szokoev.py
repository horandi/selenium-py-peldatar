year = int(input("Adj egy évszámot, megmondom szökőév-e! "))
if (year % 400) == 0:
    print("Szökőév")
elif (year % 100) == 0:
    print("Nem szökőév")
elif (year % 4) == 0:
    print("Szökőév")
else:
    print("Nem szökőév")
