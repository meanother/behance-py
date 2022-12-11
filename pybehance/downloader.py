import pathlib

import httpx
from bs4 import BeautifulSoup

from pybehance.settings import BEHANCE_STORAGE_URL

from typing import Optional, Union


class BehanceDownloader:
    def __init__(self, storage_path: str = BEHANCE_STORAGE_URL, path_to_save: Optional[Union[str, pathlib.Path]] = None):
        self.storage_path = storage_path
        self.pictures: list = []
        self.path_to_save = path_to_save

    def check_path_to_save_exist(self):
        if self.path_to_save:
            if not pathlib.Path(self.path_to_save).is_dir():
                pathlib.Path(self.path_to_save).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _requests(url: str):
        response = httpx.get(url)
        response.raise_for_status()
        return response.text

    def get_pictures_list(self, link: str):
        raw_html = self._requests(link)
        tree = BeautifulSoup(raw_html, "html.parser")

        for _item in tree.find_all('img'):
            try:
                src_set = _item.get("srcset").split(",")
                for _image in src_set:
                    image = _image.strip()
                    if image[:len(self.storage_path)] == self.storage_path:
                        self.pictures.append(image.split()[0])
            except AttributeError:
                pass

    def get_data(self):
        return self.pictures

    def _download(self, link: str):
        with httpx.stream("GET", link) as response:
            file_name = link.split("/")[-1]
            path_to_save = pathlib.Path(self.path_to_save)/file_name if self.path_to_save else file_name
            with open(path_to_save, "wb") as image_file:
                for chunk in response.iter_bytes(chunk_size=1024):
                    if chunk:
                        image_file.write(chunk)

    def download_pictures(self):
        self.check_path_to_save_exist()
        if not self.pictures:
            self.get_data()
        for image_url in self.pictures:
            self._download(image_url)
