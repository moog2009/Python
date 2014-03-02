# -*- coding: utf-8 -*-

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'ex46',
	'author': 'gaosy',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'gaosy@',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex46'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)