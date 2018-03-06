from podcast_stats import get_parsed_feed
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
    now = datetime.now()
    feed["entries"].append(
        mock.Mock(
            title="Latest Episode",
            published_parsed=(now - timedelta(days=1)).timetuple()
        )
    )
    feed["entries"].append(
        mock.Mock(
            title="Previous Episode",
            published_parsed=(now - timedelta(days=7)).timetuple()
        )
    )
    feed["entries"].append(
        mock.Mock(
            title="First Episode",
            published_parsed=(now - timedelta(days=20)).timetuple()
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
