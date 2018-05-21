import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_context("notebook", font_scale = 1.0)
sns.set_style("white")
sns.set_style("ticks", {"xtick.direction":"in", "ytick.direction":"in"})

#wave_bins = np.array([8360, 8998, 9598, 10198, 10798, 10868, 11290])/1e4
d= np.genfromtxt("w12_g102_tspec_rp_tied_mcmc_with_dilution.txt")
d = d[-3::, :]
xerr = np.array([600., 70., 422])/1.e4/2.

plt.figure(figsize = (6.5,3))
plt.errorbar(d[:,0], d[:,1]*1e6 - np.mean(d[:,1]*1e6), yerr = d[:,2]*1e6, xerr
=xerr, linestyle = 'none', zorder = 100, marker = 'o', color = 'w', markeredgecolor = 'k', ecolor ='k', markeredgewidth = 1.3)

plt.axhline(0, linestyle = 'dotted', color = '0.5', zorder=-100)

delta = 30.
He = 10830.

a = 0.056/70.*1e6
b = 0.003/70.*1e6

x = np.array([He - delta, He - delta, He + delta, He + delta])/1e4
y = np.array([0., a, a, 0.])
plt.plot(x, y, color = '#0165fc', label = 'Model 1 (all gas)')

y = np.array([0., b, b, 0.])
plt.plot(x, y, color = '#fd411e', label = 'Model 2 (Roche only)')

plt.legend(loc = 'upper left')
plt.xlabel("Wavelength (microns)")
plt.ylabel("Relative transit depth (ppm)")

plt.tight_layout()
plt.savefig("fig1.pdf")
#plt.show()
