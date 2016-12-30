import random
import numpy as np
from boids.Boid import Boid


class Flock(object):
    def __init__(self, size=50, fly_middle_strength=0.01, fly_away_limit=100, speed_match_strength=0.125, distance_limit=10000,
                 x_coord_range=(-450, 50), y_coord_range=(300, 600),
                 x_velo_range=(0, 10), y_velo_range=(-20, 20)):
        self.size = size
        self.x_coord_range = x_coord_range
        self.y_coord_range = y_coord_range
        self.x_velo_range = x_velo_range
        self.y_velo_range = y_velo_range
        self.boids = self.create_boids()
        self.fly_middle_strength = fly_middle_strength
        self.fly_away_limit = fly_away_limit
        self.speed_match_strength = speed_match_strength
        self.distance_limit = distance_limit

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
            boid.fly_middle(self, self.fly_middle_strength)
        for boid in self.boids:
            boid.fly_away(self, self.fly_away_limit)
        for boid in self.boids:
            boid.match_speed(self, self.speed_match_strength, self.distance_limit)
            boid.move()
