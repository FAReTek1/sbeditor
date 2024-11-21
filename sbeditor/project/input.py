from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass

from .projectitem import ProjectItem


class Input(ProjectItem):
    def __init__(self, param_type: str, value, input_type: str | int = "string", shadow_status: int = None, *,
                 input_id: str = None,
                 pos: tuple[int | float, int | float] = None, obscurer=None, block: 'Block' = None):
        """
        Input into a scratch block. Can contain reporters
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Blocks
        """
        self.value = None
        self.obscurer = None
        self.pos = None
        self.shadow_idx = None
        self.type_id = None
        self.input_id = None

        self.block = block

        if isinstance(value, Input):
            param_type = value.id
            input_type = value.type_id
            shadow_status = value.shadow_idx
            input_id = value.input_id
            pos = value.pos
            obscurer = value.obscurer

            value = value.value

        super().__init__(param_type)

        if isinstance(obscurer, Block):
            if obscurer.type == "Normal":
                obscurer = obscurer.id
            else:
                obscurer = obscurer.json[1]

        if isinstance(value, Block):
            value = value.id
            input_type = "block"

        if isinstance(value, Broadcast) or isinstance(value, Variable) or isinstance(value, List):
            input_type = type(value).__name__.lower()

            value, input_id = value.name, value.id

        if isinstance(input_type, str):
            self.type_id = INPUT_CODES[input_type.lower()]
        else:
            self.type_id = input_type

        self.input_id = input_id
        self.value = value

        if obscurer is not None:
            shadow_status = 3

        elif shadow_status is None:
            shadow_status = 1

        self.shadow_idx = shadow_status
        #  self.input_id = input_id
        self.pos = pos

        self.obscurer = obscurer

    @property
    def shadow_status(self):
        return (None,
                "shadow",
                "no shadow",
                "shadow obscured by input"
                )[self.shadow_idx]

    @property
    def type_str(self) -> str:
        keys = tuple(INPUT_CODES.keys())
        values = tuple(INPUT_CODES.values())

        return keys[values.index(self.type_id)]

    def __repr__(self):
        return f"Input<{self.id}>"

    @staticmethod
    def from_json(data, _id: str = None):
        shadow_idx = data[0]

        if shadow_idx == 3:
            # If it's an obscured input, the second value is the id of the obscuring block
            inp = data[2]
            obscurer = data[1]
        else:
            inp = data[1]
            obscurer = None

        if isinstance(inp, list):
            inp_id = None
            pos = None
            if inp[0] > 10:
                # If it's a broadcast, variable or list
                inp_id = inp[2]

                if len(inp) > 3:
                    # If it also has additional attributes, that is the position
                    pos = inp_id[3:5]

            # This is a 'block'
            return Input(_id, inp[1], inp[0], shadow_status=shadow_idx, input_id=inp_id, pos=pos, obscurer=obscurer)
        else:
            # The value parameter is just a block id
            return Input(_id, data[1], "block", shadow_status=shadow_idx, obscurer=obscurer)

    @property
    def target(self):
        return self.block.target

    @property
    def value_obj(self):
        if self.type_str == "broadcast":
            print(self.input_id)
            return self.target.get_broadcast_by_id(self.input_id)
        if self.type_str == "variable":
            print(self.input_id)
            return self.target.get_var_by_id(self.input_id)
        if self.type_str == "list":
            print(self.input_id)
            return self.target.get_list_by_id(self.input_id)
        return self.value

    @property
    def json(self):
        value = self.value
        if self.type_str == "block":
            # If it's a block id, then the value is not an array, just a block id
            inp = value
        else:
            if self.type_str in ("broadcast", "variable", "list"):
                vo = self.value_obj
                if vo is None:
                    value = ''
                    self.type_id = 8
                    self.value = ''
                    self.input_id = None
                else:
                    value = vo.name

            inp = [self.type_id, value]

            if self.input_id is not None:
                inp.append(self.input_id)

            if self.pos is not None and self.type_id > 11:
                inp += list(self.pos)

        if self.shadow_idx == 3:
            return self.id, (self.shadow_idx, self.obscurer, inp)

        return self.id, (self.shadow_idx, inp)