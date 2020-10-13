filename = "test_data.txt"
# change this if filename is different

import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

data = np.loadtxt(filename, usecols=(0, 1, 2, 3), skiprows=1, unpack=True)
x_data = data[0]
y_data = data[1]
x_error = data[2]
y_error = data[3]


def my_func(t, a, tau, T, phi):
    return a*np.exp(-t/tau)*np.cos(2*np.pi*t/T + phi)


popt, pcov = optimize.curve_fit(my_func, x_data, y_data)

print(pcov)
a = popt[0]
tau = popt[1]
T = popt[2]
phi = popt[3]
u_a = pcov[0, 0] ** 0.5
u_tau = pcov[1, 1] ** 0.5
u_T = pcov[2, 2] ** 0.5
u_phi = pcov[3, 3] ** 0.5


def fitfunction(t):
    return a*np.exp(-t/tau)*np.cos(2*np.pi*t/T+phi)


start = min(x_data)
stop = max(x_data)
xs = np.arange(start, stop, (stop-start)/1000)
curve = fitfunction(xs)

font = FontProperties()
font.set_family('serif')
font.set_name('Times New Roman')
font.set_style('italic')
font.set_size(14.0)

plt.rcParams["figure.figsize"] = (10, 6)

plt.errorbar(x_data, y_data, yerr=y_error, xerr=x_error, fmt=".")

plt.plot(xs, curve)

plt.xlabel("Time [in seconds]", fontproperties=font)
plt.ylabel('Angle of Amplitude [in Radians]', fontproperties=font)
plt.title("Fitted curve of the Amplitude of the pendulum over time", fontproperties=font)

plt.show()

print("A: ", a, "+/-", u_a)
print("tau:", tau, "+/-", u_tau)
print("T:", T, "+/-", u_T)
print("phi:", phi, "+/-", u_phi)

plt.rcParams['figure.figsize'] = (10, 3)

residual = y_data - fitfunction(x_data)

zeroliney = [0, 0]
zerolinex = [start, stop]

plt.errorbar(x_data, residual, yerr=y_error, xerr=x_error, fmt=".")

plt.plot(zerolinex, zeroliney)

plt.xlabel("Time [in seconds]", fontproperties=font)
plt.ylabel("Residuals of the amplitude", fontproperties=font)
plt.title("Residuals of the fit", fontproperties=font)

plt.show()
