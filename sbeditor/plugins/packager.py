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
        ret += f"\"{lst.name}\": sprite.add_list(\"{lst.name}\", \"{lst.value}\"),"
    ret += "}\n"

    def package_block(block: Block):
        ret2 = f"\t\tBlock(None, \"{block.opcode}\", shadow={block.is_shadow})"
        for inp in block.inputs:
            obscurer = None
            if inp.obscurer is not None:
                ret2 += package_block(inp.obscurer)

            if inp.type_id == 2:
                ret2 += (f"\n.add_input(Input("
                         f"\"{inp.id}\", sprite.add_block({package_block(sprite.get_block_by_id(inp.value))}), shadow_status={inp.shadow_idx}, input_id={inp.input_id}, obscurer={obscurer}"
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
            ret2 += (f"\n.add_field("
                     f"Field(\"{field.id}\", \"{field.value}\", \"{field.value_id}\")"
                     f")")
        if block.mutation is not None:
            ret2 += (f"\n.add_mutation("
                     f"Mutation(proc_code=\"{block.mutation.proc_code}\", argument_ids={block.mutation.argument_ids}, "
                     f"warp={block.mutation.warp}, argument_names={block.mutation.argument_names}, "
                     f"argument_defaults={block.mutation.argument_defaults}, has_next={block.mutation.has_next}"
                     f"))")

        return ret2

    for chain in sprite.all_chains:
        # bprint(chain)

        ret += f"\tlink_chain(\n"

        for block in chain:
            if isinstance(block, Block):
                ret += f"{package_block(block)},\n"

        ret += "\n\t)\n"

    return ret