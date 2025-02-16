import os

builtin = ["echo", "exit 0", "type"]

while True:
    user_input = input("$ ")

    match user_input.split(" "):
        case ["exit", "0"]:
            exit()
        case ["echo", *arg]:
            print(*arg)
        case ["type", *arg]:
            temp = arg
            print(type(temp))
            forType = " ".join(arg)
            if forType in builtin:
                print(forType, "is shell builtin command")
            else:
                print(forType, ": command not found")
        case _:
            print(user_input,": is not a valid command")
