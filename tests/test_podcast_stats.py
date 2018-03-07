from podcast_stats import get_parsed_feed, weekday_distribution
from podcast_stats.main import run

from unittest import mock
import pytest
from datetime import datetime, timedelta
from click.testing import CliRunner

@pytest.fixture
def dummy_feed():
    feed = {
        "entries": []
    }
    # we start on a Sunday
    start = datetime(2017, 1, 1)
    feed["entries"].append(
        mock.Mock(
            title="Latest Episode",
            # this episode is on a Saturday
            published_parsed=(start - timedelta(days=1)).timetuple()
        )
    )
    feed["entries"].append(
        mock.Mock(
            title="Previous Episode",
            # this episode is on a Sunday
            published_parsed=(start - timedelta(days=7)).timetuple()
        )
    )
    feed["entries"].append(
        mock.Mock(
            title="First Episode",
            # this episode is on a Monday
            published_parsed=(start - timedelta(days=20)).timetuple()
        )
    )
    return feed

def test_get_feed(dummy_feed):
    with mock.patch("podcast_stats.feedparser.parse", return_value=dummy_feed):
        feed = get_parsed_feed("")

    assert 4 == len(feed)
    assert "[Next unpublished episode]" == feed[-1]["title"]

def test_get_invalid_feed():
    with mock.patch("podcast_stats.feedparser.parse", return_value=None):
        with pytest.raises(ValueError):
            get_parsed_feed("")

def test_cli(dummy_feed):
    runner = CliRunner()
    with mock.patch("podcast_stats.feedparser.parse", return_value=dummy_feed):
        result = runner.invoke(run, ['--feed_url', 'http://feed.url'])
    assert result.exit_code == 0

def test_week_day_distribution(dummy_feed):
    with mock.patch("podcast_stats.feedparser.parse", return_value=dummy_feed):
        feed = get_parsed_feed("")

    weekday_distr = weekday_distribution(feed)

    assert weekday_distr[0] == 1
    assert weekday_distr[1] == 0
    assert weekday_distr[2] == 0
    assert weekday_distr[5] == 1
    assert weekday_distr[6] == 1
