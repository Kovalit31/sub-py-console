import importlib
import os
def main(args):
    print("Example\n")
    try:
        if args[0] == "start_command":
            from bin import PATH
            from lib.console.tools import pid_tool
            with open(os.path.join(PATH, "new_example.py"), "w") as f:
                f.write('def main(args):\n\tprint("Command Started")')
            pid = pid_tool.create_pid(["new_example"], module="example", nohup=True)
            pid_tool.start_pid(pid, pid_module="example", module="example")
            try:
                while True:
                    try:
                        from run import example_command
                        importlib.reload(example_command)
                        example_command.main()
                        pid_tool.stopped_pid(pid, if_nohup=True)
                        break
                    except:
                        pass
                os.remove(os.path.join(PATH, "new_example.py"))
            except:
                print("Error occured")
                pid_tool.stopped_pid(pid, if_nohup=True)
    except:
        pass

if __name__ == '__main__':
    print("START THIS FILE IN CONSOLE!")
