from .fastapi_init import app
from .logger_init import *

try:
    import to_path
except ImportError:
    print('Error import to_path')
