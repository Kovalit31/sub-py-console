import os, sys
import config as cfg

def main():
    while True:
        try:
            request_command = input(f"{cfg.PS1}")
            command_splitted = request_command.split(" ")
            continue_run = True
            try:
                try:
                    exec(f"{command_splitted[0]}.get_metadata()")
                except:
                    pass
                exec(f"import {cfg.MODULE_BIN_PATH}{command_splitted[0]}")
            except:
                continue_run = False
                print("No such command")
            if continue_run:
                if command_splitted[0] != "quit" and command_splitted[0] != "exit":
                    exec(f"{command_splitted[0]}.main({command_splitted[1:]})")
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    main()