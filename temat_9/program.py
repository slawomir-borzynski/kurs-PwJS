# -*- coding: utf-8 -*-
import mojeklasy

def test_mojeklasy():
    
    print("zadanie 1 - odniesienie do mojeklasy:") 
    wspolrzedna = mojeklasy.punkt2D(7,8)
    wspolrzedna.drukuj()
    wspolrzedna.zeruj()
    wspolrzedna.drukuj()
    print("koniec zadania 1")
    
    print("\n")
    
    print("zadanie 2 - odniesienie do mojeklasy:")
    wspolrzedna3D=mojeklasy.punkt3D(7,8,9)
    wspolrzedna3D.drukuj()
    wspolrzedna3D.zeruj()
    wspolrzedna3D.drukuj()
    print("koniec zadania 2")    
    
    print("\n")
    
    print("zadanie 3 - odniesienie do mojeklasy:")
    A=mojeklasy.punkt2D(2,3)
    B=mojeklasy.punkt2D(5,6)
    print("Dlugosc odcinka o podanych wspolrzednych wynosi ",mojeklasy.Odcinek(A,B).oblicz())
   

if __name__ == "__main__":
    test_mojeklasy()