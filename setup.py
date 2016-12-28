from setuptools import find_packages, setup

setup(name = 'boids',
    version = '0.1',
    description = '',
    author = 'Simon Stiebellehbner',
    author_email = 'ucabsti@ucl.ac.uk',
    maintainer = 'Simon Stiebellehner',
    maintainer_email = 'ucabsti@ucl.ac.uk',
    url = 'https://github.com/stiebels/',
    packages = find_packages(exclude=['*test']),
    license = 'MIT',
    install_requires = ['numpy', 'matplotlib', 'random', 'argparse'],
	scripts= ['scripts/boids']
    )
