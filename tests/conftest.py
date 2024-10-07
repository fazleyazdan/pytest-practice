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
    file_path = r"tests\test_projects\HTTPClient-0.3-3.jar"
    return file_path

@pytest.fixture
def get_wrong_file():
    file_path = r"tests\test_project\wrongfile3.0"
    return file_path


@pytest.fixture
def get_package_details():
    package_details = {
    "description": "KiwiLogger\r\nA simple Python logger class that logs messages to Logtail, a local file, and/or the terminal. Easily configurable and customizable.\r\n\r\nFeatures\r\nLog messages to Logtail (an online logging service)\r\nLog messages to a local file\r\nLog messages to the terminal (stdout)\r\nSpecify the logging level (e.g., INFO, ERROR, CRITICAL)\r\nAdd structured logging (extra data) to log messages\r\n\r\nInstallation\r\nBefore using KiwiLogger, you need to install the multikiwilogger library:\r\n\r\nbash\r\nCopy code\r\npip install multikiwilogger\r\n\r\nUsage\r\npython\r\n\r\nCopy code\r\nfrom multikiwilogger import KiwiLogger\r\n\r\n# Initialize the logger\r\nmlog = KiwiLogger(log_online=True, log_local=True, log_terminal=True)\r\n\r\n# Log a simple message\r\nmlog('This is an INFO message.')  # Defaults to INFO level\r\n\r\n# Log a message with a specific level\r\nmlog('Something bad happened.', level='ERROR')\r\n\r\n# Log a message with structured logging (extra data)\r\nmlog('Log message with structured logging.', level='INFO', extra={\r\n    'item': \"Orange Soda\",\r\n    'price': 100.00\r\n})\r\n\r\nConfiguration\r\nInitialize the KiwiLogger with the following optional parameters:\r\n\r\nname (default: __name__): The name of the logger.\r\nlevel (default: logging.INFO): The minimum log level for messages.\r\nlog_online (default: True): Log messages to Logtail.\r\nlog_local (default: False): Log messages to a local file.\r\nlog_terminal (default: True): Log messages to the terminal (stdout).\r\n\r\nEnvironment Variables\r\nKiwiLogger relies on the LOGTAIL_SOURCE_TOKEN environment variable to send logs to Logtail. Set this variable in your environment or add it to a .env file:\r\n\r\nmakefile\r\nCopy code\r\nLOGTAIL_SOURCE_TOKEN=your_logtail_source_token_here\r\nReplace your_logtail_source_token_here with the actual source token provided by Logtail.\r\n\r\nLicense\r\nThis project is licensed under the MIT License.\r\n",
    "extra_metadata": {},
    "id": "d5beabd62dbb9832795b6a5ac1cfd0b7a9299f1b0b8b50f3b3e385b88039e926",
    "language": "python",
    "name": "multikiwilogger",
    "project_homepage": "",
    "registry_name": "pypi",
    "vendor_name": "OZRay"
    }
    return package_details
