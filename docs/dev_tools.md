## Development tools and why

### [Poetry](https://python-poetry.org/)

We use Poetry as a dependency management tool to keep track
of the libraries needed to build the project. This makes it 
easier for anyone to replicate the project. 

The main alternatives to Poetry are Pip and Pipenv:

- [Pip](https://pypi.org/project/pip/) 

  Pip is a package manager, meaning that dependency updates 
  must be done manually. This will defeat the purpose of using
  it for automation.

- [Pipenv](https://pipenv.pypa.io/en/latest/)

  The main differences between Pipenv and Poetry are that Poetry
  has much faster install times and supports `pyproject.toml`, 
  which is the official Python file for dependency management (see
  [PEP 518](https://www.python.org/dev/peps/pep-0518/#file-format)).


### [Invoke](https://www.pyinvoke.org/)

Invoke is our task runner of choice. It inherits a minimal yet 
powerful philosophy from GNU Make and is broadly used among the 
Python community.

Some alternatives are:

- [Pypyr](https://pypyr.io/docs/)

  Pypyr uses pipelines defined in yaml. There are many differences
  between these two, but the key for choosing one over the other
  was being more used to Python and finding easier to work with 
  Invoke's approach.

- [doit](https://pydoit.org/contents.html#)

  _doit_ has quite a similar approach to Invoke and uses Python as 
  well. However, Invoke's community is much bigger, which usually
  translates to more resources and easier troubleshooting.
