import random

print("bienvenue dans le jeu Rock, Paper, scissors !!! ")
# choix de l'ordinateur
options = ["Rock", "Paper", "Scissors"]
# initialisation des variables
manche = 0
playerpoints = 0
computerpoints = 0

choix_player = None         
choix_computer = None

while manche < 3 : 
   
    choix_player = str(input("Veuillez choisir Rock (R), Paper (P) ou Scissors (S) : "))
    # controle de la valeur de la variable utilisée par le joueur 
    while (choix_player != "r" and choix_player != "R" and choix_player != "p" and choix_player != "P" and choix_player != "s" and choix_player != "S") :
        choix_player = str(input("Veuillez choisir Rock (R), Paper (P) ou Scissors (S) : "))    
    choix_computer = random.choice(options)  
    # conditions de victoire
    if (choix_computer == "Rock" and (choix_player == "p" or choix_player == "P")) or (choix_computer == "Paper" and (choix_player == "s" or choix_player == "S")) or (choix_computer == "Scissors" and (choix_player == "r" or choix_player == "R")) :
        playerpoints += 1
        print(" Vous gagnez Joueur : ",playerpoints, "Ordinateur  : ",computerpoints)
        choix_computer = random.choice(options)
    # conditions d'échec            
    elif (choix_computer == "Rock" and (choix_player == "s" or choix_player == "S")) or (choix_computer == "Paper" and (choix_player == "r" or choix_player == "R")) or (choix_computer == "Scissors" and (choix_player == "p" or choix_player == "P")) :
        computerpoints += 1
        print(" Vous perdez Joueur : ",playerpoints, "Ordinateur  : ",computerpoints)
        choix_computer = random.choice(options)
    # conditions d'égalité    
    elif (choix_computer == "Rock" and (choix_player == "r" or choix_player == "R")) or (choix_computer == "Paper" and (choix_player == "p" or choix_player == "P")) or (choix_computer == "Scissors" and (choix_player == "s" or choix_player == "S")) :
        print(" Egalité Joueur : ",playerpoints, "Ordinateur  : ",computerpoints)
        choix_computer = random.choice(options)
          
    manche += 1
    
    # affichage des résultats finaux    
if playerpoints > computerpoints :
    print("Fin de partie : Vous avez gagné ! " "Joueur : " ,playerpoints, "Ordinateur  : ",computerpoints) 
elif playerpoints < computerpoints :
    print("Fin de partie : Vous avez perdu ! " "Joueur : " ,playerpoints, "Ordinateur  : ",computerpoints) 
elif playerpoints == computerpoints :
    print("Fin de partie : Egalité parfaite ! " "Joueur : " ,playerpoints, "Ordinateur  : ",computerpoints)             