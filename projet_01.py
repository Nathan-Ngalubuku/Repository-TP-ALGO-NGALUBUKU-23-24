# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:17:11 2024

@author: NZONGBO DUNGUSE
        MBAYA MUTOKA
"""
import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import odeint

#parametres du systeme

masse = 10 #kg
raideur_k = 4000 #N/m
alpha = 20 #Ns/m
x_o = 0.01 # m
v_o = 0 # m/s
f_o = 100 #N
omega =  10 #rad/s

 #question a
 
#équation différentielle du syteme

def systeme(y,t):
    x, v = y
    dx_dt = v
    dv_dt = -(alpha / masse)* v - (raideur_k / masse) * x
    return [dx_dt, dv_dt]

#conditions initiales
y_o = [x_o, v_o]

#temps d'intégration 
temps = np.linspace(0, 10, 1000)

#resoudre l'équation diff
solution = odeint(systeme, y_o, temps)

#extarction des positions et les vitesses
x, v = solution.T

#plotter les oscillations avec force externe
plt.plot(temps, x)
plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.title('Oscillations libres du systeme Mécanique')
plt.show()

#Question b)
#définition de l'équation dif du systeme avec Force ext.
def systeme_forcee(y,t):
    x, v = y
    dx_dt = v
    dv_dt = -(alpha / masse)* v - (raideur_k / masse) * x + (f_o / masse) * np.cos(omega * t)
    return [dx_dt, dv_dt]

#conditions initiales
y_o = [x_o, v_o]

#temps d'intégration 
temps = np.linspace(0, 10, 1000)

#resoudre l'équation diff
solution_forcee = odeint(systeme_forcee, y_o, temps)

#position
x_forcee, v_forcee = solution_forcee.T

#plotter les oscillations
plt.plot(temps, x_forcee)
plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.title('Oscillations du systeme Mécanique avec force externe')
plt.show()

#question c)
#calcul des energies
e_cin = 0.5*masse*v**2
e_pot = 0.5*raideur_k*x**2

#calcul de l'énergie mécanique totale
e_mec = e_cin + e_pot

#plotter
plt.plot(temps, e_cin, label='Energie Cinétique')
plt.plot(temps, e_pot, label='Energie Potentielle')
plt.plot(temps, e_mec, label='Energie Mécanique')
plt.xlabel('Temps (s)')
plt.ylabel('Energie (J)')
plt.title('Energies du systeme Mécanique avec force externe')
plt.legend()
plt.show()

