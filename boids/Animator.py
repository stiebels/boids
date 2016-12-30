from matplotlib import pyplot as plt
from matplotlib import animation
from boids.Flock import Flock


class Animator(object):
    def __init__(self, path, size=50, fly_middle_strength=0.01, fly_away_limit=100, speed_match_strength=0.125, distance_limit=10000,
                 frames=470, interval=50, xlim=(-500, 1500), ylim=(-500, 1500)):
        self.frames = frames
        self.flock = Flock(size, fly_middle_strength, fly_away_limit, speed_match_strength, distance_limit)
        self.figure = plt.figure()
        self.axes = plt.axes(xlim=xlim, ylim=ylim)
        self.count = 0
        self.scatter = self.axes.scatter(self.format_flock()[0], self.format_flock()[1])
        self.ani = animation.FuncAnimation(self.figure, self.animate, frames=self.frames, interval=interval)
        self.Writer = animation.writers['ffmpeg']
        self.writer = self.Writer(fps=15, metadata=dict(artist='Simon Stiebellehner'), bitrate=1800)
        if path:
            self.ani.save(path, writer=self.writer)
        else:
            plt.show()


    def format_flock(self):
        boids_x_coords = []
        boids_y_coords = []
        for boid in self.flock.boids:
            boids_x_coords.append(boid.x_coord)
            boids_y_coords.append(boid.y_coord)
        return boids_x_coords, boids_y_coords


    def animate(self, i):
        self.count += 1
        if self.count > self.frames:
            plt.close(self.figure)
        self.flock.update_boids()
        scatter = self.scatter.set_offsets(list(zip(self.format_flock()[0], self.format_flock()[1])))
