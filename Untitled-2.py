class rectongle ():
     # atribut #

     def __init__(self, longueur , largeur ):
        self.longueur = longueur
        self. largeur =  largeur

      # cretion d un  objet de la class rectongle #

     def perimetre (self):
         perimetre = 2*(self.longueur + self.largeur)
         return perimetre
     
     def Aire (self):
         aire = self.longueur * self.largeur
         return aire
     
     def carre (self):
         if self.longueurb == self.largeur :
            return True
         else :
             return False
        
     def affiche_rectongale(self):
         print ( "longueur est  :  {self.longueur()} largeur est : {self.largeur()}")
         print ( "perimetre est : {self.perimetre()} Aire est : {self.aiter()}")
         if self.carre():
            print ( "carre est:{self.carre()}")
         else :
             print("False")