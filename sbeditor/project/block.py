from .projectitem import ProjectItem

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
        self.fetcher = None
        # This is the block object where the Fetch 'block' will append fetches to, to get its index and place its block

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
            for inp in inputs:
                inp.block = self

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

    @property
    def stack_type(self):
        _stack_type = STACK_TYPES.get(self.opcode)
        if _stack_type == '':
            _stack_type = None

        return _stack_type

    @staticmethod
    def from_input(inp: Input, *, adjust_to_default_pos: bool = True):
        if inp.pos is None and adjust_to_default_pos:
            inp.pos = (0, 0)

        if inp.type_str == "block":
            return inp.json[0]

        return Block(array=inp.json[1][-1])

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

    @property
    def json(self) -> tuple | list:
        if self.type != "Normal":
            _json = [self.type_id]

            if self.type_id < 11:
                # Numbers, colors & strings
                _json.append(self.value)
            else:
                if self.type_id == 11:
                    item_obj = self.target.get_broadcast_by_id(self.item_id)
                elif self.type_id == 12:
                    item_obj = self.target.get_var_by_id(self.item_id)
                else:
                    item_obj = self.target.get_list_by_id(self.item_id)

                # Broadcasts, variables & lists
                if item_obj is None:
                    _json.append(None)
                    _json.append(self.item_id)
                else:
                    _json.append(item_obj.name)
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

        if not self.can_next and self.next is not None:
            warnings.warn(f"{self} can't next: {self.__dict__}")

            ret["next"] = None

        if self.parent is None:
            ret["x"] = self.x
            ret["y"] = self.y

        if self.comment_id is not None:
            ret["comment"] = self.comment_id

        inputs = {}
        for input_ in self.inputs:
            input_json = input_.json
            inputs[input_json[0]] = input_json[1]
        ret["inputs"] = inputs

        fields = {}
        for field in self.fields:
            field_json = field.json

            fields[field_json[0]] = field_json[1]
        ret["fields"] = fields

        if hasattr(self, "mutation"):
            if self.mutation is not None:
                ret["mutation"] = self.mutation.json

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

            block = Block(_id, opcode, next_, parent, inputs, fields, is_shadow, (x, y), comment_id, mutation)
            for inp in block.inputs:
                inp.parent = block

            return block

    def get_input(self, input_id: str):
        for input_ in self.inputs:
            if input_.id == input_id:
                return input_

    def add_input_or_block(self, inp):
        if isinstance(inp.value, Block):
            self.target.add_block(inp.value)

        return self.add_input(inp)

    def add_input(self, inp: Input):
        if self.type != "Normal":
            raise ValueError("Can't add inputs to an array block!")
        inp.parent = self
        new_inps = [inp]
        for input_ in self.inputs:
            if input_.id != inp.id:
                new_inps.append(input_)

        self.inputs = new_inps

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

    @property
    def stack_parent(self):
        parent_chain = self.parent_chain
        parent_chain.reverse()
        for parent in parent_chain:
            if parent.stack_type == "stack":
                return parent

    def attached_block(self):
        if self.type != "Normal":
            return
        elif self.next is None:
            return

        return self.target.get_block_by_id(self.next)

    @property
    def parent_block(self):
        if self.type != "Normal":
            return
        elif self.parent is None:
            return

        return self.target.get_block_by_id(self.parent)

    @property
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

    def attach(self, block):
        if hasattr(block, "run"):
            block.run(self.target, self)

        if not isinstance(block, Block):
            warnings.warn(f"{block} is not a block:")

            return self

        block.target = self.target

        self.target.add_block(block)

        block.parent = self.id
        block.next = self.next

        if self.next is not None:
            my_next = self.target.get_block_by_id(self.next)
            my_next.parent = block.id

        self.next = block.id
        return block

    @property
    def is_input(self):
        return self.parent_block.next != self.id

    @property
    def parent_inputs(self):
        # If this block is an input, get the input that links to this block
        for input_ in self.parent_block.inputs:
            if input_.value == self.id:
                return input_

    def slot_above(self, block):
        # Add a block above this block in the stack. Only works with stack blocks
        if self.stack_type != "stack":
            raise ValueError("Can't slot above a reporter!")

        if hasattr(block, "run"):
            block.run(self.target, self)

        if not isinstance(block, Block):
            warnings.warn(f"{block} is not a block")

            return self

        block.target = self.target

        self.target.add_block(block)

        if self.is_input:
            # get what input this is
            my_input = self.parent_inputs
            my_input.value = block.id

        else:
            self.parent_block.next = block.id

        block.parent = self.parent
        self.parent = block.id

        block.next = self.id

        return block

    def link_inputs(self):
        if self.type != "Normal":
            return

        for input_ in self.inputs:
            input_.parent = self

            if input_.type_str == "block":
                block = self.target.get_block_by_id(input_.value)

                if block is not None:
                    if hasattr(block, "run"):
                        block.run(self.target, self)

                    block.parent = self.id

            if input_.obscurer is not None:
                if isinstance(input_.obscurer, str):
                    obscurer = self.target.get_block_by_id(input_.obscurer)
                    obscurer.parent = self.id

    def attach_chain(self, chain: ['Block']):
        b = self
        for block in chain:
            b = b.attach(block)
            b.link_inputs()

    @property
    def previous_chain(self):
        chain = [self]
        while True:
            prev = chain[-1]
            parent = prev.parent_block
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

    @property
    def stack_chain(self):
        return self.previous_chain[0:-1] + self.attached_chain

    @property
    def subtree(self):
        if self.type != "Normal":
            return [self]

        _full_chain = [self]

        for child in self.children:
            _full_chain.append(child.subtree)

        if self.next is not None:
            print(self.next)
            next_block = self.target.get_block_by_id(self.next)
            _full_chain += next_block.subtree

        return _full_chain

    @property
    def children(self):
        if self.type != "Normal":
            return []

        _children = []

        for input_ in self.inputs:
            if input_.type_str == "block":
                block = None
                if isinstance(input_.value, list):
                    block = Block(array=input_.value)

                else:
                    if input_.value is not None:
                        block = self.target.get_block_by_id(input_.value)
                if block is not None:
                    _children.append(block)

            if input_.obscurer is not None:
                if isinstance(input_.obscurer, list):
                    block = Block(array=input_.obscurer)
                else:
                    block = self.target.get_block_by_id(input_.obscurer)
                if block is not None:
                    _children.append(block)

        return _children

    @property
    def parent_chain(self):
        chain = [self]
        while True:
            parent = chain[-1].parent_block

            if parent in chain:
                break
            elif parent is None:
                break

            chain.append(parent)
        chain.reverse()
        return chain

    @property
    def category(self):
        if self.type != "Normal":
            return self.type
        split = self.opcode.split('_')
        return split[0]