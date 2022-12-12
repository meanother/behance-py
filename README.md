# behance-py
> Free download of pictures from behance.net

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Code Coverage][coverage-image]][coverage-url]
[![Code Quality][quality-image]][quality-url]
[![Downloads](https://static.pepy.tech/personalized-badge/pybehance?period=total&units=international_system&left_color=yellow&right_color=blue&left_text=Downloads)](https://pepy.tech/project/pybehance)
[![Downloads](https://static.pepy.tech/personalized-badge/pybehance?period=month&units=international_system&left_color=green&right_color=red&left_text=Downloads/month)](https://pepy.tech/project/pybehance)
<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/pybehance
[pypi-url]: https://pypi.org/project/pybehance/
[build-image]: https://github.com/meanother/behance-py/actions/workflows/build.yml/badge.svg
[build-url]: https://github.com/meanother/behance-py/actions/workflows/build.yml
[coverage-image]: https://codecov.io/gh/meanother/behance-py/branch/main/graph/badge.svg
[coverage-url]: https://codecov.io/gh/meanother/behance-py
[quality-image]: https://api.codeclimate.com/v1/badges/f4db74d41103b03e0025/maintainability
[quality-url]: https://codeclimate.com/github/meanother/behance-py/maintainability


## Installation
```shell
pip install pybehance
```

## Use

```python
from pybehance import Behance

EXAMPLE_URL = "https://www.behance.net/gallery/157806987/Folio-Reader-Types"

behance = Behance()  # without special path to save pics
behance = Behance(path_to_save="/path/to/save/example_dir")
behance.get_pictures_list(EXAMPLE_URL)

behance.get_data()  # return list
behance.download_pictures()  # download all pictures
```