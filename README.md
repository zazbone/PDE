# PDE

## For developpers

This repos is composed of 2 part:

- lib with function for PDE
- exercices, test part of the repos using jupyter files

Setup your venv for developpement

```shell
python -m venv venv
venv/bin/pip install dev_req.txt
venv/bin/pip install -e .
```

Enable jupyter kernel
```shell
venv/bin/python -m ipython kernel install --user --name=myproject
```

Then open the project with jupyter notebook
```shell
venv/bin/python -m jupyter notebook
```

## Sources
- [introduction]()
