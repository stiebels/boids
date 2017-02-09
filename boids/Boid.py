import numpy as np
np.seterr(over='ignore') # Suppressing Numpy float precision warnings

'''
Implements smallest entity in Flock: Boid
'''

class Boid(object):
    # Boid is smallest entity and part of Flock
    def __init__(self, x_coordinate, y_coordinate, x_velocity, y_velocity):
        self.x_coord = x_coordinate
        self.y_coord = y_coordinate
        self.x_velo = x_velocity
        self.y_velo = y_velocity
        self.position = np.asarray((self.x_coord, self.y_coord))
        self.velocity = np.asarray((self.x_velo, self.y_velo))


    def fly_middle(self, Flock, fly_middle_strength):
        # Boid tends to fly to middle of flock
        fly_middle_reg = fly_middle_strength / Flock.size
        for boid in Flock.boids:
            rel_pos = boid.position - self.position
            self.velocity += rel_pos * fly_middle_reg


    def fly_away(self, Flock, fly_away_limit, scaling=2):
        # Boid flies away if too close to other boid
        for boid in Flock.boids:
            rel_pos_sq = sum((boid.position - self.position) ** scaling)
            if rel_pos_sq < fly_away_limit:
                rel_pos = self.position - boid.position
                self.velocity += rel_pos


    def match_speed(self, Flock, speed_match_strength, distance_limit, scaling=2):
        # Boid tends to match speed with other boids
        speed_match_reg = speed_match_strength / Flock.size
        for boid in Flock.boids:
            rel_pos_sq = sum((boid.position - self.position) ** scaling)
            if rel_pos_sq < distance_limit:
                rel_velo = boid.velocity - self.velocity
                self.velocity += rel_velo * speed_match_reg


    def move(self):
        # Final change of position of boid (i.e. movement)
        self.position += self.velocity
        self.x_coord, self.y_coord = self.position
