import pytest

def test_area(my_rectangle):
    assert my_rectangle.area() == 200

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 60

def test_strange_rectangle(strange_rect, my_rectangle):

    assert strange_rect != my_rectangle

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle