from setuptools import setup
from setuptools import find_packages

setup(
    name='playlist_generator',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/blanketastronomer/playlist_generator',
    license='MIT',
    author='blanketastronomer',
    author_email='blanketastronomer@users.noreply.github.com',
    description=' A GUI playlist generator for my commandline music player.',
    python_requires=">=3.6.5",
    entry_points={
        'console_scripts': [
            'playlist_generator = playlist_generator.scripts.run:run'
        ]
    }
)
