import bcrypt


def create_hash(password):
    hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt(10))
    hash = hash.hex()  # hex encode
    return hash


def verify_hash(password, hash):
    hash = bytes.fromhex(hash)  # bytes encode from hex
    return bcrypt.checkpw(password.encode('utf8'), hash)
