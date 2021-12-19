print ("convertir les degrés fahrenheit en degrés celsius [1] ou les degrés celsius en degrés fahrenheit [2] ? ")

choix = input ("choisir le sens de la conversion : ")

# controle de la valeur entrée par l'utilisateur (A t-il compris comment fonctionne le programme ?)

while choix != "1" and choix != "2" :
    print ("convertir les degrés fahrenheit en degrés celsius [1] ou les degrés celsius en degrés fahrenheit [2] ? ")
    choix = input ("choisir le sens de la conversion : ")
    if choix == "1" or choix == "2":
        break
    else :continue

temp = "mauvaise température"

# controle de la valeur entrée par l'utilisateur (Dans quel sens veut-il convertir ?)

while type(temp) != float :
    temp = float(input ("saisir la température à convertir : "))
    
# conversion en degrés celsius    

if choix == "1" :
    print(temp,"degrés fahrenheit = ",  temp*1.8 + 32, "degrés celsius" )

# conversion en degrés fahrenheit

else :
    print(temp, "degrés celsius  = ", (temp-32)/1.8 , "degrés fahrenheit" )

# controle de la valeur entrée par l'utilisateur (veut-il continuer ou pas ?)

continuer = None
 
while type(continuer) != int :
    continuer = int(input ("voulez vous continuer ? oui [1] , non [2] : "))
    
while continuer != 1 and continuer != 2 :
    print("saisir 1 ou 2")
    continuer = int(input ("voulez vous continuer ? oui [1] , non [2] : "))
    
while continuer  == 1 :
    print ("convertir les degrés fahrenheit en degrés celsius [1] ou les degrés celsius en degrés fahrenheit [2] ? ")
    choix = input ("choisir le sens de la conversion : ")
    while choix != "1" and choix != "2" :
        print ("convertir les degrés fahrenheit en degrés celsius [1] ou les degrés celsius en degrés fahrenheit [2] ? ")
        choix = input ("choisir le sens de la conversion : ")
        if choix == "1" or choix == "2":
            break

    temp = "mauvaise température"
    while type(temp) != float :
        temp = float (input ("saisir la température à convertir : "))
        
    if choix == "1" :
        print(temp,"degrés fahrenheit = ",  temp*1.8 + 32, "degrés celsius" )
    else :
        print(temp, "degrés celsius  = ", (temp-32)/1.8 , "degrés fahrenheit" )
    continuer = int(input ("voulez vous continuer ? oui [1] , non [2] : "))
    if continuer != 1:break