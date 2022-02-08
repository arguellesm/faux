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
reopened.


## GitLab CI/CD

We'll use GitLab CI/CD to trigger unit tests whenever
a PR is opened. The tests must pass for the PR to be
approved and merged.
