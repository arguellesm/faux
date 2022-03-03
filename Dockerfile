FROM python:3.9-slim-bullseye

LABEL org.opencontainers.image.version="0.0.5-beta"
LABEL org.opencontainers.image.authors="arguellesm@github"

RUN mkdir -p /app/test && \
    useradd -U -m faux && \
    chown -R faux:faux /app 

USER faux

ENV PATH=$PATH:/home/faux/.local/bin

WORKDIR /app/test

COPY poetry.lock pyproject.toml tasks.py /app/

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

ENTRYPOINT ["inv", "test"]
