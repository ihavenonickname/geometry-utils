from setuptools import setup

from sv_geometry import __version__ as version

setup(
    name='geometry-utils',
    version=version,
    description='A collection of functions for bidimensional and tridimensional arithmetic geometry.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ihavenonickname/geometry-utils',
    author='Gabriel Blank Stift Mousquer',
    author_email='gabrielblanksm@gmail.com',
    license='MIT',
    packages=['geometry_utils'],
    include_package_data=True,
)
