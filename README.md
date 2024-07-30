# JOLTEON: The JOint Lensed Transient Events Observation Network

![Jolteon](https://github.com/erinhay/jolteon/blob/main/jolteon.png)

## Challenge Aims
The Rubin Observatory's Legacy Survey of Space and Time is expected to observe hundreds of gravitationally lensed transients. With the JOint Lensed Transient Events Observation Network (JOLTEON), our goal is to provide resources for the development and testing of tools for lensed transient discovery with Rubin-LSST. We aim to provide publicly available LSST-like data products to serve as a testing ground for *your* lensed transient search methods. As a community, we will work collaboratively to "catch 'em all!"

If you are interested in testing your own method, want to make suggestions for the direction of JOLTEON, or just want to follow our progress, we welcome all LSST community members to become collaborators by joining the ``#sl-transient-search-challenge`` channel on the LSSTC slack!

## Leadership

JOLTEON is organized by a leadership team formed of Ana Sainz de Murieta, Dan Ryczanowski, Erin Hayes, and Luke Weisenbach. The leadership team is supported by the LSST Dark Energy Science Collaboration (DESC) Strong Lensing Topical Team Leads, Nikki Arendse, Suhail Dhawan, and Anowar Shajib, and the LSST Strong Lensing Science Collaboration (SLSC) Co-Chairs, Graham Smith and Simon Birrer.

## Data
The Extended LSST Astronomical Time-series Classification Challenge (ELAsTiCC) provides a sample of millions of simulated transient light curves as expected from Rubin-LSST. Among the simulated objects are resolved gravitationally lensed SN Ia, Ib/c, and II. These data will provide the basis of the light curve level data products, providing the challenge to distinguish the resolved lensed SNe from the other transients in the ELAsTiCC data. We also plan to extend the ELAsTiCC simulations to include unresolved lensed transients, like many of those we expect to find during LSST, and to include realistic microlensing models.

We will be releasing jupyter notebooks describing how to access the ELAsTiCC data soon!

For image level data products, our aim is to provide simulated lens + lensed transient postage stamps and difference images, along with a collection of host + transient images of the most frequent false positives.

## Science Goals
Below we describe some key science goals that we aim to explore with JOLTEON (a non-exhautive list!):
* What is the false positive rate/purity of the sample of objects identified by various search methods? What causes contaminants to passing through as successful within search methods?
* How quickly are lensed SNe correctly identified with various methods? What is the impact of this on measurements of cosmological parameters (e.g. $H_0$)?
* What is the impact of microlensing on various detection methods?
* On what timescale are real-time classifications of lensed transients stable?







