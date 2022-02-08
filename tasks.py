from invoke import task
import glob


@task(help={'format': 'Pylint output format (parseable, colorized, json, msvs).'})
def check(c, format='colorized'):
    """
    Check Python syntax.

    Parameters
    ----------
    format : str
        Pylint output format.
    """

    files = ' '.join(glob.glob('./src/*.py'))

    c.run('pylint -E -f {} {}'.format(format, files))


@task
def test(c):
    """
    Run Pytest tests.
    """

    c.run('python -m pytest test')


@task
def docker(c):
    """
    Run Pytest tests inside docker container.
    """

    c.run('docker run -t -v `pwd`:/app/test arguellesm/faux')
