from terminaltables import AsciiTable
import click

from podcast_stats import get_parsed_feed, weekday_distribution

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

    # Draw weekday distribution
    weekday_distr = weekday_distribution(parsed_feed)
    weekday_table_data = [
        ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"], weekday_distr
    ]
    table = AsciiTable(weekday_table_data, title="Weekday Heatmap")
    print("\n")
    print(table.table)

    print("\n")
    # create table data
    table_data = [["Title", "Date published", "Days since last episode"]]
    for episode in sorted(parsed_feed, key=lambda x: x["time_since_last"], reverse=True):
        table_data.append([
            episode["title"], episode["published_datetime"].isoformat(), episode["time_since_last"].days
        ])
    table = AsciiTable(table_data, title="Episodes by days since previous one")
    print(table.table)
