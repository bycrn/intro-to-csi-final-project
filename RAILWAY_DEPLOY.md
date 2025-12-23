# 🚂 Railway Deployment Guide - Taoyuan Waste Classifier Backend

## 🚀 Quick Deploy (Recommended)

### Method 1: Deploy from GitHub (Easiest)

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Add Railway deployment configuration"
   git push origin main
   ```

2. **Deploy on Railway:**
   - Go to [railway.app](https://railway.app) and sign up/login with GitHub
   - Click "New Project" > "Deploy from GitHub repo"
   - Select your `intro-to-csi-final-project` repository
   - Railway will automatically detect the Dockerfile and deploy

3. **Set up environment variables:**
   - In Railway dashboard: Variables tab
   - Add: `PYTHONPATH` = `/app`
   - Add: `ENVIRONMENT` = `production`
   - Railway will automatically set `PORT` variable

4. **Get your backend URL:**
   - Go to Settings > Domains
   - Copy the generated URL (like `https://taoyuan-waste-backend-production.up.railway.app`)

## ⚙️ Alternative: Railway CLI Deploy

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Initialize project (run from project root)
railway init

# Deploy
railway up
```

## 🔧 Configuration Details

Your Railway deployment is configured with:
- **Docker build** using `backend/Dockerfile`
- **Memory limit:** 2GB (needed for YOLO models)
- **CPU limit:** 1 core
- **Auto-restart** on failure
- **Health checks** on the root endpoint

## 📡 Update Frontend Configuration

After Railway deployment, update your frontend:

1. **Copy your Railway backend URL**
2. **Update Netlify environment variables:**
   - Go to Netlify dashboard > Site settings > Environment variables
   - Update `VITE_API_URL` to your Railway URL
   - Example: `https://taoyuan-waste-backend-production.up.railway.app`

3. **Or update locally and redeploy:**
   ```bash
   # Edit frontend/.env.production
   VITE_API_URL=https://your-railway-backend-url.up.railway.app
   
   # Commit and push to trigger Netlify rebuild
   git add .
   git commit -m "Update API URL for Railway backend"
   git push origin main
   ```

## 🔍 Monitoring & Logs

- **View logs:** Railway dashboard > Deployments > Click on latest deployment
- **Monitor resources:** Dashboard shows CPU/memory usage
- **Check health:** Visit your Railway URL in browser (should show API status)

## 💰 Pricing

- **Free tier:** $5 credit per month (sufficient for development/testing)
- **Pro plan:** $20/month for production use
- Your YOLO backend will use ~1-2GB RAM and moderate CPU

## 🐛 Troubleshooting

**Build fails?**
- Check Docker logs in Railway dashboard
- Ensure `backend/Dockerfile` builds locally: `docker build -t test backend/`

**Out of memory?**
- Upgrade to Railway Pro for more resources
- Or use smaller YOLO model (`yolo11s.pt` instead of `yolo11m.pt`)

**API not responding?**
- Check health endpoint: `https://your-app.up.railway.app/`
- Verify environment variables are set
- Check Railway logs for startup errors

**CORS issues?**
- Ensure your backend allows requests from your Netlify domain
- Update CORS settings in `backend/app/main.py`

## ✅ Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] Railway project created and deployed
- [ ] Backend health check passes (`/` endpoint responds)
- [ ] Railway URL copied
- [ ] Frontend `VITE_API_URL` updated with Railway URL
- [ ] Frontend redeployed on Netlify
- [ ] Full end-to-end test (upload image, get classification)

## 🌐 Example URLs

- **Railway Backend:** `https://taoyuan-waste-backend-production.up.railway.app`
- **API Health Check:** `https://your-app.up.railway.app/`
- **API Documentation:** `https://your-app.up.railway.app/docs`
- **Netlify Frontend:** `https://your-site.netlify.app`

Your full-stack app will be live with:
- Frontend on Netlify (fast, global CDN)  
- Backend on Railway (powerful, YOLO-capable)

## 🔐 Security Note

Railway automatically provides HTTPS, but ensure your frontend-backend communication uses the secure Railway URL.