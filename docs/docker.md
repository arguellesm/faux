# Test docker container

## Criteria

We'll be considering the following criteria:

- **Stability**. We expect the container to continue to function
in the future and to not be vulnerable to environment-specific 
issues.

- **Maintenance**. We expect the container to be well maintained
and to receive regular updates that will impact the following:

  - _Security_. As unupdated systems will be vulnerable to new 
  security bugs patched in current or future versions.

  - _Dependencies_. The project might need to update its current
  dependency set.

- **Python 3.9**. The imagen should ship with Python 3.9 as newer 
versions of Python, namely 3.10, won't work with Faux.

- **Small size**. This is by no means a deal breaker, but it'd be
better if our base image is the smaller size.

- **Fast build times**. Again, this is not a deal breaker unless
the build takes too long, but faster build times are a plus.

## Options

We'll be considering some official Python images as well as Debian
and Ubuntu images. All images were found by searching 'python',
'debian' and 'ubuntu' on [Docker Hub](https://hub.docker.com/).

- `3.9-alpine`
- `3.9-bullseye`
- `3.9-slim`
- `bullseye-slim`
- `20.04`

## Comparisons

### Stability

All chosen images are stated to be stable. However, we found several 
articles and Github issues discussing why Alpine is not a good alternative
as it can lead to bugs and crashes. This is because Alpine uses the `musl`
C library instead of `glibc`, which is used in most distributions. 

### Maintenance

All of the alternatives seem to be equally well-maintained and are the 
official version from each organization.

### Python 3.9

Python 3.9 is already available in all Python images (`3.9-alpine`,
`3.9-slim` and `3.9-bullseye`). 

Although it's not installed in `bullseye-slim` and `20.04`, it could 
be installed through their package managers.

### Size

Python's `3.9-bullseye` was by far the biggest of them with 885MB. Python's
`3.9-slime` waws the next one in size and Python's `3.9-alpine` was the 
smallest.

```
python          3.9-alpine      29035fe3290e   28 minutes ago      48.3MB
python          3.9-slim        8da5d5abf979   29 minutes ago       122MB
python          3.9-bullseye    92db3217958c   29 minutes ago       885MB
debian          bullseye-slim   7a8792605f8c   29 minutes ago      80.4MB
ubuntu          20.04           54c9d81cbb44   30 minutes ago      72.8MB
```

### Build time

The longtest build time was from Debian's `bullseye`, while the fastest ones
were Python's `bullseye-slim` and `ubuntu`.

```
sudo docker build --no-cache alpine         0,04s user 0,04s system 0% cpu 11,529 total
sudo docker build --no-cache bullseye       0,07s user 0,11s system 0% cpu 1:38,51 total
sudo docker build --no-cache slim           0,04s user 0,04s system 0% cpu 14,411 total
sudo docker build --no-cache bullseye-slim  0,04s user 0,04s system 1% cpu 6,751 total
sudo docker build --no-cache ubuntu         0,03s user 0,04s system 0% cpu 8,145 total
```

## Process of elimination and final choice

We first decided to not consider `3.9-alpine` based on the issues found when
researching. As for `3.9-bullseye`, it didn't have any major advantages when 
compared to the rest and it had a significantly bigger size. Considering this, 
we opted for not choosing that one either. 

Stability and maintenance are equally good for the three last candidates. Build 
time and size are better in `ubuntu` and `3.9-bullseye-slim`, while ready-to-go
Python is available in `3.9-slim` and `3.9-bullseye-slim`. Given that, it seems
that the best one overall is `3.9-bullseye-slim`, which will be using for the
project.
