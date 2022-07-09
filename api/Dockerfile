FROM python:3.10-slim-buster@sha256:e826527702aa0f69734a796bc950943106c6edf78e6c7ffc13c4d70d4025fa15

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Activate Python virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
WORKDIR /api
RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt

ENV FLASK_APP=app
ENV FLASK_ENV=production

EXPOSE 8000
