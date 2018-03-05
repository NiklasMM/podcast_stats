podcast_stats
=============

A script to pull the rss feed for a podcast and run some analysis on it.

Usage
-----
 	podcast_stats --feed_url <url>
 
 or just `podcast_stats` and it will ask you for the url.
 
Installation
------------

Clone the repo (or download it, or whatever... I'm not your dad).

	git clone https://github.com/NiklasMM/podcast_stats.git

Install with pip. I recommend doing this in a virtualenv.

	pip install podcast_stats

#### Requirements

podcast_stats uses the following packages from pypi (they will be installed automatically):

* [click](https://pypi.python.org/pypi/click) - for the cli
* [feedparser](https://pypi.python.org/pypi/feedparser/5.2.1) - to parse the RSS feeds
* [terminaltables](https://pypi.python.org/pypi/terminaltables/3.1.0) - to display the data nicely

Example
-------------
If you try it with the very good podcast [Geek News Radio](http://sixgun.org/geeknewsradio/), like this:

	podcast_stats --feed_url http://sixgun.org/feed/gnr/
	
You should see something like this:

```
+-----------------------------------------------------+----------------+-------------------------+
| Title                                               | Date published | Days since last episode |
+-----------------------------------------------------+----------------+-------------------------+
| GNR 30 – It’s Been a Long Road                      | 2017-01-20     | 44                      |
| GNR 48 – Fungal Warp                                | 2017-11-12     | 42                      |
| GNR 54 – Absolutely Holdened It                     | 2018-01-19     | 28                      |
| GNR 56 – Terrible at Torpedoes                      | 2018-02-25     | 27                      |
| GNR 36 – Immortal Jellyfish                         | 2017-04-25     | 26                      |
| GNR 22 – What is Game?                              | 2016-09-03     | 23                      |
| GNR 42 – This is How the Board Game Democracy Falls | 2017-07-20     | 23                      |
| GNR 26 – Grab Them by the Zapus                     | 2016-10-22     | 20                      |
| GNR 46 – Schleichfahrting Around                    | 2017-09-24     | 19                      |
| GNR 8 – Spending Time with Landing Gear             | 2016-02-25     | 19                      |
| GNR 10 – The Dark Zone                              | 2016-03-22     | 19                      |
| GNR 19 – Power Armour Gone Up its Own Arse          | 2016-07-14     | 18                      |
| GNR 16 – Gun Bants                                  | 2016-06-09     | 18                      |
| GNR 27 – The End Times                              | 2016-11-09     | 18                      |
| GNR 40 – Grimdark                                   | 2017-06-10     | 17                      |
| GNR 25 – Choose the Oud                             | 2016-10-02     | 17                      |
| GNR 34 – Slow Burn                                  | 2017-03-14     | 17                      |
| GNR 29 – Tanksplaining                              | 2016-12-06     | 17                      |
| GNR 4 – Give Me Nexus or Give Me Death              | 2016-01-07     | 16                      |
| GNR 15 – Peak Silicon Valley                        | 2016-05-22     | 16                      |
| GNR 45 – Sigmarines and Twig People                 | 2017-09-04     | 16                      |
| GNR 41 – Dank Millennium                            | 2017-06-26     | 15                      |
| GNR 43 – Plunkbag                                   | 2017-08-05     | 15                      |
| GNR 13 – Thanks, Obama                              | 2016-04-23     | 14                      |
| GNR 35 – More Mass, More Effect                     | 2017-03-29     | 14                      |
| GNR 44 – How to Launch Naval Invasions              | 2017-08-19     | 14                      |
| GNR 33 – The Harbinger of Doom Bar                  | 2017-02-25     | 14                      |
| GNR 20 – Fucked Up Beyond All Redemption            | 2016-07-28     | 13                      |
| GNR 5 – Bitcoin is Fucked                           | 2016-01-21     | 13                      |
| GNR 21 – Unrelenting Fury                           | 2016-08-10     | 13                      |
| GNR 14 – Will the Real Satoshi Please Stand Up      | 2016-05-06     | 12                      |
| GNR 2 – The P in SPECIAL                            | 2015-12-15     | 12                      |
| GNR 6 – Wa Du-Showxa ere Lang Belta                 | 2016-02-02     | 11                      |
| GNR 12 – Air as a Service                           | 2016-04-08     | 11                      |
| GNR 50 – if (fuckYou()) fuckYou();                  | 2017-12-02     | 11                      |
| GNR 31 – The White Russian Incident                 | 2017-01-31     | 11                      |
| GNR 18 – Engineering Challenge                      | 2016-06-26     | 10                      |
| GNR 32 – Reverse Hardness                           | 2017-02-11     | 10                      |
| GNR 37 – One Serving of Proto-Paste a Day           | 2017-05-05     | 10                      |
| GNR 28 – Pro-Penis Patch                            | 2016-11-19     | 10                      |
| GNR 39 – Permanent HOTAS                            | 2017-05-23     | 9                       |
| GNR 49 – Columbo on the Orient Express              | 2017-11-21     | 9                       |
| GNR 55 – Fancy Blondes                              | 2018-01-28     | 8                       |
| GNR 52 – HOTAS for Life                             | 2017-12-17     | 8                       |
| GNR 38 – Space Prole Revolution                     | 2017-05-13     | 8                       |
| [Next unpublished episode]                          | unknown        | 7                       |
| GNR 24 – Metalbants                                 | 2016-09-14     | 6                       |
| GNR 9 – Make XCOM Great Again                       | 2016-03-03     | 6                       |
| GNR 3 – Powered by Pure Plot                        | 2015-12-22     | 6                       |
| GNR 47 – Literally Littoral                         | 2017-09-30     | 6                       |
| GNR 51 – Mexican Standoff with Turtles              | 2017-12-08     | 6                       |
| GNR 17 – Total Warbants                             | 2016-06-15     | 5                       |
| GNR 11 – The Hundred Euro Pencil                    | 2016-03-28     | 5                       |
| GNR 53 – Ahab’s Quest                               | 2017-12-22     | 5                       |
| GNR 7 – Lara’s Hair                                 | 2016-02-06     | 4                       |
| GNR 23 – Forge World Dash Button                    | 2016-09-07     | 4                       |
| GNR 1 – What the Fuck                               | 2015-12-03     | 0                       |
+-----------------------------------------------------+----------------+-------------------------+

```

Licence
-------
MIT 

Authors
-------

`podcast_stats` was written by `Niklas Meinzer <github@niklas-meinzer.de>`_.
