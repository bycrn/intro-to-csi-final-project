# Deployment Guide

This guide covers various deployment options for the Taoyuan Waste Sorting application.

## Docker Deployment (Recommended)

The easiest way to deploy both frontend and backend together.

### Prerequisites
- Docker
- Docker Compose

### Steps

1. Clone the repository:
```bash
git clone <repository-url>
cd intro-to-csi-final-project
```

2. Build and run with Docker Compose:
```bash
docker-compose up -d
```

3. Access the application:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

4. Stop the services:
```bash
docker-compose down
```

## Manual Deployment

### Backend Deployment

#### Option 1: Traditional Server (Ubuntu/Debian)

1. Install Python 3.9+:
```bash
sudo apt update
sudo apt install python3.9 python3.9-venv python3-pip
```

2. Create and activate virtual environment:
```bash
cd backend
python3.9 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install and configure Nginx as reverse proxy:
```bash
sudo apt install nginx
```

Create Nginx config `/etc/nginx/sites-available/waste-sorting`:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

5. Create systemd service `/etc/systemd/system/waste-sorting-api.service`:
```ini
[Unit]
Description=Taoyuan Waste Sorting API
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/backend
Environment="PATH=/path/to/backend/venv/bin"
ExecStart=/path/to/backend/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

6. Enable and start service:
```bash
sudo systemctl enable waste-sorting-api
sudo systemctl start waste-sorting-api
```

#### Option 2: Heroku

1. Create `Procfile` in backend directory:
```
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

2. Create `runtime.txt`:
```
python-3.9.16
```

3. Deploy:
```bash
heroku create your-app-name
git subtree push --prefix backend heroku main
```

#### Option 3: Railway/Render

1. Connect your GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### Frontend Deployment

#### Option 1: Netlify

1. Build the application:
```bash
cd frontend
npm install
npm run build
```

2. Deploy to Netlify:
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy
netlify deploy --prod --dir=dist
```

Or use Netlify's GitHub integration for automatic deployments.

#### Option 2: Vercel

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Deploy:
```bash
cd frontend
vercel --prod
```

#### Option 3: GitHub Pages

1. Update `vite.config.js` with base path:
```javascript
export default defineConfig({
  base: '/intro-to-csi-final-project/',
  // ... rest of config
})
```

2. Build and deploy:
```bash
npm run build
# Use gh-pages or manual deployment to gh-pages branch
```

#### Option 4: Firebase Hosting

1. Install Firebase CLI:
```bash
npm install -g firebase-tools
```

2. Initialize Firebase:
```bash
firebase init hosting
```

3. Build and deploy:
```bash
npm run build
firebase deploy
```

## Environment Configuration

### Backend

Create `.env` file in backend directory:
```env
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# Model Configuration
MODEL_PATH=yolov8n.pt

# Firebase (optional)
FIREBASE_CREDENTIALS_PATH=/path/to/credentials.json
```

### Frontend

Create `.env.production` file in frontend directory:
```env
VITE_API_URL=https://your-backend-api.com
```

Update the API URL in source files to use environment variables.

## SSL/HTTPS Setup

### Using Let's Encrypt with Certbot

1. Install Certbot:
```bash
sudo apt install certbot python3-certbot-nginx
```

2. Obtain certificate:
```bash
sudo certbot --nginx -d your-domain.com
```

3. Auto-renewal is configured automatically by Certbot

## Performance Optimization

### Backend
- Use Gunicorn with multiple workers:
```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

- Implement caching for model predictions
- Use Redis for session storage

### Frontend
- Enable Vite build optimizations (already configured)
- Use CDN for static assets
- Implement lazy loading for routes
- Compress images

## Monitoring

### Backend Monitoring
- Use Sentry for error tracking
- Implement logging with Python's logging module
- Monitor with Prometheus + Grafana

### Frontend Monitoring
- Use Google Analytics or Plausible
- Implement error boundary in Vue
- Monitor Core Web Vitals

## Scaling

### Horizontal Scaling
- Use load balancer (Nginx, HAProxy)
- Deploy multiple backend instances
- Share model files via network storage

### Database (if needed)
- Add PostgreSQL for user data
- Use Firebase Firestore for cloud storage
- Implement caching layer with Redis

## Security Checklist

- [ ] Enable HTTPS/SSL
- [ ] Configure CORS properly (restrict origins)
- [ ] Implement rate limiting
- [ ] Add authentication if needed
- [ ] Sanitize file uploads
- [ ] Keep dependencies updated
- [ ] Use environment variables for secrets
- [ ] Implement proper error handling
- [ ] Add request validation
- [ ] Set up security headers

## Troubleshooting

### Backend Issues
- Check logs: `journalctl -u waste-sorting-api -f`
- Verify model file exists
- Check Python version compatibility
- Ensure all dependencies installed

### Frontend Issues
- Clear browser cache
- Check API endpoint configuration
- Verify CORS settings
- Check console for errors

### Docker Issues
- Check logs: `docker-compose logs -f`
- Rebuild images: `docker-compose build --no-cache`
- Check port conflicts
- Verify volume mounts

## Maintenance

### Regular Updates
```bash
# Backend
pip install --upgrade -r requirements.txt

# Frontend
npm update

# Docker
docker-compose pull
docker-compose up -d
```

### Backup
- Backup model files
- Backup configuration files
- Backup uploaded images (if stored)
- Backup database (if applicable)

## Cost Estimation

### Free Tier Options
- **Backend**: Railway (500 hours/month), Render (750 hours/month)
- **Frontend**: Netlify, Vercel, GitHub Pages (unlimited)
- **Total**: $0/month for small scale

### Production Scale
- **Backend**: $5-20/month (DigitalOcean, Linode)
- **Frontend**: $0-5/month (Netlify Pro optional)
- **Domain**: $10-15/year
- **Total**: $5-25/month + domain

## Support

For deployment issues:
1. Check the logs
2. Review the documentation
3. Search for similar issues
4. Create an issue on GitHub

---

Happy Deploying! ♻️
