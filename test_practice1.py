import pytest
from practice1 import hotel_cost,plane_ride_cost,rental_car_cost,trip_cost

def test_answer():
    assert hotel_cost(3) == 280

def test2_answer():
    assert plane_ride_cost("Tampa") == 220


def test3_answer():
    assert rental_car_cost(2) == 80
    assert rental_car_cost(3) == 100

def test4_answer():
    assert trip_cost("Tampa",3,88) == 688