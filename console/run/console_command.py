import importlib
from run.pid import console_null
importlib.reload(console_null)
def main():
	console_null.main()