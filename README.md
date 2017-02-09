# The Boids Package

The Boids is a software package written in Python that was created and packaged as part of the assessment of the course MPHYG001 at University College London:
http://github-pages.ucl.ac.uk/rsd-engineeringcourse/

The package simulates the flight of a flock, displaying it in an animated plot.

The Boids package includes the following main classes:

1. <b><code>Boid</code></b> - This class incorporates the flying behaviour of the boids and their movement.
2. <b><code>Flock</code></b> - This class acts as a controlling instance that creates and updates the boid instances.
3. <b><code>Animator</code></b> - This class incorporates the plotting and animation behaviour.


<b>Description of the command line interface:</b>

```
usage: boids [-h] [-c CONFIG] [-s SIZE] [-fm FLY_MIDDLE_STRENGTH]
             [-fa FLY_AWAY_LIMIT] [-sm SPEED_MATCH_STRENGTH]
             [-dl DISTANCE_LIMIT] [-p PATH] [-f FRAMES]

This package simulates the aggregate motion of a flock.

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG             Uses pre-defined config file to specify parameters (1
                        (true) / 0 (false); default: 0 (false)). Overwrites
                        all other input parameters except saving the
                        animation.
  -s SIZE               Specifies size of flock, i.e. number of flock members
                        (default: 50)
  -fm FLY_MIDDLE_STRENGTH
                        Specifies how strongly flock members are attracted to
                        center (default: 0.01)
  -fa FLY_AWAY_LIMIT    Specifies distance limit for flying away from other
                        flock members. If flock member is within this limit to
                        other member it flies away from it (default: 100)
  -sm SPEED_MATCH_STRENGTH
                        Specifies how strongly flock member match speed of
                        other members (default: 0.125)
  -dl DISTANCE_LIMIT    Specifies distance limit for speed matching. If flock
                        member is within this limit to other member it matches
                        its speed accordingly (default: 10000)
  -p PATH               If animation should be saved, specify path here (e.g.
                        /home/usr/boids.mp4 | default: None)
  -f FRAMES             Specify duration/length of animation in number of
                        frames (default: 450)

```