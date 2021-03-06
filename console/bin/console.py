import importlib
import os
import shutil

import run
from lib.console import config
from lib.console.tools import pid_tool, search_util
import tmp
from run import pid
import bin

def command_starter():
    while True:
        try:
            inputed = input(config.PS1).lower()
            if inputed and inputed != 'exit':
                command_arr = inputed.split(" ")
                if search_util.search_bin_file(bin.PATH, command_arr[0] + ".py"):
                    c = pid_tool.create_pid(command_arr, module="console")
                    if pid_tool.start_pid(c, pid_module="console", module="console"):
                        start_command(command_arr[0])
                else:
                    print("No such command")
            elif inputed == 'exit':
                raise EOFError()
            else:
                pass
        except EOFError or KeyboardInterrupt:
            target_dirs = [pid.PATH, run.PATH, tmp.PATH]
            for y in target_dirs:
                target_dir = y
                contents = [os.path.join(target_dir, i) for i in os.listdir(target_dir)]
                for x in contents:
                    if not x.endswith("__init__.py") and not x.endswith("pid"):
                        if os.path.isfile(x) or os.path.islink(x):
                            os.remove(x)
                        else:
                            shutil.rmtree(x)
            break

def start_command(command):
    try:
        while True:
            try:
                from run import console_command
                importlib.reload(console_command)
                console_command.main()
                break
            except Exception as e:
                if config.DEBUG:
                    print(e)
    except Exception as e:
        if config.DEBUG:
            print(e)
            print(dir())
            print("run PATH: ", run.PATH)
        print(f"Cannot start '{command}' command: Error occured.")
        print("Please check command availability and try again.")


def main(*args):
    print('''
Sub-Py console
Universal Python console for starting and working with user input commands.
''')
    print("Licensed under GNU General Public License, version 2")
    command_starter()
