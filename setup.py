import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="podcast_stats",
    version="0.1.0",
    url="https://github.com/borntyping/cookiecutter-pypackage-minimal",

    author="Niklas Meinzer",
    author_email="github@niklas-meinzer.de",

    description="A script to pull the rss feed for a podcast and run some analysis on it.",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=requirements,

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    entry_points='''
        [console_scripts]
        podcast_stats=podcast_stats.main:run
    '''
)
