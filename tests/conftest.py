import pytest
import source.shapes as shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(7,3)

@pytest.fixture
def sha1_hash():
    return 'f03223c94b1b485c5757abadc866e6eacb53ba03'

@pytest.fixture
def sha256_hash():
    return '43f2cf8376289d32605b25a128a04e2257c142e316e5cb4811350be7396d6a10'

@pytest.fixture
def md5_hash():
    return 'c762fba3f2441cc665c630fcc7fa98cc'

@pytest.fixture
def blake2b_256_hash():
    return '768a601cc6c120eba4899b62f0e1c8fc11b992846a6315e6e3dbcf490e40d558'



