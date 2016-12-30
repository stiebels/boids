import random
import numpy as np
from boids.Boid import Boid


class Flock(object):
    def __init__(self, size, fly_middle_strength, fly_away_limit, speed_match_strength, distance_limit,
                 x_coord_range, y_coord_range,
                 x_velo_range, y_velo_range):
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
            boid.fly_middle(self, fly_middle_strength=self.fly_middle_strength)
        for boid in self.boids:
            boid.fly_away(self, fly_away_limit=self.fly_away_limit)
        for boid in self.boids:
            boid.match_speed(self, speed_match_strength=self.speed_match_strength, distance_limit=self.distance_limit)
            boid.move()
