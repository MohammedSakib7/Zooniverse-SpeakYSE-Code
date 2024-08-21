import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main(filename):
    file_path = filename
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
    plt.errorbar(time_r, mag_r, yerr=magerr_r, fmt='o', ecolor='red', capsize=2, label='R Band')
    plt.errorbar(time_g, mag_g, yerr=magerr_g, fmt='o', ecolor='green', capsize=2, label='g Band')
    plt.gca().invert_yaxis()

    plt.title('Light Curves for R and g Bands')
    plt.xlabel('Time (JD)')
    plt.ylabel('Brightness (Magnitude)')
    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()