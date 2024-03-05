#[GROUPE DE : NGALUBUKU NZONSANG ET SHUKANYA OTSHINGA]
#[PROMOTION : L2 / LMD GENIE CIVIL]


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def systeme_masse_ressort_amortisseur(x, t, m, b, k, F):
    dxdt = np.zeros_like(x)
    dxdt[0] = x[1]
    dxdt[1] = (F(t) - b * x[1] - k * x[0]) / m
    return dxdt

# Paramètres du système
m = 15.0  # Masse en kg
frottement = 25.0  # Coefficient de frottement de l'amortisseur en Ns/m
raideur = 6000.0  # Constante de raideur du ressort en N/m
position_initiale = 0.05  # Position initiale en m
vitesse_initiale = 0.0  # Vitesse initiale en m/s

# Fonction pour la force extérieure F(t)
F0 = 120.0  # Amplitude de la force en N
w = 15.0  # Fréquence de la force en rad/s
def force_exterieure(t):
    return F0 * np.cos(w * t)  # deuxième cas (a) Force extérieure F(t) = F0*cos(wt)

# Intervalle de temps
temps_initial = 0.0
temps_final = 12.0  # Temps final
pas_de_temps = 0.02  # Pas de temps

# Vecteur d'état initial
etat_initial = np.array([position_initiale, vitesse_initiale])

# Résolution de l'équation différentielle pour le premier cas(a) 
temps_a = np.arange(temps_initial, temps_final, pas_de_temps)
etat_a = odeint(systeme_masse_ressort_amortisseur, etat_initial, temps_a, args=(masse, frottement, raideur, lambda t: 0.0))

# Résolution de l'équation différentielle pour le deuxième cas (b) Une force extérieure F(t) = F0*cos(wt)
temps_b = np.arange(temps_initial, temps_final, pas_de_temps)
etat_b = odeint(systeme_masse_ressort_amortisseur, etat_initial, temps_b, args=(masse, frottement, raideur, force_exterieure))

# Affichage de la réponse du système pour les deux cas
plt.figure(figsize=(10, 8))

# Cas a)
plt.subplot(3, 2, 1)
plt.plot(temps_a, etat_a[:, 0], 'r', label='Position (m)')
plt.plot(temps_a, etat_a[:, 1], 'b', label='Vitesse (m/s)')
plt.xlabel('Temps (s)')
plt.ylabel('Position, Vitesse')
plt.legend()
plt.title('Réponse du système pour le premier cas (a)')

# Cas b)
plt.subplot(3, 2, 2)
plt.plot(temps_b, etat_b[:, 0], 'g', label='Position (m)')
plt.plot(temps_b, etat_b[:, 1], 'y', label='Vitesse (m/s)')
plt.xlabel('Temps (s)')
plt.ylabel('Position, Vitesse')
plt.legend()
plt.title('Réponse du système pour le deuxième cas (b)')

# Calcul des énergies cinétique, potentielle et mécanique pour le cas a)
E_cinetique_a = 0.5 * masse * etat_a[:, 1]**2
E_potentielle_a = 0.5 * raideur * etat_a[:, 0]**2
E_mecanique_a = E_cinetique_a + E_potentielle_a

# Plot de l'énergie cinétique pour le cas a)
plt.subplot(3, 2, 3)
plt.plot(temps_a, E_cinetique_a, 'm', label='Energie cinétique')
plt.xlabel('Temps (s)')
plt.ylabel('Ec (J)')
plt.legend()
plt.title('Énergie cinétique pour le cas a)')

# Plot de l'énergie potentielle pour le cas a)
plt.subplot(3, 2, 4)
plt.plot(temps_a, E_potentielle_a, 'c', label='Energie potentielle')
plt.xlabel('Temps (s)')
plt.ylabel('Ep (J)')
plt.legend()
plt.title('Énergie potentielle pour le cas a)')

# Plot de l'énergie mécanique pour le cas a)
plt.subplot(3, 2, 5)
plt.plot(temps_a, E_mecanique_a, 'k', label='Energie mécanique')
plt.xlabel('Temps (s)')
plt.ylabel('Em (J)')
plt.legend()
plt.title('Énergie mécanique pour le cas a)')

plt.tight_layout()
plt.show()
