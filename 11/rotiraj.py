# import the Python Image 
# processing Library
from PIL import Image
import os

slike_dir = './paris/'
slike = os.listdir(slike_dir)

for slika in slike:
    # Giving The Orginal image Directory 
    # Specified
    putanja_do_slike = slike_dir + slika
    print(putanja_do_slike)
    Original_Image = Image.open(putanja_do_slike)
      
    # Rotate Image By 180 Degree
    rotated_image1 = Original_Image.rotate(-90)
      
    rotated_image1.save(putanja_do_slike)
    
print("Gotovo!")