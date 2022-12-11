# behance-py
> Free download of pictures from behance.net

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]

...

<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/pybehance
[pypi-url]: https://pypi.org/project/pybehance/
[build-image]: https://github.com/meanother/behance-py/actions/workflows/build.yml/badge.svg
[build-url]: https://github.com/meanother/behance-py/actions/workflows/build.yml


## Installation
```shell
pip install pybehance
```

## Use

```python
from pybehance import Behance

EXAMPLE_URL = "https://www.behance.net/gallery/157806987/Folio-Reader-Types"

#  behance = Behance() without special path
behance = Behance(path_to_save="/path/to/save/example_dir")
behance.get_pictures_list(EXAMPLE_URL)

behance.get_data()  # return list
behance.download_pictures()  # download all pictures


```