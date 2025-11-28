import pytest

from model.particle import Particle
from model.vec3 import Vec3


def test_particle_creation():
    particle = Particle()
    assert particle
    assert particle.position == Vec3()
    assert particle.color == Vec3()
    assert particle.direction == Vec3()
    assert particle.life == 0
    assert particle.max_life == 100
    assert particle.size == pytest.approx(1.0)


def test_particle_value():
    position = Vec3(1, 2, 3)
    direction = Vec3(4, 5, 6)
    color = Vec3(7, 8, 9)
    max_life = 10
    life = 20
    size = 2.0
    particle = Particle(position, direction, color, life, max_life, size)

    assert particle.position == position
    assert particle.direction == direction
    assert particle.color == color
    assert particle.max_life == max_life
    assert particle.life == life
    assert particle.size == size
