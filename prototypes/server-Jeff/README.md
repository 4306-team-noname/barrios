# Server prototype

## Usage
If you haven't already activated a Python virtual environment, go to the top-level of the `barrios` directory and type:

```bash
python -m venv venv
```

This will create a virtual environment located at `barrios/venv`. To activate the environment type:

```bash
# Windows/Git bash
source venv/Scripts/activate

# Linux
source venv/bin/activate
```

You should see `(venv)` included somewhere in your terminal prompt.

Now that you have a virtual environment running, navigate back to the `server-prototype` directory, and install the requirements.

```bash
cd prototypes/server-Jeff

pip install -r requirements.txt
```

This should run for a bit while pip downloads and installs the necessary packages. When it's done, navigate to the `src` directory and run the `emmett` command:

```bash
cd src
emmed develop
```

The server should be running at `http://localhost:8000`.