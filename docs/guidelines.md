## Development Guidelines

All major development will be completed in this repository. While you are encouraged to explore and code in the DevContainer provided by Jeff, class requirements for project iterations require that each member of the team commit code to the repository. So, you need to know how to use Git and GitHub at a basic level.

> [!NOTE]
> The following commands assume you're working in a Linux environment. On a Windows machine, you should execute them in WSL or with the Git terminal for Windows

To contribute to this repository, you need to first clone it to your local machine. The easiest way to do this is in a terminal.

Navigate to a directory on your machine where you prefer to store your code. For me, that's `~/dev/projects`, it may be different for you. I'm just going to refer to it as the `projects` from now on.

```bash
cd ~/dev/projects
```

Clone the repository.

```bash
git clone https://github.com/4306-team-noname/barrios.git
```

Navigate to the repository folder, then clone the client data.

```bash
git clone https://github.com/4306-team-noname/iss-data.git
```

Open the `barrios` directory in VS Code.

```bash
code .
```

Create a python virtual environment. You can do this with VS Code through the command palette (`Ctrl+Shif+P`) by searching for `Python: Create Environment` or through the terminal:

```bash
python -m venv .venv
```

If you create the environment through the command palette, it will be activated automatically. If you do it through the terminal, you'll need to do one more command.

```bash
# On Windows Git Bash
source .venv/Scripts/activate

# On Linux
source .venv/bin/activate
```

You may need to reload the window to ensure VS Code's internal error checker os scoped to your newly created `.venv` environment. `Ctrl+Shif+p > Developer: Reload Window`

Follow the "GitHub Flow" procedure described below to develop new features for the app.
## GitHub flow

[GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)

![Github Flow](https://github.com/4306-team-noname/barrios/blob/598026f08027dbf52ced8c1cb8168cb317da6f46/assets/Iteration3/GitHub%20Flow.drawio.png)