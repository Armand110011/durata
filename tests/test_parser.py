import pytest

from durata import parse, humanize


@pytest.mark.parametrize(
    "text,expected",
    [
        ("30s", 30),
        ("5m", 300),
        ("1h30m", 5400),
        ("2d12h", 216000),
        ("1d 6h", 108000),
    ],
)
def test_parse_ok(text, expected):
    assert parse(text) == expected


def test_humanize_roundtrip():
    assert humanize(5400) == "1h30m"
    assert humanize(0) == "0s"


@pytest.mark.parametrize("bad", ["", "abc", "10x", "1h!"])
def test_parse_rejects_garbage(bad):
    with pytest.raises(ValueError):
        parse(bad)
