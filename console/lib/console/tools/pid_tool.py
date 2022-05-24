import os
import importlib
from lib.console import config
from lib.console.tools import count_to_word
import tmp
import run
from run import pid


def create_pid(command_arr, module="default", nohup=False):
    pid_count_path = os.path.join(tmp.PATH, "count.py")
    if not os.path.exists(pid_count_path):
        with open(pid_count_path, "w") as f:
            f.write("COUNT = 0")
            f.close()
    try:
        from tmp import count
        importlib.reload(count)
        counter = count.COUNT
        if nohup:
            counter = counter + 1
            with open(pid_count_path, "w") as f:
                f.write("COUNT = {0}".format(counter))
                f.close()
        word_count = count_to_word.main(counter)
        pid_file = f"{module}_{'_'.join(word_count)}.py"
        with open(os.path.join(pid.PATH, pid_file), "w") as f:
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
    return counter

def start_pid(_pid, pid_module="default", module="default"):
    count_word = "_".join(count_to_word.main(_pid))
    filename = "{0}_command.py".format(module)
    path = os.path.join(run.PATH, filename)
    try:
        with open(path, "w") as f:
            f.write(f"import importlib\nfrom run.pid import {pid_module}_{count_word}\nimportlib.reload({pid_module}_{count_word})\ndef main():\n\t{pid_module}_{count_word}.main()")
            f.close()
    except:
        print(f'I/O error: Cannot open file: {path}\n')
        return False
    return True

def stopped_pid(_pid, if_nohup=False):
    from tmp import count
    importlib.reload(count)
    counter = count.COUNT
    pid_count_path = os.path.join(tmp.PATH, "count.py")
    if if_nohup:
        counter = counter - 1
        with open(pid_count_path, "w") as f:
            f.write("COUNT = {0}".format(counter))
            f.close()
    else:
        pass # Do nothing.


def main(args):
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