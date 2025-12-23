# Taoyuan Waste Classification System - Deployment Guide

## 🚀 Quick Start Deployment Options

### 1. **Local Development** (Recommended for testing)
```bash
./deploy.sh local
```
- Accessible at: http://localhost
- Backend API: http://localhost:8000
- Uses Docker Compose for easy setup

### 2. **Production (Self-hosted)**
```bash
./deploy.sh production
```
- Production-optimized containers
- Multi-worker FastAPI backend
- Nginx serving frontend

### 3. **Cloud Deployment (Fly.io)**
```bash
./deploy.sh fly
```
- Automatic HTTPS
- Global CDN
- Auto-scaling
- Free tier available

## 📋 Prerequisites

### For Local/Production:
- Docker & Docker Compose
- 4GB+ RAM (for YOLO models)
- 2GB+ disk space

### For Cloud (Fly.io):
- Fly CLI: `curl -L https://fly.io/install.sh | sh`
- Fly.io account (free)

## 🔧 Setup Instructions

### First-time Setup:
```bash
# Clone and setup development environment
git clone <your-repo>
cd intro-to-csi-final-project
./setup-dev.sh
```

### Deploy Locally:
```bash
./deploy.sh local
```

### Deploy to Cloud:
```bash
# Install Fly CLI (macOS)
curl -L https://fly.io/install.sh | sh

# Login to Fly.io
flyctl auth login

# Deploy
./deploy.sh fly
```

## 🌐 Deployment Environments

| Environment | URL | Use Case |
|------------|-----|----------|
| Local | http://localhost | Development & Testing |
| Production | Your server IP | Self-hosted production |
| Fly.io | https://taoyuan-waste-classifier.fly.dev | Cloud production |

## 📊 Resource Requirements

### Minimum:
- **CPU**: 2 cores
- **RAM**: 4GB (YOLO models are memory-intensive)
- **Storage**: 2GB

### Recommended:
- **CPU**: 4 cores
- **RAM**: 8GB
- **Storage**: 5GB

## 🔍 Monitoring & Troubleshooting

### Check Service Status:
```bash
# Docker Compose
docker-compose ps
docker-compose logs -f

# Fly.io
flyctl status -a taoyuan-waste-classifier
flyctl logs -a taoyuan-waste-classifier
```

### Common Issues:

1. **Out of Memory**: Increase Docker memory limit to 4GB+
2. **Port conflicts**: Stop services using ports 80/8000
3. **YOLO model loading**: Requires ~2GB RAM, be patient during startup

### Performance Optimization:

1. **Use smaller YOLO model** (yolo11s.pt) for faster inference
2. **Enable GPU** for better performance (modify Dockerfile)
3. **Increase worker count** for high traffic

## 🔐 Security Considerations

- Frontend uses HTTPS in production
- Backend runs as non-root user
- CORS properly configured
- Security headers enabled in Nginx

## 🎯 API Endpoints

- `GET /` - Health check
- `POST /api/classify` - Image classification
- `GET /docs` - API documentation

## 📱 Frontend Features

- Drag & drop image upload
- Camera capture support
- Real-time classification results
- Bilingual interface (Chinese/English)
- Waste sorting guidelines

## 💡 Tips for Production

1. **Monitor resource usage** during peak times
2. **Set up log rotation** for long-term deployments  
3. **Consider Redis caching** for frequently accessed data
4. **Use CDN** for static assets in high-traffic scenarios
5. **Set up monitoring** with tools like Prometheus/Grafana

---

**Need help?** Check the logs first, then refer to the troubleshooting section above.