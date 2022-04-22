from lib.console import config
import importlib
import os


try:
    if config.ENV_PATH_ALL:
        pass
    else:
        raise Exception("Cannot start console without known installation path")
except:
    raise Exception("Cannot install module without known installation path")

def command_starter():
    while True:
        try:
            inputed = input(config.PS1).lower()
            if inputed and inputed != 'exit':
                command_arr = inputed.split(" ")
                command_init(command_arr)
            elif inputed == 'exit':
                break
            else:
                pass
        except EOFError or KeyboardInterrupt:
            break


def command_init(whatuse):
    with open(config.ENV_BIN_PATH + os.sep +"command_py.py", "w") as f:
        if "." in whatuse[0]:
            f.write(
                f"from {config.MODULE_BIN_PATH}.{''.join(whatuse[0].split('.')[0:-1])} import {whatuse[0].split('.')[-1]}\n"
            )
            f.write(f"def main():\n    ")
            f.write("{0}.main({1})".format(whatuse[0].split('.')[-1], whatuse[1:]))
        else:
            f.write(f"from {config.MODULE_BIN_PATH} import {whatuse[0]}\n")
            f.write(f"def main():\n    ")
            f.write("{0}.main({1})".format(whatuse[0], whatuse[1:]))
        f.close()
    try:
        from bin import command_py
        importlib.reload(command_py)
        command_py.main()
    except Exception as e:
        if config.DEBUG:
            print(e)
            print(dir())
        if e:
            print(f"Cannot start '{whatuse[0]}' command: Error occured.")
            print("Please check command availability and try again.")


def main(*args):
    print(config.HAT)
    print("Licensed under", config.LICENSE)
    command_starter()
