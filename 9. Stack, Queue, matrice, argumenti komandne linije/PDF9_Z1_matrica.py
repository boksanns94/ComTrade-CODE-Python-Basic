from sys import argv

if len(argv) != 3:
    print("Unesite tacno 3 argumenta! Naziv python fajla, broj redova i broj kolona.")
    exit()

redovi = int(argv[1])
if redovi > 50:
    print("Greska: prevelik broj redova. Max je 50.")
    exit()
kolone = int(argv[2])
if kolone > 50:
    print("Greska: prevelik broj kolona. Max je 50.")
    exit()

matrica = []
print("Unesite elemente matrice: ")
for i in range(redovi):
    print(f"Unesite elemente {i+1}. reda matrice:")
    trenutni_red = []
    for j in range(kolone):
        unos = input(f"Unesite element [{i}][{j}]: ")
        trenutni_red.append(unos)
    print(f"Zavrsili smo unos {i+1}. reda matrice: {trenutni_red}")
    matrica.append(trenutni_red)

for i in range(redovi):
    for j in range(kolone):
        print(matrica[i][j],end=" ")
    print()