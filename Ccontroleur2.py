# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:32:20 2018

@author: Demay
"""

from Cjeu import *
from Cwin import * 
from time import *

#====================================================================================================================================
#====================================================================================================================================

class Controleur():
    def __init__(self):
        self.grille=Grille()
        self.win=Win()

    #-----------------------------------------------------------------------------------------------------------------------------
        
    def first_win(self):
                
        self.win.reset()
        self.grille.reset()
        
        self.win.first_win(self)        
        self.grille.score=0
    #-----------------------------------------------------------------------------------------------------------------------------
    
    def recup_dat(self, ligne , colonne , pseudo):
        self.win.recup_dat1(ligne , colonne , pseudo)
                
        self.grille.ligne = self.win.lignew
        self.grille.colonne = self.win.colonnew
        
        self.grille.start_chrono()
        
        Controleur.shuffleb(self)
    #-----------------------------------------------------------------------------------------------------------------------------
       
    def shuffleb(self):
        self.grille.shuffle()
        Controleur.sett_window(self)
    #-----------------------------------------------------------------------------------------------------------------------------
   
    def sett_window(self):
        
        self.grille.color_all()
        
        self.win.score = self.grille.score
        
        self.win.set_window(self)
        
        #on prend une case de la grille et on lui associe un bouton
        for elt in self.grille.grille :            
            #on récupère les caracteristiques de la case qui seront utiles pour l'image correspondant
            Win.make_Button(self.win, self.grille.grille[elt].col , self.grille.grille[elt].list[0] , elt[0] , elt[1], self)
            
    #-----------------------------------------------------------------------------------------------------------------------------        
        
    def main_func(self, ligne , colonne):
        
        self.grille.grille[ligne , colonne].tur()
        
        #affichage du changement / des lignes si il y en a 
        Controleur.sett_window(self)
        
        self.win.wait_aff()
                
        self.grille.main_func()
        
        self.win.score = self.grille.score
        
        Controleur.sett_window(self)
        
        temp3 = self.grille.chrono()
        self.win.set_time_label(temp3)
        if temp3 <0 :
            Controleur.first_win(self)
    #-----------------------------------------------------------------------------------------------------------------------------
        
    def retiragegrille_aff(self):
        Controleur.shuffleb(self)
    #-----------------------------------------------------------------------------------------------------------------------------
    def recherche_joueur(pseudo):
        ps = Grille.recherchejoueur(pseudo)
        return( ps)
    #-----------------------------------------------------------------------------------------------------------------------------
    def save_player(dico):
        Grille.save_joueur(dico)
#====================================================================================================================================
#====================================================================================================================================
