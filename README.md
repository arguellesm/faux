# Faux

Faux is a tool aimed to reduce misinformation along the web. It analyzes 
texts and headlines to categorize them as fake news, clickbait articles 
or seemingly-normal-things. 

## Table of contents

- [Why and how](https://github.com/arguellesm/faux#why-and-how)
- [Dependencies](https://github.com/arguellesm/faux#dependencies)
- [Installation](https://github.com/arguellesm/faux#installation)
- [Usage](https://github.com/arguellesm/faux#usage)
- [Documentation](https://github.com/arguellesm/faux#read-the-docs)

## Why and how

We've lately seen an increase in misleading information presented 
as true in the media. This project seeks an easy-access to 
reliable news and sources for everyone, no matter their previous 
knowledge or background.

Faux takes news and headlines as input and applies heuristics to 
classify them. Being a cloud service, it's constantly being 
updated and refined to achieve the best possible outcome.

## Requirements

- Python **3.5+**.

## Dependencies

Managed with [Poetry](https://python-poetry.org/), check out [`pyproject.toml`](pyproject.toml).

## Installation

#### Poetry

Poetry will manage and install dependencies, ensuring that your 
_Faux_ built is ready to use. According to the [official Poetry
documentation](https://python-poetry.org/docs/#installation), 
install with:

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

```

#### This repository

[Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
this repository and run:

```
cd faux
poetry install
```

This will install all dependencies.

## Usage

#### Syntax check

You can check the syntax of every `.py` file under `src` with:

```
poetry shell
inv check
```

## Read the docs!

Feel free to read a bit more about the project:

- [Users and user journey](docs/users.md)
- [Development tools and why](docs/dev_tools.md)
