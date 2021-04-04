# PIL je biblioteka za obradu slike,
# os i sys za pristup OS-u
from PIL import Image
import os, sys

# Putanja do foldera
putanja = r'C:\Users\Python 1\Desktop\11_cas\paris'
# Izlistaj sve slike u folderu
slike = os.listdir(putanja)
# Prosledili smo smer u kom zelimo da rotiramo slike
print(sys.argv)
smer = str(sys.argv[1])

# Za svaku sliku
for slika in slike:
    # Otvori je koristeci PIL
    putanja_do_slike = putanja + "\\" + slika    
    img = Image.open(putanja_do_slike)
    
    # Zavisno od smera koji smo prosledili, rotiraj
    if smer == "ulevo":
        rotated = img.rotate(90)
    elif smer == "udesno":
        rotated = img.rotate(-90)
        
    # Sacuvaj sliku
    rotated.save(putanja_do_slike)

print("Zavrseno!")