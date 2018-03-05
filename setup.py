import setuptools

setuptools.setup(
    name="podcast_stats",
    version="0.1.0",
    url="https://github.com/borntyping/cookiecutter-pypackage-minimal",

    author="Niklas Meinzer",
    author_email="github@niklas-meinzer.de",

    description="A script to pull the rss feed for a podcast and run some analysis on it.",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=['feedparser', 'terminaltables', 'click'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    entry_points='''
        [console_scripts]
        podcast_stats=podcast_stats.main:run
    '''
)
