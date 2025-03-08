# AI Agentic Healthcare App

## Overview
This is an AI-powered healthcare application that allows users to:
- Upload and analyze medical documents and test reports.
- Chat with their reports using an AI-powered assistant.
- Search for doctors and clinics using LLM-based search.

The backend is built with **FastAPI** in a **microservices architecture**, using **Poetry** as the package manager.

---

## Getting Started

### **1. Prerequisites**
Make sure you have the following installed:
- **Python 3.10+** ([Download Here](https://www.python.org/downloads/))
- **Poetry** (Dependency management)  
  Install Poetry if not already installed:
  ```sh
  curl -sSL https://install.python-poetry.org | python3 -
  ```
- **Docker & Docker Compose** (For running services)  
  Install Docker from [Docker's website](https://www.docker.com/).

---

### **2. Setup the Project**
Clone the repository:
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

Initialize the Poetry virtual environment:
```sh
poetry install
```
Activate the virtual environment:
```sh
poetry shell
```

---

### **3. Environment Configuration**
Create a `.env` file in the project root and add the following:
```env
# Database Configuration
DATABASE_HOST=postgres
DATABASE_PORT=5432
DATABASE_NAME=healthcare
DATABASE_USER=admin
DATABASE_PASSWORD=admin
DATABASE_URL=postgresql://admin:admin@postgres:5432/healthcare

# Redis Configuration
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_URL=redis://redis:6379/0

# Application Secret Key
SECRET_KEY=your_secret_key_here

# API Keys (if needed)
EXTERNAL_API_KEY=your_api_key_here
```

The `docker-compose.yml` file will automatically reference these environment variables.

---

### **4. Running the Development Server**
To start the FastAPI dev server, run:
```sh
poetry run fastapi dev app/main.py
```

Now, open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the interactive API documentation.

---

### **5. Running with Docker**
To start the app with Docker Compose:
```sh
docker-compose up --build
```

#### **Docker Compose Services**
The `docker-compose.yml` file defines the following services:
- **fastapi (FastAPI application)**: The main backend service.
- **postgres (PostgreSQL)**: Stores user and application data.
- **redis**: Provides caching and session management.
- **traefik**: Acts as a reverse proxy and API gateway.

Docker will use the `.env` file for configuration.

---

### **6. Linting & Formatting**
To maintain code quality, run:
```sh
poetry run black .
poetry run isort .
poetry run flake8 .
```

---

### **7. Running Tests**
To execute the test suite:
```sh
poetry run pytest
```

---

## **Project Structure**
```
📦 your-repo/
 ┣ 📂 app/                  # Main application module
 ┃ ┣ 📂 api/                # API routes
 ┃ ┣ 📂 models/             # Database models
 ┃ ┣ 📂 services/           # Business logic
 ┃ ┣ 📂 core/               # Configuration & settings
 ┃ ┗ main.py               # FastAPI entry point
 ┣ 📜 .env                  # Environment variables
 ┣ 📜 pyproject.toml        # Poetry dependency file
 ┣ 📜 Dockerfile            # Docker setup
 ┣ 📜 docker-compose.yml    # Docker Compose services
 ┣ 📜 README.md             # Documentation
 ┗ 📜 .gitignore            # Ignored files
```

---

## **Contributing**
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

---

## **License**
This project is licensed under the **MIT License**.