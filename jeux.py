print("Bienvenue dans le jeu de pierre, feuille, ciseaux !")
print("")
import random
x=["pierre","feuille","ciseaux"]

while True:
    choix=input("choisissez entre pierre, feuille ou ciseaux : ") 
    if choix not in x:
        print("choix invalide, essayez à nouveau")
    else:
        break
ordinateur=random.choice(x)
print(f"l'ordinateur a choisi : {ordinateur}")
score_joueur=0
score_ordinateur=0
if choix==ordinateur:
    print("égalité")
    score_joueur+=1
    score_ordinateur+=1
elif (choix=="pierre" and ordinateur=="ciseaux") or (choix=="feuille" and ordinateur=="pierre") or (choix=="ciseaux" and ordinateur=="feuille"):
    print("vous avez gagné")
    score_joueur+=1
else:
    print("vous avez perdu")
    score_ordinateur+=1
print("score du joueur : ", score_joueur)
print("score de l'ordinateur : ", score_ordinateur)
if score_joueur > score_ordinateur:
    print("félicitations , vous avez gagné la partie !")
elif score_joueur < score_ordinateur:
    print("désolé , vous avez perdu la partie !")
else:
    print("la partie est nulle !")
