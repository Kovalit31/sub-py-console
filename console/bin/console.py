from lib import config

def command_starter():
    while True:
        try:
            inputed = input(config.PS1).lower()
            if inputed:
                command_arr = inputed.split(" ")
                command_init(command_arr)
        except EOFError or KeyboardInterrupt as e:
            break

def command_init(whatuse):
    with open("command_py.py", "w") as f:
        f.write(f"from {config.MODULE_BIN_PATH} import {whatuse[0]}\n")
        f.write(f"def main():\n    ")
        f.write("{0}.main()".format(whatuse[0])) #[\"{1}\"] , whatuse[1:].join('","')
        f.close()
    try:
        import command_py
        command_py.main()
        del(command_py)
    except Exception as e:
        if config.DEBUG:
            print(e)
            print(dir())

def main():
    print(config.HAT)
    print("Licensed under",config.LICENSE)
    command_starter()
