from setuptools import find_packages, setup


setup(name = 'boids',
    version = '1.0.0',
    description = '',
    author = 'Simon Stiebellehner',
    author_email = 'ucabsti@ucl.ac.uk',
    maintainer = 'Simon Stiebellehner',
    maintainer_email = 'ucabsti@ucl.ac.uk',
    url = 'https://github.com/stiebels/',
    packages = find_packages(exclude=['*test']),
    license = 'MIT',
    install_requires = ['numpy', 'matplotlib', 'argparse', 'pyyaml'],
    test_requires=['mock', 'pyyaml'],
    scripts= ['scripts/boids'],
    include_package_data=True,
    package_data = {"":["config.yml"]},
    data_files=[('', ['config.yml'])]
    )
