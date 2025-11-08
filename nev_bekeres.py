nev = input("Kerek egy nevet(gyk:Béla): ")
print(len(nev))

if any(char.isdigit() for char in nev):
    print("Na,ne szotakozzál..")
else:
    print("Megfelelő név")
