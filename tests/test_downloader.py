from unittest import mock

from pytest_httpx import HTTPXMock
from pybehance.downloader import BehanceDownloader


def test_check_path():
    behance = BehanceDownloader()
    assert behance.path_to_save is None


def test_check_special_path():
    behance = BehanceDownloader(path_to_save="/Users/arty/code/behance-py")
    assert behance.path_to_save == "/Users/arty/code/behance-py"


def test_request(httpx_mock: HTTPXMock):
    url = "https://www.behance.net/gallery/157806987/Folio-Reader-Types"
    behance = BehanceDownloader()
    #
    expected = "example text"
    httpx_mock.add_response(
        method="GET",
        url=url,
        status_code=200,
        text="example text"
    )
    actual = behance._requests(url)
    assert actual == expected


def test_get_data():
    url = "https://www.behance.net/gallery/157806987/Folio-Reader-Types"
    behance = BehanceDownloader()
    behance.get_pictures_list(url)
    data = behance.get_data()
    assert type(data) == list
    assert len(data) == 9

