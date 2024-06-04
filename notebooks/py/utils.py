import numpy as np
import matplotlib.pyplot as plt

ordered = np.array(['u ', 'g ', 'r ', 'i ', 'z ', 'Y '])

def plot_lightcurve(snid, data, colors = {'u ': '#9467bd', 'g ': '#377eb8', 'r ': '#4daf4a', 'i ': '#e3c530', 'z ': '#ff7f00', 'Y ': '#e41a1c'}):

    filters = ordered[np.isin(ordered, data['BAND'])]
    fig, ax = plt.subplots(len(filters), 1, figsize=(8, len(filters)*2), sharex=True)

    for b, band in enumerate(filters):
        single_band = data[data['BAND'] == band]
        _, _, bars = ax[b].errorbar(single_band['MJD'], single_band['FLUXCAL'], yerr=single_band['FLUXCALERR'],
                                    ls='None', marker='o', color=colors[band])
        [bar.set_alpha(0.3) for bar in bars]
        ax[b].set_ylabel(band+'-band')

    ax[-1].set_xlabel('MJD [days]', fontsize=24)
    ax[0].set_title('SN '+str(snid), fontsize=28)
    fig.supylabel('Flux', fontsize=24, y=0.53)
    fig.align_ylabels()
    fig.tight_layout()
    fig.subplots_adjust(hspace=0, wspace=0)
    fig.show()
    return fig, ax

