from ...sbuild import *


def UltraJoin(*args: list[Block | Input]):
    if len(args) == 1:
        return args[0]

    return (Operators.Join()
            .set_string1(args[0])
            .set_string2(UltraJoin(*args[1:])))
