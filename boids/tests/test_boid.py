from ..Flock import Flock
from ..Boid import Boid
import pickle
import random
import os
import yaml


def load_flock_test():
    # Generates flock object based on config file, i.e. allows specification of test case using the yaml config file
    directory = str(os.path.dirname(os.path.abspath(__file__)))[:-11]
    config_yml = yaml.safe_load(open(directory + 'config.yml'))
    size = config_yml['flock_size']
    fly_middle_strength = config_yml['fly_middle_strength']
    fly_away_limit = config_yml['fly_away_limit']
    speed_match_strength = config_yml['speed_match_strength']
    distance_limit = config_yml['distance_limit']
    x_velo_range = config_yml['x_velo_range']
    y_velo_range = config_yml['y_velo_range']
    x_coord_range = config_yml['x_coord_range']
    y_coord_range = config_yml['y_coord_range']
    t_Flock = Flock(size, fly_middle_strength, fly_away_limit, speed_match_strength, distance_limit,
                       x_coord_range, y_coord_range, x_velo_range, y_velo_range)
    return t_Flock


def load_boid_fixture():
    # Loads a predefined Boid object (fixture)
    directory = str(os.path.dirname(os.path.abspath(__file__)) + '/fixtures/')
    file = open(directory+"boid.p",'rb')
    m_Boid = pickle.load(file)
    file.close()
    return m_Boid


def load_flock_fixture():
    # Loads a predefined Flock object (fixture)
    directory = str(os.path.dirname(os.path.abspath(__file__)) + '/fixtures/')
    file = open(directory+"flock.p",'rb')
    m_Flock = pickle.load(file)
    file.close()
    return m_Flock


def test_Boid_init():
    # Tests constructor of class 'Boid'
    m_Boid = load_boid_fixture()
    t_Boid = Boid(x_coordinate=-100, y_coordinate=400, x_velocity=5, y_velocity=10)

    for key in m_Boid.__dict__:
        try:
            assert(m_Boid.__dict__[key] == t_Boid.__dict__[key]).all()
        except(AttributeError):
            assert(m_Boid.__dict__[key] == t_Boid.__dict__[key])


def test_fly_middle():
    # Tests function match_speed by comparing return array (i.e. computation result) to fixture
    random.seed(0)
    t_Flock = load_flock_test()
    m_Flock = load_flock_fixture()

    for i in range(m_Flock.size):
        assert(t_Flock.boids[i].velocity == m_Flock.boids[i].velocity).all()
        m_Flock.boids[i].fly_middle(m_Flock, t_Flock.fly_middle_strength)
        t_Flock.boids[i].fly_middle(t_Flock, t_Flock.fly_middle_strength)
        assert(t_Flock.boids[i].velocity == m_Flock.boids[i].velocity).all()


def test_fly_away():
    # Tests function match_speed by comparing return array (i.e. computation result) to fixture
    random.seed(0)
    t_Flock = load_flock_test()
    m_Flock = load_flock_fixture()

    for i in range(m_Flock.size):
        assert(t_Flock.boids[i].velocity == m_Flock.boids[i].velocity).all()
        m_Flock.boids[i].fly_away(m_Flock, t_Flock.fly_away_limit)
        t_Flock.boids[i].fly_away(t_Flock, t_Flock.fly_away_limit)
        assert(t_Flock.boids[i].velocity == m_Flock.boids[i].velocity).all()


def test_match_speed():
    # Tests function match_speed by comparing return array (i.e. computation result) to fixture
    random.seed(0)
    t_Flock = load_flock_test()
    m_Flock = load_flock_fixture()

    for i in range(m_Flock.size):
        assert(t_Flock.boids[i].velocity == m_Flock.boids[i].velocity).all()
        m_Flock.boids[i].match_speed(m_Flock, t_Flock.speed_match_strength, t_Flock.distance_limit)
        t_Flock.boids[i].match_speed(t_Flock, t_Flock.speed_match_strength, t_Flock.distance_limit)
        assert(t_Flock.boids[i].velocity == m_Flock.boids[i].velocity).all()


def test_move():
    # Tests function match_speed by comparing computation result to fixture
    random.seed(0)
    t_Flock = load_flock_test()
    m_Flock = load_flock_fixture()
    for i in range(m_Flock.size):
        assert(t_Flock.boids[i].x_coord == m_Flock.boids[i].x_coord)
        assert(t_Flock.boids[i].y_coord == m_Flock.boids[i].y_coord)
        m_Flock.boids[i].move()
        t_Flock.boids[i].move()
        assert(t_Flock.boids[i].x_coord == m_Flock.boids[i].x_coord)
        assert(t_Flock.boids[i].y_coord == m_Flock.boids[i].y_coord)


