## Development tools and why

### Dependency management

A tool for dependency management was needed to keep track
of the required libraries for building the project and making 
them easy to install for anyone. 

These were the criteria considered when choosing one:
- Common within the Python community
- Ease of use
- Simplicity

The main alternatives for managing dependencies in Python 
were:
  
- [**Pipenv**](https://pipenv.pypa.io/en/latest/)
  
  A dependency manager that seeks to merge the
  capabilities of `pip` and `pipenv`. It's widely used 
  among the community and it's mainly configured through
  the `setup.py` and `Pipeline` files. 

- [**Poetry**](https://python-poetry.org/)

  Very similar to Pipenv, but with faster installation
  time. Most importantly, Poetry supports setting dependencies 
  via `pyproject.toml`, which is the official Python file for 
  dependency management (see [PEP 518](https://www.python.org/dev/peps/pep-0518/#file-format)).
  
Mainly because of `pyproject.toml` support, we chose **Poetry** as
our dependency manager.


### Task runner

A task runner in this project will serve two main purposes: 
_automation_ and _replicability_. 

The criteria for choosing one were the following:
- Common within the Python community
- Ease of use
- Simplicity

The most common task runners in Python were:

- [**Pypyr**](https://pypyr.io/docs/)

  Pypyr uses pipelines defined in yaml. As good as it might be,
  we preferred something closer to Python syntax as it will be
  easier to use in the long term.

- [**doit**](https://pydoit.org/contents.html#)

  _doit_ uses Python and has a quite simple and familiar 
  structure because of that.
  
- [**Invoke**](https://www.pyinvoke.org/)

  Invoke also uses Python and defining and running tasks is 
  simple.


_doit_ and Invoke seemed very similar to one another. When 
looking at examples from their respective manuals, we found
**Invoke** slightly simpler and cleaner, thus deciding on that
one. 


### Test framework

A test framework will allow us to structure tests and execute 
them comfortably.

These were the considered criteria:
- Common within the Python community
- Included in Python
- Ease of use
- Simplicity

When searching for test frameworks, we searched for `python + 
[term]` and `python + [term] + stackoverflow`. These were the 
main results:

- [**Pytest**](https://docs.pytest.org/en/latest/)

  Pytest is an external module for test management. It provides
  detailed information on failed assertions and implements a 
  simple way of writing tests.
  
- [**Unittest**](https://docs.python.org/3/library/unittest.html)

  Unittest is a built-in module in Python that comes with many
  assertion methods. It's a bit less intuitive than Pytest as
  tests need to be inside a class that inherits from 
  `unittest.TestCase`.

Even though Unittest is already included in Python, we opted
for Pytest for its simplicity.


### Assertion library

Assertion libraries essentially offer a range of assertion 
methods to choose from when writing tests.

The same search strategy and criteria were used for finding an
assertion library. The most common results were:

- [**Assertpy**](https://pypi.org/project/assertpy/)
  
  Assertpy is an external assertion library. 

- [**Unittest**](https://docs.python.org/3/library/unittest.html)

  Unittest has many assertion methods with descriptive names,
  making it easy to understand what's happening. As we said 
  above, it's already built in Python.

- [**The `assert` statement**](https://docs.python.org/3/reference/simple_stmts.html#assert) (which is not really a library)

  As the name suggests, `assert` is just a Python statement
  for basic assertions.

We discarded using Assertpy to use as few external libraries
as possible, leaving us with **Unittest** as our assertion library.
we'll be also using the `assert` statement to allow simplicity
when needed.
