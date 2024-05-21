import pytest
from munch import Munch
import source.generate_hashes as generate_hashes

def test_hash_file()-> Munch:
    file_path = r"C:\Users\Fazle Yazdan\Downloads\exoplatform.portal.api-1.0.jar"
    result = generate_hashes.hash_file(file_path)
    
    assert result.sha1 == 'f03223c94b1b485c5757abadc866e6eacb53ba03'
    assert result.sha256 == '43f2cf8376289d32605b25a128a04e2257c142e316e5cb4811350be7396d6a10'
    assert result.md5 == 'c762fba3f2441cc665c630fcc7fa98cc'
    assert result.blake2b_256 == '768a601cc6c120eba4899b62f0e1c8fc11b992846a6315e6e3dbcf490e40d558'
    
def test_wrong_hash()-> Munch:
    file_path = r"C:\Users\Fazle Yazdan\Downloads\exoplatform.portal.api-1.0.jar"
    result = generate_hashes.hash_file(file_path)
    
    assert result.sha1 != 'incorrect hash'
    assert result.sha256 != 'incorrect hash'
    assert result.md5 != 'incorrect hash'
    assert result.blake2b_256 != 'incorrect hash'
    
def test_file_not_found()-> Munch:
    file_path = r"C:\Users\Fazle Yazdan\Downloads\exoplatformasd.portal.api-1.0.jar"
    with pytest.raises(FileNotFoundError):
        generate_hashes.hash_file(file_path)
    assert True