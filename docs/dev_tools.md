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


### Test runner 

A test runner will allow us to structure tests and execute 
them comfortably.

These were the considered criteria:
- Common within the Python community
- Included in Python
- Ease of use
- Simplicity

When searching for test runners, we searched for `python + 
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

The project doesn't have any specific needs regarding assertions, 
but we expect the following from our assertion library:
- To have a minimum of popularity, as that will be useful 
for troubleshooting. We will be using Github starts to measure this,
and won't consider tools that have less than 100.
- To be a currently maintained project.
- To be somehow close to natural language.
- A plus for being a built0-in module from Python.

We'll be discussing the following alternatives:

- [**Assertpy**](https://pypi.org/project/assertpy/)
  
  Assertpy is an external assertion library. 
  - It has quite a big community with over 300 stars on Github and 
  several forks.
  - It is maintained with more or less recent commits from 6 months ago.
  - Assertions are easy to understand and resemble natural language:
    ```python
    assert_that(1 + 1).is_equal_to(2)
    ``` 
  - It's not a built-in module

  Apart from that, Assertpy seems a bit popular and has been already 
  used in other projects. For the sake of not using the same tools, we'll
  be discarding this one.

- [**Unittest**](https://docs.python.org/3/library/unittest.html)

  Unittest is Python's unit testing framework.

  - Big community, plenty of information on Github. Since it's embedded 
  in Python repository we won't be counting stars here.
  - It is maintained as part of the Python project.
  - Assertions look a bit more function-like than those of Assertpy:
    ```python
    self.assertEqual(1 + 1), 2)
    ```
  - It's a built-in module.

  Again, this has been used many times and we'll be avoiding it for that
  reason. On top of that, Unittest has a particular way of approaching
  tests, where a child class of `TestCase` is expected, making the process
  a bit more sluggish.

- [**Grappa**](https://github.com/grappa-py/grappa)

  - Decently sized community with 129 stars and some forks.
  - The project hasn't had any activity since over a year ago.
  - Assertions have a different look than what's usually expected but 
  they are easy to understand:
    ```python
    2 | should.be.equal.to(1 + 1)
    ```
  - Not a built-in module.

  Grappa is fine for the most part, although the lack of recent activity 
  is not the best.

- [**Verify**](https://github.com/grappa-py/grappa)

  - Only 67 starts on Github.
  - No activity since 5 years ago.
  - Quite natural looking assertions:
    ```python
    ensure(1 + 1).Equal(2)
    ```

  Discarded for the first two reasons.

- [**Pytruth**](https://github.com/google/pytruth)

  - Again, decently sized community with 132 stars and 25 forks.
  - Lasts commits are from 11 months ago.
  - Assertions are basicly the same as in Assertpy:
    ```python
    AssertThat(1 + 1).IsEqualTo(2)
    ```
  - Not a built-in module.

We'll not be using Grappa for the lack of recent activity in the 
project. Assertpy and Pytruth are the two best options, Assertpy being
probably the best of them. However, because it has been common and 
it's used in other projects, we'll be trying out Pytruth.
