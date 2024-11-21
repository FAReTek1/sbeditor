import math
from hashlib import md5


def full_flat(a):
    ret = []
    for i in a:
        if isinstance(i, list):
            ret += full_flat(i)
        else:
            ret.append(i)

    return ret


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


def obfuscate_str(string: str):
    return md5(string.encode("utf-8")).hexdigest()
