# Added modules from src/
import sys
from pathlib import Path

PATH_TO_SRC_MODULES = Path(__file__).absolute().parent.parent
sys.path.append(PATH_TO_SRC_MODULES.__str__())
