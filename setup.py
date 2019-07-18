import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / 'README.md').read_text()

setup(
    name='sv_geometry',
    version='0.1.1',
    description='A suite of handy geometry-related functions',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/ihavenonickname/sv-geometry',
    author='Gabriel Blank Stift Mousquer',
    author_email='gabrielblanksm@gmail.com',
    license='MIT',
    packages=[
        'sv_geometry.bidimensional',
        'sv_geometry.tridimensional'
    ],
    include_package_data=True,
)
