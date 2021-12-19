#Mini python

#0= quitter
#1=écrire dans le répertoire
#2=rechercher dans le répertoire
#Demander « Votre choix ?»
#Si c’est 0 : fin du programme
#Si c’est  1 : l’utilisateur écrit un nom
#Si c’est 0, revenir au menu
#Si c’est un nom, le programme devra lui demander de saisir le numéro correspondant
#Entrer un nouveau nom (ou 0 pour terminer)
#Si c’est 2 : l’utilisateur devra saisir un nom
#Si Nom recherché présent, il devra être affiché le numéro de téléphone correspondant
#Si Nom recherché absent, il devra être affiché « inconnu »
#Redirection vers le menu principal

#Fonction :
#_ Menu
#_ Lecture
#_ Écriture

repertoire = {"Marc" : "06 43 66 75 82" , 
             "Matthieu" : "07 60 65 57 31" }

# Mise à Jour du répertoire :        
def ecriture (w, x) :
    while (w != 0 ):
        w = (input("saisir un nom (entrer 0 pour terminer) : "))
        x = (input("saisir un numéro : "))
        repertoire["w"] = x
        
        if (w == 0) :
            for num in repertoire.values():
                print(num)
            for name in repertoire.keys():
                print(name)
            print("répertoire mis à jour")    
            menu()
            break
                

# Recherche d'un particulier présent dans le répertoire      
def lecture(name) :
    for name in repertoire.keys():
        if (bool (repertoire.has_key(name) ) == 1):
            print("Le numero recherché est : ", repertoire.get(name))
        else :
            print("inconnu : ") 


# Affichage du menu :

def menu () :
   
    while True :
        print("Bienvenue dans le menu principal ! ")
        choix = int(input("veuillez choisir une action (0) (1) (2) : "))
        
        if (choix == 1):
            choix2 = input("saisir un nom (entrer 0 pour terminer) : ")
            choix3 = input("saisir un numéro : ")
            ecriture(choix2, choix3)
            if(choix == 0):
                menu()
                break
                
        if (choix == 2) :
            choix4 = input("saisir un nom : ")
            lecture(choix4)
            menu()
            break
       
menu()