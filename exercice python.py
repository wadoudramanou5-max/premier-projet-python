'''print("")
print("Exercice 1")
print("")
n=int(input("entrer le nombre d'éléments : "))
print("")
liste=[]

for i in range(n):
    nombre=int(input("entrer un nombre : "))
    liste.append(nombre)
minimum=liste[0]
for nombre in liste:
    if minimum > nombre:
        minimum=nombre
print("")
print("la plus petite valeur est : ", minimum)
'''




'''print("")
print("Exercice 2")
print("")
tache=[]
n=int(input("entrer le nombre d'éléments de la liste : "))
print("ajouter des éléments à votre liste de taches : ")
for i in range(n):
            tach=(input("entrer la tache : "))
            tache.append(tach)
print(tache)
for i in range (1000):
 print("1 : ajouter des taches ")   
 print("2 : marquer comme terminer ")
 print("3 : supprimer taches")
 choix=(input("que souhaitez-vous faire? entrer 1,2 ou 3 : "))
 match choix:
    case "1":
          taches=input("entrer la tache a ajouter : ")
          tache.append(taches)
          print(tache)
        
    case "2":
        
            print("")
            indice=int(input("A quelle position se situe la tache à marqué comme terminer ? : "))
            print(tache[indice] , " est marqué comme Terminé")
    
    case "3":
        
         indice=int(input("A quelle position se trouve la tache à supprimer ? : "))
         tache.pop(indice)
         print(tache)
    
    case _ :
        print("commande invalide")'''







'''print("")
print("Exercice 3")
caractere=["a","b","n","%","&","1","2","6","e","#","@"]
print("")
f=int(input("entrer le nombre de caracteres que vous souhaitez donner  à votre mot de passe : "))
mot_de_passe=""
print("")
import random
for i in range(f):
    mot_de_passe+=random.choice(caractere)
print("votre mot de passe est : " , mot_de_passe)'''



'''print("")
print("Exercice 4")
print("")
nbrnote=int(input("entrer nombre de notes de l'éleve : "))
print("")
colnote=[]
somme=0

for i in range(nbrnote):
    note=float(input("entrer la note : "))
    colnote.append(note)
    max=colnote[0]
    min=colnote[0]
    if max<colnote[i]:
        max=colnote[i]
    elif min>colnote[i]:
        min=colnote[i]
    somme+=note
moy=somme/nbrnote
print("la moyenne de l'éleve est : ", moy)
print("")
print("la plus forte note est : ", max)
print("")
print("la plus faible note est : " ,min)
print("")
'''



