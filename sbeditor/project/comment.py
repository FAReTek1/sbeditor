from .projectitem import ProjectItem

class Comment(ProjectItem):
    def __init__(self, _id: str = None, block_id: str = None, pos: tuple[float | int, float | int] = (0, 0),
                 width: float | int = 100, height: float | int = 100, minimized: bool = False, text: str = ''):
        """
        A comment attached to a block
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Comments
        """
        super().__init__(_id)

        self.block_id = block_id
        self.x, self.y = pos
        self.width, self.height = width, height
        self.minimized = minimized
        self.text = text

    def __repr__(self):
        return f"Comment<{self.block_id} @({self.x}, {self.y})>"

    @property
    def json(self):
        return self.id, {
            "blockId": self.block_id,

            "x": self.x,
            "y": self.y,

            "width": self.width,
            "height": self.height,

            "minimized": self.minimized,
            "text": self.text,
        }

    @staticmethod
    def from_json(data, _id: str = None):
        block_id = data["blockId"]

        pos = data["x"], data["y"]
        width, height = data["width"], data["height"]

        minimized = data["minimized"]
        text = data["text"]
        return Comment(_id, block_id, pos, width, height, minimized, text)
