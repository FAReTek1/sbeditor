from .projectitem import ProjectItem


class Variable(ProjectItem):
    def __init__(self, name: str, value, is_cloud_var: bool = False, var_id: str = None):
        """
        Class representing a variable.
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Targets
        """
        super().__init__(var_id)

        self.name = name
        self.value = value
        self.is_cloud_var = is_cloud_var

    def __repr__(self):
        if self.is_cloud_var:
            return f"CVar<{self.name} = {self.value}>"
        else:
            return f"Var<{self.name} = {self.value}>"

    @staticmethod
    def from_json(data, _id: str = None):
        name = data[0]
        value = data[1]
        is_cloud_var = False
        if len(data) > 2:
            is_cloud_var = data[2]

        return Variable(name, value, is_cloud_var, var_id=_id)

    @property
    def json(self) -> tuple[dict | list, str | None]:
        if self.is_cloud_var:
            return [self.name, self.value, True], self.id

        return [self.name, self.value], self.id
