class ModuleVars:
    pass


md = ModuleVars()


def full_flat(a):
    ret = []
    for i in a:
        if isinstance(i, list):
            ret += full_flat(i)
        else:
            ret.append(i)

    return ret