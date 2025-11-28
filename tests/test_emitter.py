import pytest

from model.emitter import Emitter
from model.vec3 import Vec3


def test_emitter_creation():
    position = Vec3(0, 0, 0)
    num_particles = 1000
    emitter = Emitter(position, num_particles)

    assert emitter
    assert emitter.position == position
    assert emitter.num_particles == num_particles
    assert isinstance(emitter.particles, list)
    assert len(emitter.particles) == num_particles
