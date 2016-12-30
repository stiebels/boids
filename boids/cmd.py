from argparse import ArgumentParser
from boids.Animator import Animator

'''
This class implements the command line interface.
'''

def runModule():
    parser = ArgumentParser(description='This package simulates the aggregate motion of a flock.')
    parser.add_argument('-c', dest='config', default=False, type=str, help='Uses pre-defined config file to specify parameters (True/False; default: False). Overwrites all other input parameters except saving the animation.')
    parser.add_argument('-s', dest='size', default=50, type=int, help='Specifies size of flock, i.e. number of flock members (default: 50)')
    parser.add_argument('-fm', dest='fly_middle_strength', default=0.01, type=float, help='Specifies how strongly flock members are attracted to center (default: 0.01)')
    parser.add_argument('-fa', dest='fly_away_limit', default=100, type=float, help='Specifies distance limit for flying away from other flock members. If flock member is within this limit to other member it flies away from it (default: 100)')
    parser.add_argument('-sm', dest='speed_match_strength', default=0.125, type=float, help='Specifies how strongly flock member match speed of other members (default: 0.125)')
    parser.add_argument('-dl', dest='distance_limit', default=10000, type=float, help='Specifies distance limit for speed matching. If flock member is within this limit to other member it matches its speed accordingly (default: 10000)')
    parser.add_argument('-p', dest='path', default=None, type=str, help='If animation should be saved, specify path here (e.g. /home/usr/boids.mp4 | default: None)')
    parser.add_argument('-f', dest='frames', default=450, help='Specify duration/length of animation in number of frames (default: 450)')

    args = parser.parse_args()
    Animator(size=args.size, fly_middle_strength=args.fly_middle_strength, fly_away_limit=args.fly_away_limit,
             speed_match_strength=args.speed_match_strength, distance_limit=args.distance_limit, path=args.path,
             frames=args.frames, config=args.config)

if __name__ == '__main__':
    runModule()