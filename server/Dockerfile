FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code/
COPY . /code/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

