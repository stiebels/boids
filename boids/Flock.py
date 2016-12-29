import random
import numpy as np
from boids.Boid import Boid


class Flock(object):
    def __init__(self, size=50,
                 x_coord_range=(-450, 50), y_coord_range=(300, 600),
                 x_velo_range=(0, 10), y_velo_range=(-20, 20)):
        self.size = size
        self.x_coord_range = x_coord_range
        self.y_coord_range = y_coord_range
        self.x_velo_range = x_velo_range
        self.y_velo_range = y_velo_range
        self.boids = self.create_boids()

    def create_boids(self):
        boids = np.asarray([Boid(
            random.uniform(self.x_coord_range[0], self.x_coord_range[1]),
            random.uniform(self.y_coord_range[0], self.y_coord_range[1]),
            random.uniform(self.x_velo_range[0], self.x_velo_range[1]),
            random.uniform(self.y_velo_range[0], self.y_velo_range[1])
        ) for boid in range(0, self.size)])
        return boids

    def update_boids(self):
        for boid in self.boids:
            boid.fly_middle(self)
        for boid in self.boids:
            boid.fly_away(self)
        for boid in self.boids:
            boid.match_speed(self)
            boid.move()
