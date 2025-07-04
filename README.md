# Project Setup Guide

Welcome to the project! This README file will guide you through the setup process for running the application using Docker. Please follow the steps below carefully.

---

## Prerequisites

Before starting, ensure you meet the following requirements:

- A Unix-based operating system (Linux) or Windows with WSL enabled.
- **Docker** installed on the host machine. You can install Docker by following the official guide: [Get Docker](https://docs.docker.com/get-docker/).
- **Docker Compose** (comes pre-installed with Docker Desktop).

---

## Step 1: Configure the `.env` File

1. Locate the `.env` file provided in the project root directory.
2. Fill in the required connection details. Here's an example of how your `.env` file should look:

   > **Note**: Leave `POSTGRES_HOST`, `POSTGRES_PORT`, `REDIS_HOST`, `REDIS_PORT` with their default values. Update other fields as per your requirements.

---

## Step 3: Run the Project

After configuring the `.env` file and ensuring Docker is installed, you can start the application by running the following command in your terminal:

   ```bash
  docker compose up --build -d
  ```

## Additional Notes

- To view the logs of the running containers, use:

  ```bash
  docker compose logs -f
  ```


- To stop and remove the running containers, execute:

  ```bash
  docker compose down
  ```