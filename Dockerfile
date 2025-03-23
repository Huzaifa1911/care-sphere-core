# Use the correct Python version
FROM python:3.13

WORKDIR /app

# Install dependencies for Poetry
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    rm -rf /var/lib/apt/lists/*

# Ensure Poetry is in PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy only Poetry dependency files first (for caching)
COPY pyproject.toml poetry.lock ./

# Ensure dependencies are installed globally (no virtualenv)
RUN poetry config virtualenvs.create false  
RUN poetry install --no-root 

# Copy the rest of the application code
COPY . .

# Command to run the FastAPI application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
