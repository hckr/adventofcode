#!/usr/bin/env python3
import sys
import re
from collections import defaultdict
from copy import deepcopy

particles = {}
i = 0
for line in sys.stdin:
    particles[i] = list(map(int, re.findall(r'-?\d+', line)))
    i += 1


def collide(particles):
    collisions = defaultdict(list)
    for i, particle in particles.items():
        collisions[tuple(particle[:3])].append(i)
    for i, collided_particles in collisions.items():
        if len(collided_particles) > 1:
            for p in collided_particles:
                del particles[p]


def simulate(particles, collisions=False, t=5000):
    particles = deepcopy(particles)
    for _ in range(t):
        for i, particle in particles.items():
            # change velocity by acceleration
            particle[3] += particle[6]
            particle[4] += particle[7]
            particle[5] += particle[8]
            # change position by velocity
            particle[0] += particle[3]
            particle[1] += particle[4]
            particle[2] += particle[5]
        if collisions:
            collide(particles)
    return particles


print(min(simulate(particles).items(),
      key=lambda p: abs(p[1][0])+abs(p[1][1])+abs(p[1][2]))[0])
print(len(simulate(particles, collisions=True)))
