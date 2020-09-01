FROM python:slim

LABEL maintainer="Sai <sai@inanutshell.io>"
LABEL website="https://sai.inanutshell.io"

RUN pip install --no-cache-dir --quiet awscli

COPY sync.py /sync.py

CMD [ "python3", "/sync.py" ]