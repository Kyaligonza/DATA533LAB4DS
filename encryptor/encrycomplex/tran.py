"""The module encrypts the message by jumbling up the letters in the message text letter by letter. This kind of encryption
is called Transposition Encryption."""
try:
    import random
except ImportError:
    print("The function did not work!!")
else:
    print("Succfully imported the module!!")
def tran(a):
    try:
        random.seed(1001)
        e = ''
        i = random.sample(range(len(a)),len(a))
        for index in i:
            e += a[index]
        return e
    except TypeError:
        print("Pass a string in the argument!!")
    else:
        print("Success!!")
