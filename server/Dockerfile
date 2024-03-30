FROM python:3-slim-buster

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code/
COPY . /code/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /code/
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# This command isn't correct, can't find the right path to wsgi
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "server.wsgi", "-t", "0"] 