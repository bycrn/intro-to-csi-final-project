# 🚀 Netlify Deployment Guide

## Quick Deploy to Netlify

### Option 1: Deploy from GitHub (Recommended)

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Add Netlify deployment configuration"
   git push origin main
   ```

2. **Connect to Netlify:**
   - Go to [netlify.com](https://netlify.com) and sign up/login
   - Click "New site from Git" 
   - Choose GitHub and select your repository
   - Netlify will auto-detect the settings from `netlify.toml`

3. **Configure environment variables in Netlify:**
   - Go to Site settings > Environment variables
   - Add: `VITE_API_URL` = `https://your-backend-api-url.com`
   - Add: `NODE_ENV` = `production`

### Option 2: Manual Deploy

1. **Build locally:**
   ```bash
   cd frontend
   npm install
   npm run build
   ```

2. **Deploy to Netlify:**
   - Drag and drop the `frontend/dist` folder to [netlify.com/drop](https://app.netlify.com/drop)

## 🔧 Backend Deployment Options

Since Netlify can't host your Python/YOLO backend, deploy it separately:

### Recommended Backend Hosts:
1. **Railway** (easiest): https://railway.app
2. **Render** (free tier): https://render.com  
3. **Fly.io** (good performance): https://fly.io

### Backend Deployment Commands:
```bash
# Railway
railway login
railway deploy

# Render - connect your GitHub repo

# Fly.io
flyctl deploy
```

## 📡 Update API URL

After deploying your backend, update the frontend:

1. **In Netlify dashboard:**
   - Go to Site settings > Environment variables
   - Update `VITE_API_URL` to your backend URL

2. **Or update the file:**
   ```bash
   # Edit frontend/.env.production
   VITE_API_URL=https://your-actual-backend-api.com
   ```

## 🌐 Custom Domain (Optional)

1. In Netlify: Site settings > Domain management
2. Add your custom domain
3. Netlify will handle HTTPS automatically

## ✅ Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] Netlify site connected to GitHub repo  
- [ ] Backend deployed to Railway/Render/Fly.io
- [ ] `VITE_API_URL` updated in Netlify environment variables
- [ ] Test the deployed frontend
- [ ] Test API communication between frontend and backend

## 🔍 Troubleshooting

**Frontend not loading?**
- Check build logs in Netlify dashboard
- Ensure `npm run build` works locally

**API calls failing?**
- Check CORS settings in backend
- Verify `VITE_API_URL` environment variable
- Test backend URL directly in browser

**Images not uploading?**
- Check file size limits (Netlify: 5MB functions, Backend host specific)
- Verify CORS headers allow file uploads

Your frontend will be live at: `https://amazing-app-name.netlify.app`