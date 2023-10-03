Install [micromamba](https://mamba.readthedocs.io/en/latest/micromamba-installation.html)

Make sure you're in the correct folder, eg(`barrios/prototypes/server`)

## Create Micromamba Environment
```bash
micromamba create -f env.yaml
```

## Activate Micromamba Environment
```bash
micromamba activate barrios-server-prototype
```

## Install additional requirements
The dependencies in `requirements.txt` are not available in the Conda Forge repository. They can be installed after the `barrios-server-prototype` environment is activated

```bash
pip install -r requirements.txt
```

## Environment path

```bash
~/micromamba/envs/barrios-server-prototype/bin/python
```

You can activate the environment in VS Code using the Micromamba extension so you don't get editor warnings for missing modules.

## Start the server
The following command will start the server located in `barrios/prototypes/server/src/server.py` on the default port `8000`.

```bash
sanic src.server:app --debug --workers=2 -d
```

## TODO
- [ ] Define a flow for uploading data
  - [ ] Expected data shape
  - [ ] error states