import unittest
import math
from Calculadora_de_matrices import *
class TestStringMethods(unittest.TestCase):

    def test_suma_de_vectores_complejos(self):
        a=[[(1.0, 0.0)]]
        b=[[(2.0, 0.0)]]
        self.assertEqual(suma_de_vectores_complejos(a,b),[(3.0, 0.0)])
    def test_inversa_de_vectores_complejos(self):
        a=[[(1.0, 0.0)]]
        self.assertEqual(inversa_de_vectores_complejos(a),[(-1.0, -0.0)])
    def test_escalar_x_complejo(self):
        E=5
        C=(4,3)
        self.assertEqual(escalar_x_complejo(E,C),(20,15))
    def test_suma_matrices(self):
        A=[[(6.0, -4.0)], [(7.0, 3.0)], [(4.2, -8.1)], [(0.0, -3.0)]]
        B=[[(16.0, 2.3)], [(0.0, -7.0)], [(6.0, 0.0)], [(0.0, -4.0)]]
        self.assertEqual(suma_matrices(A,B),[[(22.0, -1.7000000000000002)], [(7.0, -4.0)], [(10.2, -8.1)], [(0.0, -7.0)]])
    def test_inversa_matriz(self):
        A=[[(6.0, -4.0)], [(7.0, 3.0)], [(4.2, -8.1)], [(0.0, -3.0)]]
        self.assertEqual(inversa_matriz(A),[[(-6.0, 4.0)], [(-7.0, -3.0)], [(-4.2, 8.1)], [(-0.0, 3.0)]])
    def test_esacalar_X_Mcompleja(self):
        E=5
        C=[[(1.0, 2.0), (1.0, 2.0)], [(1.0, 2.0), (1.0, 2.0)]]
        self.assertEqual(esacalar_X_Mcompleja(E,C),[[(5.0, 10.0), (5.0, 10.0)], [(5.0, 10.0), (5.0, 10.0)]])                         
    def test_traspuesta_matriz_o_Vector(self):
        A=[[(6.0, -4.0)], [(7.0, 3.0)], [(4.2, -8.1)], [(0.0, -3.0)]]
        self.assertEqual(traspuesta_matriz_o_Vector(A),[[(6.0, -4.0), (7.0, 3.0), (4.2, -8.1), (0.0, -3.0)]])
    def test_conjugada(self):
        A=[[(6.0, -4.0)], [(7.0, 3.0)], [(4.2, -8.1)], [(0.0, -3.0)]]
        self.assertEqual(conjugada(A),[[(6.0, 4.0)], [(7.0, -3.0)], [(4.2, 8.1)], [(0.0, 3.0)]]) 
    def test_adjunta_daga(self):
        A=[[(1.0, 2.0), (1.0, 2.0)], [(1.0, 2.0), (1.0, 2.0)]]
        self.assertEqual(adjunta_daga(A),[[(1.0, 2.0), (1.0, 2.0)], [(1.0, 2.0), (1.0, 2.0)]])
    def test_producto_AB(self):
        A=[[(1.0, 0.0), (-2.0, 0.0), (-3.0, 0.0)], [(0.0, 0.0), (2.0, 0.0), (-3.0, 0.0)], [(0.0, 0.0), (0.0, 0.0), (3.0, 0.0)]]
        B=[[(5.0, 0.0), (0.0, 0.0), (0.0, 0.0)], [(4.0, 0.0), (-3.0, 0.0), (0.0, 0.0)], [(-2.0, 0.0), (1.0, 0.0), (5.0, 0.0)]]
        self.assertEqual(producto_AB(A,B),([[(3.0, 0.0), (3.0, 0.0), (-15.0, 0.0)], [(14.0, 0.0), (-9.0, 0.0), (-15.0, 0.0)], [(-6.0, 0.0), (3.0, 0.0), (15.0, 0.0)]]))
    def test_distancia(self):
        A=(1.0, 0.0)
        B=(2,3)
        self.assertEqual(distancia(A,B),3.1622776601683795)
    def test_prod_interno(self):
        A=[[(1.0, 0.0), (-2.0, 0.0), (-3.0, 0.0)], [(0.0, 0.0), (2.0, 0.0), (-3.0, 0.0)], [(0.0, 0.0), (0.0, 0.0), (3.0, 0.0)]]
        B=[[(5.0, 0.0), (0.0, 0.0), (0.0, 0.0)], [(4.0, 0.0), (-3.0, 0.0), (0.0, 0.0)], [(-2.0, 0.0), (1.0, 0.0), (5.0, 0.0)]]
        self.assertEqual(prod_interno(A,B),[(3.0, 0.0), (-9.0, 0.0), (15.0, 0.0)])

    def test_norma(self):
        A=[[(6.0, -4.0)], [(7.0, 3.0)], [(4.2, -8.1)], [(0.0, -3.0)]]
        self.assertEqual(norma(A), 9.0)
    def test_es_hermitaria(self):
        A=[[(1.0, 0.0), (1.0, 0.0)], [(1.0, 0.0), (1.0, 0.0)]]
        self.assertEqual(es_hermitaria(A), 0)#significa que si es hermitaria el 0
    def test_es_unitaria(self):
        A=[[(1.0, 0.0), (1.0, 0.0)], [(1.0, 0.0), (1.0, 0.0)]]
        self.assertEqual(es_unitaria(A), 1) 


        
if __name__ == '__main__':
    unittest.main()

