class Fraction:
    #costructeur de la classe Fraction
    def __init__(self, num, den):
        #on verifie que le denominateur est un entier strictement positif
        assert isinstance(den, int) and den > 0, "le dénominateur doit etre un entier strictement positif"
        #on simplifie la fraction en utilisant le PGCD
        pgcd = self.pgcd(num, den)
        self.num = num // pgcd #attribut privé num
        self.den = den // pgcd #attrivut privé den
        
    #methode pour calculer le PGCD de deux nombres
    def pgcd(self, a, b):
        #algorithme d'euclide
        while b != 0:
            a, b = b, a % b
        return a
    #methode speciale str
    def __str__(self):
        #on affiche le numerateur et le denominateur separes par un /
        #sauf si le denominateur vaut 1, auquel cas on affiche seulement le numerateur
        if self.den == 1:
            return str(self.num)
        else:
            return str(self.num)+"/" + str(self.den)
    #methode speciale eq
    def __eq__(self, other):
        #on compare les numerateurs et les denominateurs des deux fractions
        #si ils sont egaux, les fractons sont egales 
        return self.num ==other.num and self.den == other.den
#creation des instances F1,F2,F3 et F4
F1 = Fraction(3, 4)
F1 = Fraction(-8, 1)
F1 = Fraction(2, 3)
F1 = Fraction(21, 28)
#affichage des instances 
print(F1) # 3/4
print(F2) # -8
print(F3) # 2/3
print(F4) # 3/4
#comparateur des instances 
print(F1==F2) # False
print(F1==F3) # False
print(F1==F1) # True