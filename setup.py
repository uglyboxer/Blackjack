try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Blackjack Simulator',
    'author': 'Cole Howard',
    'url': 'https://www.github.com/uglyboxer',
    'download_url': 'Where to download it.',
    'author_email': 'uglyboxer@gmail.com',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['blackjack', 'blackjack.packages'],
    'scripts': [],
    'name': 'Blackjack'
}

setup(**config)
