"""podcast_stats - A script to pull the rss feed for a podcast and run some analysis on it."""
import feedparser
from datetime import datetime, timedelta
from time import mktime

__version__ = '0.1.0'
__author__ = 'Niklas Meinzer <github@niklas-meinzer.de>'
__all__ = []


def get_parsed_feed(feed_url):
    """
        Pull a podcast rss feed from a given url and calculate
        time between episodes.

        :raises ValueError:
            If the feed does not have all of the required data
    """

    parsed_feed = feedparser.parse(feed_url)
    if parsed_feed is None:
        raise ValueError("No feed could be found")
    last_datetime = None

    episodes = []

    for index, entry in enumerate(reversed(parsed_feed["entries"])):
        struct_time = mktime(entry.published_parsed)
        published_datetime = datetime.fromtimestamp(struct_time)
        if index == 0:
            # use an empty timedelta for the first episode
            time_since_last = timedelta()
        else:
            time_since_last = published_datetime - last_datetime

        episodes.append(
            {
                "title": entry.title,
                "published_datetime": published_datetime,
                "time_since_last": time_since_last,
                "published": True
            }
        )
        last_datetime = published_datetime

    # Add a dummy episode to measure the time from the last episode until now
    episodes.append({
        "title": "[Next unpublished episode]",
        "published_datetime": datetime.now(),
        "time_since_last": datetime.now() - last_datetime,
        "published": False
    })

    return episodes


def weekday_distribution(feed):
    result = [0] * 7

    for entry in feed:
        if entry["published"]:
            result[entry["published_datetime"].weekday()] += 1

    return result
