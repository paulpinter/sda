import sys
import os

# necessary for pytest to find the src folder
# relative to conftest.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
