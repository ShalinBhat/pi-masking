import hashlib

def mask_data(data):
    return hashlib.sha256(data.encode()).hexdigest()
