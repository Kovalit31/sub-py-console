import os, sys
import config as cfg

def main():
    while True:
        try:
            request_command = input(f"{cfg.PS1}")
            command_splitted = request_command.split(" ")
            continue_run = True
            try:
                exec(f'''import {cfg.MODULE_BIN_PATH}{command_splitted[0]}
{command_splitted[0]}.main({command_splitted[1:]})
''')
            except:
                print("No such command")
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    main()