# Particle System — GEO Sequence Exporter

This project implements a simple particle emitter simulation in Python.

The system simulates thousands of particles affected by gravity, color variation, directional emission, and lifetime-based respawning.
Each animation frame is exported to a .geo file compatible with Houdini’s PGEOMETRY format.

---

```mermaid
classDiagram
    class Particle {
        + Vec3 position
        + Vec3 direction
        + Vec3 color
        + int life
        + int max_life
        + float size
        + __str__()
    }

    class Emitter {
        - Vec3 _position
        - int _num_particles
        - list~Particle~ _particles
        + __init__(position, num_particles)
        + _init_particles()
        + _create_particle() Particle
        + update(dt)
        + write_geo(file_name)
        + render()
        + position
        + num_particles
        + particles
    }

    class Vec3 {
        + x
        + y
        + z
        + copy()
        + (other operations)
    }

    Emitter --> Particle : generates
    Emitter --> Vec3 : uses
```

---

This project will export the `.geo` files into the `OUTPUT_DIR` as shown in the image.

![Particles](./particles/particles_geo.png)