FROM python:3.7
WORKDIR /app
COPY requirements.txt .
RUN apt update \
    && apt install -y mecab libmecab-dev mecab-ipadic-utf8 \
    && pip install -r ./requirements.txt