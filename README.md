# Custom Shell Implementation

This project is a simple command-line shell built in Python! It mimics basic shell functionality, handling built-in commands, path resolution, and external executables.

## 🛠 Features

- **Built-in commands:** `echo`, `exit 0`, `type`, `pwd`, `cd`
- **Path resolution:** Finds executables in directories listed in the `PATH` environment variable.
- **Command execution:** Runs external programs using `subprocess.run`.
- **Platform support:** Works on Linux and Windows (with support for `.exe`, `.bat`, and `.cmd` extensions on Windows).

## 🏃‍♀️ How It Works

The shell continuously waits for user input, processes the command, and executes it. It can handle both built-in and external commands.

### 📂 Built-in Commands

- `exit 0`: Exits the shell.
- `echo <args>`: Prints arguments to the terminal.
- `type <command>`: Shows whether a command is built-in or the path to its executable.
- `pwd`: Prints the current working directory.
- `cd <path>`: Changes the current directory.

### 🚀 External Commands

If the command isn’t built-in, the shell searches for it in the directories listed in the `PATH`. If found, it executes the command; otherwise, it returns a "command not found" error.

## 📂 Project Structure

```
├── shell.py           # Main Python script containing the shell implementation
├── README.md          # Project documentation
```

## 🛠 Installation & Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/custom-shell.git
cd custom-shell
```

2. Run the script:

```bash
python shell.py
```

3. Start using the shell!

```bash
$ echo Hello World
Hello World
$ pwd
/home/user/custom-shell
$ type ls
ls is /bin/ls
$ exit 0
```

## 🧠 How Command Resolution Works

- **Built-in command?** → Execute directly.
- **In ******\*\*********`PATH`******\*\*\*\*******?\*\* → Run with `subprocess.run`.
- **Not found?** → Print an error message.

The `getPath` function loops through the `PATH` directories to locate the executable.

## 🛠 Example Usage

```bash
$ echo Hello
Hello
$ pwd
/home/user
$ cd /tmp
$ pwd
/tmp
$ type echo
echo is shell builtin command
$ python -V
Python 3.12.7
```

## 📜 License

MIT License

---

Let me know if you'd like me to tweak anything or add more details! 🚀
