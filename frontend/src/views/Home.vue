<template>
  <div class="home">
    <div class="container">
      <div class="card main-card">
        <h2>上傳或拍照識別垃圾類型</h2>
        <p class="subtitle">Upload or Take a Photo to Identify Waste Type</p>
        
        <div class="upload-section">
          <div class="upload-buttons">
            <label for="file-upload" class="btn btn-primary">
              📁 選擇圖片 / Choose Image
            </label>
            <input 
              id="file-upload" 
              type="file" 
              accept="image/*" 
              @change="handleFileSelect"
              style="display: none"
            >
            
            <label for="camera-upload" class="btn btn-secondary">
              📷 拍照 / Take Photo
            </label>
            <input 
              id="camera-upload" 
              type="file" 
              accept="image/*" 
              capture="environment"
              @change="handleFileSelect"
              style="display: none"
            >
          </div>
          
          <div v-if="preview" class="preview-section">
            <img :src="preview" alt="Preview" class="preview-image">
            <button @click="clearImage" class="btn btn-small">清除 / Clear</button>
          </div>
          
          <button 
            v-if="selectedFile && !loading" 
            @click="classifyImage" 
            class="btn btn-success btn-large"
          >
            🔍 開始分類 / Classify
          </button>
          
          <div v-if="loading" class="loading">
            <div class="spinner"></div>
            <p>正在分析中... Analyzing...</p>
          </div>
        </div>
        
        <div v-if="result && !loading" class="result-section">
          <div 
            class="result-card" 
            :style="{ borderColor: result.category.color, backgroundColor: result.category.color + '20' }"
          >
            <h3>分類結果 / Classification Result</h3>
            
            <div class="category-badge" :style="{ backgroundColor: result.category.color }">
              {{ result.category.name }}
            </div>
            
            <div class="category-name-en">
              {{ result.category.name_en }}
            </div>
            
            <div v-if="result.primary_object" class="detected-object">
              <strong>檢測到物品 / Detected Object:</strong> {{ result.primary_object }}
              <span class="confidence">({{ (result.confidence * 100).toFixed(1) }}%)</span>
            </div>
            
            <div class="instructions">
              <p><strong>處理方式 / Instructions:</strong></p>
              <p class="instruction-text">{{ result.category.instructions }}</p>
              <p class="instruction-text-en">{{ result.category.instructions_en }}</p>
            </div>
            
            <div v-if="result.detected_objects && result.detected_objects.length > 1" class="all-detections">
              <p><strong>所有檢測物品 / All Detections:</strong></p>
              <ul>
                <li v-for="(obj, idx) in result.detected_objects" :key="idx">
                  {{ obj.object }} - {{ (obj.confidence * 100).toFixed(1) }}% ({{ obj.category }})
                </li>
              </ul>
            </div>
          </div>
        </div>
        
        <div v-if="error" class="error-message">
          ❌ {{ error }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      selectedFile: null,
      preview: null,
      loading: false,
      result: null,
      error: null
    }
  },
  methods: {
    handleFileSelect(event) {
      const file = event.target.files[0]
      if (file) {
        this.selectedFile = file
        this.result = null
        this.error = null
        
        // Create preview
        const reader = new FileReader()
        reader.onload = (e) => {
          this.preview = e.target.result
        }
        reader.readAsDataURL(file)
      }
    },
    
    clearImage() {
      this.selectedFile = null
      this.preview = null
      this.result = null
      this.error = null
    },
    
    async classifyImage() {
      if (!this.selectedFile) return

      this.loading = true
      this.error = null
      this.result = null

      try {
        const formData = new FormData()
        formData.append('file', this.selectedFile)

        const response = await axios.post(
          'http://localhost:8000/api/classify',
          formData,
          { headers: { 'Content-Type': 'multipart/form-data' } }
        )

        if (response.data.success) {
          this.result = response.data
        } else {
          this.error = response.data.message || '分類失敗 / Classification failed'
        }
      } catch (err) {
        this.error = '無法連接到服務器 / Cannot connect to server: ' + (err.message || '')
      } finally {
        this.loading = false
      }
  }}
}


</script>

<style scoped>
.home {
  padding: 2rem 0;
}

.card {
  background: var(--vanilla);
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 20px var(--color-shadow);
}

.main-card {
  max-width: 800px;
  margin: 0 auto;
}

h2 {
  color: var(--black-forest);
  margin-bottom: 0.5rem;
  font-size: 1.75rem;
}

.subtitle {
  color: var(--f);
  margin-bottom: 2rem;
  font-size: 1rem;
}

.upload-section {
  margin: 2rem 0;
}

.upload-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
  text-decoration: none;
  display: inline-block;
}

.btn-primary {
  background: var(--faded-copper);
  color: var(--vanilla);
}

.btn-primary:hover {
  background: var(--faded-copper);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px var(--color-shadow);
}

.btn-secondary {
  background: var(--ash-brown);
  color: var(--vanilla);
}

.btn-secondary:hover {
  background: var(--ash-brown);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px var(--color-shadow);
}

.btn-success {
  background: #588157;
  color: var(--vanilla);
}

.btn-success:hover {
  background: #588157;
}

.btn-large {
  padding: 1rem 2rem;
  font-size: 1.125rem;
  width: 100%;
  max-width: 300px;
  margin: 1rem auto;
  display: block;
}

.btn-small {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  background: var(--burnt-peach);
  color: var(--vanilla);
  margin-top: 1rem;
}

.btn-small:hover {
  background: var(--burnt-peach);
}

.preview-section {
  margin: 2rem 0;
  text-align: center;
}

.preview-image {
  max-width: 100%;
  max-height: 400px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  display: block;   
  margin: 0 auto; 
}

.loading {
  text-align: center;
  padding: 2rem;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid var(--ash-brown);
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.result-section {
  margin-top: 2rem;
}

.result-card {
  padding: 2rem;
  border-radius: 12px;
  border: 3px solid;
  animation: fadeIn 0.5s;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.result-card h3 {
  margin-bottom: 1rem;
  color: #333;
}

.category-badge {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  border-radius: 25px;
  color: var(--vanilla);
  font-size: 1.25rem;
  font-weight: 600;
  margin: 1rem 0;
}

.category-name-en {
  font-size: 1.125rem;
  color: #666;
  margin-bottom: 1rem;
}

.detected-object {
  background: #f5f5f5;
  padding: 1rem;
  border-radius: 8px;
  margin: 1rem 0;
}

.confidence {
  color: var(--fern);
  font-weight: 600;
  margin-left: 0.5rem;
}

.instructions {
  margin: 1.5rem 0;
  padding: 1rem;
  background: var(--dry-sage);
  border-radius: 8px;
}

.instruction-text {
  margin: 0.5rem 0;
  font-size: 1rem;
  color: #333;
}

.instruction-text-en {
  margin: 0.5rem 0;
  font-size: 0.9rem;
  color: #666;
}

.all-detections {
  margin-top: 1rem;
  padding: 1rem;
  background: #f0f0f0;
  border-radius: 8px;
}

.all-detections ul {
  list-style: none;
  padding: 0;
  margin-top: 0.5rem;
}

.all-detections li {
  padding: 0.5rem;
  margin: 0.25rem 0;
  background: white;
  border-radius: 4px;
}

.error-message {
  background: #ffe6e6;
  color: #6E0D25;
  padding: 1rem;
  border-radius: 8px;
  margin-top: 1rem;
  border-left: 4px solid #6E0D25;
}

@media (max-width: 768px) {
  .card {
    padding: 1.5rem;
  }
  
  h2 {
    font-size: 1.5rem;
  }
  
  .upload-buttons {
    flex-direction: column;
  }
  
  .btn {
    width: 100%;
  }
}
</style>