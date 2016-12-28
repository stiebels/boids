from argparse import ArgumentParser
from matplotlib import pyplot as plt

'''
This class implements the command line interface.
'''

# DUMMY


def runModule():
    parser = ArgumentParser(description='This package simulates the aggregate motion of a flock of birds.')
    # parser.add_argument(dest='', help='')

    args = parser.parse_args()


if __name__ == '__main__':
    runModule()