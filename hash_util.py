import hashlib
import json

def hash_string_256(string):
    """Hash a string using SHA-256 for a given input.

    Arguments:
        :string: The string to be hashed. """
    return hashlib.sha256(string).hexdigest()


def hash_block(block):
    """Hashes a block and returns a string representation of it.

    Arguments:
        :block: The block that should be hashed. """
    #Use json.dumps to turn the block into a string before encoding it to bytes. Use hexdigest to turn a byte hash into a string hash.
    return hash_string_256(json.dumps(block, sort_keys=True).encode())