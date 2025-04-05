import pytest
from vector import Vector
from particle import Particle


def test_vector_operations():
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    assert (v1 + v2) == Vector(4, 6)
    assert (v1 - v2) == Vector(2, 2)
    assert (v1 * 2) == Vector(6, 8)
    assert (v1 / 2) == Vector(1.5, 2)

def test_mag():
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    assert v1.mag() == 5
    assert v2.mag() == 5**(1/2)

def test_normalize():
    v1 = Vector(3, 4)

    assert v1.normalize() == Vector(0.6, 0.8)

def test_attract():
    p1 = Particle(Vector(0, 0), Vector(0, 0), 10, Vector(0, 0), Vector(0, 0), 7, 5)
    p2 = Particle(Vector(10, 0), Vector(0, 0), 5, Vector(0, 0), Vector(0, 0), 7, 5)
    
    p1.attract(p2)
    assert p2.force.x != 0 and p2.force.y == 0

def test_check_collision():
    p1 = Particle(Vector(0, 0), Vector(0, 0), 10, Vector(0, 0), Vector(0, 0), 7, 5)
    p2 = Particle(Vector(8, 0), Vector(0, 0), 5, Vector(0, 0), Vector(0, 0), 7, 5)
    p3 = Particle(Vector(20, 0), Vector(0, 0), 5, Vector(0, 0), Vector(0, 0), 7, 5)
    
    assert p1.check_collision(p2) is True
    assert p1.check_collision(p3) is False