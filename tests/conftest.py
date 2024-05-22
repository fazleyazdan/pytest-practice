import pytest
import source.shapes as shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(7,3)

@pytest.fixture
def sha1_hash():
    return '8c601a287ffbf8a89b9c491d5966b999cd71dd8b'

@pytest.fixture
def sha256_hash():
    return '2f973c1111ede6485a9012cef2f146fe36a83412270ffe991ab2e1ddecd9e1e3'

@pytest.fixture
def md5_hash():
    return 'a226700bfd3f7782ac9ebc07ddf5edab'

@pytest.fixture
def blake2b_256_hash():
    return '36d2c657a273e18fca0c8717e988177dd0eee5f9914cdf26d3d615e65961398f'

@pytest.fixture
def get_file():
    file_path = r"C:\Users\Fazle Yazdan\Desktop\My_projects\pytest-pratice\tests\HTTPClient-0.3-3.jar"
    return file_path

