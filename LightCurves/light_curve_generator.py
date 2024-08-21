import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


directory = 'samples'
savedir = 'sampleplots'

for file_name in os.listdir(directory):
    if file_name == ".DS_Store":
        continue
    print(file_name)

    file_path = os.path.join(directory, file_name)

    data = pd.read_csv(file_path)

    data_r = data[data['band'] == 'R']
    data_g = data[data['band'] == 'g']

    time_r = data_r['time'].to_numpy()
    mag_r = data_r['mag'].to_numpy()
    magerr_r = data_r['magerr'].to_numpy()

    time_g = data_g['time'].to_numpy()
    mag_g = data_g['mag'].to_numpy()
    magerr_g = data_g['magerr'].to_numpy()

    plt.figure(figsize=(10, 6))
    plt.errorbar(time_r, mag_r, yerr=magerr_r, fmt='s', color='red', capsize=2, label='R Band')
    plt.errorbar(time_g, mag_g, yerr=magerr_g, fmt='s', color='green', capsize=2, label='g Band')
    plt.gca().invert_yaxis()

    plt.title(f'Light Curves for {os.path.splitext(file_name)[0]}')
    plt.xlabel('Time (JD)')
    plt.ylabel('Brightness (Magnitude)')
    plt.legend()

    plot_path = os.path.join(savedir, f'{os.path.splitext(file_name)[0]}.png')
    plt.savefig(plot_path)
    plt.close()

    print(f'Saved plot for {file_name} as {plot_path}')
