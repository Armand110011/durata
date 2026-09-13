import re

# seconds per unit
_UNITS = {
    "s": 1,
    "m": 60,
    "h": 3600,
    "d": 86400,
    # BUG: "w" (weeks) is documented in the README but missing here,
    # so parse("2w") raises ValueError instead of returning 1209600.
}

_TOKEN = re.compile(r"(\d+)([a-z])")


def parse(text: str) -> int:
    """Parse a human duration like '1h30m' into whole seconds."""
    if not isinstance(text, str):
        raise ValueError("duration must be a string")
    cleaned = text.strip().replace(" ", "").lower()
    if not cleaned:
        raise ValueError("empty duration")

    total = 0
    pos = 0
    for match in _TOKEN.finditer(cleaned):
        if match.start() != pos:
            raise ValueError(f"malformed duration: {text!r}")
        value, unit = int(match.group(1)), match.group(2)
        if unit not in _UNITS:
            raise ValueError(f"unknown unit {unit!r} in {text!r}")
        total += value * _UNITS[unit]
        pos = match.end()

    if pos != len(cleaned):
        raise ValueError(f"malformed duration: {text!r}")
    return total


def humanize(seconds: int) -> str:
    """Format a number of seconds as a compact duration string."""
    if not isinstance(seconds, int) or seconds < 0:
        raise ValueError("seconds must be a non-negative integer")
    if seconds == 0:
        return "0s"

    parts = []
    for unit in ("d", "h", "m", "s"):
        size = _UNITS[unit]
        qty, seconds = divmod(seconds, size)
        if qty:
            parts.append(f"{qty}{unit}")
    return "".join(parts)
