import math

class Shape():

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width


#Metoda __eq__, którą podałeś, jest specjalną metodą w Pythonie, która definiuje, jak porównywać dwa obiekty pod kątem równości przy użyciu operatora ==
#Metoda __eq__ w klasie Rectangle pozwala na porównywanie dwóch prostokątów za pomocą operatora ==. Najpierw sprawdza, czy obiekt, z którym porównujemy, jest instancją klasy Rectangle; 
# jeśli nie, zwraca False. Następnie porównuje szerokość i długość obu prostokątów: jeśli oba wymiary są równe, zwraca True, w przeciwnym razie False. Dzięki tej metodzie porównywanie 
# prostokątów staje się intuicyjne i zgodne z oczekiwaniami użytkownika.
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        
        #Jeśli oba są prawidziwe to True
        #Mogę przez to porownywac instancje, rec1 == rect3, czyli pokazuje jak sie porownywac
        return self.width == other.width and self.length == other.length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length * 2) + (self.width * 2)
