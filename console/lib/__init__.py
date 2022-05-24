from importlib import reload
from os.path import dirname
from . import console
reload(console)
PATH = dirname(__file__)