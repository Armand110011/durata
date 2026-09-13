# durata

[![CI](https://github.com/OWNER/durata/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/durata/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/durata.svg)](https://pypi.org/project/durata/)
[![Python](https://img.shields.io/pypi/pyversions/durata.svg)](https://pypi.org/project/durata/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Tiny, dependency-free parser for human-friendly durations. Turn `"1h30m"` into
seconds and back again.

```python
from durata import parse, humanize

parse("1h30m")     # 5400
parse("2d12h")     # 216000
parse("2w")        # 1209600
humanize(5400)     # "1h30m"
```

## Install

```bash
pip install durata
```

## Supported units

| Unit | Meaning |
|------|---------|
| `s`  | seconds |
| `m`  | minutes |
| `h`  | hours   |
| `d`  | days    |
| `w`  | weeks   |

Units may be combined (`"1d6h"`) and repeated components are summed. Whitespace
is ignored.

## API

- `parse(text: str) -> int` — parse a duration string to whole seconds.
- `humanize(seconds: int) -> str` — format seconds as a compact duration string.

Both raise `ValueError` on malformed input.

## Contributing

Bug reports and PRs welcome — please open an issue with a minimal repro first.
Run the suite with `pytest`.

## License

MIT © 2026 durata contributors
