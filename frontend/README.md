# Frontend - Taoyuan Waste Sorting Helper

Vue.js 3 web application for waste classification.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Run development server:
```bash
npm run dev
```

3. Build for production:
```bash
npm run build
```

4. Preview production build:
```bash
npm run preview
```

## Project Structure

```
frontend/
├── src/
│   ├── views/
│   │   ├── Home.vue      # Main classification page
│   │   └── Rules.vue     # Rules and guidelines page
│   ├── App.vue           # Root component
│   └── main.js           # Application entry
├── public/               # Static assets
├── index.html            # HTML template
├── package.json          # Dependencies
└── vite.config.js        # Vite configuration
```

## Pages

### Home (/)
Main classification interface:
- Upload image from device
- Take photo with camera
- Display classification results
- Show disposal instructions

### Rules (/rules)
Waste sorting guidelines:
- Categories overview
- Sorting rules for Taoyuan
- Practical tips
- Contact information

## API Integration

The frontend communicates with the backend API at `http://localhost:8000`.

### Configuration

Update the API URL in components or use the Vite proxy (configured in `vite.config.js`):

```javascript
// Direct API call
axios.post('http://localhost:8000/classify', formData)

// Or use proxy
axios.post('/api/classify', formData)
```

## Styling

- Uses Noto Sans TC font for proper Chinese character display
- Responsive design for mobile and desktop
- Gradient background with card-based UI
- Category-specific color coding

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers (iOS Safari, Chrome Mobile)
- Camera API requires HTTPS in production

## Development Tips

### Hot Module Replacement
Vite provides instant HMR - changes appear immediately in the browser.

### Vue DevTools
Install Vue DevTools browser extension for debugging.

### Camera Testing
- Use `capture="environment"` for rear camera on mobile
- Test on actual devices for camera functionality
- Camera requires HTTPS in production

## Production Deployment

1. Build the application:
```bash
npm run build
```

2. Deploy the `dist/` directory to your hosting service:
- Netlify
- Vercel
- GitHub Pages
- Firebase Hosting

3. Update API endpoints to production URLs

### Environment Variables

Create `.env` file for environment-specific settings:

```env
VITE_API_URL=https://api.your-domain.com
```

Use in code:
```javascript
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
```

## Components

### Home.vue
Main classification interface with:
- File upload handling
- Camera capture
- Image preview
- API integration
- Results display

### Rules.vue
Information page with:
- Category descriptions
- Sorting guidelines
- Practical tips
- Contact information

## Customization

### Colors
Category colors can be customized by modifying the color codes:
- Recyclables: #4CAF50 (Green)
- Kitchen Waste: #FF9800 (Orange)
- General Waste: #757575 (Gray)

### Language
The interface is bilingual (Chinese/English). To add more languages:
1. Create translation objects
2. Use Vue i18n plugin
3. Add language selector

### Branding
Update the logo and color scheme in `App.vue` to match your branding.
