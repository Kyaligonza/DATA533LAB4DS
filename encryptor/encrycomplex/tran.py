"""The module encrypts the message by jumbling up the letters in the message text letter by letter. This kind of encryption
is called Transposition Encryption."""

import random
def tran(a):
    random.seed(1001)
    e = ''
    i = random.sample(range(len(a)),len(a))
    for index in i:
        e += a[index]
    return e
