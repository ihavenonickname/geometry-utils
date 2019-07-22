from setuptools import setup

from sv_geometry import __version__ as version

setup(
    name='sv-geometry',
    version=version,
    description='A collection of functions for bidimensional and tridimensional arithmetic geometry.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ihavenonickname/sv-geometry',
    author='Gabriel Blank Stift Mousquer',
    author_email='gabrielblanksm@gmail.com',
    license='MIT',
    packages=['sv_geometry'],
    include_package_data=True,
)
