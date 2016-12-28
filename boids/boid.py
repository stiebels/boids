from matplotlib import pyplot as plt
from matplotlib import animation
import random


boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
    x_coord,y_coord,x_velo,y_velo=boids
    # Fly towards the middle
    for i in range(50):
        for j in range(50):
            x_velo[i]=x_velo[i]+(x_coord[j]-x_coord[i])*0.01/len(x_coord)
    for i in range(50):
        for j in range(50):
            y_velo[i]=y_velo[i]+(y_coord[j]-y_coord[i])*0.01/len(x_coord)
    # Fly away from nearby boids
    for i in range(50):
        for j in range(50):
            if (x_coord[j]-x_coord[i])**2 + (y_coord[j]-y_coord[i])**2 < 100:
                x_velo[i]=x_velo[i]+(x_coord[i]-x_coord[j])
                y_velo[i]=y_velo[i]+(y_coord[i]-y_coord[j])
    # Try to match speed with nearby boids
    for i in range(50):
        for j in range(50):
            if (x_coord[j]-x_coord[i])**2 + (y_coord[j]-y_coord[i])**2 < 10000:
                x_velo[i]=x_velo[i]+(x_velo[j]-x_velo[i])*0.125/len(x_coord)
                y_velo[i]=y_velo[i]+(y_velo[j]-y_velo[i])*0.125/len(x_coord)
    # Move according to velocities
    for i in range(50):
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
