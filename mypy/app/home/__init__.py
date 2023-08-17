import sys
import os
token_path = os.path.abspath('module.py')
sys.path.append(token_path)
print(token_path)
from .module import _generate_token