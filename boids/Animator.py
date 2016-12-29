from matplotlib import pyplot as plt
from matplotlib import animation
from boids import Flock


class Animator(object):
    def __init__(self, size=50, frames=50, interval=50, xlim=(-500, 1500), ylim=(-500, 1500)):
        self.flock = Flock(size)
        self.figure = plt.figure()
        self.axes = plt.axes(xlim=xlim, ylim=ylim)
        self.scatter = self.axes.scatter(self.format_flock()[0], self.format_flock()[1])
        self.ani = animation.FuncAnimation(self.figure, self.animate, frames=frames, interval=interval)

    def format_flock(self):
        boids_x_coords = []
        boids_y_coords = []
        for boid in self.flock.boids:
            boids_x_coords.append(boid.x_coord)
            boids_y_coords.append(boid.y_coord)
        return boids_x_coords, boids_y_coords

    def animate(self, i):
        self.flock.update_boids()
        scatter = self.scatter.set_offsets(list(zip(self.format_flock()[0], self.format_flock()[1])))
