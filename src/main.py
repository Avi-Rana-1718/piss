import re
import os
import subprocess
from enum import Enum

VERSION = "1.0"

ART = r"""
        _
 _ __  (_) ___  ___
| '_ \ | |/ __|/ __|
| |_) || |\__ \\__ \
| .__/ |_||___/|___/
|_|
""".strip("\n")


SNAKE = "~~~~~~~~~~~~~~~~~~~~~~(:>  sssss"



class InbuiltCmds(Enum):
    HELP = "help"
    CD = "cd"
    EXIT = "exit"
    CLEAR = "clear"
    

def main():
    print(ART)
    print()
    print(f" piss v{VERSION} — Python Interactive Shell System")
    print()
    print(SNAKE)
    
    while True:
    
        print("> ", end="")
        
        try:
            msg = input()
        except KeyboardInterrupt:
            break
        
        args = read_input(msg)
        return_code = run_input(args);
        
        if return_code == 0:
            break


def read_input(input):
    split_delimeters = " \t\r\n\a"
    
    cleaned = input.strip(split_delimeters)
    
    if not cleaned:
        return []
    
    
    return re.split(r"[" + split_delimeters + "]+", cleaned)
    
    

def run_input(args) -> int:
    
    if not args:
        return 1
    
    if args[0] in InbuiltCmds:
        return handle_inbuild_cmds(args)
    
    try:
     subprocess.run(args)
    except FileNotFoundError:
        print(f"piss: Command not found: {args[0]}")
    except Exception as e:
        print(f"piss: {e}")
    
    return 1

def handle_inbuild_cmds(args) -> int:
    process_name: InbuiltCmds = InbuiltCmds(args[0])
    
    match process_name:
        case InbuiltCmds.EXIT:
            return 0
        case InbuiltCmds.CLEAR:
            print("\033[H\033[2J", end="", flush=True)
            return 1
        case InbuiltCmds.CD:
            try:
                os.chdir(args[1])
            except Exception as e:
                print(f"piss: {e}")
        case InbuiltCmds.HELP:
                print("piss help")

if __name__ == "__main__":
    main()

