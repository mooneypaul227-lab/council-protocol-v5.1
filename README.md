# Council Protocol-v5.1
**Security Management**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.103+-green.svg)](https://fastapi.tiangolo.com/)

A comprehensive security management framework for the Council Protocol architecture v5.1.

## Features

- 🔐 **Security-First Design**: Built with security management as a core principle
- 🚀 **FastAPI Backend**: High-performance Python API framework
- 🐳 **Docker Ready**: Containerized deployment with docker-compose
- 📊 **Monitoring & Analytics**: Integrated Prometheus + Grafana stack
- 🗄️ **PostgreSQL Database**: Robust relational data storage
- ⚡ **Redis Caching**: High-speed in-memory cache layer
- 🧪 **Comprehensive Testing**: pytest suite with example tests
- 📚 **API Documentation**: Interactive Swagger UI & ReDoc

## Quick Start

### Prerequisites
- Python 3.11+
- Docker & Docker Compose (for containerized deployment)
- Git

### Local Development
```bash
# Clone repository
git clone https://github.com/mooneypaul227-lab/council-protocol-v5.1.git
cd council-protocol-v5.1

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env

# Run application
python main.py
