from .projectitem import ProjectItem
import warnings
from ..utils.consts import EXTENSIONS


class Extension(ProjectItem):
    def __init__(self, _id: str):
        """
        Represents an extension found in the extension key in project.json
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Projects
        :param _id: code of the extension, e.g. pen
        """
        self.name = None
        super().__init__(_id)

        if _id in EXTENSIONS.keys():
            # Valid code
            self.is_standard = True
            self.name = EXTENSIONS[_id]
        else:
            # Non-standard extension
            self.is_standard = False

            warnings.warn(f"{_id} is not a standard extension code")

    def __repr__(self):
        return f"Ext<{self.id}>"

    @staticmethod
    def from_json(data, _id: str = None):
        return Extension(data)

    @property
    def json(self):
        return self.id
