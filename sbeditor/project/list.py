from .projectitem import ProjectItem


class List(ProjectItem):
    def __init__(self, name: str, value: list, list_id: str = None):
        """
        Class representing a list.
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Targets
        """

        self.name = name
        self.value = value
        super().__init__(list_id)

    def __repr__(self):
        return f"List<{self.name} len = {len(self.value)}>"

    @staticmethod
    def from_json(data, _id: str = None):
        return List(data[0], data[1], _id)

    @property
    def json(self):
        return self.id, [self.name, self.value]
