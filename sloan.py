#########################################################################################
#	Computational Physics HW5 Problem 2
#	
#	This program fits SDSS DR 13 data with a linear, quadratic, and broken linear function
#
#	Written by Jacqueline Antwi-Danso 03/17
#########################################################################################
import fitsio 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import plot, xlabel, ylabel, title, show, xlim

# flags for bad data and conversion from flux to magnitude (to determine bad magnitude values)
# obtained from https://data.sdss.org/datamodel/files/SPECTRO_REDUX/specObj.html
data = fitsio.FITS('/Users/Vivian/Desktop/Computational/hw5/specObj-dr13.fits')
cut = data[1].where('PLATE == 4602 && ZWARNING == 0')
z = data[1][cut]['Z']
zerr = data[1][cut]['Z_ERR']
flux = data[1][cut]['SPECTROFLUX'][:,3]
mag = 22.5 - 2.5 * np.log10(flux)

#guess parameters for linear fit
max_loc, min_loc = np.where(mag == max(mag)), np.where(mag == min(mag))
guess_slope = float((max(mag)-min(mag))/(z[max_loc] - z[min_loc]))
guess_intercept = np.mean(mag - (guess_slope * z))
p0 = [guess_slope, guess_intercept]

#functions to be given to curvefit for fitting
def line(x, slope, intercept):
	return (x * slope) + intercept

def quad(x, a, b, c):
	return a*(x**2) + (b * x) + c

# Fit the data with 3 functions above using curvefit 
popt, pcov = curve_fit(line, z, mag, sigma = zerr, p0 = p0)
print('**** Linear fit paramters ****')
print("slope = ", popt[0], "+/-", pcov[0,0]**0.5)
print("intercept = ", popt[1], "+/-", pcov[1,1]**0.5)

popt1, pcov1 = curve_fit(quad, z, mag, sigma = zerr)
print('**** Quadratic fit paramters ****')
print(" a = ", popt1[0], "+/-", pcov1[0,0]**0.5)
print(" b = ", popt1[1], "+/-", pcov1[1,1]**0.5)
print(" c = ", popt1[2], "+/-", pcov1[2,2]**0.5)

# broken line part
fit1, fit2 = np.where(z < 1.0), np.where(z > 1.0)
popt2, pcov2 = curve_fit(line, z[fit1], mag[fit1], sigma = zerr[fit1])
popt3, pcov3 = curve_fit(line, z[fit2], mag[fit2], sigma = zerr[fit2])
print('**** Broken line fit paramters ****')
print("slope1 = ", popt2[0], "+/-", pcov2[0,0]**0.5)
print("intercept1 = ", popt2[1], "+/-", pcov2[1,1]**0.5)
print("slope2 = ", popt3[0], "+/-", pcov3[0,0]**0.5)
print("intercept2 = ", popt3[1], "+/-", pcov3[1,1]**0.5)

# Make plot of data and overplot 3 different fits from above 
plt.errorbar(z, mag, xerr=zerr, fmt='o', ls ='none', color='gray')
plt.plot(z, line(z, popt[0], popt[1]), color='magenta')
plt.plot(z, quad(z, popt1[0], popt1[1], popt1[2]), color='blue', ls='', marker='.')
plt.plot(z, line(z, popt2[0], popt2[1]), color='green')
plt.plot(z, line(z,	popt3[0], popt3[1]), color='green')
plt.xlim(-0.5,max(z))
plt.ylim(min(mag), max(mag))
plt.title('R-band Magnitude as a Function of Redshift')
plt.xlabel('Redshift')
plt.ylabel('R-band Magnitude')
plt.show()