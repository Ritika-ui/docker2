# 🚀 Docker + Nginx DevOps Mini Project
## 🌐 Live Demo
https://first-project-with-docker-ci.onrender.com



This project demonstrates a basic DevOps setup using **Docker**, **Docker Compose**, and **Nginx** with a simple Flask application.

---

## 📌 Project Overview

This setup includes:
- A Flask application (backend)
- Docker containerization
- Docker Compose for multi-container setup
- Nginx as a reverse proxy
- Volume for live code updates

---

## 🧱 Project Structure
# 🚀 Docker + Nginx DevOps Mini Project

project/
│
├── app/
│ └── app.py
│
├── Dockerfile
├── docker-compose.yml
│
└── nginx/
└── nginx.conf

---

## 🐍 Application (Flask)

The app includes:
- `/` → returns a welcome message
- `/hello` → returns a secondary message

---

## 🐳 Dockerfile

- Uses Python base image
- Sets working directory
- Copies application code
- Installs Flask
- Runs the app

---

## ⚙️ Docker Compose

Defines two services:

### 1. App Service
- Builds Docker image
- Runs Flask app on port `5000`
- Uses volume for live updates

### 2. Nginx Service
- Acts as reverse proxy
- Exposes port `8080`
- Forwards requests to the app

---

## 🌐 Architecture Flow

Browser → localhost:8080 → Nginx → app:5000 → Flask App

