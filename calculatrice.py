print(" ==== MA CALCULATRICE ==== ")

# Demander les deux nombres
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

# Afficher les opérations possibles
print("\nChoisissez une opération :")
print("1. Addition (+)")
print("2. Soustraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choix = input("Votre choix (1, 2, 3 ou 4) : ")

# Effectuer le calcul
if choix == "1":
    resultat = a + b
    print("Résultat :", resultat)

elif choix == "2":
    resultat = a - b
    print("Résultat :", resultat)

elif choix == "3":
    resultat = a * b
    print("Résultat :", resultat)

elif choix == "4":
    if b != 0:
        resultat = a / b
        print("Résultat :", resultat)
    else:
        print("Erreur : division par zéro impossible.")

else:
    print("Choix invalide. Relancez le programme.")