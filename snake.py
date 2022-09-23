from fltk import *
from time import sleep
from random import randint
import sys  #importe une commande pour fermer le programme



def case_vers_pixel(case):
    """
	Fonction recevant les coordonnées d'une case du plateau sous la 
	forme d'un couple d'entiers (id_colonne, id_ligne) et renvoyant les 
	coordonnées du pixel se trouvant au centre de cette case. Ce calcul 
	prend en compte la taille de chaque case, donnée par la variable 
	globale taille_case.
    """
    i, j = case
    return (i + .5) * taille_case, (j + .5) * taille_case

########################fonctions Pommmes #########################################
def affiche_pommes(pommes):
    """ cette fonction permet uniquement de caracteriser l'affichage
        d'une pomme c'est a dire sous quelle forme elle va apparaitre
        :param pommes: list"""

    
    for pomme in pommes:
        x, y = case_vers_pixel(pomme)
        cercle(x, y, taille_case/2,
               couleur='darkred', remplissage='red')
        rectangle(x-2, y-taille_case*.4, x+2, y-taille_case*.7,
                  couleur='darkblue', remplissage='darkgreen')

        

def poser_pommes():
    """ Fonction qui pose les pommes aleatoirement sur les coordonées du plateau
        tout en retirant les coordonnées du corps du serpent.
        Cette fonction est appelee lorsque le serpent mange une pomme pour en poser
        une autre (voir dans la fonction new_position_serpent) ainsi il n'y
        aura jamais deux pommes simultanément
        """
    
    while jouer:
        new_pommes=(randint(0,39),randint(0,29))
        if new_pommes not in pommes and new_pommes not in serpent:
            pommes.append(new_pommes)
            return None


 ################################serpent deplacements fonction######################      
def affiche_serpent(serpent):
    """
        Cette focntion va caracteriser toutes les boules du serpent
        :param serpent: list
        """

    for taille in range (len(serpent)):
        x, y = case_vers_pixel(serpent[taille])  

        cercle(x, y, taille_case/2 + 1,
               couleur='darkgreen', remplissage='blue')

        

def new_position_serpent(serpent,direction):
    """
        cette fonction est la plus importante, elle va tout d'abord
        permettre de delimiter le terrain, si  mode_pacman=False alors
        lorsque la tete du serpent sortira du plateau la fonction va renvoyer False,
        cepandant si mode_pacmman=True alors lorsque le serpent sortira d'un coté
        du plateau il apparaitra dans le coté opposé.
        A chaque fois que la tete du serpent se deplace on suprime la queue du
        serpent et on ajoute la tete aux nouvelles coordonnées sauf si la tete du
        serpent se retrouve sur une pomme alors on ne suprime pas la queue et
        on ajoute tout de meme la tete faisant ainsi grandir le serpent. De meme
        la pomme est suprimee et une autre pomme est posee grace a la fonction poser_pommes().
        Si la tete du serpent se retrouve dans une  coordonnée d'un element du serpent
        alors le programme renvoie False en effet le serpent s'est mordu la queue.
        :param serpent: list
        :param direction: tupple

        """
    
    abs_tete,ordo_tete=serpent[-1]
    ordo_newtete=ordo_tete+direction[1]
    abs_newtete=abs_tete+direction[0]
    

    if mode_pacman==True:  #reenvoie le serpent a l'oppose lorsqu'il passe la limite du plateau 
        if abs_newtete<0:
            abs_newtete=40
        elif abs_newtete>39:
            abs_newtete=0
        if ordo_newtete<0:
            ordo_newtete=30
        elif ordo_newtete>29:
            ordo_newtete=0
        

    if mode_pacman==False and (abs_newtete <0 or abs_newtete >39 or ordo_newtete<0 or ordo_newtete>29):#sortit de la map
        return False

    if (abs_newtete,ordo_newtete)in pommes: #mange une pomme:le serpent grandit et une autre pomme apparait
        poser_pommes()
        pommes.remove((abs_newtete,ordo_newtete))
        
        
    
    elif (abs_newtete,ordo_newtete) in serpent and len(serpent)>1:#serpent mord son corps
        return False
        
    else: 
        serpent.pop(0)
        
    serpent.append((abs_newtete,ordo_newtete))#rajoute la tete
    
    return True
    

def change_direction(direction, touche):
    """
        fonction qui change les coordonnées dans laquel la tete
        du serpent se dirige grace aux fleches directionnelles et
        la tete ne peux pas aller sur le corps du serpent (pas de marche arriere).
        :param direction: tupple
        :param touche: class 'function
        '"""
   
    if touche == 'Up' and direction!=(0,1):# flèche haut pressée
        
        return (0, -1)
    elif touche == 'Down' and direction!=(0,-1):# flèche bas pressée
        return (0,1)
    elif touche== 'Right' and direction!=(-1,0):# flèche droite pressée
        return (1,0)
    elif touche== 'Left' and direction!=(1,0):# flèche gauche pressée
        return(-1,0)
    else:
        
        return direction
#########################################programme principal###############################################################


    
# dimensions du jeu
taille_case = 15
largeur_plateau = 40  # en nombre de cases
hauteur_plateau = 30  # en nombre de cases
choix=True
# programme principal
if __name__ == "__main__":
    while choix:
        cree_fenetre(taille_case * largeur_plateau,
                 taille_case * hauteur_plateau)
        rectangle
        image(110, 83, 'complement/serpent.gif', ancrage='center')#affiche le petit serpent
        texte(310,50,"Choisissez le mode de jeux",couleur='black',ancrage='center')

        Bouton_basique = rectangle(50,80,550,170,couleur='green',remplissage='green')
        texte(310, 130, "Snake basique", couleur="red", ancrage='center')
        coordonne_basique=[50,80,550,170]


        Bouton_pacman = rectangle(50,190,550,280,couleur='yellow',remplissage='yellow')
        texte(310, 240, "Snake PAC-MAN", couleur="red", ancrage='center')
        coordonne_pacman=[50,190,550,280]

        Bouton_accelerer= rectangle(50,300,550,390,couleur='red',remplissage='red')
        texte(310, 350, "Snake qui accélère", couleur="green", ancrage='center')
        coordonne_accelerer=[50,300,550,390]

        Bouton_quitter= rectangle(450,400,550,440, couleur='black',remplissage='black')
        texte(500, 420, "Quitter", couleur="white", ancrage='center')
        coordonne_quitter=[450,400,550,440]


        Bouton_bientot= rectangle(50,400,300,440, couleur='black',remplissage='black')
        texte_bientot=texte(175, 420, "Bientot Joueur vs Ordi", couleur="white", ancrage='center',taille=18)
        
        Bouton_rapport= rectangle(310,400,440,440, couleur='black',remplissage='black')
        texte_rapport=texte(375,420,"Rapport",couleur='white',ancrage='center',taille=18)
        coordonne_rapport=[310,400,440,440]
        
        while True:#boucle pour le menu : qui permet de choisir le mode de jeu en renvoyant les differentes valeurs aux variables mode_acclerer et mode_pacman si les deux valent False alors le programme lance le snake basique

            clique = attend_clic_gauche()
            if (clique[0] >= coordonne_basique[0] and clique[0] <=coordonne_basique[2]) and (clique[1] >= coordonne_basique[1] and clique[1] <=coordonne_basique[3]) :#snake basique
                efface_tout()
                mode_pacman=False
                mode_accelerer=False 
                break
            if (clique[0]>=coordonne_pacman[0] and clique[0] <=coordonne_pacman[2]) and (clique[1] >= coordonne_pacman[1] and clique[1] <=coordonne_pacman[3]) :#snake pacman
                efface_tout()
                mode_pacman=True
                mode_accelerer=False
                break
            if (clique[0]>=coordonne_accelerer[0] and clique[0] <=coordonne_accelerer[2]) and (clique[1] >= coordonne_accelerer[1] and clique[1] <=coordonne_accelerer[3]) :#snake accelerer
                efface_tout()
                mode_pacman=False
                mode_accelerer=True
                break
            if (clique[0]>=coordonne_quitter[0] and clique[0] <=coordonne_quitter[2]) and (clique[1] >= coordonne_quitter[1] and clique[1] <=coordonne_quitter[3]) :#touche pour quitter le jeux
                ferme_fenetre()
                sys.exit()

            if (clique[0]>=coordonne_rapport[0] and clique[0] <=coordonne_rapport[2]) and (clique[1] >= coordonne_rapport[1] and clique[1] <=coordonne_rapport[3]) :#touche pour afficher le rapport
                efface(Bouton_rapport)
                efface(Bouton_bientot)
                efface(texte_rapport)
                efface(texte_bientot)
                rectangle(50,400,440,440,couleur='purple',remplissage='purple')
                texte(50,410, " Lisez sur l'invite de commande le rapport",couleur='black',taille=15)
                
                Bouton_quitter=rectangle(450,400,550,440, couleur='black',remplissage='black')
                texte(500, 420, "Quitter", couleur="white", ancrage='center')
                fic=open("complement/rapportSnakesansé.txt","r")#ouvre le document rapport.txt uniquement pour la lecture
                print(fic.read())#affiche le document
                
        # initialisation du jeu
        framerate = 10   # taux de rafraîchissement du jeu en images/s
        direction = (0, 0)  # direction initiale du serpent
        pommes = [] # liste des coordonnées des cases contenant des pommes
        serpent = [(0, 0)] # liste des coordonnées de cases adjacentes décrivant le serpent
        rectangle(0,0,600,450,couleur='SpringGreen2',remplissage='SpringGreen2')
        texte(300,200,"Appuyer pour Jouer",couleur='black',ancrage='center')
        
        mise_a_jour()
        attend_ev()
        
        
        
        
        # boucle principale
        
        jouer = True
        cmpt_pomme=1
        cmpt_accelerer=0
        while jouer:
            #ajoute une pomme lorsque la partie se lance
            
            if cmpt_pomme==1:
                 poser_pommes()
                 cmpt_pomme=0
            # affichage 
            
            efface_tout()
            rectangle(0,0,600,450,couleur='SpringGreen2',remplissage='SpringGreen2')#couleur fond
            score=len(serpent)-1
            texte(550, 10,f"Score={score}", taille = 15, couleur = 'red', ancrage='center')#affichage score
            affiche_pommes(pommes) 
            affiche_serpent(serpent)  
            mise_a_jour()
            
           
            
            
            # gestion des événements
           
           
              
            ev = donne_ev()
            ty = type_ev(ev)
            if ty == 'Quitte':
                jouer = False
            
            elif ty == 'Touche':
                
                
                direction = change_direction(direction, touche(ev))
                
                
            
            if   new_position_serpent(serpent,direction)==False: #si le serpent est sortit du terrain ou a mange sa queue
                
                break

            #si dans le menu le clique est réaliser sur le bouton accelerer, alors mode_accelerer=True
            
            if mode_accelerer==True:
                cmpt_accelerer+=1/2
                if framerate<20:#si la vitesse est inferieure a 20 on augmente la vitesse lorsque le cmpt_accelerer est divisible par 5 
                    if cmpt_accelerer%5==0:
                        framerate+=1/10
                        
                                          
                else:#si la vitesse est superieure ou egale a 20 on augmente la vitesse lorsque le cmpt_accelerer est divisible par 20
                    if cmpt_accelerer%20==0:
                        framerate+=1/100
                
                        
                        
                        
                        
            

            # attente avant rafraîchissement
            sleep(1/framerate)    
        image(300, 200, 'complement/gameover.gif', ancrage='center')#affcihe l'image game over 
        texte(300,250,f" Score:{score}",couleur='white',ancrage='center')#affiche le score sur l'image
        texte(300,300,"Cliquez pour rejouer",couleur='white',ancrage='center') 
        mise_a_jour()
       
        attend_ev()
            
            
            

        # fermeture et sortie
        ferme_fenetre()

