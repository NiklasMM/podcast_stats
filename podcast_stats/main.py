from terminaltables import AsciiTable
import click

from podcast_stats import get_parsed_feed

@click.command()
@click.option('--feed_url', prompt=True)
def run(feed_url):
    """
        Pull a podcast rss feed from a given url and print a table
        with all episodes sorted by time between episodes

        :raises ValueError:
            If the feed does not have all of the required data
    """
    # get the feed and parse it
    parsed_feed = get_parsed_feed(feed_url)

    # create table data
    table_data = [["Title", "Date published", "Days since last episode"]]
    for episode in sorted(parsed_feed, key=lambda x: x["time_since_last"], reverse=True):
        table_data.append([
            episode["title"], episode["published_datetime"], episode["time_since_last"].days
        ])
    table = AsciiTable(table_data)
    print(table.table)
