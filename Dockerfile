# Use Python 3.12 as the base image
FROM python:3.12-slim

# Install Poetry and set configuration for no virtual environment
RUN pip install poetry==1.7.1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONPATH = /app
# Set working directory
WORKDIR /app

# Copy Poetry config files first to leverage Docker cache for dependencies
COPY pyproject.toml poetry.lock ./

# Install dependencies without dev dependencies for production
RUN poetry install --no-root

# Copy the application source code into the container
COPY ./app /app

# Expose the port for FastAPI
EXPOSE 8000

# Verify contents of the directory
RUN echo "Contents of /app:" && ls -R /app

# Command to run FastAPI server
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
