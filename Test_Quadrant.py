from Coordinate import Coordinate
from Quadrant import Quadrant
import pytest


def test_first_quadrant():
    x = 10
    y = 20
    coordinates = Coordinate(x, y)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result == "First"


def test_second_quadrant():
    x = -10
    y = 20
    coordinates = Coordinate(x, y)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result == "Second"


def test_third_quadrant():
    x = -10
    y = -20
    coordinates = Coordinate(x, y)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result == "Third"


def test_fourth_quadrant():
    x = 10
    y = -20
    coordinates = Coordinate(x, y)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result == "Fourth"