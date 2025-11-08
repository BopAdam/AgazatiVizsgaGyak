def beker_adat(nev):
    while True:
        try:
            adat = float(input(f"Kérem adja meg a(z) {nev}-t: "))
            return adat 
        except ValueError:
            print("Hibás adat, kérem számot adjon meg.")

def szamit_terfogat(r, h):
    pi = 3.14159265359
    return (r ** 2) * pi * h

def main():
    sugar = beker_adat("sugár")
    magassag = beker_adat("magasság")
    terfogat = szamit_terfogat(sugar, magassag)
    print("Hengeres hasáb térfogata: ", terfogat)

if __name__ == "__main__":
    main()