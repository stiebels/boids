
class Boid(object):

    def __init__(self, x_coordinate, y_coordinate, x_velocity, y_velocity):
        self.x_coord = x_coordinate
        self.y_coord = y_coordinate
        self.x_velo = x_velocity
        self.y_velo = y_velocity


    def fly_middle(self, Flock, fly_middle_strength=0.01):
        fly_middle_reg = fly_middle_strength / Flock.size
        for boid in Flock.boids:
            self.x_velo += (boid.x_coord - self.x_coord) * fly_middle_reg
            self.y_velo += (boid.y_coord - self.y_coord) * fly_middle_reg


    def fly_away(self, Flock, avoid_distance=100, scaling=2):
        for boid in Flock.boids:
            distance = (boid.x_coord - self.x_coord) ** scaling + (boid.y_coord - self.y_coord) ** scaling
            if distance < avoid_distance:
                self.x_velo += self.x_coord - boid.x_coord
                self.y_velo += self.y_coord - boid.y_coord


    def match_speed(self, Flock, speed_match_strength=0.125, scaling=2, flying_distance=10000):
        speed_match_reg = speed_match_strength / Flock.size
        for boid in Flock.boids:
            distance = (boid.x_coord - self.x_coord) ** scaling + (boid.y_coord - self.y_coord) ** scaling
            if distance < flying_distance:
                self.x_velo += (boid.x_velo - self.x_velo) * speed_match_reg
                self.y_velo += (boid.y_velo - self.y_velo) * speed_match_reg


    def move(self):
        self.x_coord += self.x_velo
        self.y_coord += self.y_velo
