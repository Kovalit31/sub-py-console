import importlib
import shutil
import os
from bin.tools import count_to_word
from bin.tools import pid_tool
import tmp
from lib.console import config
import run
from run import pid


def command_starter():
    while True:
        try:
            inputed = input(config.PS1).lower()
            if inputed and inputed != 'exit':
                command_arr = inputed.split(" ")
                c = pid_tool.create_pid(command_arr, module="console")
                if pid_tool.start_pid(c, pid_module="console", module="console"):
                    start_command(command_arr[0])
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


# def command_init(whatuse, count):
#     arr = count_to_word.main(count)
#     with open(os.path.join(pid.PATH, f"command_{'_'.join(arr)}.py"), "w") as f:
#         if "." in whatuse[0]:
#             f.write(
#                 f"from {config.MODULE_BIN_PATH}.{''.join(whatuse[0].split('.')[0:-1])} import {whatuse[0].split('.')[-1]}\n"
#             )
#             f.write(f"def main():\n    ")
#             f.write("{0}.main({1})".format(whatuse[0].split('.')[-1], whatuse[1:]))
#         else:
#             f.write(f"from {config.MODULE_BIN_PATH} import {whatuse[0]}\n")
#             f.write(f"def main():\n    ")
#             f.write("{0}.main({1})".format(whatuse[0], whatuse[1:]))
#         count += 1
#         f.close()
#         start_command(whatuse[0], '_'.join(arr))
#         return count

    


def main(*args):
    print(config.HAT)
    print("Licensed under", config.LICENSE)
    command_starter()
