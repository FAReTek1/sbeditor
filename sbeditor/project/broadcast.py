from .projectitem import ProjectItem

class Broadcast(ProjectItem):
    def __init__(self, broadcast_name: str, broadcast_id: str = None):
        """
        Class representing a broadcast.
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Targets
        """
        self.name = broadcast_name
        super().__init__(broadcast_id)

    def __repr__(self):
        return f"Broadcast<{self.name}>"

    @property
    def json(self):
        return self.id, self.name

    @staticmethod
    def from_json(data, _id: str = None):
        return Broadcast(data, _id)