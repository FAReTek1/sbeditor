from abc import ABC, abstractmethod
import json


class ProjectItem(ABC):
    """
    Abstract base class with:
    - JSON read/write capabilities
    - An ID which may or may not be useful
    """
    # Thanks to TimMcCool's ScratchAttach v2.0 project_json_capabilities.py module for inspiration of this class

    def __init__(self, _id: str = None):
        self.id = _id

    @staticmethod
    @abstractmethod
    def from_json(data, _id: str = None):
        pass

    @property
    @abstractmethod
    def json(self) -> tuple[dict | list, str | None] | dict:
        pass

    def __repr__(self):
        return f"ProjectItem<{self.id}>"

    def json_str(self):
        return json.dumps(self.json)

    def save_json(self, fp: str = None):
        if fp is None:
            fp = f"ProjectItem{self.id}.json"
        data = self.json
        print(f"Save to {type(self).__name__}? hmm")

        with open(fp, "w", encoding="utf-8") as save_json_file:
            json.dump(data, save_json_file)
