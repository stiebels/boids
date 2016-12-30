from matplotlib import pyplot as plt
from matplotlib import animation
from boids.Flock import Flock
import yaml
import os


class Animator(object):
    def __init__(self, path, size, fly_middle_strength, fly_away_limit, speed_match_strength, distance_limit,
                 frames, config, interval=50, xlim=(-500, 1500), ylim=(-500, 1500)):

        if config==False:
            directory = str(os.path.dirname(os.path.abspath('__file__')))
            config_yml = yaml.safe_load(open(directory + '/config.yml'))
            size = config_yml['flock_size']
            fly_middle_strength = config_yml['fly_middle_strength']
            fly_away_limit = config_yml['fly_away_limit']
            speed_match_strength = config_yml['speed_match_strength']
            distance_limit = config_yml['distance_limit']
            self.frames = config_yml['frames']
            interval = config_yml['interval']
            x_velo_range = config_yml['x_velo_range']
            y_velo_range = config_yml['y_velo_range']
            x_coord_range = config_yml['x_coord_range']
            y_coord_range = config_yml['y_coord_range']
            self.flock = Flock(size, fly_middle_strength, fly_away_limit, speed_match_strength, distance_limit,
                               x_coord_range, y_coord_range, x_velo_range, y_velo_range)
            self.figure = plt.figure()
            self.axes = plt.axes(xlim=config_yml['xlim'], ylim=config_yml['ylim'])

        else:
            self.frames = frames
            self.flock = Flock(size, fly_middle_strength, fly_away_limit, speed_match_strength, distance_limit,
                               x_coord_range=(-450, 50), y_coord_range=(300, 600),
                               x_velo_range=(0, 10), y_velo_range=(-20, 20))
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
