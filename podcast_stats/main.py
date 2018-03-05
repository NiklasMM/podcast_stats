import feedparser
from time import mktime
from datetime import datetime, timedelta
from terminaltables import AsciiTable
import click


@click.command()
@click.option('--feed_url', prompt=True)
def run(feed_url):
    """
        Pull a podcast rss feed from a given url and print a table
        with all episodes sorted by time between episodes
    """
    # get the feed and parse it
    d = feedparser.parse(feed_url)

    last_datetime = None

    episodes = []

    for index, entry in enumerate(reversed(d["entries"])):
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
                "published_datetime": published_datetime.strftime("%Y-%m-%d"),
                "time_since_last": time_since_last
            }
        )
        last_datetime = published_datetime

    # Add a dummy episode to measure the time from the last episode until now
    episodes.append({
        "title": "[Next unpublished episode]",
        "published_datetime": "unknown",
        "time_since_last": datetime.now() - last_datetime
    })

    # create table data
    table_data = [["Title", "Date published", "Days since last episode"]]
    for episode in sorted(episodes, key=lambda x: x["time_since_last"], reverse=True):
        table_data.append([
            episode["title"], episode["published_datetime"], episode["time_since_last"].days
        ])
    table = AsciiTable(table_data)
    print(table.table)
