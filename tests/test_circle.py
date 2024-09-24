import pytest
import math

import source.shapes as shapes

class TestCircle():

    def setup_method(self, method):
        #Metoda ta jest wywoływana przed każdym testem w klasie testowej.
        #Jej zadaniem jest przygotowanie środowiska do testu, np. tworzenie obiektów, inicjalizacja danych itp.
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        #Metoda ta jest wywoływana po zakończeniu każdego testu.
        #Jej zadaniem jest sprzątanie po teście, czyli usunięcie zasobów, obiektów lub przywrócenie stanu środowiska do czystego stanu.
        print(f"Tearing down {method}")    
        del self.circle

#Test setapowanej metody
    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius


