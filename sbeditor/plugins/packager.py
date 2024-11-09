from sbeditor.common import md
from sbeditor.sbuild import Data, Block, Target, Operators, Input

ret_idxs = {}


class Return(Data.AddToList):
    def __init__(self, value, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
        super().__init__(shadow=shadow, pos=pos)
        self.value = value
        self.block = None
        self.set_item(self.value)

    def run(self, target: 'Target', block: 'Block'):
        ret_list = target.add_list("__return__")
        self.set_list(ret_list)
        self.block = block


class Fetch(Data.ItemOfList):
    def __init__(self, call: Block, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
        super().__init__(shadow=shadow, pos=pos)
        self.value = call

        self.target = None
        self.block = None
        self.index = -1

    def run(self, target: 'Target', block: 'Block'):
        ret_list = target.add_list("__return__")
        self.set_list(ret_list)
        self.set_index("?", "string")

        self.target = target
        self.block = block

    def on_linked(self):
        ret_list = self.target.add_list("__return__")
        stack_parent = self.stack_parent

        if stack_parent.id not in ret_idxs:
            ret_idxs[stack_parent.id] = []

        # Find the current index
        ret_idxs[stack_parent.id].append(self)
        stack_parent.slot_above(self.value)

        self.index = len(ret_idxs[stack_parent.id])
        self.set_index(
            Operators.Subtract(shadow=True)
            .set_num1(
                Data.LengthOfList(shadow=True)
                .set_list(ret_list)
            )
            .set_num2(
                "?"
            )
        )

        # Update the indexes of the other fetchers
        for i, fetch in enumerate(ret_idxs[stack_parent.id]):
            fetch: Block

            md.CURRENT_TARGET.get_block_by_id(
                fetch.get_input("INDEX").value
            ).add_input(Input("NUM2", len(ret_idxs[stack_parent.id]) - i - 1))

        # Delete the item after it is used
        stack_parent.attach(
            Data.DeleteOfList(shadow=True)
            .set_list(ret_list)
            .set_index(
                Data.LengthOfList(shadow=True)
                .set_list(ret_list)
            )
        )


def package(sprite: Target):
    pass
