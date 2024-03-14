#PROJET ALGO DES ETUDIANTS : NGALUBUKU NZONSANG NATHAN ET MAHAMAT KABUNDI MOUSSE 

from datetime import datetime

class Client:
    def __init__(self, nom, date_naissance, numero_telephone):
        self.nom = nom
        self.date_naissance = date_naissance
        self.numero_telephone = numero_telephone
        self.facture = 0

class GestionClients:
    def __init__(self):
        self.clients = []

    def ajouter_client(self, client):
        self.clients.append(client)

class ImportCDR:
    def __init__(self, file_path):
        self.cdr_data = []
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split('|')
                cdr_dict = {
                    'Identifiant': int(data[0]),
                    'Type call': int(data[1]),
                    'Date et heure': datetime.strptime(data[2], '%Y%m%d%H%M%S'),
                    'Appelant': data[3],
                    'Appelé': data[4],
                    'Durée': int(data[5]),
                    'Taxe': int(data[6]),
                    'TotalVolume': int(data[7])
                }
                self.cdr_data.append(cdr_dict)

class GenererFacture:
    def __init__(self, client, cdr_data):
        self.client = client
        self.cdr_data = cdr_data

    def generer_facture_client(self):
        for cdr in self.cdr_data:
            if cdr['Type call'] == 0:  # Appel
                if cdr['Appelant'][:3] == cdr['Appelé'][:3]:  # Même réseau
                    self.client.facture += cdr['Durée'] * 0.025
                else:
                    self.client.facture += cdr['Durée'] * 0.05
            elif cdr['Type call'] == 1:  # SMS
                if cdr['Appelant'][:3] == cdr['Appelé'][:3]:  # Même réseau
                    self.client.facture += 0.001
                else:
                    self.client.facture += 0.002
            elif cdr['Type call'] == 2:  # Internet
                self.client.facture += cdr['TotalVolume'] * 0.03

class Statistiques:
    def __init__(self, cdr_data):
        self.cdr_data = cdr_data

    def calculer_statistiques(self):
        nb_appels = sum(1 for cdr in self.cdr_data if cdr['Type call'] == 0)
        duree_appels = sum(cdr['Durée'] for cdr in self.cdr_data if cdr['Type call'] == 0)
        nb_sms = sum(1 for cdr in self.cdr_data if cdr['Type call'] == 1)
        volume_internet = sum(cdr['TotalVolume'] for cdr in self.cdr_data if cdr['Type call'] == 2)
        return nb_appels, duree_appels, nb_sms, volume_internet

# Test unitaire
print()
client_test = Client("John Nzema", "2023-01-11", "243818140560")
cdr_import = ImportCDR("C:/Users/Sophos/Desktop/cdr.txt")
generer_facture = GenererFacture(client_test, cdr_import.cdr_data)
generer_facture.generer_facture_client()
statistiques = Statistiques(cdr_import.cdr_data)
nb_appels, duree_appels, nb_sms, volume_internet = statistiques.calculer_statistiques()

print(f"Facture de {client_test.nom}: ${client_test.facture}")
print(f"Nombre d'appels: {nb_appels}, Durée totale des appels: {duree_appels} secondes")
print(f"Nombre de SMS: {nb_sms}")
print(f"Volume internet utilisé: {volume_internet} MegaByte")
print()
print()
client_test2 = Client("Nathan Ngalubuku", "2023-01-11", "243818140120")
cdr_import = ImportCDR("C:/Users/Sophos/Desktop/tp_algo.txt")
generer_facture = GenererFacture(client_test2, cdr_import.cdr_data)
generer_facture.generer_facture_client()
statistiques = Statistiques(cdr_import.cdr_data)
nb_appels, duree_appels, nb_sms, volume_internet = statistiques.calculer_statistiques()

print(f"Facture de {client_test2.nom}: ${client_test2.facture}")
print(f"Nombre d'appels: {nb_appels}, Durée totale des appels: {duree_appels} secondes")
print(f"Nombre de SMS: {nb_sms}")
print(f"Volume internet utilisé: {volume_internet} MegaByte")
print()