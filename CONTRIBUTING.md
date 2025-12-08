# Contributing to Taoyuan Waste Sorting Helper

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Environment details (OS, browser, versions)

### Suggesting Features

Feature requests are welcome! Please include:
- Clear description of the feature
- Use cases and benefits
- Potential implementation approach
- Mockups or examples (if applicable)

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test your changes**
5. **Commit with clear messages**
6. **Push to your fork**
7. **Create a Pull Request**

## Development Setup

### Prerequisites
- Python 3.9+
- Node.js 16+
- Git

### Setup Instructions

1. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/intro-to-csi-final-project.git
cd intro-to-csi-final-project
```

2. Set up backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up frontend:
```bash
cd frontend
npm install
```

## Code Style Guidelines

### Python (Backend)

- Follow PEP 8 style guide
- Use type hints where appropriate
- Add docstrings for functions and classes
- Keep functions focused and small
- Use meaningful variable names

Example:
```python
def classify_waste(image: Image.Image) -> Dict[str, Any]:
    """
    Classify waste item from image.
    
    Args:
        image: PIL Image object
        
    Returns:
        Dictionary containing classification results
    """
    # Implementation
    pass
```

### JavaScript/Vue (Frontend)

- Use ES6+ features
- Follow Vue.js style guide
- Use meaningful component names
- Keep components focused
- Add comments for complex logic

Example:
```vue
<script>
export default {
  name: 'WasteClassifier',
  methods: {
    /**
     * Handle file selection
     * @param {Event} event - File input change event
     */
    handleFileSelect(event) {
      // Implementation
    }
  }
}
</script>
```

## Project Structure

```
intro-to-csi-final-project/
├── backend/                 # Python FastAPI backend
│   ├── app/
│   │   ├── main.py         # FastAPI application
│   │   └── detector.py     # YOLOv8 detection logic
│   └── requirements.txt
├── frontend/               # Vue.js frontend
│   ├── src/
│   │   ├── views/         # Page components
│   │   ├── App.vue        # Root component
│   │   └── main.js        # Entry point
│   └── package.json
└── docs/                  # Documentation
```

## Adding New Features

### Adding a New Waste Category

1. **Backend** - Update `backend/app/detector.py`:
```python
self.waste_category_map = {
    # Add new mappings
    "new_item": "new_category",
}
```

2. **Backend** - Update category info in `backend/app/main.py`:
```python
{
    "id": "new_category",
    "name": "新類別",
    "name_en": "New Category",
    "color": "#COLOR_CODE",
    # ...
}
```

3. **Frontend** - Colors will automatically update from API

### Adding a New Language

1. Install Vue I18n:
```bash
npm install vue-i18n
```

2. Create translation files in `frontend/src/locales/`

3. Update components to use i18n

### Adding Firebase Integration

1. Install Firebase SDK:
```bash
# Backend
pip install firebase-admin

# Frontend
npm install firebase
```

2. Update configuration files

3. Add authentication components

## Testing

### Backend Testing

Create tests in `backend/tests/`:
```python
import pytest
from app.detector import WasteDetector

def test_detector_initialization():
    detector = WasteDetector()
    assert detector.is_loaded()

def test_waste_classification():
    # Test classification logic
    pass
```

Run tests:
```bash
pytest
```

### Frontend Testing

Create tests in `frontend/src/tests/`:
```javascript
import { mount } from '@vue/test-utils'
import Home from '@/views/Home.vue'

describe('Home.vue', () => {
  it('renders upload buttons', () => {
    const wrapper = mount(Home)
    expect(wrapper.find('.upload-buttons').exists()).toBe(true)
  })
})
```

Run tests:
```bash
npm run test
```

## Documentation

When adding features:
- Update relevant README files
- Add JSDoc/docstrings
- Update API documentation
- Add examples if needed

## Commit Messages

Use clear, descriptive commit messages:

```
feat: Add Korean language support
fix: Resolve camera capture issue on iOS
docs: Update deployment guide
style: Format code with prettier
refactor: Simplify classification logic
test: Add unit tests for detector
```

Format: `<type>: <description>`

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

## Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new features
3. **Ensure tests pass**
4. **Update CHANGELOG** if significant
5. **Request review** from maintainers

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] Tests pass
- [ ] No console errors
- [ ] Works on mobile and desktop

## Code Review

All submissions require review. We aim to:
- Review within 48 hours
- Provide constructive feedback
- Approve and merge quality contributions

## Questions?

Feel free to:
- Open an issue for discussion
- Contact maintainers
- Join community discussions

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project website (if applicable)

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information

## Getting Help

If you need help:
1. Check existing documentation
2. Search existing issues
3. Ask in discussions
4. Create a new issue

---

Thank you for contributing to Taoyuan Waste Sorting Helper! ♻️

Your contributions help make waste sorting easier for everyone in Taoyuan.
