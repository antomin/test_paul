# Project Setup Guide

Welcome to the project! This README file will guide you through the setup process for running the application using Docker. Please follow the steps below carefully.

---

## Prerequisites

Before starting, ensure you meet the following requirements:

- A Unix-based operating system (Linux/MacOS) or Windows with WSL enabled.
- **Docker** installed on the host machine. You can install Docker by following the official guide: [Get Docker](https://docs.docker.com/get-docker/).
- **Docker Compose** (comes pre-installed with Docker Desktop).

---

## Step 1: Configure the `.env` File

1. Locate the `.env` file provided in the project root directory.
2. Fill in the required connection details. Here's an example of how your `.env` file should look:

   > **Note**: Leave `POSTGRES_HOST` and `REDIS_HOST` with their default values (`localhost`). Update other fields as per your requirements.

---

## Step 2: Install Docker on the Host

If Docker is not already installed on your system, follow the detailed instructions for your specific platform on the official Docker website:

- [Install Docker](https://docs.docker.com/get-docker/)

Ensure that both **Docker** and **Docker Compose** are properly installed and functioning by running the following commands in your terminal: