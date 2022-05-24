from os.path import dirname
from importlib import reload
from . import pid
reload(pid)
PATH = dirname(__file__)