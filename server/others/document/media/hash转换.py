# Python Version
M = int(1e9 + 7)
B = 233
print(M)

def get_hash(s):
    res = 0
    for char in s:
        res = (res * B + ord(char)) % M
    return res


def cmp(s, t):
    return get_hash(s) == get_hash(t)


print(get_hash('f'))
