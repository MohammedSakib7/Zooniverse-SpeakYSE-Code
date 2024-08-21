import pandas as pd
import numpy as np
import os
import csv
from collections import defaultdict

file_path = 'ZTFBTS_TransientTable.csv'
data = pd.read_csv(file_path)

grouped = data.groupby('type')
num_samples_per_type = len(data) // len(grouped)
sampled_ztfids = []

for type_name, group in grouped:
    sampled_group = group.sample(n=min(len(group), num_samples_per_type), random_state=1)
    sampled_ztfids += sampled_group['ZTFID'].tolist()

# We have a list of ids from the weighted sampling
dir1 = "hostImgs"
dir2 = "light-curve-plots"
dir3 = "spectra_imgs"
dir4 = "images"

images = sorted(os.listdir(dir1))
plots = sorted(os.listdir(dir2))
spectras = sorted(os.listdir(dir3))
datas = sorted(os.listdir(dir4))

sampled_ztfids = set(sampled_ztfids)

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

for data in datas:
    if data == ".DS_Store":
        continue
    key = data.split("_")[0]
    if key in hashmap:
        hashmap[key].append(os.path.join(dir4, data))


with open('generated_manifest.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["id", "image1", "image2", "image3", "image4"] #field names here
    writer.writerow(field) 
    for key, pair in hashmap.items():
        if len(pair) == 4 and key in sampled_ztfids:
            new_row  = [key] + pair
            writer.writerow(new_row)
    
    file.close()

with open('generated_manifest1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["id", "image1", "image2", "image3"] #field names here
    writer.writerow(field) 
    for key, pair in hashmap.items():
        if len(pair) == 3 and key in sampled_ztfids:
            new_row  = [key] + pair
            writer.writerow(new_row)
    
    file.close()

