from .projectitem import ProjectItem

class Field(ProjectItem):
    def __init__(self, param_type: str, value, value_id: str = None):
        """
        A field for a scratch block
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Blocks
        """
        if isinstance(value, Broadcast) or isinstance(value, Variable) or isinstance(value, List):
            value, value_id = value.name, value.id

        self.value = value
        self.value_id = value_id

        super().__init__(param_type)

    def __repr__(self):
        return f"Field<{self.id}>"

    @property
    def json(self):
        if self.value_id is not None:
            return self.id, [self.value, self.value_id]

        return self.id, [self.value]

    @staticmethod
    def from_json(data, _id: str = None):
        if len(data) > 1:
            value_id = data[1]
        else:
            value_id = None
        return Field(_id, data[0], value_id)