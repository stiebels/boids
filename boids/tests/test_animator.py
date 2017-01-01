import pickle
import os
import random
from mock import patch
from boids.Animator import Animator


def load_ani_fflock_fixture():
    # Loads a predefined format_flock result
    directory = str(os.path.dirname(os.path.abspath(__file__)) + '/fixtures/')
    file = open(directory+"animator_fflock.p",'rb')
    m_animator_fflock = pickle.load(file)
    file.close()
    return m_animator_fflock


def test_format_flock():
    random.seed(0)
    t_Animator = Animator(size=50, fly_middle_strength=0.01, fly_away_limit=100,
             speed_match_strength=0.125, distance_limit=10000, path=str(os.path.dirname(os.path.abspath(__file__)) + '/test_file.mp4'),
             frames=5, config=False)
    assert(t_Animator.format_flock() == load_ani_fflock_fixture())


def test_Animator_init():
    with patch.object(Animator, '__init__', return_value=None) as m_Animator:
        t_Animator = Animator(size=50, fly_middle_strength=0.01, fly_away_limit=100,
                              speed_match_strength=0.125, distance_limit=10000, path='dummy',
                              frames=5, config=False)
        m_Animator.assert_called_with(size=50, fly_middle_strength=0.01, fly_away_limit=100,
                                      speed_match_strength=0.125, distance_limit=10000, path='dummy',
                                      frames=5, config=False)

