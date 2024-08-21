import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_spectra(file_path, output_dir):
    data = pd.read_csv(file_path)
    
    wavelength = data.iloc[:, 0]
    intensity = data.iloc[:, 1]
    
    plt.figure(figsize=(10, 6))
    plt.plot(wavelength, intensity, color='blue', linestyle='-', marker='')
    plt.xlabel('Wavelength (Angstroms)')
    plt.ylabel('Intensity')
    plt.title(f'Spectra Plot for {os.path.basename(file_path)}')
    plt.grid(True)
    
    output_file = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(file_path))[0]}.png")
    plt.savefig(output_file)
    plt.close()

in_dir = "ZTFBTS_spectra"
out_dir = "spectra_imgs"

for filename in os.listdir(in_dir):
    file_path = os.path.join(in_dir, filename)
    plot_spectra(file_path, out_dir)
