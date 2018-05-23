import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def weighted_mean(data, err):            #calculates the weighted mean for data points data with std devs. err
    ind = err != 0.0
    weights = 1.0/err[ind]**2
    mu = np.sum(data[ind]*weights)/np.sum(weights)
    var = 1.0/np.sum(weights)
    return [mu, np.sqrt(var)]

sns.set_context("notebook", font_scale = 1.0)
sns.set_style("white")
sns.set_style("ticks", {"xtick.direction":"in", "ytick.direction":"in"})

#equivalent widths from Antonija's email
width_a = 0.056/70.*1e6
width_b = 0.003/70.*1e6
width_c = 0.02/70.*1e6
width_d = 0.000/70.*1e6

#wave_bins = np.array([8360, 8998, 9598, 10198, 10798, 10868, 11290])/1e4
d= np.genfromtxt("w12_g102_tspec_rp_tied_mcmc_with_dilution.txt")
d = d[-3::, :]
xerr = np.array([600., 70., 422])/1.e4/2.

#get weighted average of two neighboring data points
y, yerr = np.array([d[0,1], d[2,1]]), np.array([d[0,2], d[2,2]])
mu, sig = weighted_mean(y, yerr)
diff_sig = np.sqrt(sig**2 + d[1,2]**2)*1e6

#observed ampltidue of feature
observed = (d[1,1] - mu)*1e6

#calculate significance of difference with He line
print "observed feature (ppm)", observed, "+/-", diff_sig
print "detection significance, ppm error (model A)", (width_a - observed)/diff_sig, diff_sig
print "detection significance, ppm error (model B)", (width_b - observed)/diff_sig, diff_sig


print "mean flux decrement", 1 - np.mean(d[:,1])

plt.figure(figsize = (6.5,3))
plt.errorbar(d[:,0], d[:,1]*1e6 - np.mean(d[:,1]*1e6), yerr = d[:,2]*1e6, xerr
=xerr, linestyle = 'none', zorder = 100, marker = 'o', color = 'w',
markeredgecolor = 'k', ecolor ='k', markeredgewidth = 1.2, linewidth = 1.0)

plt.axhline(0, linestyle = 'dotted', color = '0.5', zorder=-100)

delta = 30.
He = 10830.


x = np.array([He - delta, He - delta, He + delta, He + delta])/1e4
y = np.array([0., width_a, width_a, 0.])
plt.plot(x, y, color = '#0165fc', label = 'Model A (all gas)', zorder= -10)

y = np.array([0., width_b, width_b, 0.])
plt.plot(x, y, color = '#fd411e', label = 'Model A (Roche only)', zorder = -8)

y = np.array([0., width_c, width_c, 0.])
plt.plot(x, y, color = 'orange', label = 'Model B (all gas)', zorder = -9)

y = np.array([0., width_d, width_d, 0.])
plt.plot(x, y, color = 'cyan', label = 'Model B (Roche only)', zorder = -7)

plt.legend(loc = 'upper left')
plt.xlabel("Wavelength (microns)")
plt.ylabel("Relative transit depth (ppm)")

plt.tight_layout()
plt.savefig("fig1.pdf")
#plt.show()
