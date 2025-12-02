#!/usr/bin/env -S uv run --script


from pathlib import Path
from ncca.ngl.vec3 import Vec3
from model.emitter import Emitter

OUTPUT_DIR = Path("~/Documents/BU/particles").expanduser()
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

emitter = Emitter(Vec3(0, 0, 0), 1000)

for i in range(250):
    emitter.write_geo(f"{OUTPUT_DIR}/Particle.{i:04}.geo")
    emitter.update(0.01)
