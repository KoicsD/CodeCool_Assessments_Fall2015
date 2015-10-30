__author__ = 'KoicsD'
# generating n times char c, the same as 'c' * n


def generate_n_char(n: int, c: str):
    if len(c) > 1:
        raise ValueError()

    ret = ""
    for i in range(n):
        ret += c
    return ret
