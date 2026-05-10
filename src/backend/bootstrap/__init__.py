from .fastapi_init import app

try:
    import to_path
except ImportError:
    print('Error import to_path')
