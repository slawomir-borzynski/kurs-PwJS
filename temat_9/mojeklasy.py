# -*- coding: utf-8 -*-
import math
class punkt2D:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def drukuj(self):
        print("Obecne wspolrzedne to: x=",self.x," y=",self.y)
        
    def zeruj(self):
        self.x=0
        self.y=0
        
class punkt3D(punkt2D):
    def __init__(self,x,y,z):
        punkt2D.__init__(self, x, y)
        self.z=z

    def drukuj(self):
        punkt2D.drukuj(self)
        print("Dodatkowa wspolrzedna z=",self.z)
    
    def zeruj(self):
        punkt2D.zeruj(self)
        self.z=0
        
        

class Odcinek:
    def __init__(self,a,b):
        self.x1=a.x
        self.x2=b.x
        self.y1=a.y
        self.y2=b.y
        
    def oblicz(self):
        x_sub_pow = math.pow((self.x2-self.x1),2)
        y_sub_pow = math.pow((self.y2-self.y1),2)        
        length = math.pow((x_sub_pow + y_sub_pow),0.5)
        return length
    
def testy():
    print("zadanie 1:") 
    wspolrzedna = punkt2D(3,4)
    wspolrzedna.drukuj()
    wspolrzedna.zeruj()
    wspolrzedna.drukuj()
    print("koniec zadania 1")
    
    print("\n")
    
    print("zadanie 2:")
    wspolrzedna3D=punkt3D(1,2,3)
    wspolrzedna3D.drukuj()
    wspolrzedna3D.zeruj()
    wspolrzedna3D.drukuj()
    print("koniec zadania 2")    
    
    print("\n")
    
    print("zadanie 3:")
    A=punkt2D(1,2)
    B=punkt2D(3,4)
    print("Dlugosc odcinka o podanych wspolrzednych wynosi ",Odcinek(A,B).oblicz())
    C=punkt2D(-2,-2)
    D=punkt2D(3,3)
    print("Dlugosc odcinka o podanych wspolrzednych wynosi ",Odcinek(C,D).oblicz())



if __name__ == "__main__":
 testy()
