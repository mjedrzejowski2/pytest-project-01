import pytest
import source.shapes as shapes

#Dekorator @pytest.fixture definiuje funkcję pomocniczą o nazwie my_rectangle, która tworzy i przygotowuje instancję klasy Rectangle z określonymi wymiarami (długość 10 i szerokość 20)
# do użycia w testach. Instrukcja yield przekazuje instancję prostokąta do funkcji testowej, a kod po yield wykonuje się po zakończeniu testu, umożliwiając przeprowadzenie działań porządkowych,
#  takich jak usunięcie instancji prostokąta.
@pytest.fixture
def my_rectangle():
    print("Setting up fixture")
    rectangle = shapes.Rectangle(10, 20)
    yield rectangle
    print("Tearing down fixture")
    del rectangle

@pytest.fixture
def strange_rect():
    print("Setting up fixture")
    strange_rectangle = shapes.Rectangle(5, 10)
    yield strange_rectangle
    print("Tearing down fixture")
    del strange_rectangle        