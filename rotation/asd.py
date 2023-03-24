import string


def make_rot_n(n):
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    trans = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: str.translate(s, trans)


with open("encrypted.txt", "r") as f:
    c = f.readline().strip()
    n = ord(c[0]) - ord("p")
    rot_n = make_rot_n(-n)
    print(rot_n(c))
