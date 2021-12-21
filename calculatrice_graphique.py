""""
----
789*
456-
123+
0./=
----

"""""

from tkinter import *

expression = " "

def appuyer(touche):
    if touche == "=":
        calculer()
        return
    global expression
    expression += str(touche)
    equation.set(expression)


def calculer():
    try:
        global expression
        total = str(eval(expression))
        
        equation.set(total)
        expression = total
    except :
        equation.set("erreur")
        expression = " "

def effacer():
    global expression 
    expression = " "
    equation.set(" ")

if __name__ == "__main__":
    
    fen = Tk()
    # couleur de fond
    fen.configure(background="#101419")
    # titre de l'interface
    fen.title("calculatrice")
    # taille de la fenêtre
    fen.geometry("225x385")
    # calcul entré par l'utilisateur
    equation = StringVar()
    # stockage du résultat
    resultat = Label(fen, bg="darkgreen", fg="#FFF", textvariable=equation, height = "2", width = 27)
    resultat.grid(columnspan=4)
    # boutons de la calculatrice
    boutons = [7,8,9,"*",4,5,6,"-",1,2,3,"+",0,".","/","="]
    ligne = 1
    colonne = 0
    
    for bouton in boutons:
        
        b = Label(fen, text = str(bouton), bg = "grey", fg = "#FFF", height = 4, width = 6)
        # rendre le texte interactif
        b.bind("<Button-1>",lambda element, bouton=bouton: appuyer(bouton))
        
        b.grid(row=ligne, column=colonne)
        colonne +=1
        if colonne == 4:
            colonne = 0
            ligne += 1
    
    b = Label(fen, text = "Effacer", bg = "darkred", fg = "#FFF", height = 4, width = 27)
    b.bind("<Button-1>",lambda element: effacer())
    b.grid(columnspan=4)
    fen.mainloop()