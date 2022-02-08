# CI Systems

## GitHub Actions

GitHub Actions will be used to test the project with
different Python versions.

Because Poetry needs at least Python 3.5, we'll conduct
preliminary tests from that version up to 3.10. These
tests were done locally using Docker containers. After
that, we found that:

- `numpy` requires Python >=3.8.
- `scipy` can't be built from sources on Python 3.10.

With this information, we'll be testing the project
on 3.8 and 3.9 whenever a PR is either opened or 
reopened. The [**`setup-python`**](https://github.com/actions/setup-python)
action is used to set up a version-specific Python 
environment, in which the project is then built and 
tested.

Because the GitLab CI/CD test is run inside a Docker
container that ships with Python 3.9, there is no need 
to test for that version in the GitHub action. 


## GitLab CI/CD

We'll use GitLab CI/CD to trigger unit tests whenever
a PR is opened. The tests must pass for the PR to be
approved and merged.
