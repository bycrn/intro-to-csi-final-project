#!/bin/bash

# Development Environment Setup Script
# Sets up the Taoyuan Waste Classifier for local development

set -e

echo "🔧 Setting up Taoyuan Waste Classifier development environment..."

# Check if Docker is running
if ! docker info >/dev/null 2>&1; then
  echo "❌ Docker is not running. Please start Docker Desktop and try again."
  exit 1
fi

# Check if Node.js is installed (for frontend development)
if ! command -v node &> /dev/null; then
  echo "⚠️  Node.js not found. Installing via homebrew..."
  if command -v brew &> /dev/null; then
    brew install node
  else
    echo "❌ Please install Node.js manually from https://nodejs.org/"
    exit 1
  fi
fi

# Check if Python is available (for backend development)
if ! command -v python3 &> /dev/null; then
  echo "❌ Python 3 is required but not found. Please install Python 3.9+."
  exit 1
fi

echo "📦 Installing frontend dependencies..."
cd frontend
npm install
cd ..

echo "📦 Installing backend dependencies..."
cd backend
if [[ ! -d "venv" ]]; then
  echo "Creating Python virtual environment..."
  python3 -m venv venv
fi

source venv/bin/activate
pip install -r requirements.txt
cd ..

echo "🏗️  Building Docker images..."
docker-compose build

echo "🚀 Starting development environment..."
docker-compose up -d

echo "⏳ Waiting for services to be ready..."
sleep 10

# Health check
echo "🔍 Checking service health..."
if curl -f http://localhost:8000 >/dev/null 2>&1; then
  echo "✅ Backend is healthy"
else
  echo "⚠️  Backend might still be starting up"
fi

if curl -f http://localhost >/dev/null 2>&1; then
  echo "✅ Frontend is healthy"
else
  echo "⚠️  Frontend might still be starting up"
fi

echo "🎉 Development environment setup complete!"
echo ""
echo "📱 Access your application:"
echo "   Frontend: http://localhost"
echo "   Backend API: http://localhost:8000"
echo "   API Documentation: http://localhost:8000/docs"
echo ""
echo "📋 Useful commands:"
echo "   View logs: docker-compose logs -f"
echo "   Stop services: docker-compose down"
echo "   Rebuild: docker-compose build --no-cache"
echo "   Shell into backend: docker-compose exec backend bash"