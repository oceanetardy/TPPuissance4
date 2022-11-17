from turtle import *
nb_pions_colonne=7*[0]
grille = [7*[0], 7*[0],7*[0],7*[0],7*[0],7*[0],7*[0]]
joueur=1

#Affichage de la grille
def affichage_grille():
    for i in range(6):
        print(grille[i])     
    print('\n 0  1  2  3  4  5  6')
    print('Numéro des colonnes')
    

def complet():
    complet=True
    for i in range(6):
        for j in range(7):
            if grille[i][j]==0:
                complet=False
    return complet
        
#Compte si des pions sont alignés                
def victoire():
    pions_alignes=0
    
#quand 4 pions alignés verticalement:
    for j in range(7):
        pion_jaune=0
        pion_rouge=0
        for i in range(6):
            if grille[i][j]==1:
                pion_jaune=pion_jaune+1
                pion_rouge=0
                if pion_jaune>=4:
                    pions_alignes=1
                    return pions_alignes
            elif grille[i][j]==2:
                pion_jaune=0
                pion_rouge=pion_rouge+1
                if pion_rouge>=4:
                    pions_alignes=2
                    return pions_alignes
            else:
                pion_jaune=0
                pion_rouge=0
                    
                                 
#quand 4 pions alignés horizontalement
                    
    for i in range(6):
        pion_jaune=0
        pion_rouge=0
        for j in range(7):
            if grille[i][j]==1:
                pion_jaune=pion_jaune+1
                pion_rouge=0
                if pion_jaune>=4:
                    pions_alignes=1
                    return pions_alignes
            elif grille[i][j]==2:
                pion_jaune=0
                pion_rouge=pion_rouge+1
                if pion_rouge>=4:
                    pions_alignes=2
                    return pions_alignes
            else:
                pion_jaune=0
                pion_rouge=0

#Lorsque 4 pions sont alignés sur les diagonales décroissantes                 
    if (grille[2][0]==1 and grille[3][1]==1 and grille[4][2]==1 and grille[5][3]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[2][0]==2 and grille[3][1]==2 and grille[4][2]==2 and grille[5][3]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
    if (grille[2][1]==1 and grille[3][2]==1 and grille[4][3]==1 and grille[5][4]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[2][1]==2 and grille[3][2]==2 and grille[4][3]==2 and grille[5][4]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
    if (grille[2][2]==1 and grille[3][3]==1 and grille[4][4]==1 and grille[5][5]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[2][2]==2 and grille[3][3]==2 and grille[4][4]==2 and grille[5][5]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
    if (grille[2][3]==1 and grille[3][4]==1 and grille[4][5]==1 and grille[5][6]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[2][3]==2 and grille[3][4]==2 and grille[4][5]==2 and grille[5][6]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
    if (grille[1][3]==1 and grille[2][4]==1 and grille[3][5]==1 and grille[4][6]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[1][3]==2 and grille[2][4]==2 and grille[3][5]==2 and grille[4][6]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
        
    if (grille[0][3]==1 and grille[1][4]==1 and grille[2][5]==1 and grille[3][6]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[0][3]==2 and grille[1][4]==2 and grille[2][5]==2 and grille[3][6]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
                    
    if (grille[0][2]==1 and grille[1][3]==1 and grille[2][4]==1 and grille[3][5]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[0][2]==2 and grille[1][3]==2 and grille[2][4]==2 and grille[3][5]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
             
    if (grille[1][1]==1 and grille[2][2]==1 and grille[3][3]==1 and grille[4][4]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[1][1]==2 and grille[2][2]==2 and grille[3][3]==2 and grille[4][4]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
        
    if (grille[1][2]==1 and grille[2][3]==1 and grille[3][4]==1 and grille[4][5]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[1][2]==2 and grille[2][3]==2 and grille[3][4]==2 and grille[4][5]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
    if (grille[0][1]==1 and grille[1][2]==1 and grille[2][3]==1 and grille[3][4]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[0][1]==2 and grille[1][2]==2 and grille[2][3]==2 and grille[3][4]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        

    if (grille[1][0]==1 and grille[2][1]==1 and grille[3][2]==1 and grille[4][3]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[1][0]==2 and grille[2][1]==2 and grille[3][2]==2 and grille[4][3]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
    if (grille[0][0]==1 and grille[1][1]==1 and grille[2][2]==1 and grille[3][3]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[0][0]==2 and grille[1][1]==2 and grille[2][2]==2 and grille[3][3]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
        
        
                      
##Lorsque 4 pions sont alignés sur les diagonales croissantes 
    if (grille[3][0]==1 and grille[2][1]==1 and grille[1][2]==1 and grille[0][3]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[3][0]==2 and grille[2][1]==2 and grille[1][2]==2 and grille[0][3]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
    if (grille[4][0]==1 and grille[3][1]==1 and grille[2][2]==1 and grille[1][3]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[4][0]==2 and grille[3][1]==2 and grille[2][2]==2 and grille[1][3]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
    if (grille[5][0]==1 and grille[4][1]==1 and grille[3][2]==1 and grille[2][3]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[5][0]==2 and grille[4][1]==2 and grille[3][2]==2 and grille[2][3]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
    if (grille[5][1]==1 and grille[4][2]==1 and grille[3][3]==1 and grille[2][4]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[5][1]==2 and grille[4][2]==2 and grille[3][3]==2 and grille[2][4]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
    if (grille[5][2]==1 and grille[4][3]==1 and grille[3][4]==1 and grille[2][5]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[5][2]==2 and grille[4][3]==2 and grille[3][4]==2 and grille[2][5]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
        
    if (grille[5][3]==1 and grille[4][4]==1 and grille[3][5]==1 and grille[2][6]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[5][3]==2 and grille[4][4]==2 and grille[3][5]==2 and grille[2][6]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
    if (grille[3][1]==1 and grille[2][2]==1 and grille[1][3]==1 and grille[0][4]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[3][1]==2 and grille[2][2]==2 and grille[1][3]==2 and grille[0][4]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
    if (grille[3][2]==1 and grille[2][3]==1 and grille[1][4]==1 and grille[0][5]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[3][2]==2 and grille[2][3]==2 and grille[1][4]==2 and grille[0][5]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
    if (grille[3][3]==1 and grille[2][4]==1 and grille[1][5]==1 and grille[0][6]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[3][3]==2 and grille[2][4]==2 and grille[1][5]==2 and grille[0][6]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
    if (grille[4][3]==1 and grille[3][4]==1 and grille[2][5]==1 and grille[1][6]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[4][3]==2 and grille[3][4]==2 and grille[2][5]==2 and grille[1][6]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
    if (grille[4][1]==1 and grille[3][2]==1 and grille[2][3]==1 and grille[1][4]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[4][1]==2 and grille[3][2]==2 and grille[2][3]==2 and grille[1][4]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
        
    if (grille[4][2]==1 and grille[3][3]==1 and grille[2][4]==1 and grille[1][5]==1):
        pion_jaune=4
        pion_rouge=0
        if pion_jaune>=4:
            pions_alignes=1
            return pions_alignes
    if (grille[4][2]==2 and grille[3][3]==2 and grille[2][4]==2 and grille[1][5]==2):
        pion_jaune=0
        pion_rouge=4
        if pion_rouge>=4:
            pions_alignes=2
            return pions_alignes
        
       
        
#Teste si le chiffre saisi par le joueur est correct                        
def testchiffre(joueur):
    if joueur==1:
        couleur_joueur='JAUNE'
    else:
        couleur_joueur='ROUGE'
    colonne_correcte=False
    while not colonne_correcte:
        colonne=input("%s : Dans quelle colonne voulez-vous mettre votre pion? :" % couleur_joueur)
# Teste si la chaine saise est un entier :
        if not colonne.isdigit():
            print("ERREUR: Vous devez saisir un nombre entier.")
# Teste si la valeur numérique est comprise entre 0 et 6 :
        elif int(colonne)<0 or int(colonne)>6:
            print("ERREUR: La colonne saisie n'est pas valide. Elle doit être comprise entre 0 et 6.")
        else:
            colonne_correcte=True
    return int(colonne)

#Fonction pour joueur en prenant en compte le joueur
def jouer(joueur):
    if joueur==1:
        couleur_joueur='JAUNE'
    else:
        couleur_joueur='rouge'
    colonne=testchiffre(joueur)
    while nb_pions_colonne[colonne]==6:
        print('COLONNE PLEINE : Jouez dans une autre colonne car la colonne %d est pleine' % (colonne))
        colonne=testchiffre(joueur)
    grille[5-nb_pions_colonne[colonne]][colonne]=joueur
#Dessine le pion sur la grille graphique :
    dessiner_pion(colonne,nb_pions_colonne[colonne],couleur_joueur,joueur)
    nb_pions_colonne[colonne]+=1
    print('\nLe joueur %s a mit son pion dans la colonne %d ' % (couleur_joueur,colonne))
    
#Dessine la grille dans turtle    
def dessiner_grille():
    up()
    goto(x_base,y_base)
    down()
# traits horizontaux :
    for i in range(8):
        forward(7*largeur)
        up()
        goto(x_base,y_base+i*largeur)
        down()
# traits verticaux :
    up()
    goto(x_base,y_base)
    setheading(90)
    down()
    for i in range(9):
        forward(6*largeur)
        up()
        goto(x_base+i*largeur,y_base)
        down()
# affiche le numéro des colonnes sous la grille :
    for i in range(7):
        up()
        goto(x_base+i*largeur+largeur//2,y_base-largeur//2)
        down()
        write(str(i))
        
#Dessine le pion dans turtle
def dessiner_pion(x,y,couleur_joueur,joueur):
    up()
    goto(x_base+(x+1)*largeur-largeur//14,y_base+(y+1)*largeur-largeur//1.9)
    down()
    couleur_joueur=joueur
    if couleur_joueur==1:
# pion jaune si couleur=1 :
        color('yellow')
    else:
# pion rouge si couleur=2 :
        color('red')
    begin_fill()
    width(2)
    circle(largeur/2.35)
    end_fill()
    



#PROGRAMME
#Dessine la grille dans turtle
largeur=95.5
x_base=-350
y_base=-315
speed(0)
pencolor("blue")
setup(1000,800)
bgpic("puissance.png")

width(0)
hideturtle()
dessiner_grille()


print('Le joueur 1 est le joueur JAUNE. Le joueur 2 est le joueur ROUGE. JAUNE commence.')
print('Jouez!!!:')
gagnant=0

while not complet() or gagnant==0 :
    affichage_grille()
    jouer(joueur)
    joueur=3-joueur
    gagnant=victoire()
    if gagnant==1:
        print('Le joueur JAUNE a gagné')
        affichage_grille()
        break
    elif gagnant==2:
        print('Le joueur ROUGE a gagné')
        affichage_grille()
        break

affichage_grille()
if complet():
    print('Match null : La grille est pleine')
    
    

done()
