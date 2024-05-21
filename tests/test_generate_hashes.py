import pytest
import source.generate_hashes as generate_hashes

def test_hash_file(sha1_hash, sha256_hash, md5_hash, blake2b_256_hash):
    file_path = r"C:\Users\Fazle Yazdan\Downloads\exoplatform.portal.api-1.0.jar"
    result = generate_hashes.hash_file(file_path)
    
    assert result.sha1 == sha1_hash
    assert result.sha256 == sha256_hash
    assert result.md5 == md5_hash
    assert result.blake2b_256 == blake2b_256_hash
    
def test_incorrect_hash():
    file_path = r"C:\Users\Fazle Yazdan\Downloads\exoplatform.portal.api-1.0.jar"
    result = generate_hashes.hash_file(file_path)
    
    assert result.sha1 != 'incorrect hash'
    assert result.sha256 != 'incorrect hash'
    assert result.md5 != 'incorrect hash'
    assert result.blake2b_256 != 'incorrect hash'
    
def test_file_not_found():
    file_path = r"C:\Users\Fazle Yazdan\Downloads\exoplatformasd.portal.api-1.0.jar"
    with pytest.raises(FileNotFoundError):
        generate_hashes.hash_file(file_path)
    assert True