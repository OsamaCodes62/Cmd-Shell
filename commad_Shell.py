import os
import subprocess

builtin = ["echo", "exit 0", "type"]
extension = [".exe", ".bat", ".cmd"]
def getPath(cmd):
    paths = os.getenv("PATH").split(os.pathsep)
    for path in paths:
        if os.name == "nt":
            for exe in extension:
                fullpath = os.path.join(path, cmd+exe)
                if os.path.exists(fullpath):
                    return fullpath
        else:
            fullpath = os.path.join(path, cmd)
            if os.path.exists(fullpath):
                return fullpath

    return None

while True:
    user_input = input("$ ")

    match user_input.split(" "):
        case ["exit", "0"]:
            exit()
        case ["echo", *arg]:
            print(*arg)
        case ["type", *arg]:
            forType = " ".join(arg)
            thePath = getPath(forType)
            if forType in builtin:
                print(forType, "is shell builtin command")
            elif thePath:
                print(f"{forType} is {thePath}")
            else:
                print(forType, ": command not found")
        case ["pwd"]:
            print(os.getcwd())
        case ["cd", *arg]:
            path = "".join(arg)
            os.chdir(path)
        case _:
            user_cmd = user_input.split(" ")
            fullCommand = getPath(user_cmd[0])

            if fullCommand:
                try:
                    subprocess.run(user_cmd)
                except:
                    print(user_input,": is not a valid command")
            else:
                print(user_input,": is not a valid command")
