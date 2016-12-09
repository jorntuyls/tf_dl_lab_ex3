# tf_dl_lab_ex3

This is a course assignment for a deep learning course at university of Freiburg.
Implementation of master and slave for parallel random hyperparameter search.

## Setup  

Install setuptools (Mac OS X)

```
curl https://bootstrap.pypa.io/ez_setup.py -o - | python
```

Install requirements

```
pip install -r requirements.txt
```

## Execution

1. Run master (initializes two worker files)
```
python master.py
```

2. Run workers 0 and 1 in different threads
```
python worker.py 0
python worker.py 1
```
