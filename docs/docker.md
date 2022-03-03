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

We'll be considering some official Python images as well as Ubuntu 
images. All images were found by searching 'python' and 'ubuntu' 
on [Docker Hub](https://hub.docker.com/).

- `3.9-alpine`
- `3.9-bullseye`
- `3.9-slim`
- `3.9-bullseye-slim`
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
`3.9-slim`, `3.9-bullseye` and `3.9-bullseye-slim`). 

Although it's not installed in `20.04`, it could be installed through 
its package manager.

### Size

Python's `3.9-bullseye` was by far the biggest of them with 885MB. Python's
`3.9-slime` waws the next one in size and Python's `3.9-alpine` was the 
smallest.

```
python          3.9-alpine          29035fe3290e   28 minutes ago      48.3MB
python          3.9-slim            8da5d5abf979   29 minutes ago       122MB
python          3.9-bullseye        92db3217958c   29 minutes ago       885MB
python          3.9-bullseye-slim   7a8792605f8c   29 minutes ago      80.4MB
ubuntu          20.04               54c9d81cbb44   30 minutes ago      72.8MB
```

We also conducted a size tests with the Dockerfile needed to build the project.
The Dockerfile used for Python images (except Alpine) is the one that can be 
currently found here. For Ubuntu, we had to add the following lines before
the `mkdir` command:

```
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip
```

As for Alpine, we installed more packages as it didn't come with `gcc` nor `g++`
(among others) and they were needed to manage the dependency set we currently have.
This resulted in the following lines before the `mkdir` command:

```
RUN apk update && \
    apk add gcc \
    g++\
    libc-dev \
    libffi-dev \
```

We also changed `useradd` for `adduser`, as the first one isn't available in
Alpine.

Even after adding this, we still faced issues with `numpy` and BLAS/LAPACK 
libraries. Because of this reason we weren't able to successfully build it
and that's also why it doesn't appear in the results bellow.

These are the sizes obtained with these Dockerfiles:

```
python       3.9-slim             189911089e91   29 seconds ago   511MB
python       3.9-bullseye         b1500797ba20   31 seconds ago   1.3GB
python       3.9-bullseye-slim    164e1c98f165   48 minutes ago   511MB
ubuntu       20.04                a6f3597b527e   5 seconds ago    818MB
```

Considering these results we can see that `3.9-slim` and `3.9-bullseye-slim`
are the smallest ones.


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
researching, and also the problems faced when designing a Dockerfile for it. 
As for `3.9-bullseye`, it didn't have any major advantages when compared to 
the rest and it had a significantly bigger size. Considering this, we opted 
for not choosing that one either. 

Stability and maintenance are equally good for the three last candidates. Build 
time and size are better in `3.9-slim` and `3.9-bullseye-slim`, while ready-to-go
Python is also available in those two. Given that, it seems that the one of the
best images might be `3.9-bullseye-slim`, as it similar in size and features 
to `3.9-slim` but not as common of an image. 

In any case, both would work equally well and we could consider creating multiple
images in the future.
