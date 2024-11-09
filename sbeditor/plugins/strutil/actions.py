from ...sbuild import *

def UltraJoin(*args: list[Block | Input]):
    if len(args) == 1:
        return args[0]

    join = Operators.Join()
    join.set_string1(args[0])
    join.set_string2(UltraJoin(*args[1:]))

    return join
