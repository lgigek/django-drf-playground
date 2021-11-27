FROM python:3.9.1-slim

# Creates application directory
WORKDIR /app

# Creates an appuser and change the ownership of the application's folder
RUN useradd appuser && chown appuser /app

# Installs poetry and pip
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false --local

# Copy dependency definition to cache
COPY --chown=appuser poetry.lock pyproject.toml README.md /app/

# Installs projects dependencies as a separate layer
RUN poetry install --no-root

# Copies and chowns for the userapp on a single layer
COPY --chown=appuser . /app