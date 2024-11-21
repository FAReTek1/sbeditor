import copy
import warnings

from sbeditor.utils.common import md
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


def package(sprite: Target, prf: str = None):
    def add_prf(name: str):
        return name if name.startswith("__") and name.endswith("__") else f"{prf}{name}"

    # Copy sprite so we don't edit the original stuff
    sprite = copy.deepcopy(sprite)
    if prf is None:
        prf = f"{sprite.name} | "

    # Rename broadcasts variables & lists
    for broadcast in sprite.broadcasts:
        broadcast.name = add_prf(broadcast.name)
    for variable in sprite.variables:
        variable.name = add_prf(variable.name)
    for lst in sprite.lists:
        lst.name = add_prf(lst.name)

    ret = "from sbeditor import *\n" \
          "def add_to_sprite(sprite: Target):\n" \
          "\tset_current_target(sprite)\n"

    ret += "\tbroadcasts = {"
    for broadcast in sprite.broadcasts:
        ret += f"\"{broadcast.name}\": sprite.add_broadcast(\"{broadcast.name}\"),"
    ret += "}\n"

    ret += "\tvariables = {"
    for variable in sprite.variables:
        ret += f"\"{variable.name}\": sprite.add_variable(\"{variable.name}\", \"{variable.value}\", {variable.is_cloud_var}),"
    ret += "}\n"

    ret += "\tlists = {"
    for lst in sprite.lists:
        ret += f"\"{lst.name}\": sprite.add_list(\"{lst.name}\", {lst.value}),"
    ret += "}\n"

    def package_block(block: Block):
        if not (isinstance(block, list) or isinstance(block, Block)):
            warnings.warn(f"{block} is not a block!")
            raise ValueError(f"bad input {block}")
            # return ''

        if isinstance(block, list):
            block = Block(array=block, target=sprite)
            arry = block.json[1]

            if block.type == "broadcast":
                arry[2] = f"broadcasts[\"{add_prf(block.name)}\"].id"
            if block.type == "list":
                arry[2] = f"lists[\"{add_prf(block.name)}\"].id"
            if block.type == "variable":
                arry[2] = f"variables[\"{add_prf(block.name)}\"].id"

            return f"Block(array=[{arry[0]}, \"{arry[1]}\", {arry[2]}])"

        elif block.type != "Normal":
            return f"Block(array={block.json[1]})"
        else:
            ... # print(f"-- {block}, {type(block)}")

        ret2 = f"\t\tBlock(None, \"{block.opcode}\", shadow={block.is_shadow})"
        for inp in block.inputs:
            obscurer = None
            if inp.obscurer is not None:
                # print("obscurer:", inp.obscurer)
                if isinstance(inp.obscurer, list):
                    inner_block = inp.obscurer
                else:
                    inner_block = sprite.get_block_by_id(inp.obscurer)
                packaged = package_block(inner_block)
                packaged = f"sprite.add_block({packaged})" if packaged != '' else "''"
                obscurer = packaged
                # ret2 += (f"\n.add_input(Input("
                #          f"\"{inp.id}\", {packaged}, shadow_status={inp.shadow_idx}, input_id={inp.input_id}, obscurer={obscurer}"
                #          f"))")

            if inp.type_id == 2 and inp.value is not None:
                # print("value:", inp.value)
                if isinstance(inp.value, list):
                    inner_block = Block(array=inp.value)
                else:
                    inner_block = sprite.get_block_by_id(inp.value)

                # print(inp.__dict__, type(inner_block))
                packaged = package_block(inner_block)
                packaged = f"sprite.add_block({packaged})" if packaged != '' else "''"

                ret2 += (f"\n.add_input(Input("
                         f"\"{inp.id}\", {packaged}, shadow_status={inp.shadow_idx}, input_id={inp.input_id}, obscurer={obscurer}"
                         f"))")
            elif inp.type_id < 11:
                ret2 += (f"\n.add_input(Input("
                         f"\"{inp.id}\", \"{inp.value}\", {inp.type_id}, {inp.shadow_idx}, input_id={inp.input_id}, obscurer={obscurer}"
                         f"))")
            else:
                if inp.type_id == 11:
                    ret2 += (f"\n.add_input(Input("
                             f"\"{inp.id}\", \"{inp.value}\", {inp.type_id}, {inp.shadow_idx}, input_id=broadcasts[\"{inp.value}\"].id, obscurer={obscurer}"
                             f"))")
                elif inp.type_id == 12:
                    ret2 += (f"\n.add_input(Input("
                             f"\"{inp.id}\", \"{inp.value}\", {inp.type_id}, {inp.shadow_idx}, input_id=variables[\"{inp.value}\"].id, obscurer={obscurer}"
                             f"))")
                else:
                    ret2 += (f"\n.add_input(Input("
                             f"\"{inp.id}\", \"{inp.value}\", {inp.type_id}, {inp.shadow_idx}, input_id=lists[\"{inp.value}\"].id, obscurer={obscurer}"
                             f"))")

        for field in block.fields:
            value = field.value
            if field.value_id is not None:
                if field.id == "VARIABLE":
                    value_id = f"variables[\"{add_prf(field.value)}\"].id"
                    value = add_prf(value)
                elif field.id == "LIST":
                    value_id = f"lists[\"{add_prf(field.value)}\"].id"
                    value = add_prf(value)
                else:
                    value_id = "None"
            else:
                value_id = "None"

            ret2 += (f"\n.add_field("
                     f"Field(\"{field.id}\", \"{value}\", {value_id})"
                     f")")

        if block.mutation is not None:
            ret2 += f"\n.add_mutation(Mutation("

            if block.mutation.proc_code is not None:
                # Add the name of the module on top asw
                ret2 += f"proc_code=\"{add_prf(block.mutation.proc_code)}\", "
            if block.mutation.argument_ids is not None:
                ret2 += f"argument_ids={block.mutation.argument_ids}, "
            if block.mutation.warp is not None:
                ret2 += f"warp={block.mutation.warp}, "
            if block.mutation.argument_names is not None:
                ret2 += f"argument_names = {block.mutation.argument_names}, "
            if block.mutation.argument_defaults is not None:
                ret2 += f"argument_defaults={block.mutation.argument_defaults}, "
            if block.mutation.has_next is not None:
                ret2 += f"has_next={block.mutation.has_next}"
            ret2 += f"))"

        return ret2

    for chain in sprite.all_chains:
        # bprint(chain)

        ret += f"\tlink_chain(\n"

        for block in chain:
            if isinstance(block, Block):
                ret += f"{package_block(block)},\n"

        ret += "\n\t)\n"

    ret += f"\n\treturn broadcasts, variables, lists"

    return ret
