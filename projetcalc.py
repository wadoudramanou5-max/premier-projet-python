def Addition(a,b):
    return a+b

def Soustraction(a,b):
    return a-b

def Multiplicaton(a,b):
    return a * b

def Division(a,b):
    if b==0:
        return "Erreur"
    else:
        return a / b    

def Exposant(a,b):
    return a**b

nbr1=float(input("entrer un nombre : "))
print("")
nbr2=float(input("entrer un autre nombre : "))
print("")
print("")
print("+: Addition \n -: Soustraction\n *: Multiplication \n /: Division \n ** : Exposant d'un nombre ")
choix=str(input("choisir opérateur + , -  , * , / ,  : "))

print("")

match choix:
    case "+":
        resultat=Addition(nbr1,nbr2)
        print (resultat)
    case "-":
        resultat=Soustraction(nbr1,nbr2)
        print(resultat)
    case "*":
        resultat=Multiplicaton(nbr1,nbr2)
        print(resultat)
    case "/":
        resultat=Division(nbr1,nbr2)
        print(resultat)
    case "^":
        print("le deuxieme nombre est considérer comme l'exposant dans ce cas")
        resultat=Exposant(nbr1,nbr2)
        print(resultat)
    case _:
        print("opérateur inconnu")



