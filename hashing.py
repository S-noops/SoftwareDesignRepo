import hashlib 


def encrypt(text):
    b = text.encode()
    enc = hashlib.sha1(b).hexdigest()
    return enc
