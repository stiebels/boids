from matplotlib import pyplot as plt
from matplotlib import animation
import random


flock_size = 50
init_x_coord = (-450, 50)
init_y_coord = (300, 600)
init_x_velo = (0, 10)
init_y_velo = (-20, 20)
avoid_distance = 100
flying_distance = 10000
fly_middle_reg = 0.01/flock_size
speed_match_reg = 0.125/flock_size
scaling = 2


boids_x_coords=[random.uniform(init_x_coord[0], init_x_coord[1]) for x in range(flock_size)]
boids_y_coords=[random.uniform(init_y_coord[0], init_y_coord[1]) for x in range(flock_size)]
boid_x_velos=[random.uniform(init_x_velo[0], init_x_velo[1]) for x in range(flock_size)]
boid_y_velos=[random.uniform(init_y_velo[0], init_y_velo[1]) for x in range(flock_size)]
boids=(boids_x_coords,boids_y_coords,boid_x_velos,boid_y_velos)

def update_boids(boids):
    x_coord,y_coord,x_velo,y_velo=boids
    # Fly towards the middle
    for i in range(flock_size):
        for j in range(flock_size):
            x_velo[i]=x_velo[i]+(x_coord[j]-x_coord[i])*fly_middle_reg
    for i in range(flock_size):
        for j in range(flock_size):
            y_velo[i]=y_velo[i]+(y_coord[j]-y_coord[i])*fly_middle_reg
    # Fly away from nearby boids
    for i in range(flock_size):
        for j in range(flock_size):
            if (x_coord[j]-x_coord[i])**scaling + (y_coord[j]-y_coord[i])**scaling < avoid_distance:
                x_velo[i]=x_velo[i]+(x_coord[i]-x_coord[j])
                y_velo[i]=y_velo[i]+(y_coord[i]-y_coord[j])
    # Try to match speed with nearby boids
    for i in range(flock_size):
        for j in range(flock_size):
            if (x_coord[j]-x_coord[i])**scaling + (y_coord[j]-y_coord[i])**scaling < flying_distance:
                x_velo[i]=x_velo[i]+(x_velo[j]-x_velo[i])*speed_match_reg
                y_velo[i]=y_velo[i]+(y_velo[j]-y_velo[i])*speed_match_reg
    # Move according to velocities
    for i in range(flock_size):
        x_coord[i]=x_coord[i]+x_velo[i]
        y_coord[i]=y_coord[i]+y_velo[i]


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
