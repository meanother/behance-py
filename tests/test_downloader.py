from unittest import mock

from pytest_httpx import HTTPXMock
from pybehance.downloader import BehanceDownloader


def test_check_path():
    behance = BehanceDownloader()
    assert behance.path_to_save is None


def test_check_special_path():
    behance = BehanceDownloader(path_to_save="/Users/arty/code/behance-py")
    assert behance.path_to_save == "/Users/arty/code/behance-py"
