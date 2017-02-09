from ..Flock import Flock
from mock import patch
import random
import os
import pickle
import yaml


def load_flock_fixture():
    # Loads a predefined Flock object (fixture)
    directory = str(os.path.dirname(os.path.abspath(__file__)) + '/fixtures/')
    file = open(directory+"flock.p",'rb')
    m_Flock = pickle.load(file)
    file.close()
    return m_Flock


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


def test_Flock_init():
    # Tests constructor of class 'Flock'
    random.seed(0)
    t_Flock = Flock(size=50, fly_middle_strength=0.01, fly_away_limit=100, speed_match_strength=0.125,
                    distance_limit=10000,
                    x_coord_range=(-450, 50), y_coord_range=(300, 600),
                    x_velo_range=(0, 10), y_velo_range=(-20, 20))
    m_Flock = load_flock_fixture()

    assert (len(m_Flock.__dict__['boids']) == len(t_Flock.__dict__['boids']))
    assert (m_Flock.__dict__['y_velo_range'] == t_Flock.__dict__['y_velo_range'])
    assert (m_Flock.__dict__['x_velo_range'] == t_Flock.__dict__['x_velo_range'])
    assert (m_Flock.__dict__['y_coord_range'] == t_Flock.__dict__['y_coord_range'])
    assert (m_Flock.__dict__['speed_match_strength'] == t_Flock.__dict__['speed_match_strength'])
    assert (m_Flock.__dict__['distance_limit'] == t_Flock.__dict__['distance_limit'])
    assert (m_Flock.__dict__['x_coord_range'] == t_Flock.__dict__['x_coord_range'])
    assert (m_Flock.__dict__['size'] == t_Flock.__dict__['size'])
    assert (m_Flock.__dict__['fly_away_limit'] == t_Flock.__dict__['fly_away_limit'])
    assert (m_Flock.__dict__['fly_middle_strength'] == t_Flock.__dict__['fly_middle_strength'])


def test_create_boids():
    # Tests function create_boids
    random.seed(0)
    t_Flock = load_flock_test()
    m_Flock = load_flock_fixture()

    for i in range(m_Flock.size):
        for key in m_Flock.boids[i].__dict__:
            try:
                assert (m_Flock.boids[i].__dict__[key] == t_Flock.boids[i].__dict__[key]).all()
            except(AttributeError):
                assert (m_Flock.boids[i].__dict__[key] == t_Flock.boids[i].__dict__[key])


def test_update_boids():
    # Tests function update_boids
    random.seed(0)
    t_Flock = load_flock_test()

    for i in range(t_Flock.size):
        with patch.object(t_Flock.boids[i], 'fly_middle') as m_fly_middle:
            with patch.object(t_Flock.boids[i], 'fly_away') as m_fly_away:
                with patch.object(t_Flock.boids[i], 'match_speed') as m_match_speed:
                    with patch.object(t_Flock.boids[i], 'move') as m_move:
                        t_Flock.update_boids()
                        # Checks that for each boid, each of the function defining the movement is called once
                        assert (m_fly_middle.call_count == 1)
                        assert (m_fly_away.call_count == 1)
                        assert (m_match_speed.call_count == 1)
                        assert (m_move.call_count == 1)





