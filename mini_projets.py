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

Name = ["Marc", "Matthieu"] 
Phonenumber = ["06 43 66 75 82", "07 60 65 57 31"]
repertoire = dict(zip(Name, Phonenumber))

# Mise à Jour du répertoire :        
def ecriture () :
    
    w = (input("saisir un nom : "))
    x = (input("saisir un numéro : "))
    Name.append(w)
    Phonenumber.append(x)
    repertoire = dict(zip(Name, Phonenumber))
  
    
    while (w != 0 ):
        w = int(input("saisir un nom (entrer 0 pour terminer) : "))
        if (w == 0) :
            break
        x = (input("saisir un numéro : "))
        Name.append(w)
        Phonenumber.append(x) 
        repertoire = dict(zip(Name, Phonenumber))
        
      
        
    print(repertoire)
    print("répertoire mis à jour")
    menu()   
        
                

# Recherche d'un particulier présent dans le répertoire      
def lecture(name) :
    for i in range (0,len(Name)) :
        if (Name[i] == name):
            print("Le numero associé à",name,"est :",repertoire.get(name))
        else :
            print("inconnu : ") 
    menu()


# Affichage du menu :

def menu ():
   
    print("Bienvenue dans le menu principal ! ")
    choix = int(input("veuillez choisir une action (0) (1) (2) : "))
    
    while (choix != 0 and choix != 1 and choix != 2) :
        print("Bienvenue dans le menu principal ! ")
        choix = int(input("veuillez choisir une action (0) (1) (2) : "))
        
    if (choix == 1):
        ecriture()
    
    if(choix == 0):
        print("fin de programme")
        return
        
    if (choix == 2) :
        choix2 = input("saisir un nom : ")
        lecture(choix2)

menu()