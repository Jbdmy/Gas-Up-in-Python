# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 20:53:20 2017

@author: Demay & de Russé
"""



class case:
    def __init__(self, var ,  ligne , collonne   ,  color= None):
        
        self.pos=(ligne , collonne)
        self.col = 10000
        self.list  = [1,2]
        
        
        if var == 6:
            self.list[0]= 6
            self.list[1]=[2,4,0,0]
        elif var == 18 :
            self.list[0]=18
            self.list[1]=[2,0,0,16]
        elif var == 12 :
            self.list[0]=12
            self.list[1]=[0,4,8,0]
        elif var == 24 :
            self.list[0]=24
            self.list[1]=[0,0,8,16]
            
        elif var == 10 :
            self.list[0]=10
            self.list[1]=[2,0,8,0]          
        elif var == 20 :
            self.list[0]=20
            self.list[1]=[0,4,0,16]
        elif var == 30 :
            self.list[0]=30
            self.list[1]=[2,4,8,16]
        
        elif var == 26 :
            self.list[0]=26
            self.list[1]=[2,0,8,16]
        
        elif var == 22 :
            self.list[0]=22
            self.list[1]=[2,4,0,16]
        elif var == 14 :
            self.list[0]=14
            self.list[1]=[2,4,8,0]
        elif var == 28 :
            self.list[0]=28
            self.list[1]=[0,4,8,16]

#----------------------------------------------------------------------- 
   
    def tur(self):
        eltdelaliste = 0
        for iii in range(0,4):
            a=0
            a=int(self.list[1][iii])*2
            if a > 16:
                a = 2
            eltdelaliste += a
        if eltdelaliste == 6:
            self.list[0]= 6
            self.list[1]=[2,4,0,0]
        elif eltdelaliste == 18:
            self.list[0]=18
            self.list[1]=[2,0,0,16]
        elif eltdelaliste == 12:
            self.list[0]=12
            self.list[1]=[0,4,8,0]
        elif eltdelaliste == 24:
            self.list[0]=24
            self.list[1]=[0,0,8,16]
        elif eltdelaliste == 10:
            self.list[0]=10
            self.list[1]=[2,0,8,0] 
        elif eltdelaliste == 20:
            self.list[0]=20
            self.list[1]=[0,4,0,16]
        elif eltdelaliste == 30:
            self.list[0]=30
            self.list[1]=[2,4,8,16]
        elif eltdelaliste == 26:
            self.list[0]=26
            self.list[1]=[2,0,8,16]
        elif eltdelaliste == 22:
            self.list[0]=22
            self.list[1]=[2,4,0,16]
        elif eltdelaliste == 14:
            self.list[0]=14
            self.list[1]=[2,4,8,0]
        elif eltdelaliste == 28:
            self.list[0]=28
            self.list[1]=[0,4,8,16]
            
#-----------------------------------------------------------------------        
    def dell(self):
        """apres avoir trouvé un ligne complète"""
        self.list[0]=0
        self.list[1]=[0,0,0,0]
        
        
 
    def color(self , couleur):
        self.col = couleur
        

        
