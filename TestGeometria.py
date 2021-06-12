
import Geometria
import unittest
class TestGeomotria(unittest.TestCase):
 def test_areaCuadrado(self):
     self.assertEqual(Geometria.areaCuadrado(5), 25)

 def test_areaCirculo(self):
     self.assertEqual(Geometria.areaCirculo(5), 25)
 def test_areaTriangulo(self):
     self.assertEqual(Geometria.areaTriangulo(5,3), 7.5)
 def test_areaRectangulo(self):
     self.assertEqual(Geometria.areaRectangulo(5,8), 40)

 def test_areaPentagono(self):
     self.assertEqual(Geometria.areaPentagono(5,4), 25)
 def test_areaRomboide(self):
     self.assertEqual(Geometria.areaRomboide(5,7), 25)
 def test_areaTrapecio(self):
     self.assertEqual(Geometria.areaTrapecio(5,7,9), 25)

if __name__ == '__main__':
    unittest.main()
