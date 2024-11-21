from .projectitem import ProjectItem

import requests
from zipfile import ZipFile
from pathlib import Path
import os
from hashlib import md5


class Asset(ProjectItem):
    def __init__(self, asset_id: str = None,
                 name: str = "Cat",
                 file_name: str = "b7853f557e4426412e64bb3da6531a99.svg",
                 data_format: str = None,
                 load_method: str = "url"):
        """
        Represents a generic asset. Can be a sound or an image.
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Assets
        """
        if asset_id is None:
            asset_id = file_name.split('.')[0]
        if data_format is None:
            data_format = file_name.split('.')[1]

        super().__init__(asset_id)

        self.name = name
        self.file_name = file_name

        self.data_format = data_format

        self.load_method = load_method

    def __repr__(self):
        return f"Asset<{self.name}: {self.id}>"

    @staticmethod
    def from_json(data, _id: str = None):
        _id = data["assetId"]

        name = data["name"]
        file_name = data["md5ext"]

        data_format = data["dataFormat"]
        return Asset(_id, name, file_name, data_format)

    @property
    def json(self):
        return {
            "name": self.name,

            "assetId": self.id,
            "md5ext": self.file_name,
            "dataFormat": self.data_format,
        }

    def download(self, fp: str = None):
        if fp is None:
            fp = self.name
        if not fp.endswith(f".{self.data_format}"):
            fp += f".{self.data_format}"

        # Downloading {self} to {fp}...

        directory = Path(fp).parent
        if self.file_name in os.listdir(directory):
            # We already have the file {self.file_name}!
            return

        content = ''
        # Downloading using load method: {self.load_method}
        if self.load_method == "url":
            # Requesting https://assets.scratch.mit.edu/internalapi/asset/{self.file_name}/get/"
            rq = requests.get(f"https://assets.scratch.mit.edu/internalapi/asset/{self.file_name}/get/")

            # Requested with status code: {rq.status_code}
            if rq.status_code != 200:
                raise ValueError(f"Can't download asset {self.file_name}\nIs not uploaded to scratch!")

            content = rq.content

        elif isinstance(self.load_method, list):
            # Downloading with a list-type load method
            load_type, load_path = self.load_method
            if load_type == "zip":
                # Extracting {self.file_name} from zip: {load_path}
                with ZipFile(load_path, "r") as achv:
                    content = achv.read(self.file_name)

        with open(fp, "wb") as asset_file:
            asset_file.write(content)

    @staticmethod
    def load_from_file(fp: str, name: str = None):
        image_types = ("png", "jpg", "jpeg", "svg")
        sound_types = ("wav", "mp3")

        split = fp.split(".")
        file_ext = split[-1]
        if name is None:
            name = '.'.join(split[:-1])

        if file_ext not in image_types and file_ext not in sound_types:
            raise ValueError(f"Unsupported file type: {file_ext}")

        with open(fp, "rb") as asset_file:
            md5_hash = md5(asset_file.read()).hexdigest()

        md5ext = f"{md5_hash}.{file_ext}"
        asset_json = {
            "assetId": md5_hash,
            "name": name,
            "md5ext": md5ext,
            "dataFormat": file_ext
        }

        if file_ext in image_types:
            # Bitmap resolution can be omitted,
            # Rotation center will just be (0, 0) because we can do that
            # The user can change the rotation center if they want though
            asset_json["rotationCenterX"] = 0
            asset_json["rotationCenterY"] = 0
            asset = Costume.from_json(asset_json)
        else:
            # No need to work out sample rate or count
            asset = Sound.from_json(asset_json)
        asset.load_method = "path", fp


class Costume(Asset):
    def __init__(self, _id: str = None,
                 name: str = "Cat",
                 file_name: str = "b7853f557e4426412e64bb3da6531a99.svg",
                 data_format: str = None,

                 bitmap_resolution=None,
                 rotation_center_x: int | float = 0,
                 rotation_center_y: int | float = 0):
        """
        A costume. An asset with additional properties
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Costumes
        """
        super().__init__(_id, name, file_name, data_format)

        self.bitmap_resolution = bitmap_resolution
        self.rotation_center_x = rotation_center_x
        self.rotation_center_y = rotation_center_y

    def __repr__(self):
        return f"Costume<{self.name}: {self.id}>"

    @staticmethod
    def from_json(data, _id: str = None):
        _id = data["assetId"]

        name = data["name"]
        file_name = data["md5ext"]

        data_format = data["dataFormat"]

        bitmap_resolution = data.get("bitmapResolution")

        rotation_center_x = data["rotationCenterX"]
        rotation_center_y = data["rotationCenterY"]

        return Costume(_id, name, file_name, data_format, bitmap_resolution, rotation_center_x, rotation_center_y)

    @property
    def json(self):
        _json = super().json
        if self.bitmap_resolution is not None:
            _json["bitmapResolution"] = self.bitmap_resolution

        _json["rotationCenterX"] = self.rotation_center_x
        _json["rotationCenterY"] = self.rotation_center_y

        return _json

    @staticmethod
    def new():
        return Costume.from_json({
            "name": "costume1",
            "assetId": "b7853f557e4426412e64bb3da6531a99",
            "md5ext": "b7853f557e4426412e64bb3da6531a99.svg",
            "dataFormat": "svg",
            "bitmapResolution": 1,
            "rotationCenterX": 48,
            "rotationCenterY": 50
        })


class Sound(Asset):
    def __init__(self, _id: str = None,
                 name: str = "pop",
                 file_name: str = "83a9787d4cb6f3b7632b4ddfebf74367.wav",
                 data_format: str = None,

                 rate: int = None,
                 sample_count: int = None):
        """
        A sound. An asset with additional properties
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Sounds
        """
        super().__init__(_id, name, file_name, data_format)

        self.rate = rate
        self.sample_count = sample_count

    def __repr__(self):
        return f"Sound<{self.name}: {self.id}>"

    @staticmethod
    def from_json(data, _id: str = None):
        _id = data["assetId"]

        name = data["name"]
        file_name = data["md5ext"]

        data_format = data["dataFormat"]

        rate = data.get("rate")
        sample_count = data.get("sampleCount")

        return Sound(_id, name, file_name, data_format, rate, sample_count)

    @property
    def json(self):
        _json = super().json
        if self.rate is not None:
            _json["rate"] = self.rate

        if self.sample_count is not None:
            _json["sampleCount"] = self.sample_count

        return _json
