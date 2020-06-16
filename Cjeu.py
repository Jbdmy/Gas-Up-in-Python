# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:56:37 2018

@author: Demay
"""

#import os
from random import choice 
from ccase import *
from time import *
import  pickle

global liste_position_de_recherche
global temoin
liste_position_de_recherche=[]


#====================================================================================================================================
#====================================================================================================================================
class Grille : 
            
    #--------------------------------------------------------------------------------------------------------------------------------                    
    #--------------------------------------------------------------------------------------------------------------------------------            
    def __init__(self, ligne=None, colonne=None,score=None):
        self.grille = {}
        self.ligne=ligne
        self.colonne=colonne
        self.score= score
        self.timee = 0
            
    #--------------------------------------------------------------------------------------------------------------------------------                    
    #--------------------------------------------------------------------------------------------------------------------------------                    
    def set_par(self, lignee , colonnee):
        self.ligne=  lignee
        self.colonne=  colonnee
    #--------------------------------------------------------------------------------------------------------------------------------    
    def reset(self):
        
        self.grille={}
        self.ligne=None
        self.colonne= None
        self.score=None
        
        
    #--------------------------------------------------------------------------------------------------------------------------------        
    """ cette fonction attribue chaque combinaison: ligne/ colonne: une case """
    def shuffle(self):
        list_case = [6,18,12,24,10,20,30,26,22,14,28]
        #global llligne
        #global cccolonne
        
        #onparcours tout le dictionnaire 
        for j in range(0,self.ligne): 
            for i in range(0,self.colonne): 
                a=0
                #on tire au hasard une valeur qui peut étre  associé a une case
                a  = choice(list_case) 
                #on associe, à la clef du dictionnaire représentatif de la position, une case de valeur a 
                self.grille[j,i]=case(a , j , i)
    #--------------------------------------------------------------------------------------------------------------------------------                    
    temoin = 0
    liste_position_de_recherche = []
    #--------------------------------------------------------------------------------------------------------------------------------
    """elle place rech_ligne2 sur les lignes de la première colonne  """
    #retourne la liste des début de ligne 
    #retourne la liste des elements de la ligne
    def rech_ligne3(self):
    
        global temoin
        global liste_position_de_recherche
        temoin=0
        ligne = []
        debut_gaz = [] 
        pau = 0
    
        i=0
        #on place recherche_ligne2"""
        while i <self.ligne:  
            #on l'execute"""     
            Grille.rech_ligne2(self, i)
            #le témoin nous indique si une ligne a ete trouvé(>=1) ou pas (0)"""               
            if temoin == 0:
                # on remplit la liste des cases qui forment un début de ligne avec les nouvelles cases visités par rech_ligne2""" 
                for elts in liste_position_de_recherche:
                    if elts in debut_gaz:
                        pau += 1
                    else : 
                        debut_gaz.append(elts)
                #on vide la liste des positions de recherche avant de changer de ligne        
                liste_position_de_recherche = []            
                i += 1
        
            else:
            #on remplit la liste des cases qui forment une ligne avec les nouvelles cases visités par rech_ligne2"""
                for illtt in liste_position_de_recherche:
                    if illtt in ligne:
                        pau+=1
                    else:
                        ligne.append(illtt)

                liste_position_de_recherche = []
                temoin = 0
            
                i+=1            
        #retourne un tuple formé de 2 listes qui contiennent les coordonnées des cases visités """        
        return( ligne, debut_gaz)
            
    #--------------------------------------------------------------------------------------------------------------------------------            
    """ Tête chercheuse, se ballade sur les cases autorisées et les enregistres, si elle arrive a la dernière colonne et trouve "une sortie" elle incrémente le témoin"""
    # enregistre les cases sur lesquelles elle est autorisée a aller
    #évite les valeurs en dehors de la grille
    #évite de retourner vers "son père" ie la case d'ou elle vient via val mais avec la liste, cela semble inutile (héritage des versions précéddentes de la fonnction)
    def rech_ligne2(self, ligne=None , collonne=None , val=None):
        
        pop = 0
        
    
        global liste_position_de_recherche
        #rech_ligne3 ne donne que la ligne ainsi il y a des cas ou la fonction definie l'autre coordonnée toute seule"""    
        if ligne == None:
            ligne =0
        if collonne == None:
            collonne = 0
        if val == None:
            val =9999
  
        #si on est sur la 1er case de la ligne et qu' il n'y a pas "d'entrée" on s'aréte là
        #on sait que c'est la 1er case visité car val ==0
        
        if val == 9999 and self.grille[ligne , collonne].list[1][3] == 0:
            return
        #si non on enregistre la case dans la liste des cases visités
        liste_position_de_recherche.append( (ligne , collonne))
    
    
        #si on est sur la dernière colonne et qu'il y a une sortie (le gaz est relié) le témoin devient != 0
        if collonne == self.colonne-1 and self.grille[ligne , collonne].list[1][1] != 0 :
            global temoin 
            temoin += 1
            #si on reste dans la grille en allant voir la case de droite (colonne suivante )
        if collonne+1 <= self.colonne-1 :
            #si on a une sortie vers cette case et que la case d'a coté a une entrée et que ce n'est pas la case d'ou elle vient 
            if self.grille[ligne , collonne].list[1][1] != 0 and self.grille[ligne , collonne].list[1][1] != val and self.grille[ligne , collonne+1].list[1][3] !=0  :
                #si on est deja passé sur cette case(elle est enregistré dans les cases visités), il ne se passe rien
                if (ligne , collonne+1) in liste_position_de_recherche:
                    pop+=1
                #si non on va dessus 
                else :
                    Grille.rech_ligne2( self, ligne , collonne+1 , self.grille[ligne , collonne+1].list[1][3] )
        """ on fait de même pour toutes les le dessus/ligne+1, dessous/ligne-1, gauche/colonne-1"""             
        if collonne-1 >=0:      
            if self.grille[ligne , collonne].list[1][3] != 0 and self.grille[ligne , collonne].list[1][3] != val and self.grille[ligne , collonne-1].list[1][1] !=0  :
                if (ligne , collonne-1) in liste_position_de_recherche:
                    pop+=1
                else:
                    Grille.rech_ligne2(self,  ligne , collonne-1 , self.grille[ligne , collonne-1].list[1][1] )
                
                   
        if ligne+1 <= self.ligne-1:
            if self.grille[ligne , collonne].list[1][2] != 0 and self.grille[ligne , collonne].list[1][2] != val and self.grille[ligne+1 , collonne].list[1][0] !=0 :
                if (ligne+1 , collonne) in liste_position_de_recherche:
                    pop+=1
                else:
                    Grille.rech_ligne2( self, ligne+1 , collonne , self.grille[ligne+1 , collonne].list[1][0] )
                
        if ligne-1 >=0 :        
            if self.grille[ligne , collonne].list[1][0] != 0 and self.grille[ligne , collonne].list[1][0] != val and self.grille[ligne-1 , collonne].list[1][2] !=0 :
                if(ligne-1 , collonne) in liste_position_de_recherche:
                    pop+=1
                else:
                    Grille.rech_ligne2( self, ligne-1 , collonne , self.grille[ligne-1 , collonne].list[1][2] )

        else:
            return
    
    
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------
    # Fonctions apres rech_ligne, descente cases & remplissage
    #-----------------------------------------------------------------------------------------------------------------------------
    """met les valeurs des cases qui forment une ligne complète a 0 pour pouvoir les supprimer """
    """prend en entré la liste des position des case qui forment une lignne"""
    def dellca(self):
        positions = Grille.rech_ligne3(self)
    # on incrémente les score du nombre de case qui forment la ligne"""
    
        """ score ici 
        #global score
        score += int(len(positions[0]) )"""
        self.score  += int(len(positions[0]) )
    # on appel la methode del des cases qui met leur valeur a 0""" 
        for elt in positions[0]:
            self.grille[elt[0],elt[1]].dell()
            
            
    #-----------------------------------------------------------------------------------------------------------------------------    
    """fonction chargé dde faire desccenndre les cases; apres dellca"""
    def fall(self):
    # on se place dans le coin en bas a droite"""
        c = self.colonne-1 
        while c >= 0 :
            #on remonte(les lignes) sur la colonne"""
            l = self.ligne-1 
            while l > 0:
                if self.grille[ l , c ].list[0]==0 :
                    up = l 
                    #si on est sur une case vide (valeur=0), on la remplit avec la 1er case pleine """
                    while up >= 0 :
                        if up == 0 and self.grille[up , c].list[0]==0 :
                            #on sort de la boucle si  on est arrivé en haut"""
                            l-=1
                            up -= (2+self.ligne)
                        elif self.grille[up , c].list[0]==0:
                            #si la case du dessus, a l'indice up est vide, on continue de monter"""
                            up -= 1
                        elif self.grille[up , c].list[0]!= 0:
                            #si elle est pleine on remplit la case avec la valeur de la case du  dessus et celle-ci devient vide"""
                            self.grille[l , c].list[0] = self.grille [up , c].list[0]
                            self.grille[l , c].list[1] = self.grille [up , c].list[1]
                        
                            self.grille[up , c].dell()
                            up -= (2+3)
                            l -=1
                else:
                    # on change de colonne"""
                    l -=1

            c-=1
    #-----------------------------------------------------------------------------------------------------------------------------
    """ fonction qui donne une valeur aux cases qui ont été mise a 0, aprés fall et delca """                      
    def remplissage(self):
        list_case = [6,18,12,24,10,20,30,26,22,14,28]
        # on scan tout le dictionnaire/grille a la recherche de cases à: 0"""
        for j in range(0,self.ligne):
            for i in range(0,self.colonne):
                #si la valeur de la case est a 0 alors on tire au hasard une valeur dans la liste des valeurs et on remplit la grille avec une nouvelle case"""
                if self.grille[j,i].list[0] == 0:
                    a=0
                    a  = choice(list_case)
                    self.grille[j,i]=case(a , j , i)
    

    #-----------------------------------------------------------------------------------------------------------------------------
    """ fonction chargé de modifier la couleur des cases qui  doivent etre "vert" dont la valeur associe est: 3 """
    def color_vert(self):
        positions = Grille.rech_ligne3(self)
        #On récupère la liste des cases qui font une ligne (donné par rech_ligne3 qui sait les philtrer) """
        for elt in positions[0]:
            self.grille[elt[0],elt[1]].color(3)
    #-----------------------------------------------------------------------------------------------------------------------------    
    """ fonction chargé de modifier la couleur des cases qui  doivent etre "bleu" dont la valeur associe est: 2 """        
    def color_bleu(self):
        positions = Grille.rech_ligne3(self)
        #On récupère la liste des cases qui font un début de ligne (donné par rech_ligne3 qui sait les philtrer) """    
        for elt in positions[1]:
            self.grille[elt[0],elt[1]].color(2)
    #-----------------------------------------------------------------------------------------------------------------------------    
    """ fonction qui definit la couleur de toutes les cases comme "rouge" dont la valeur associe est: 1 """        
    def color_rouge(self):    
        for ellltt in self.grille :        
            self.grille[ellltt].color(1)
            
    #--------------------------------------------------------------------------------------------------------------------------------                       
    def color_all(self):
        self.color_rouge()
        self.color_bleu()
        self.color_vert()
    #--------------------------------------------------------------------------------------------------------------------------------            
    def main_func(self):
        self.dellca()
        self.fall()
        self.remplissage()
    #--------------------------------------------------------------------------------------------------------------------------------            
    def start_chrono(self):
        a=time()
        a=int(a)        
        self.timee= a
    #--------------------------------------------------------------------------------------------------------------------------------            
    def chrono(self):
        b= time()
        b=int(b)
        
        temp = b
        temp2 = self.timee
        
        temp3 = 60-(temp-temp2)
        return temp3
    #--------------------------------------------------------------------------------------------------------------------------------            
    def recherchejoueur(nom) :
        #on utilise une methode qui ferme le fichier apres utilisation"""
        with open('data/player' , "rb") as fichier:
            #on copie le contenu du fichier (un dictionnaire) dans la variable player"""
            player = pickle.Unpickler(fichier).load()
    
        #on cherche le joueur dans le dictionnaire "player" qu'on a recuperé"""
        tem =0
        for cle in player :	
            # si il y est, c'est tres bien, il ne se passe rien 
            if cle == nom :
                tem=1
			
        if tem == 0:
        #si non on l'ajoute avec un score nul"""
            player[nom]=0
            #retourne une liste avec le pseudo, le dictionnaire des joueurs/scores , et le meilleur score du jeu"""			
        return(nom,  player , player[nom])
    #------------------------------------------------------------------------------------------------------------------------------
    """fonction permettant d'enregistrer un joueur avec son meilleur score"""
    """ en realité elle enregistre tout le "nouveau" dictionnaire et "l'ancien " est ecrasé"""
    def save_joueur(tab):
        player = tab
        #on utilise une methode qui ferme le fichier apres utilisation""" 
        with open('data/player' , "wb") as fichier:
            pickle.Pickler(fichier).dump(player)

    #================================================================================================================================
    #================== fonctions permettant le jeu sans interface ==================================================================
    #================================================================================================================================            
    def debut(self):
        ligne=input("Quelle nombre de ligne voulez-vous?")
        colonne = input("quelle nombre de colonne voulez-vous?")
        ligne=int(ligne)
        colonne = int(colonne)
        self.set_par(ligne , colonne)
        self.shuffle()
        self.start_chrono()
        self.score=0
    
    def aff(self):
        print("Grille:")
        for j in range(0,self.ligne):
            a=[]
            for i in range(0,self.colonne):
                a.append(self.grille[j,i].list)
            print(a)
            
        print("Positions")
        for j in range(0,self.ligne):
            a=[]
            for i in range(0,self.colonne):
                a.append(self.grille[j,i].pos)
            print(a)
    
    def jeu(self):
        self.aff()
        ligne=input("Dans quelle ligne est la case que vous voulez tourner?")
        colonne = input("Dans quelle colonne est la case que vous voulez tourner?")
        ligne=int(ligne)
        colonne = int(colonne)
        self.grille[ligne , colonne].tur()
        self.color_all()
        self.main_func()
#====================================================================================================================================
#====================================================================================================================================
if __name__ == '__main__':

    grille = Grille()
    game = True
    
    while game == True:
        b = Grille.recherchejoueur(input("Entrez un Pseudo \n")) 
        pseudo = b[0]
        Dico_player = b[1]
        scoreA = b[2]
        print("bonjour ",pseudo," Votre meilleur score est: ",scoreA)
        grille.debut()
        while time()- grille.timee <60:
            tps= 60-( time() -grille.timee)
            print("il vous reste: ", tps,"sec pour jouer")
            print("Score actuel: ",grille.score)
            grille.jeu()
        
        
        print("votre  score est de : ", grille.score)        
        
        if grille.score > scoreA:
            Dico_player[pseudo]=grille.score
            print("votre nouveau score est: " ,grille.score)
            Grille.save_Joueur(Dico_player)
        
        jeu = input("  o : pour continuer \n  n pour arréter \n")
        if jeu == 'o':
            game= True
        else :
            game= False
        




        