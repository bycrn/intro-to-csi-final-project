# Changelog

All notable changes to the Taoyuan Waste Sorting Helper project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-08

### Added
- Initial release of Taoyuan Waste Sorting Helper
- FastAPI backend with YOLOv8 object detection
- Vue.js 3 frontend with responsive design
- Image upload and camera capture functionality
- AI-powered waste classification
- Three waste categories: Recyclables, Kitchen Waste, General Waste
- Bilingual interface (Traditional Chinese and English)
- Comprehensive rules page for Taoyuan waste sorting
- API documentation with Swagger UI
- Docker support with docker-compose
- Deployment guides for various platforms
- Contributing guidelines
- MIT License

### Backend Features
- `/health` - Health check endpoint
- `/categories` - Get waste categories and rules
- `/classify` - Upload image for classification
- YOLOv8n integration for object detection
- COCO dataset class to waste category mapping
- CORS middleware for cross-origin requests
- Detailed error handling

### Frontend Features
- Home page with image upload/camera capture
- Real-time classification results
- Color-coded waste categories
- Disposal instructions in Chinese and English
- Rules page with comprehensive sorting guidelines
- Practical tips section
- Contact information for Taoyuan EPB
- Mobile-responsive design
- Gradient UI with card-based layout

### Documentation
- Comprehensive README with setup instructions
- Quick start guide
- Deployment guide covering multiple platforms
- Contributing guidelines
- API documentation
- Backend-specific README
- Frontend-specific README
- Environment variable examples

### Infrastructure
- Python requirements.txt with all dependencies
- Node.js package.json with Vue 3 and Vite
- Docker configurations for backend and frontend
- docker-compose.yml for easy deployment
- .gitignore for Python and Node.js
- Nginx configuration examples

### Testing
- API test script (test_api.py)
- Health check endpoint
- Example test cases structure

## [Unreleased]

### Planned Features
- Custom YOLOv8 model trained on Taiwan-specific waste items
- Firebase authentication and user accounts
- Classification history tracking
- Additional language support (Japanese, Korean, Vietnamese)
- QR code scanning for packaged items
- Offline mode with cached model
- Progressive Web App (PWA) support
- Native mobile apps (iOS and Android)
- Admin dashboard for statistics
- Community feedback and reporting
- Gamification features (achievements, points)
- Integration with Taoyuan city waste collection schedule

### Known Issues
- YOLOv8 model download requires internet connection on first run
- Camera capture requires HTTPS in production
- Some COCO classes may not map perfectly to Taiwan waste categories
- Model inference can be slow on CPU-only systems

---

## Version History

### Version 1.0.0 (Current)
First stable release with core functionality:
- Working backend API with YOLOv8
- Functional frontend with Vue 3
- Complete documentation
- Docker deployment support
- Bilingual interface

---

For detailed commit history, see the [GitHub repository](https://github.com/bycrn/intro-to-csi-final-project).
