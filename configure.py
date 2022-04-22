import os

path_installed = __file__.split(os.sep)
path_installed.pop()
for x in path_installed:
    if x == " " or x == ".":
        path_installed.remove(x)
for x in range(len(path_installed)):
    if path_installed[x] == "..":
        path_installed.pop(x)
        path_installed.pop(x-1)
path_installed = os.sep.join(path_installed)
path_in = path_installed + os.sep + "console"
path_bin = path_in + os.sep + "bin"
path_lib = path_in + os.sep + "lib"
with open(path_lib + os.sep + "console" + os.sep + "config.py", "a") as f:
    f.write(f"\nENV_BIN_PATH = \"{path_bin}\"\nENV_LIB_PATH = \"{path_lib}\"\nENV_PATH_ALL = \"{path_in}\"")

