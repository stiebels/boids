from setuptools import find_packages, setup

setup(name = 'boids',
    version = '1.0',
    description = '',
    author = 'Simon Stiebellehner',
    author_email = 'ucabsti@ucl.ac.uk',
    maintainer = 'Simon Stiebellehner',
    maintainer_email = 'ucabsti@ucl.ac.uk',
    url = 'https://github.com/stiebels/',
    packages = find_packages(exclude=['*test']),
    license = 'MIT',
    install_requires = ['numpy', 'matplotlib', 'argparse', 'pyyaml'],
    scripts= ['scripts/boids']
    )
