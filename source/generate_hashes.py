import hashlib
from munch import Munch

def hash_file(file_path: str) -> Munch:
    """
    Generate hashes of a file using multiple hash algorithms.

    Args:
        file_path (str): Path to the file.

    Returns:
        Munch: A Munch object containing various hash values of the file.
    """
    
    with open(file_path, "rb") as file:
        sha1_hash = hashlib.sha1()
        sha256_hash = hashlib.sha256()
        md5_hash = hashlib.md5()
        blake2b_hash = hashlib.blake2b(digest_size=32)
            
        while True:
            data = file.read(65536)  # Read file in chunks of 64KB
            if not data:
                break
                
            sha1_hash.update(data)
            sha256_hash.update(data)
            md5_hash.update(data)
            blake2b_hash.update(data)
                
        all_hashes = Munch(
            sha1=sha1_hash.hexdigest(),
            sha256=sha256_hash.hexdigest(),
            md5=md5_hash.hexdigest(),
            blake2b_256=blake2b_hash.hexdigest()
        )
    return all_hashes
    
  

