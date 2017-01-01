from boids.Flock import Flock
from boids.Boid import Boid
import pickle
import random
import os


def load_boid_fixture():
    # Loads a predefined Boid object

    directory = str(os.path.dirname(os.path.abspath('__file__')) + '/fixtures/')
    directory = '/home/sist/PycharmProjects/MPHYG001_assignment-2/boids/tests/fixtures/'
    print(directory)
    file = open(directory+"boid.p",'rb')
    m_Boid = pickle.load(file)
    file.close()
    return m_Boid


def load_flock_fixture():
    # Loads a predefined Boid object

    directory = str(os.path.dirname(os.path.abspath('__file__')) + '/fixtures/')
    directory = '/home/sist/PycharmProjects/MPHYG001_assignment-2/boids/tests/fixtures/'
    print(directory)
    file = open(directory+"flock.p",'rb')
    m_Flock = pickle.load(file)
    file.close()
    return m_Flock


def test_Boid_init():
    m_Boid = load_boid_fixture()
    t_Boid = Boid(x_coordinate=-100, y_coordinate=400, x_velocity=5, y_velocity=10)
    for key in m_Boid.__dict__:
        try:
            assert(m_Boid.__dict__[key] == t_Boid.__dict__[key]).all()
        except(AttributeError):
            assert(m_Boid.__dict__[key] == t_Boid.__dict__[key])


def test_fly_middle():
    random.seed(0)
    t_Flock = Flock(size=50, fly_middle_strength=0.01, fly_away_limit=100, speed_match_strength=0.125, distance_limit=10000,
                               x_coord_range=(-450, 50), y_coord_range=(300, 600),
                               x_velo_range=(0, 10), y_velo_range=(-20, 20))
    m_Flock = load_flock_fixture()
    for i in range(m_Flock.size):
        assert(t_Flock.boids[i].velocity == m_Flock.boids[i].velocity).all()
        m_Flock.boids[i].fly_middle(m_Flock, t_Flock.fly_middle_strength)
        t_Flock.boids[i].fly_middle(t_Flock, t_Flock.fly_middle_strength)
        assert(t_Flock.boids[i].velocity == m_Flock.boids[i].velocity).all()


def test_fly_away():
    random.seed(0)
    t_Flock = Flock(size=50, fly_middle_strength=0.01, fly_away_limit=100, speed_match_strength=0.125, distance_limit=10000,
                               x_coord_range=(-450, 50), y_coord_range=(300, 600),
                               x_velo_range=(0, 10), y_velo_range=(-20, 20))
    m_Flock = load_flock_fixture()
    for i in range(m_Flock.size):
        assert(t_Flock.boids[i].velocity == m_Flock.boids[i].velocity).all()
        m_Flock.boids[i].fly_away(m_Flock, t_Flock.fly_away_limit)
        t_Flock.boids[i].fly_away(t_Flock, t_Flock.fly_away_limit)
        assert(t_Flock.boids[i].velocity == m_Flock.boids[i].velocity).all()


def test_match_speed():
    random.seed(0)
    t_Flock = Flock(size=50, fly_middle_strength=0.01, fly_away_limit=100, speed_match_strength=0.125, distance_limit=10000,
                               x_coord_range=(-450, 50), y_coord_range=(300, 600),
                               x_velo_range=(0, 10), y_velo_range=(-20, 20))
    m_Flock = load_flock_fixture()
    for i in range(m_Flock.size):
        assert(t_Flock.boids[i].velocity == m_Flock.boids[i].velocity).all()
        m_Flock.boids[i].match_speed(m_Flock, t_Flock.speed_match_strength, t_Flock.distance_limit)
        t_Flock.boids[i].match_speed(t_Flock, t_Flock.speed_match_strength, t_Flock.distance_limit)
        assert(t_Flock.boids[i].velocity == m_Flock.boids[i].velocity).all()


def test_move():
    random.seed(0)
    t_Flock = Flock(size=50, fly_middle_strength=0.01, fly_away_limit=100, speed_match_strength=0.125, distance_limit=10000,
                               x_coord_range=(-450, 50), y_coord_range=(300, 600),
                               x_velo_range=(0, 10), y_velo_range=(-20, 20))
    m_Flock = load_flock_fixture()
    for i in range(m_Flock.size):
        assert(t_Flock.boids[i].x_coord == m_Flock.boids[i].x_coord)
        assert(t_Flock.boids[i].y_coord == m_Flock.boids[i].y_coord)
        m_Flock.boids[i].move()
        t_Flock.boids[i].move()
        assert(t_Flock.boids[i].x_coord == m_Flock.boids[i].x_coord)
        assert(t_Flock.boids[i].y_coord == m_Flock.boids[i].y_coord)


