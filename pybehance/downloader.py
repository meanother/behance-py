"""
Base downloader module
"""
import logging
from pathlib import Path
from typing import Optional, Union

import httpx
from bs4 import BeautifulSoup  # type: ignore

from pybehance.settings import BEHANCE_STORAGE_URL

logger = logging.getLogger(__name__)


class BehanceDownloader:
    """
    Attributes
    ----------
        storage_path : str
        path_to_save : Optional[Union[str, Path]]
    """

    def __init__(
        self,
        storage_path: str = BEHANCE_STORAGE_URL,
        path_to_save: Optional[Union[str, Path]] = None,
    ):
        self.storage_path = storage_path
        self.pictures: list = []
        self.path_to_save = path_to_save

    def check_path_to_save_exist(self):
        """check if path is not None and if dir exists, else mkdir"""
        if self.path_to_save:
            if not Path(self.path_to_save).is_dir():
                Path(self.path_to_save).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _requests(url: str):
        """make http request, return str"""
        response = httpx.get(url)
        response.raise_for_status()
        return response.text

    def get_pictures_list(self, link: str) -> list:
        """collect list of picture urls"""
        self.pictures = []
        raw_html = self._requests(link)
        tree = BeautifulSoup(raw_html, "html.parser")

        for _item in tree.find_all("img"):
            try:
                src_set = _item.get("srcset").split(",")
                for _image in src_set:
                    image = _image.strip()
                    if image[: len(self.storage_path)] == self.storage_path:
                        self.pictures.append(image.split()[0])
            except AttributeError:
                pass
        logger.info(f"url {link} has {len(self.pictures)} pictures")
        return self.pictures

    def get_data(self) -> list:
        """return pictures list"""
        return self.pictures

    def _download(self, link: str):
        """download one picture"""
        logger.info(f"Download image from url: {link}")
        with httpx.stream("GET", link) as response:
            file_name = link.split("/")[-1]
            path_to_save = Path(self.path_to_save) / file_name if self.path_to_save else file_name
            with open(path_to_save, "wb") as image_file:  # type: ignore
                for chunk in response.iter_bytes(chunk_size=1024):
                    if chunk:
                        image_file.write(chunk)
        logger.info(f"image {image_file} saved to {path_to_save}")

    def download_pictures(self):
        """download all puctures from link"""
        logger.info("Start download pictures")
        self.check_path_to_save_exist()
        if not self.pictures:
            logger.warning(f"pictures list is empty, pls use `get_pictures_list(example behance url)` method")
        for image_url in self.pictures:
            self._download(image_url)
