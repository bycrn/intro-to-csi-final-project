#!/bin/bash

# Taoyuan Waste Classifier - Deployment Script
# Usage: ./deploy.sh [local|production|fly]

set -e

DEPLOY_TYPE=${1:-local}
PROJECT_NAME="taoyuan-waste-classifier"

echo "🚀 Deploying Taoyuan Waste Classifier - $DEPLOY_TYPE mode"

case $DEPLOY_TYPE in
  "local")
    echo "📦 Building and starting local development environment..."
    docker-compose down
    docker-compose build --no-cache
    docker-compose up -d
    echo "✅ Application is running at:"
    echo "   Frontend: http://localhost"
    echo "   Backend API: http://localhost:8000"
    echo "   API Health: http://localhost:8000"
    ;;
    
  "production")
    echo "🏭 Building production containers..."
    docker-compose -f docker-compose.yml down
    docker-compose -f docker-compose.yml build --no-cache
    docker-compose -f docker-compose.yml up -d
    echo "✅ Production deployment complete!"
    echo "   Check status: docker-compose ps"
    echo "   View logs: docker-compose logs -f"
    ;;
    
  "fly")
    echo "☁️  Deploying to Fly.io..."
    
    # Check if flyctl is installed
    if ! command -v flyctl &> /dev/null; then
      echo "❌ flyctl is not installed. Install it from: https://fly.io/docs/hands-on/install-flyctl/"
      exit 1
    fi
    
    # Check if logged in
    if ! flyctl auth whoami &> /dev/null; then
      echo "🔑 Please log in to Fly.io first:"
      flyctl auth login
    fi
    
    # Launch or deploy
    if flyctl status -a $PROJECT_NAME &> /dev/null; then
      echo "📤 Deploying updates to existing app..."
      flyctl deploy
    else
      echo "🆕 Creating new app and deploying..."
      flyctl launch --no-deploy --copy-config --name $PROJECT_NAME
      flyctl deploy
    fi
    
    echo "✅ Deployment to Fly.io complete!"
    echo "   App URL: https://$PROJECT_NAME.fly.dev"
    echo "   Status: flyctl status -a $PROJECT_NAME"
    echo "   Logs: flyctl logs -a $PROJECT_NAME"
    ;;
    
  *)
    echo "❌ Invalid deployment type. Use: local, production, or fly"
    echo "Usage: ./deploy.sh [local|production|fly]"
    exit 1
    ;;
esac

echo "🎉 Deployment complete!"