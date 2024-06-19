import numpy as np
import astropy.table as at
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

def get_unresolved_lc(snid, photometry0, photometry1=None, photometry2=None, photometry3=None, show_plot=True,
                      colors = {'u ': 'tab:purple', 'g ': '#377eb8', 'r ': '#4daf4a', 'i ': '#e3c530', 'z ': '#ff7f00', 'Y ': '#e41a1c'}):

    mjd = photometry0['MJD']
    bands = photometry0['BAND']
    comb_flux = np.zeros(len(mjd))
    
    for photometry in [photometry0, photometry1, photometry2, photometry3]:
        if photometry is None:
            continue

        flux = 10**((photometry['SIM_MAGOBS'] - 27.5)/-2.5)
        comb_flux = comb_flux + flux

    comb_mag = 27.5 - 2.5*np.log10(comb_flux)
    mask = comb_mag < 50.

    data = at.Table([mjd[mask], bands[mask], comb_mag[mask]], names=['MJD', 'BAND', 'SIM_MAGOBS'], dtype=['>f8', '<U2', '>f4'])

    if show_plot:
        fig, ax = plt.subplots(6, 1, figsize=(9, 12), sharex=True)

        for b, band in enumerate(colors.keys()):
            
            mjd = photometry0[photometry0['BAND'] == band]['MJD']
            comb_flux = np.zeros(len(mjd))
            
            for photometry in [photometry0, photometry1, photometry2, photometry3]:
                
                if photometry is None:
                    continue
                
                single_band = photometry[photometry['BAND'] == band]
                single_band_flux = 10**((single_band['SIM_MAGOBS'] - 27.5)/-2.5)
                
                comb_flux = comb_flux + single_band_flux
            
            comb_mag = 27.5 - 2.5*np.log10(comb_flux)
            mask = comb_mag < 50.

            _, _, bars = ax[b].errorbar(mjd[mask], comb_mag[mask], ls='None', marker='o', color=colors[band])
            [bar.set_alpha(0.3) for bar in bars]

            ax[b].set_ylabel(band+'-band')
            ax[b].invert_yaxis()

        ax[-1].set_xlabel('MJD [days]', fontsize=24)
        ax[0].set_title('SN '+str(snid), fontsize=28)
        fig.supylabel('Magnitude', fontsize=24, y=0.53)
        fig.align_ylabels()
        fig.tight_layout()
        fig.subplots_adjust(hspace=0, wspace=0)
        fig.show()

    return data

