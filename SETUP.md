# Council Protocol v5.1 - Complete Setup Guide

## Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/mooneypaul227-lab/council-protocol-v5.1.git
cd council-protocol-v5.1
```

### 2. Development Setup (Local)
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Run the application
python main.py
```

### 3. Docker Deployment
```bash
# Build and run all services
docker-compose up -d

# Verify services are running
docker-compose ps
```

## Services & Access Points

Once running, access the following:

- **Frontend (Command Center)**: http://localhost:3000
- **API (FastAPI Docs)**: http://localhost:8000/docs
- **API Status**: http://localhost:8000/api/status
- **Monitoring (Grafana)**: http://localhost:3001 (admin/admin)
- **Prometheus Metrics**: http://localhost:9090
- **PostgreSQL Database**: localhost:5432 (council/council_password)
- **Redis Cache**: localhost:6379

## Testing

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test
```bash
pytest tests/test_main.py -v
```

### Run with Coverage
```bash
pytest tests/ --cov=. --cov-report=html
```

## Database Management

### Access PostgreSQL
```bash
psql -h localhost -U council -d council_db
```

### Run Migrations
```bash
# Initialize database (automatic on docker-compose up)
# For local development, ensure init.sql is executed
```

## Going Live - Production Deployment

### Environment Configuration
1. Update `.env` with production settings:
```bash
ENVIRONMENT=production
DATABASE_URL=postgresql://user:password@prod-db:5432/council_db
REDIS_URL=redis://prod-redis:6379
SECRET_KEY=your-production-secret-key
```

### Production Deployment Steps

#### Option 1: Docker Swarm
```bash
docker swarm init
docker stack deploy -c docker-compose.yml council-protocol
```

#### Option 2: Kubernetes
```bash
# Create namespace
kubectl create namespace council-protocol

# Apply manifests (create k8s/ directory with manifests)
kubectl apply -f k8s/ -n council-protocol
```

#### Option 3: Traditional VPS/Cloud Server
```bash
# On production server
git clone https://github.com/mooneypaul227-lab/council-protocol-v5.1.git
cd council-protocol-v5.1
docker-compose -f docker-compose.prod.yml up -d
```

### Security Checklist

- [ ] Update `SECRET_KEY` with strong random value
- [ ] Set up HTTPS/SSL certificates
- [ ] Configure firewall rules
- [ ] Enable database backups
- [ ] Set up monitoring and alerting
- [ ] Configure logging aggregation
- [ ] Enable audit logging
- [ ] Set up automated deployments (CI/CD)
- [ ] Configure rate limiting
- [ ] Enable security headers

### Health Checks & Monitoring

```bash
# Health check endpoint
curl http://localhost:8000/health

# Security status
curl http://localhost:8000/api/security/status

# API documentation
curl http://localhost:8000/api/docs
```

### Logs

View application logs:
```bash
docker-compose logs -f api
docker-compose logs -f frontend
docker-compose logs -f db
```

### Stopping Services

```bash
# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

## Support & Documentation

- **API Docs**: http://localhost:8000/docs (Interactive Swagger UI)
- **ReDoc**: http://localhost:8000/redoc
- **GitHub**: https://github.com/mooneypaul227-lab/council-protocol-v5.1

## Troubleshooting

### Port Already in Use
```bash
# Find and kill process using port
lsof -i :8000
kill -9 <PID>
```

### Database Connection Issues
```bash
# Test PostgreSQL connection
psql -h localhost -U council -d council_db -c "SELECT 1;"
```

### Docker Issues
```bash
# Rebuild images
docker-compose build --no-cache

# Restart services
docker-compose restart
```

---

**Last Updated**: 2026-07-13
**Version**: 5.1.0
