import os
import importlib
from lib.console import config
from . import count_to_word
import tmp
import run
from run import pid


def create_pid(command_arr, module="default"):
    pid_count_path = os.path.join(tmp.PATH, "count.py")
    if not os.path.exists(pid_count_path):
        with open(pid_count_path, "w") as f:
            f.write("COUNT = 0")
            f.close()
    try:
        from tmp import count
        counter = count.COUNT
        word_count = count_to_word.main(counter)
        with open(os.path.join(pid.PATH, f"{module}_{'_'.join(word_count)}.py"), "w") as f:
            if "." in command_arr[0]:
                f.write(
                    f"from {config.MODULE_BIN_PATH}.{''.join(command_arr[0].split('.')[0:-1])} import {command_arr[0].split('.')[-1]}\n"
                )
                f.write(f"def main():\n    ")
                f.write("{0}.main({1})".format(command_arr[0].split('.')[-1], command_arr[1:]))
            else:
                f.write(f"from {config.MODULE_BIN_PATH} import {command_arr[0]}\n")
                f.write(f"def main():\n    ")
                f.write("{0}.main({1})".format(command_arr[0], command_arr[1:]))
    except:
        pass
    with open(pid_count_path, "w") as f:
        f.write("COUNT = {0}".format(counter + 1))
        f.close()
    return counter

def start_pid(pid, pid_module="default", module="default"):
    filename = "{0}_{1}.py".format(module, "_".join(count_to_word.main(pid)))
    path = os.path.join(pid.PATH, filename)
    try:
        with open(os.path.join(run.PATH, f"{module}_command.py"), "w") as f:
            f.write(f"from run.pid import {pid_module}_{pid}\ndef main():\n\t{pid_module}_{pid}.main()")
            f.close()
    except:
        print(f'I/O error: Cannot open file: {path}\n')
    try:
        pass
    except:
        pass
    return False

def main(*args):
    print("Cannot load command as main file.\nUse it as module.")

# arr = count_to_word.main(count)
#     with open(os.path.join(pid.PATH, f"command_{'_'.join(arr)}.py"), "w") as f:
#         if "." in command_arr[0]:
#             f.write(
#                 f"from {config.MODULE_BIN_PATH}.{''.join(command_arr[0].split('.')[0:-1])} import {command_arr[0].split('.')[-1]}\n"
#             )
#             f.write(f"def main():\n    ")
#             f.write("{0}.main({1})".format(command_arr[0].split('.')[-1], command_arr[1:]))
#         else:
#             f.write(f"from {config.MODULE_BIN_PATH} import {command_arr[0]}\n")
#             f.write(f"def main():\n    ")
#             f.write("{0}.main({1})".format(command_arr[0], command_arr[1:]))
#         count += 1
#         f.close()
#         start_command(command_arr[0], '_'.join(arr))
#         return count