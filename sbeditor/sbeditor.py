"""
Module for parsing and building sb3 files by https://scratch.mit.edu/users/faretek1/
Reference: https://en.scratch-wiki.info/wiki/Scratch_File_Format
"""

import json
import math
import os
import shutil
from abc import ABC, abstractmethod
from hashlib import md5
from pathlib import Path
from zipfile import ZipFile

import requests
from linkcheck.logger.none import NoneLogger


class ProjectItem(ABC):
    """
    Abstract base class with:
    - JSON read/write capabilities
    - An ID which may or may not be useful

    Thanks to TimMcCool's ScratchAttach v2.0 project_json_capabilities.py module for inspiration of this class
    """

    def __init__(self, _id: str = None):
        self.id = _id

    @staticmethod
    @abstractmethod
    def from_json(data, _id: str = None):
        pass

    @abstractmethod
    def to_json(self) -> tuple[dict | list, str | None] | dict:
        pass

    def __repr__(self):
        return f"ProjectItem<{self.id}>"

    def json_str(self):
        return json.dumps(self.to_json())

    def save_json(self, fp: str = None):
        if fp is None:
            fp = f"ProjectItem{self.id}.json"
        data = self.to_json()

        with open(fp, "w", encoding="utf-8") as f:
            json.dump(data, f)


def digits_of(base: int):
    i = 48
    digits = ''
    while len(digits) < base:
        if 57 < i < 65:
            i += 1
            continue
        if i > 90:
            raise ValueError("0-9 and A-Z only support up to 43 digits!")
        digits += chr(i)
        i += 1
    return digits


def b10_to_base(b10_val: float, base: int, *, digits: iter = None, res: int = 12):
    if digits is None:
        digits = digits_of(base)
    digits = tuple(digits)

    if b10_val == 0:
        return digits[0]

    log = int(math.log(b10_val, base)) + 1
    whole_val = b10_val
    ret = ''

    for _ in range(log):
        rem = whole_val % base
        ret = digits[int(rem)] + ret

        whole_val //= base

    b10_val = b10_val % 1
    if b10_val == 0:
        return ret
    ret += '.'

    for _ in range(res):
        b10_val = b10_val * base
        ret += digits[int(b10_val)]
        b10_val %= 1

    return ret


ID_DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\"£$%^&*()-_+=[]{}:;'@#~,.?<>/\\|`¬¦"
ID_BASE = len(ID_DIGITS)

EXTENSIONS = {"boost": "LEGO BOOST Extension",
              "ev3": "LEGO MINDSTORMS EV3 Extension",
              "gdxfor": "Go Direct Force & Acceleration Extension",
              "makeymakey": "Makey Makey Extension",
              "microbit": "micro:bit Extension",
              "music": "Music Extension",
              "pen": "Pen Extension",
              "text2speech": "Text to Speech Extension",
              "translate": "Translate Extension",
              "videoSensing": "Video Sensing Extension",
              "wedo2": "LEGO Education WeDo 2.0 Extension"}

INPUT_CODES = {"null": 1,
               "block": 2,
               "number": 4,
               "positive number": 5,
               "positive integer": 6,
               "integer": 7,
               "angle": 8,
               "color": 9,
               "string": 10,
               "broadcast": 11,
               "variable": 12,
               "var": 12,
               "list": 13}

EDIT_META = True


def obfuscate_str(string: str):
    return md5(string.encode("utf-8")).hexdigest()


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

    def to_json(self) -> tuple[dict | list, str | None]:
        if self.is_cloud_var:
            return [self.name, self.value, True], self.id

        return [self.name, self.value], self.id


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

    def to_json(self):
        return self.id, [self.name, self.value]


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

    def to_json(self):
        return self.id, self.name

    @staticmethod
    def from_json(data, _id: str = None):
        return Broadcast(data, _id)


class Mutation(ProjectItem):
    def __init__(self, tag_name: str = "mutation", children: list = None,
                 proc_code: str = None, argument_ids: list[str] = None, warp: bool = None,
                 argument_names: list[str] = None, argument_defaults: list = None,
                 has_next: bool = None, *, _id: str = None):
        """
        Mutation for Control:stop block and procedures
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Mutations
        """
        # It's helpful to store the opcode with it
        if children is None:
            children = []

        super().__init__(_id)
        assert tag_name == "mutation"

        self.tag_name = tag_name
        self.children = children

        self.proc_code = proc_code
        self.argument_ids = argument_ids
        self.warp = warp

        self.argument_names = argument_names
        self.argument_defaults = argument_defaults

        self.has_next = has_next

    @staticmethod
    def from_json(data, _id: str = None):
        def load(key):
            value = data.get(key)
            if isinstance(value, str):
                return json.loads(value)
            return value

        return Mutation(
            data["tagName"],

            data["children"],
            # Seems to always be an empty array.

            data.get("proccode"),
            load("argumentids"),
            load("warp"),
            #  ^^ Same as 'run without screen refresh'

            load("argumentnames"),
            load("argumentdefaults"),

            load("hasnext"), _id=_id
        )

    def parse_proc_code(self):
        token = ''
        tokens = []
        last_char = ''

        for char in self.proc_code:
            if last_char == '%':
                if char in "sb":
                    # If we've hit an %s or %b
                    token = token[:-1]
                    # Clip the % sign off the token

                    if token != '':
                        # Make sure not to append an empty token
                        tokens.append(token)

                    # Add the parameter token
                    tokens.append(f"%{char}")
                    token = ''
                    continue

            token += char
            last_char = char

        if token != '':
            tokens.append(token)

        return tokens

    def obfuscate_proc_code(self):

        proc_code = ''
        for token in self.parse_proc_code():
            if token not in ("%s", "%b"):
                proc_code += obfuscate_str(token)
            else:
                proc_code += ' ' + token + ' '
        self.proc_code = proc_code

    def obfuscate_argument_names(self):
        for i, argument_name in enumerate(self.argument_names):
            self.argument_names[i] = obfuscate_str(argument_name)

    def __repr__(self):
        return f"Mutation<{self.id}>"

    def to_json(self):
        ret = {
            "tagName": self.tag_name,
            "children": self.children,
        }

        if self.proc_code is not None:
            ret["proccode"] = self.proc_code
            ret["argumentids"] = json.dumps(self.argument_ids)
            ret["warp"] = json.dumps(self.warp)

            if self.argument_names is not None:
                ret["argumentnames"] = json.dumps(self.argument_names)
                ret["argumentdefaults"] = json.dumps(self.argument_defaults)
        if self.has_next is not None:
            ret["hasnext"] = json.dumps(self.has_next)

        return ret


class Input(ProjectItem):
    def __init__(self, param_type: str, value, input_type: str | int = "string", shadow_status: int = None, *,
                 input_id: str = None,
                 pos: tuple[int | float, int | float] = None, obscurer: str = None):
        """
        Input into a scratch block. Can contain reporters
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Blocks
        """
        super().__init__(param_type)

        if isinstance(obscurer, Block):
            if obscurer.type == "Normal":
                obscurer = obscurer.id
            else:
                obscurer = obscurer.to_json()[1]

        if isinstance(value, Block):
            value = value.id
            input_type = "block"

        if isinstance(value, Broadcast) or isinstance(value, Variable) or isinstance(value, List):
            input_type = type(value).__name__.lower()
            # print(f"Setting type to {input_type}")

            value, input_id = value.name, value.id

        if isinstance(input_type, str):
            self.type_id = INPUT_CODES[input_type.lower()]
        else:
            self.type_id = input_type

        self.value = value

        if obscurer is not None:
            shadow_status = 3
        elif shadow_status is None:
            shadow_status = 1

        self.shadow_idx = shadow_status
        self.input_id = input_id
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
    def type_str(self):
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

    def to_json(self):
        value = self.value
        if self.type_str == "block":
            # If it's a block id, then the value is not an array, just a block id
            inp = value
        else:
            inp = [self.type_id, value]

            if self.input_id is not None:
                inp.append(self.input_id)

            if self.pos is not None and self.type_id > 11:
                inp += list(self.pos)

        if self.shadow_idx == 3:
            return self.id, (self.shadow_idx, self.obscurer, inp)

        return self.id, (self.shadow_idx, inp)


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

    def to_json(self):
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


class Block(ProjectItem):
    def __init__(self, block_id: str | None = None,
                 opcode: str = None, next_block: str = None, parent_block: str = None, inputs: list[Input] = None,
                 fields: list[Field] = None, shadow: bool = False, pos: tuple[float | int, float | int] = None,
                 comment: str = None, mutation: Mutation = None,

                 *, array: list = None, target=None, can_next: bool = True):
        """
        A block. This can be a normal block, a shadow block or an array-type block (in json)
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Blocks
        """
        if array is not None:
            self.type_id = array[0]

            keys = tuple(INPUT_CODES.keys())
            vals = tuple(INPUT_CODES.values())
            self.type = keys[vals.index(self.type_id)]
            super().__init__(self.type)

            if self.type_id < 11:
                self.value = array[1]
            else:
                self.name = array[1]
                self.item_id = array[2]
                if self.type_id > 11:
                    # Only variables and lists can have positions
                    if len(array) >= 5:
                        self.x, self.y = array[3:5]
                    elif pos is not None:
                        self.x, self.y = pos
                    else:
                        self.x, self.y = None, None
        else:
            if inputs is None:
                inputs = []
            if fields is None:
                fields = []

            super().__init__(block_id)

            self.type = "Normal"

            self.opcode = opcode
            self.next = next_block
            self.parent = parent_block
            self.inputs = inputs
            self.fields = fields
            self.is_shadow = shadow
            self.top_level = parent_block is None

            if not self.top_level:
                pos = (None, None)
            elif pos is None:
                pos = (0, 0)

            self.x, self.y = pos
            self.mutation = mutation
            self.comment_id = comment

            self.base_can_next = can_next

            target: Target
            self.target = target

    @staticmethod
    def from_input(inp: Input, *, adjust_to_default_pos: bool=True):
        if inp.pos is None and adjust_to_default_pos:
            inp.pos = (0, 0)

        if inp.type_str == "block":
            return inp.to_json()[0]

        return Block(array=inp.to_json()[1][-1])

    @property
    def can_next(self):
        if self.opcode != "control_stop":
            return self.base_can_next
        else:
            return self.mutation.has_next

    def __repr__(self):
        if self.type == "Normal":
            return f"Block<{self.opcode}, id={self.id}>"
        else:
            if hasattr(self, "id"):
                return f"Block<{self.type}, id={self.id}>"
            return f"Block<{self.type}, no id>"

    def to_json(self) -> tuple | list:
        if self.type != "Normal":
            _json = [self.type_id]

            if self.type_id < 11:
                # Numbers, colors & strings
                _json.append(self.value)
            else:
                # Broadcasts, variables & lists
                _json.append(self.name)
                _json.append(self.item_id)

            if self.x is not None and self.y is not None:
                _json.append(self.x)
                _json.append(self.y)

            return self.id, _json

        ret = {
            "opcode": self.opcode,
            "next": self.next,
            "parent": self.parent,

            "shadow": self.is_shadow,
            "topLevel": self.parent is None,
        }

        if not self.can_next:
            print(self, "can't next:", self.__dict__)

            ret["next"] = None

        if self.parent is None:
            ret["x"] = self.x
            ret["y"] = self.y

        if self.comment_id is not None:
            ret["comment"] = self.comment_id

        inputs = {}
        for input_ in self.inputs:
            input_json = input_.to_json()
            inputs[input_json[0]] = input_json[1]
        ret["inputs"] = inputs

        fields = {}
        for field in self.fields:
            field_json = field.to_json()

            fields[field_json[0]] = field_json[1]
        ret["fields"] = fields

        if hasattr(self, "mutation"):
            if self.mutation is not None:
                ret["mutation"] = self.mutation.to_json()

        return self.id, ret

    @staticmethod
    def from_json(data, _id: str = None):
        # Type ids            | e2                            | e3     | e3                  | e4
        # ------------------------------------------------------------------------------------------------------------
        # 4. Number           |                               |        |                      |                      |
        # 5. Positive number  |                               |        |                      |                      |
        # 6. Positive integer | The Value                     |        |                      |                      |
        # 7. Integer          |                               |        |                      |                      |
        # 8. Angle            |                               |        |                      |                      |
        # -----------------------------------------------------        |                      |                      |
        # 9. Color            | '#' followed by a hexadecimal |        |                      |                      |
        #                     | numeral representing the color|        |                      |                      |
        # -----------------------------------------------------        |                      |                      |
        # 10. String          | The Value                     |        |                      |                      |
        # --------------------------------------------------------------                      |                      |
        # 11. Broadcast       |                               |        |----------------------|----------------------|
        # 12. Variable        | The name                      | The ID | x-coord if top level | y-coord if top level |
        # 13. List            |                               |        |                      |                      |

        if isinstance(data, list):
            type_id = data[0]

            # block_type = tuple(INPUT_CODES.values())[type_id]
            if type_id < 11:
                # Numbers, colors & strings
                value = data[1]
                return Block(array=[type_id, value])
            else:
                # Broadcasts, variables & lists
                name = data[1]
                item_id = data[2]

                x, y = None, None
                if type_id > 11:
                    # Only variables and lists can have positions
                    if len(data) >= 5:
                        x, y = data[3:5]

                return Block(array=[type_id, name, item_id], pos=(x, y))
        else:
            data: dict
            # block_type = "Normal"

            opcode = data["opcode"]

            next_ = data["next"]
            parent = data["parent"]

            inputs_json = data["inputs"]
            inputs = []
            for input_id, input_json in inputs_json.items():
                inputs.append(Input.from_json(input_json, input_id))

            fields_json = data["fields"]
            fields = []
            for field_id, field_json in fields_json.items():
                fields.append(Field.from_json(field_json, field_id))

            is_shadow = data["shadow"]

            top_level = data["topLevel"]
            if top_level:
                x, y = data['x'], data['y']
            else:
                x, y = None, None

            if "mutation" in data:
                mutation = Mutation.from_json(data["mutation"], opcode)
            else:
                mutation = None

            comment_id = data.get("comment")

            return Block(_id, opcode, next_, parent, inputs, fields, is_shadow, (x, y), comment_id, mutation)

    def add_input(self, inp: Input):
        if self.type != "Normal":
            raise ValueError("Can't add inputs to an array block!")

        self.inputs.append(inp)

        return self

    def add_field(self, field: Field):
        if self.type != "Normal":
            raise ValueError("Can't add fields to an array block!")

        self.fields.append(field)
        return self

    def add_mutation(self, mutation: Mutation):
        if self.type != "Normal":
            raise ValueError("Can't add mutations to an array block!")
        self.mutation = mutation
        return self

    @staticmethod
    def generic(opcode: str, parent=None, next_=None, shadow: bool = False,
                pos: tuple[float | int, float | int] = None):
        if isinstance(parent, Block):
            parent = parent.id

        if isinstance(next_, Block):
            next_ = next_.id

        return Block(None, opcode, next_, parent, shadow=shadow, pos=pos)

    def attached_block(self):
        if self.type != "Normal":
            return
        elif self.next is None:
            return

        return self.target.get_block_by_id(self.next)

    def parent_block(self):
        if self.type != "Normal":
            return
        elif self.parent is None:
            return

        return self.target.get_block_by_id(self.parent)

    def attached_chain(self):
        chain = [self]
        while True:
            attached_block = chain[-1].attached_block()
            if attached_block in chain:
                break
            elif attached_block is None:
                break

            chain.append(attached_block)
        return chain

    def attach(self, block: 'Block'):
        self.target.add_block(block)

        my_next = self.target.get_block_by_id(self.next)

        block.parent = self.id
        block.next = self.next
        block.target = self.target

        self.next = block.id

        if my_next is not None:
            my_next.parent = block.id
        return block

    def link_inputs(self):
        for input_ in self.inputs:
            if input_.type_str == "block":
                block = self.target.get_block_by_id(input_.value)

                block.parent = self.id
            if input_.obscurer is not None:
                obscurer = self.target.get_block_by_id(input_.obscurer)
                obscurer.parent = self.id

            # else:
            #     print(f"bad input {input_} - {input_.type_str}")

    def attach_chain(self, chain: ['Block']):
        b = self
        for block in chain:
            b = b.attach(block)
            block.link_inputs()

    def previous_chain(self):
        chain = [self]
        while True:
            prev = chain[-1]
            parent = prev.parent_block()
            if parent in chain:
                break
            elif parent is None:
                break
            elif parent.next != prev.id:
                # This is about previously STACKED blocks, not nested ones
                break

            chain.append(parent)
        chain.reverse()
        return chain

    def stack_chain(self):
        return self.previous_chain()[0:-1] + self.attached_chain()

    def parent_chain(self):
        chain = [self]
        while True:
            parent = chain[-1].parent_block()
            if parent in chain:
                break
            elif parent is None:
                break

            chain.append(parent)
        chain.reverse()
        return chain

    def get_category(self):
        if self.type != "Normal":
            return self.type
        split = self.opcode.split('_')
        return split[0]


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

    def to_json(self):
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


class Asset(ProjectItem):
    def __init__(self, asset_id: str,
                 name: str = "b7853f557e4426412e64bb3da6531a99",
                 file_name: str = "b7853f557e4426412e64bb3da6531a99.svg",
                 data_format: str = "svg",
                 load_method: str = "url"):
        """
        Represents a generic asset. Can be a sound or an image.
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Assets
        """
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

    def to_json(self):
        return {
            "name": self.name,

            "assetId": self.id,
            "md5ext": self.file_name,
            "dataFormat": self.data_format,
        }

    def download(self, fp: str = None) -> int:
        if fp is None:
            fp = self.name
        if not fp.endswith(f".{self.data_format}"):
            fp += f".{self.data_format}"

        # print('-' * 20)
        # print(f"Downloading {self} to {fp}...")

        directory = Path(fp).parent
        if self.file_name in os.listdir(directory):
            # print(f"We already have the file {self.file_name}!")
            return

        content = ''
        # print(f"Downloading using load method: {self.load_method}")
        if self.load_method == "url":
            # print(f"Requesting https://assets.scratch.mit.edu/internalapi/asset/{self.file_name}/get/")
            rq = requests.get(f"https://assets.scratch.mit.edu/internalapi/asset/{self.file_name}/get/")

            # print(f"Requested with status code: {rq.status_code}")
            if rq.status_code != 200:
                raise ValueError(f"Can't download asset {self.file_name}\nIs not uploaded to scratch!")

            content = rq.content

        elif isinstance(self.load_method, list):
            # print(f"Downloading with a list-type load method")
            load_type, load_path = self.load_method
            if load_type == "zip":
                # print(f"Extracting {self.file_name} from zip: {load_path}")
                with ZipFile(load_path, "r") as achv:
                    content = achv.read(self.file_name)

        with open(fp, "wb") as f:
            f.write(content)

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

        with open(fp, "rb") as f:
            md5_hash = md5(f.read()).hexdigest()

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
    def __init__(self, _id: str = "b7853f557e4426412e64bb3da6531a99",
                 name: str = "Cat",
                 file_name: str = "b7853f557e4426412e64bb3da6531a99.svg",
                 data_format: str = "svg",

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

    def to_json(self):
        _json = super().to_json()
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
    def __init__(self, _id: str = "83a9787d4cb6f3b7632b4ddfebf74367",
                 name: str = "pop",
                 file_name: str = "83a9787d4cb6f3b7632b4ddfebf74367.wav",
                 data_format: str = "wav",

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

    def to_json(self):
        _json = super().to_json()
        if self.rate is not None:
            _json["rate"] = self.rate

        if self.sample_count is not None:
            _json["sampleCount"] = self.sample_count

        return _json


class Target(ProjectItem):
    def __init__(self, is_stage: bool = False, name: str = '', variables: list[Variable] = None,
                 lists: list[List] = None, broadcasts: list[Broadcast] = None, blocks: list[Block] = None,
                 comments: list[Comment] = None, current_costume: int = 0, costumes: list[Costume] = None,
                 sounds: list[Sound] = None,
                 layer_order: int = 1, volume: int | float = 100, tempo: int | float = 60, video_state: str = "off",
                 video_transparency: int | float = 50, text_to_speech_language: str = "en", visible: bool = True,
                 x: int | float = 0,
                 y: int | float = 0, size: int | float = 100, direction: int | float = 90, draggable: bool = False,
                 rotation_style: str = "all around", project: 'Project' = None):
        """
        Represents a sprite or the stage
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Targets
        """
        if name is None:
            name = ''
        elif name in ("_random_", "_mouse_", "_edge_", "_myself_"):
            raise ValueError(f"Sprite is not allowed to be called '{name}'")

        if variables is None:
            variables = []
        if lists is None:
            lists = []
        if broadcasts is None:
            broadcasts = []
        if blocks is None:
            blocks = []
        if comments is None:
            comments = []
        if costumes is None:
            costumes = [Costume()]
        if sounds is None:
            sounds = [Sound()]

        super().__init__(f"{int(is_stage)}{name}")

        self.is_stage = is_stage
        self.name = name
        self.variables = variables
        self.lists = lists
        self.broadcasts = broadcasts
        self.blocks = blocks
        for block in self.blocks:
            block.target = self

        self.comments = comments
        self.current_costume = current_costume
        self.costumes = costumes
        self.sounds = sounds
        self.layer_order = layer_order
        self.volume = volume
        self.tempo = tempo
        self.video_state = video_state
        self.video_transparency = video_transparency
        self.text_to_speech_language = text_to_speech_language
        self.visible = visible
        self.x, self.y = x, y
        self.size = size
        self.direction = direction
        self.draggable = draggable
        self.rotation_style = rotation_style

        self.project = project

    def set_asset_load_method(self, load_method: str | list[str] = "url"):
        for asset in self.assets():
            asset.load_method = load_method

    @staticmethod
    def from_json(data, _id: str = None):
        is_stage = data["isStage"]
        name = data["name"]

        json_variables = data["variables"]
        variables = []
        for var_id, array in json_variables.items():
            variables.append(Variable.from_json(array, var_id))

        json_lists = data["lists"]
        lists = []
        for list_id, list_array in json_lists.items():
            lists.append(List.from_json(list_array, list_id))

        json_broadcasts = data["broadcasts"]
        broadcasts = []
        for broadcast_id, broadcast_name in json_broadcasts.items():
            broadcasts.append(Broadcast.from_json(broadcast_name, broadcast_id))

        json_blocks = data["blocks"]
        blocks = []
        for block_id, block in json_blocks.items():
            blocks.append(Block.from_json(block, block_id))

        json_comments = data["comments"]
        comments = []
        for comment_id, comment in json_comments.items():
            comments.append(Comment.from_json(comment, comment_id))

        current_costume = data["currentCostume"]

        json_costumes = data["costumes"]
        costumes = []
        for costume in json_costumes:
            costumes.append(Costume.from_json(costume))

        json_sounds = data["sounds"]
        sounds = []
        for sound in json_sounds:
            sounds.append(Sound.from_json(sound))

        layer_order = data.get("layerOrder")
        if layer_order is None:
            layer_order = 1

        volume = data["volume"]

        tempo, video_state, video_transparency, text_to_speech_language = (None,) * 4
        visible, x, y, size, direction, draggable, rotation_style = (None,) * 7

        if is_stage:
            tempo = data["tempo"]
            video_state = data["videoState"]
            video_transparency = data["videoTransparency"]
            text_to_speech_language = data["textToSpeechLanguage"]

        else:
            visible = data["visible"]
            x = data["x"]
            y = data["y"]
            size = data["size"]
            direction = data["direction"]
            draggable = data["draggable"]
            rotation_style = data["rotationStyle"]
        return Target(is_stage, name, variables, lists, broadcasts, blocks, comments, current_costume, costumes, sounds,
                      layer_order, volume, tempo, video_state, video_transparency, text_to_speech_language, visible, x,
                      y, size, direction, draggable, rotation_style)

    def assets(self):
        return self.costumes + self.sounds

    def get_broadcast_by_name(self, name: str):
        for broadcast in self.broadcasts:
            if broadcast.name == name:
                return broadcast

    def get_broadcast_by_id(self, _id: str):
        if _id is None:
            return

        for broadcast in self.broadcasts:
            if broadcast.id == _id:
                return broadcast

    def get_blocks_by_opcode(self, opcode: str):
        if opcode is None:
            return
        blocks = []
        for block in self.blocks:
            if block.opcode == opcode:
                blocks.append(block)
        return blocks

    def get_block_by_id(self, block_id: str):
        if block_id is None:
            return

        for block in self.blocks:
            if block.id == block_id:
                return block

    def __repr__(self):
        if self.is_stage:
            return f"Stage<Bg #{self.current_costume}>"
        else:
            return f"Sprite<'{self.name}' @({self.x}, {self.y})>"

    @staticmethod
    def from_sprite3(fp: str):
        with ZipFile(fp, "r") as spr3:
            sprite_json = json.loads(spr3.read("sprite.json"))

        target = Target.from_json(sprite_json)
        target.set_asset_load_method(["zip", fp])
        return target

    def export(self, fp: str, make_zip: bool = True):
        os.makedirs(fp, exist_ok=True)

        for asset in self.assets():
            asset.download(f"{fp}\\{asset.id}")

        with open(f"{fp}\\sprite.json", "w", encoding="utf-8") as f:
            json.dump(self.to_json(), f)

        if not make_zip:
            return

        with ZipFile(f"{fp}.sprite3", "w") as achv:
            for file in os.listdir(fp):
                achv.write(f"{fp}\\{file}", arcname=file)

    def to_json(self):
        _json = {
            "isStage": self.is_stage,
            "name": self.name,
            "currentCostume": self.current_costume,
            "volume": self.volume,
            "layerOrder": self.layer_order,
        }

        if self.is_stage:
            _json["tempo"] = self.tempo
            _json["videoTransparency"] = self.video_transparency
            _json["videoState"] = self.video_state
            _json["textToSpeechLanguage"] = self.text_to_speech_language
        else:
            _json["visible"] = self.visible

            _json["x"] = self.x
            _json["y"] = self.y
            _json["size"] = self.size
            _json["direction"] = self.direction

            _json["draggable"] = self.draggable
            _json["rotationStyle"] = self.rotation_style

        variables = {}
        for variable in self.variables:
            var_json = variable.to_json()
            variables[var_json[1]] = var_json[0]
        _json["variables"] = variables

        lists = {}
        for list_ in self.lists:
            list_json = list_.to_json()
            lists[list_json[0]] = list_json[1]
        _json["lists"] = lists

        broadcasts = {}
        for broadcast in self.broadcasts:
            broadcast_json = broadcast.to_json()
            broadcasts[broadcast_json[0]] = broadcast_json[1]
        _json["broadcasts"] = broadcasts

        blocks = {}
        for block in self.blocks:
            block_json = block.to_json()
            blocks[block_json[0]] = block_json[1]
        _json["blocks"] = blocks

        comments = {}
        for comment in self.comments:
            comment_json = comment.to_json()
            comments[comment_json[0]] = comment_json[1]
        _json["comments"] = comments

        costumes = []
        for costume in self.costumes:
            costumes.append(costume.to_json())
        _json["costumes"] = costumes

        sounds = []
        for sound in self.sounds:
            sounds.append(sound.to_json())
        _json["sounds"] = sounds

        return _json

    @staticmethod
    def new_stage(tts_lang: str = "English"):
        return Target(is_stage=True, name="Stage", text_to_speech_language=tts_lang)

    @staticmethod
    def new_sprite(name: str = "Blank"):
        return Target(name=name)

    def broadcast_ids(self):
        ids = []
        for broadcast in self.broadcasts:
            ids.append(broadcast.id)
        return ids

    def variable_ids(self):
        ids = []
        for variable in self.variables:
            ids.append(variable.id)
        return ids

    def list_ids(self):
        ids = []
        for list_ in self.lists:
            ids.append(list_.id)
        return ids

    def block_ids(self):
        ids = []
        for block in self.blocks:
            if hasattr(block, "id"):
                ids.append(block.id)
        return ids

    def comment_ids(self):
        ids = []
        for comment in self.comments:
            ids.append(comment.id)
        return ids

    def all_ids(self):
        return self.variable_ids() + self.list_ids() + self.block_ids() + self.comment_ids() + self.broadcast_ids()

    def project_ids(self):
        ids = []
        for target in self.project.targets:
            ids += target.all_ids()
        return ids

    def new_id(self):
        i = 0
        all_ids = self.project_ids()

        new_id = None
        while new_id in all_ids \
                or new_id is None:
            new_id = b10_to_base(i, ID_BASE, digits=ID_DIGITS)
            i += 1

        return new_id

    def add_block(self, new_block: Block):
        """
        Adds a block. Will not attach it to other scripts
        """
        new_block.id = self.new_id()

        new_block.target = self

        self.blocks.append(new_block)

        return new_block

    def add_variable(self, name: str, value=0, is_cloud_var: bool = False):
        var_id = self.new_id()
        var = Variable(name, value, is_cloud_var, var_id)
        self.variables.append(var)

        return var

    def add_list(self, name: str, value: list = None):
        if value is None:
            value = []

        list_id = self.new_id()
        _list = List.from_json([name, value], list_id)
        self.lists.append(_list)

        return _list

    def add_broadcast(self, name):
        broadcast_id = self.new_id()
        broadcast = Broadcast(name, broadcast_id)
        self.broadcasts.append(broadcast)
        return broadcast

    def obfuscate(self, del_comments: bool = True):
        for variable in self.variables:
            variable.name = obfuscate_str(variable.name)

        for list_ in self.lists:
            list_.name = obfuscate_str(list_.name)

        for block in self.blocks:
            if block.type == "Normal":
                if block.opcode == "procedures_prototype":
                    block.mutation.obfuscate_proc_code()
                    block.mutation.obfuscate_argument_names()

                elif block.opcode == "procedures_call":
                    if block.mutation.proc_code not in (
                            "​​log​​ %s",
                            "​​breakpoint​​",
                            "​​error​​ %s",
                            "​​warn​​ %s"
                    ):
                        block.mutation.obfuscate_proc_code()

                elif block.opcode in ("argument_reporter_string_number",
                                      "argument_reporter_boolean"):
                    for field in block.fields:
                        if field.id == "VALUE":
                            if field.value not in ("is compiled?", "is turbowarp?"):
                                field.value = obfuscate_str(field.value)
                block.comment_id = None

        if del_comments:
            new_comments = []
            for i, comment in enumerate(self.comments):
                if self.is_stage:
                    if (comment.text.startswith(
                            "Configuration for https://turbowarp.org/\n"
                            "You can move, resize, and minimize this comment, but don't edit it by hand. "
                            "This comment can be deleted to remove the stored settings.")
                            and comment.text.endswith(" // _twconfig_")):
                        new_comments.append(comment)

            self.comments = new_comments

    def get_custom_blocks(self):
        blocks = []
        for block in self.blocks:
            if block.mutation is not None:
                if block.mutation.proc_code is not None:
                    blocks.append(block)
        return blocks


Sprite = Target


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

            print(f"{_id} is not a standard extension code")

    def __repr__(self):
        return f"Ext<{self.id}>"

    @staticmethod
    def from_json(data, _id: str = None):
        return Extension(data)

    def to_json(self):
        return self.id


class Meta(ProjectItem):
    def __init__(self, semver: str = "3.0.0", vm: str = "", agent: str = ""):
        """
        Represents metadata of the project
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Metadata
        """
        self.semver = semver
        self.vm = vm
        self.agent = agent

        super().__init__(semver)

    def __repr__(self):
        return f"Meta<{self.semver} : {self.vm} : {self.agent}>"

    def to_json(self):
        return {
            "semver": self.semver,
            "vm": self.vm,
            "agent": self.agent
        }

    @staticmethod
    def from_json(data, _id: str = None):
        semver = data["semver"]
        vm = data.get("vm")
        agent = data.get("agent")

        if EDIT_META or vm is None:
            vm = "0.1.0"
        if EDIT_META or agent is None:
            agent = "Python: sbeditor.py by https://scratch.mit.edu/users/faretek1/"
        return Meta(semver, vm, agent)


class Monitor(ProjectItem):
    def __init__(self, _id: str = None,
                 mode: str = "default",
                 opcode: str = "data_variable",
                 params: dict = None,
                 sprite_name: str = None,
                 value=0,
                 width: int | float = 0,
                 height: int | float = 0,
                 x: int | float = 5,
                 y: int | float = 5,
                 visible: bool = False,
                 slider_min: int | float = 0,
                 slider_max: int | float = 100,
                 is_discrete: bool = True):
        """
        Represents a variable/list monitor
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Monitors
        """
        super().__init__(_id)

        self.mode = mode

        self.opcode = opcode
        self.params = params

        self.sprite_name = sprite_name

        self.value = value

        self.width, self.height = width, height
        self.x, self.y = x, y

        self.visible = visible

        self.slider_min, self.slider_max = slider_min, slider_max
        self.is_discrete = is_discrete

    def __repr__(self):
        return f"Monitor<{self.opcode}>"

    @staticmethod
    def from_json(data, _id: str = None):
        _id = data["id"]
        mode = data["mode"]

        opcode = data["opcode"]
        params = data["params"]

        sprite_name = data["spriteName"]

        value = data["value"]

        width, height = data["width"], data["height"]
        x, y = data["x"], data["y"]

        visible = data["visible"]

        if "isDiscrete" in data.keys():
            slider_min, slider_max = data["sliderMin"], data["sliderMax"]
            is_discrete = data["isDiscrete"]
        else:
            slider_min, slider_max, is_discrete = None, None, None

        return Monitor(_id, mode, opcode, params, sprite_name, value, width, height, x, y, visible, slider_min,
                       slider_max, is_discrete)

    def to_json(self):
        _json = {
            "id": self.id,
            "mode": self.mode,

            "opcode": self.opcode,
            "params": self.params,

            "spriteName": self.sprite_name,

            "value": self.value,

            "width": self.width,
            "height": self.height,

            "x": self.x,
            "y": self.y,

            "visible": self.visible
        }
        if self.is_discrete is not None:
            _json["sliderMin"] = self.slider_min
            _json["sliderMax"] = self.slider_max
            _json["isDiscrete"] = self.is_discrete

        return _json


class Project(ProjectItem):
    def __init__(self, targets: list[Target] = None, extensions: list[Extension] = None, monitors: list[Monitor] = None,
                 meta: Meta = None, _id: int | str = None):
        """
        Represents a whole project. Has targets, monitors, extensions, and metadata
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Projects
        """
        if targets is None:
            targets = [Target.new_stage()]
        if extensions is None:
            extensions = []
        if monitors is None:
            monitors = []
        if meta is None:
            meta = Meta()

        self.targets = targets
        for target in self.targets:
            target.project = self

        self.extensions = extensions
        self.monitors = monitors
        self.meta = meta
        super().__init__(_id)

    def set_asset_load_method(self, load_method: str | list[str] = "url"):
        for target in self.targets:
            target.set_asset_load_method(load_method)

    @staticmethod
    def from_json(data, _id: str = "json"):
        json_targets = data["targets"]
        json_monitors = data["monitors"]
        json_extensions = data["extensions"]
        json_meta = data["meta"]

        targets = []
        for target in json_targets:
            target_obj = Target.from_json(target)
            targets.append(target_obj)

        extensions = []
        for extension in json_extensions:
            extensions.append(Extension(extension))

        monitors = []
        for monitor in json_monitors:
            monitors.append(Monitor.from_json(monitor))

        meta = Meta.from_json(json_meta)

        return Project(targets, extensions, monitors, meta, _id)

    @staticmethod
    def from_sb3(fp: str):
        with ZipFile(fp) as sb3:
            project = Project.from_json(json.loads(sb3.read("project.json")), fp)

        project.set_asset_load_method(["zip", fp])
        return project

    @staticmethod
    def from_id(project_id: int):
        project_token = requests.get(f"https://api.scratch.mit.edu/projects/{project_id}").json()["project_token"]
        return Project.from_json(
            requests.get(f"https://projects.scratch.mit.edu/{project_id}?token={project_token}").json(), project_id)

    def to_json(self):
        _json = {
            "meta": self.meta.to_json()
        }
        extensions = []
        for extension in self.extensions:
            extensions.append(extension.to_json())
        _json["extensions"] = extensions

        monitors = []
        for monitor in self.monitors:
            monitors.append(monitor.to_json())
        _json["monitors"] = monitors

        targets = []
        for target in self.targets:
            targets.append(target.to_json())
        _json["targets"] = targets

        return _json

    def assets(self):
        assets = []
        for target in self.targets:
            assets += target.assets()
        return assets

    def export(self, fp: str, make_zip: bool = True):
        if os.path.isdir(fp):
            try:
                shutil.rmtree(fp)
            except PermissionError as e:
                print(f"Permission error ignored: {e}")

        os.makedirs(fp, exist_ok=True)

        for asset in self.assets():
            asset.download(f"{fp}\\{asset.id}")

        with open(f"{fp}\\project.json", "w", encoding="utf-8") as f:
            json.dump(self.to_json(), f)

        if not make_zip:
            return

        with ZipFile(f"{fp}.sb3", "w") as achv:
            for file in os.listdir(fp):
                achv.write(f"{fp}\\{file}", arcname=file)

    def get_target(self, name: str) -> Target | None:
        for target in self.targets:
            if target.name == name:
                return target

    def add_target(self, target: Target):
        target.project = self
        self.targets.append(target)

    @property
    def stage(self):
        for target in self.targets:
            if target.is_stage:
                return target

    def obfuscate(self):
        for target in self.targets:
            target.obfuscate()
