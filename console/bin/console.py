import importlib
from copy import deepcopy
import os
from bin.tools import count_to_word
from lib.console import config
import run
from run import pid


def command_starter():
    counter = 0
    while True:
        try:
            inputed = input(config.PS1).lower()
            if inputed and inputed != 'exit':
                command_arr = inputed.split(" ")
                counter = command_init(command_arr, counter)
            elif inputed == 'exit':
                break
            else:
                pass
        except EOFError or KeyboardInterrupt:
            copy = deepcopy(os.listdir(pid.PATH).remove('__init__.py'))
            for x in range(len(copy)):
                if copy[x] is not "__init__.py":
                    os.remove(os.path.join(pid.PATH, copy[x]))

def start_command(command, pid):
    with open(os.path.join(run.PATH, "console_command.py"), "w") as f:
        f.write(f"from run.pid import command_{pid}\ndef main():\n\tcommand_{pid}.main()")
        f.close()
    try:
        from run import console_command
        importlib.reload(console_command)
        console_command.main()
    except Exception as e:
        if config.DEBUG:
            print(e)
            print(dir())
            print("run PATH: ", run.PATH)
        if e:
            print(f"Cannot start '{command}' command: Error occured.")
            print("Please check command availability and try again.")


def command_init(whatuse, count):
    arr = count_to_word.main(count)
    with open(os.path.join(pid.PATH, f"command_{'_'.join(arr)}.py"), "w") as f:
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
        count += 1
        f.close()
        start_command(whatuse[0], '_'.join(arr))
        return count

    


def main(*args):
    print(config.HAT)
    print("Licensed under", config.LICENSE)
    command_starter()
