#!/opt/hfs20.5.332/bin/hython

import hou

from model.emitter import Emitter
from model.vec3 import Vec3

OUTPUT_DIR = "/transfer/ParticleHoudini"


def write_particles(emitter, file_name):
    geo = hou.Geometry()
    geo.addAttrib(hou.attribType.Point, "Cd", hou.Vector3(0, 0, 0))
    geo.addAttrib(hou.attribType.Point, "pscale", 1)
    point_objects = []

    for particle in emitter._particles:
        p = geo.createPoint()
        pos = particle.position
        p.setPosition(hou.Vector3(pos.x, pos.y, pos.z))
        color = particle.color
        p.setAttribValue("Cd", hou.Vector3(color.x, color.y, color.z))

        point_objects.append(p)

    geo.saveToFile(file_name)


def main():
    emitter = Emitter(Vec3(0, 0, 0), 1000)
    for frame in range(250):
        write_particles(emitter, f"{OUTPUT_DIR}/HouParticles.{frame:04}.geo")
        emitter.update(0.1)


if __name__ == "__main__":
    main()
