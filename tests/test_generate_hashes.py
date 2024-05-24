import pytest
import source.generate_hashes as generate_hashes


def test_hash_file(get_file, sha1_hash, sha256_hash, md5_hash, blake2b_256_hash):
    result = generate_hashes.hash_file(get_file)
    
    assert result.sha1 == sha1_hash
    assert result.sha256 == sha256_hash
    assert result.md5 == md5_hash
    assert result.blake2b_256 == blake2b_256_hash
    
def test_incorrect_hash(get_file):
    result = generate_hashes.hash_file(get_file)
    
    assert result.sha1 != 'incorrect hash'
    assert result.sha256 != 'incorrect hash'
    assert result.md5 != 'incorrect hash'
    assert result.blake2b_256 != 'incorrect hash'
    
def test_file_not_found(get_wrong_file):
    with pytest.raises(FileNotFoundError):
        generate_hashes.hash_file(get_wrong_file)