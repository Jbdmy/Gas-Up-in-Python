# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:57:30 2018

@author: Demay
"""

#=============================================================================================================================
import Ccontroleur2

from tkinter import *
import PIL.Image
import PIL.ImageTk
from functools import partial
from PIL import ImageTk

#=============================================================================================================================


#====================================================================================================================================
#====================================================================================================================================
class Win:
    #-----------------------------------------------------------------------------------------------------------------------------    
    #-----------------------------------------------------------------------------------------------------------------------------    
    def __init__(self, ligne=None, colonne=None ,lab=None):
        self.lignew=0
        self.colonnew=0
        self.window = Tk()
        self.score= 0
        self.lab_time= lab
        
    #-----------------------------------------------------------------------------------------------------------------------------    
    #-----------------------------------------------------------------------------------------------------------------------------                       
  
    def make_Button(self, couleur, valeur, ligne , colonne, objet):
        image = None
    
    #en fonction de la couleur on va chercher dans les image avec cette couleur"""
        if couleur == 1 :
            """ on va cherche l'image qui a la forme associé a la valeur"""
            if valeur == 6:
                image = ImageTk.PhotoImage(file="img/106.png")
            if valeur == 18:
                image = ImageTk.PhotoImage(file="img/118.png") 
            if valeur == 12:
                image = ImageTk.PhotoImage(file="img/112.png")   
            if valeur == 24:
                image = ImageTk.PhotoImage(file="img/124.png")            
            if valeur == 10:
                image = ImageTk.PhotoImage(file="img/110.png")            
            if valeur == 30:
                image = ImageTk.PhotoImage(file="img/130.png")            
            if valeur == 20:
                image = ImageTk.PhotoImage(file="img/120.png")            
            if valeur == 14:
                image = ImageTk.PhotoImage(file="img/114.png")            
            if valeur == 22:
                image = ImageTk.PhotoImage(file="img/122.png")
            if valeur == 26:
                image = ImageTk.PhotoImage(file="img/126.png")
            if valeur == 28:
                image = ImageTk.PhotoImage(file="img/128.png")
        if couleur == 2 :
            if valeur == 6:
                image = ImageTk.PhotoImage(file="img/206.png")
            if valeur == 18:
                image = ImageTk.PhotoImage(file="img/218.png") 
            if valeur == 12:
                image = ImageTk.PhotoImage(file="img/212.png")   
            if valeur == 24:
                image = ImageTk.PhotoImage(file="img/224.png")            
            if valeur == 10:
                image = ImageTk.PhotoImage(file="img/210.png")            
            if valeur == 30:
                image = ImageTk.PhotoImage(file="img/230.png")            
            if valeur == 20:
                image = ImageTk.PhotoImage(file="img/220.png")            
            if valeur == 14:
                image = ImageTk.PhotoImage(file="img/214.png")            
            if valeur == 22:
                image = ImageTk.PhotoImage(file="img/222.png")
            if valeur == 26:
                image = ImageTk.PhotoImage(file="img/226.png")
            if valeur == 28:
                image = ImageTk.PhotoImage(file="img/228.png")
        if couleur == 3 :
            if valeur == 6:
                image = ImageTk.PhotoImage(file="img/306.png")
            if valeur == 18:
                image = ImageTk.PhotoImage(file="img/318.png") 
            if valeur == 12:
                image = ImageTk.PhotoImage(file="img/312.png")   
            if valeur == 24:
                image = ImageTk.PhotoImage(file="img/324.png")            
            if valeur == 10:
                image = ImageTk.PhotoImage(file="img/310.png")            
            if valeur == 30:
                image = ImageTk.PhotoImage(file="img/330.png")            
            if valeur == 20:
                image = ImageTk.PhotoImage(file="img/320.png")            
            if valeur == 14:
                image = ImageTk.PhotoImage(file="img/314.png")            
            if valeur == 22:
                image = ImageTk.PhotoImage(file="img/322.png")
            if valeur == 26:
                image = ImageTk.PhotoImage(file="img/326.png")
            if valeur == 28:
                image = ImageTk.PhotoImage(file="img/328.png")
            
        #on crée un bouton relié a la fonction main_func et on lui associe les paramètres de ligne, colonne ou il est 
        
        
        
        b = Button(self.window , command = partial(Ccontroleur2.Controleur.main_func, objet , ligne , colonne), image = image, borderwidth = 0, width = 60, height = 60)
        b.image = image #crée une copie
        #on placa le bouton dans la fenetre, a la place ou on veut qu'il soit, décalé de 1 pour laisser une place pour les labels"""
        b.grid (column=colonne+1 ,row= ligne+1)
    
    #-----------------------------------------------------------------------------------------------------------------------------    
    """ place les images de l'essence et du scooter en foction de la taille de la grille que veux l'utilisateur"""
    def cadre(self):
    
        for i in range(1,self.lignew+1):
            image = None
            #on prend une image """
            image = ImageTk.PhotoImage(file="img/gasoline-pump.png")
            #on crée un bouton qui a l'image comme apparence et qui n'est relié a aucune fonction """
            #on voulait pouvoir changer l'image mais on a manqué de temps"""
            b = Button(self.window , image = image, borderwidth = 0, width = 60, height = 60)
            #on crée une copie"""
            b.image = image
            #on place le bouton """
            b.grid(column = 0, row = i)
    
        for i in range(1,self.lignew+1):
            #idem a d'autres positions"""
            photo = PhotoImage(file="img/scoot.gif") # Pas de convertion avec du GIF :D
            b = Button(self.window , image = photo, borderwidth = 0, width = 60, height = 60)
    
            b.image = photo
            b.grid(column = self.colonnew+1, row = i)

    #-----------------------------------------------------------------------------------------------------------------------------
    """recupère le nombre de Ligne/collones et lance le jeu"""
    def recup_dat1(self, ligne, colonne, pseudo ):
        global root
                
        lligne = int(ligne.get())
        ccolonne = int(colonne.get())
        self.lignew = lligne
        self.colonnew= ccolonne
    
        pseudo = str(pseudo.get())
        # on cherche le score de l'utilissateur ou on l'inscrit et on récupère en dico_play[1] le dictionnaire joueur/score"""
        # dico_play[0] est le pseudo du joueur, dico_play[2] est son meilleur score """
        """dico_play=Win.recherchejoueur(pseudo)"""
        dico_play= Ccontroleur2.Controleur.recherche_joueur(pseudo)
    
    # si l'utilisateur jouait on inscrit son score si il est son meilleur"""
        if self.score != 0:
            if dico_play[1][pseudo]< self.score:
                dico_play[1][pseudo]=self.score
                # on enregistre le pseudo et le score du joueur """
                """Win.save_joueur(dico_play[1])"""
                Ccontroleur2.Controleur.save_player(dico_play[1])
            
        """dico_play=Win.recherchejoueur(pseudo)"""
        dico_play= Ccontroleur2.Controleur.recherche_joueur(pseudo)
            #on cherche le meilleur score ever """
        temm = 0
        na = None
        for cle  in dico_play[1]:
            if dico_play[1][cle] >= temm:
                na = cle
                temm = dico_play[1][cle]
         
        # on remplit la fenetre principale """
        Win.cadre(self)
        
        # on affiche les meilleurs scores: joueurs et ever"""
        lab_best = Label(self.window, text='')
        lab_best.grid(column =0 , row=self.lignew+1 )
        lab_best.config(text="best ever:\n' "+na+"' avec: "+str(temm)+" points")
    
        lab_play = Label(self.window, text='')
        lab_play.grid(column =0 , row=self.lignew+2 )
        lab_play.config(text="votre meilleur score \n '"+pseudo+ "' est:"+str(dico_play[2]))
       
        root.destroy()
        
    #-----------------------------------------------------------------------------------------------------------------------------
    """ fonction lancant une fenetre afin de recueillir les donnés (nb de lignes, colonnes, pseudo)"""    
    def first_win(self, objet):
    
        global root      
        
        #On definit cette fenetre comme prioritaire contre window """
        root = Toplevel(self.window)
        root.grab_set()
        root.focus_set()
        #On definit les variables """
        ligne = StringVar(root)
        colonne = StringVar(root)
        pseudo = StringVar(root)
        #place les titres"""
        label = Label(root, text='Ligne')
        label.grid(column=0, row=0)
        #on place les entry pour recuperer less valeurs definies par l'utilisateur """
        entry_name = Entry(root, textvariable=ligne)
        entry_name.grid(column=0, row=1)
    
        # idem"""
        label1 = Label(root, text='Colonne')
        label1.grid(column=1, row=0)
      
        entry_name1 = Entry(root, textvariable=colonne)
        entry_name1.grid(column=1, row=1)
    
        label2 = Label(root, text='Pseudo')
        label2.grid(column=2, row=0)
    
        entry_name2 = Entry(root, textvariable=pseudo)
        entry_name2.grid(column=2, row=1)
    
    
        #on definit un bouton qui lancera recup_dat"""
        """ pb ici """
        button = Button(root, text='C est parti!', command=partial(Ccontroleur2.Controleur.recup_dat,objet, ligne, colonne, pseudo))   
        button.grid(column=1, row=2)
    
    #-----------------------------------------------------------------------------------------------------------------------------
    def reset(self):
        for element in self.window.winfo_children():
            element.destroy()
    
    #-----------------------------------------------------------------------------------------------------------------------------
    
    def set_window(self, objet=None):
        #on ajoute un label pour le score et un bouton pour melanger la grille    
        label1 = Label(self.window, text= self.score)
        label1.grid(column=0, row=0)
        
        #le bouton pour mélanger
        k = Button(self.window , command =partial( Ccontroleur2.Controleur.retiragegrille_aff, objet) , text = "Shuffle" )  
        k.grid(column=1, row=0)
    #-----------------------------------------------------------------------------------------------------------------------------
    def wait_aff(self):
        self.window.update()
        self.window.after(400)
    #-----------------------------------------------------------------------------------------------------------------------------
    def set_time_label(self, temp3):
        self.lab_time= Label(self.window, text=int(temp3))
        self.lab_time.grid(column =2 , row=0 )                

#====================================================================================================================================
#====================================================================================================================================









            