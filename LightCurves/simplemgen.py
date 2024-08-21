import os
import csv
from collections import defaultdict

dir1 = "hostImgs"
dir2 = "light-curve-plots"
dir3 = "spectra_imgs"
dir4 = "images"

images = sorted(os.listdir(dir1))
plots = sorted(os.listdir(dir2))
spectras = sorted(os.listdir(dir3))
data = sorted(os.listdir(dir4))

hashmap = defaultdict(list)
for image in images:
    if image == ".DS_Store":
        continue
    key = image.split(".")[0]
    hashmap[key].append(os.path.join(dir1, image))

for plot in plots:
    if plot == ".DS_Store":
        continue
    key = plot.split(".")[0]
    hashmap[key].append(os.path.join(dir2, plot))

for spectra in spectras:
    if spectra == ".DS_Store":
        continue
    key = spectra.split(".")[0]
    if key in hashmap:
        hashmap[key].append(os.path.join(dir3, spectra))

print("Created " + str(len(hashmap)) + " subjects")


with open('generated_manifest.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["id", "image1", "image2", "image3"] #field names here
    writer.writerow(field) 
    for key, pair in hashmap.items():
        if len(pair) == 3:
            new_row  = [key] + pair
            writer.writerow(new_row)
    
    file.close()

with open('generated_manifest1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["id", "image1", "image2", "image3"] #field names here
    writer.writerow(field) 
    for key, pair in hashmap.items():
        if len(pair) == 2:
            new_row  = [key] + pair
            writer.writerow(new_row)
    
    file.close()



    # Use for-loop and writer.writerow([...]) to write each row