try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Colonials Team Project',
    'author': 'Awilda Lopez, Bala Venkatesan, Faith Bradley, Rebecca Bilbro',
    'url': 'https://github.com/Colonials/capstone.git',
    'download_url': 'https://github.com/Colonials/capstone.git',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'capstone'
}

setup(**config)