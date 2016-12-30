import numpy as np
np.seterr(over='ignore')


class Boid(object):

    def __init__(self, x_coordinate, y_coordinate, x_velocity, y_velocity):
        self.x_coord = x_coordinate
        self.y_coord = y_coordinate
        self.x_velo = x_velocity
        self.y_velo = y_velocity
        self.position = np.asarray((self.x_coord, self.y_coord))
        self.velocity = np.asarray((self.x_velo, self.y_velo))


    def fly_middle(self, Flock, fly_middle_strength=0.01):
        fly_middle_reg = fly_middle_strength / Flock.size
        for boid in Flock.boids:
            rel_pos = boid.position - self.position

            self.velocity += rel_pos * fly_middle_reg


    def fly_away(self, Flock, fly_away_limit=100, scaling=2):
        for boid in Flock.boids:
            rel_pos_sq = sum((boid.position - self.position) ** scaling)
            if rel_pos_sq < fly_away_limit:
                rel_pos = self.position - boid.position

                self.velocity += rel_pos


    def match_speed(self, Flock, speed_match_strength=0.125, scaling=2, distance_limit=10000):
        speed_match_reg = speed_match_strength / Flock.size
        for boid in Flock.boids:
            rel_pos_sq = sum((boid.position - self.position) ** scaling)
            if rel_pos_sq < distance_limit:
                rel_velo = boid.velocity - self.velocity

                self.velocity += rel_velo * speed_match_reg


    def move(self):
        self.position += self.velocity
        self.x_coord, self.y_coord = self.position
