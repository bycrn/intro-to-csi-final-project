<template>
  <div class="rules">
    <div class="container">
      <div class="card">
        <h2>桃園市垃圾分類規則</h2>
        <p class="subtitle">Taoyuan Waste Sorting Rules</p>
        
        <div class="loading" v-if="loading">
          <div class="spinner"></div>
          <p>載入中... Loading...</p>
        </div>
        
        <div v-else-if="categories">
          <section class="general-rules">
            <h3>基本規則 / General Rules</h3>
            <ul class="rules-list">
              <li v-for="(rule, idx) in generalRules" :key="idx">
                {{ rule }}
              </li>
            </ul>
          </section>
          
          <section class="categories-section">
            <h3>垃圾分類類別 / Waste Categories</h3>
            
            <div 
              v-for="category in categories" 
              :key="category.id" 
              class="category-card"
              :style="{ borderLeftColor: category.color }"
            >
              <div class="category-header">
                <div 
                  class="category-color-badge" 
                  :style="{ backgroundColor: category.color }"
                ></div>
                <div>
                  <h4>{{ category.name }}</h4>
                  <p class="category-name-en">{{ category.name_en }}</p>
                </div>
              </div>
              
              <div class="category-description">
                <p><strong>說明 / Description:</strong></p>
                <p>{{ category.description }}</p>
                <p class="description-en">{{ category.description_en }}</p>
              </div>
              
              <div class="category-examples">
                <p><strong>例子 / Examples:</strong></p>
                <div class="examples-tags">
                  <span 
                    v-for="(example, idx) in category.examples" 
                    :key="idx"
                    class="example-tag"
                    :style="{ backgroundColor: category.color + '30', borderColor: category.color }"
                  >
                    {{ example }}
                  </span>
                </div>
              </div>
            </div>
          </section>
          
          <section class="tips-section">
            <h3>💡 實用提示 / Useful Tips</h3>
            <div class="tips-grid">
              <div class="tip-card">
                <div class="tip-icon">🕐</div>
                <h4>收集時間 / Collection Time</h4>
                <p>請在指定時間將垃圾拿到垃圾車</p>
                <p class="tip-en">Bring waste to collection truck at designated times</p>
              </div>
              
              <div class="tip-card">
                <div class="tip-icon">💧</div>
                <h4>清洗回收物 / Clean Recyclables</h4>
                <p>所有回收物品必須清洗乾淨</p>
                <p class="tip-en">All recyclables must be cleaned</p>
              </div>
              
              <div class="tip-card">
                <div class="tip-icon">🗑️</div>
                <h4>專用垃圾袋 / Designated Bags</h4>
                <p>一般垃圾需使用專用垃圾袋</p>
                <p class="tip-en">Use designated bags for general waste</p>
              </div>
              
              <div class="tip-card">
                <div class="tip-icon">♻️</div>
                <h4>分類正確 / Sort Correctly</h4>
                <p>正確分類有助於環境保護</p>
                <p class="tip-en">Correct sorting helps protect the environment</p>
              </div>
            </div>
          </section>
          
          <section class="contact-section">
            <h3>📞 需要幫助？ / Need Help?</h3>
            <p>桃園市環保局: 1999 (市民專線)</p>
            <p class="contact-en">Taoyuan Environmental Protection Bureau: 1999 (Citizen Hotline)</p>
            <p>網站 / Website: <a href="https://www.tyepb.gov.tw" target="_blank">www.tyepb.gov.tw</a></p>
          </section>
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
  name: 'Rules',
  data() {
    return {
      loading: true,
      categories: null,
      generalRules: [],
      error: null
    }
  },
  async mounted() {
    await this.fetchCategories()
  },
  methods: {
    async fetchCategories() {
      try {
        this.loading = true
        this.error = null
        
        console.log('🔄 Fetching categories from backend...')
        
        // Fixed endpoint - matches your backend structure
        const response = await axios.get('http://localhost:8000/rules')
        
        // Extract data from your taoyuan_rules.json structure
        this.categories = response.data.categories
        this.generalRules = response.data.general_rules || []
        
        console.log('✅ Loaded:', this.categories.length, 'categories')
        
      } catch (err) {
        console.error('❌ Fetch error:', err)
        this.error = '無法載入規則 / Cannot load rules'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>


<!-- Style  -->


<style scoped>
  :root { 
  --dry-sage: #bdbd9b;      
  --ash-brown: #6C584C;      
  --black-forest: #283618;           /* Vert très foncé (texte) */
  --vanilla: rgb(240,234,210); 
  --fern: #588157;
  
  /* Couleurs système */
  --color-shadow: #283618; /* black forest en ombre */
  --faded-copper: #A98467;  
  --burnt-peach: #E07A5F;
}
.rules {
  padding: 2rem 0;
}

.card {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  max-width: 1000px;
  margin: 0 auto;
}

h2 {
  color: #333;
  margin-bottom: 0.5rem;
  font-size: 1.75rem;
}

.subtitle {
  color: #666;
  margin-bottom: 2rem;
  font-size: 1rem;
}

h3 {
  color: #444;
  margin: 2rem 0 1rem 0;
  font-size: 1.5rem;
  border-bottom: 2px solid var(--black-forest);
  padding-bottom: 0.5rem;
}

.loading {
  text-align: center;
  padding: 3rem;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid var(--vanilla);
  border-top: 4px solid var(--ash-brown);
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.general-rules {
  margin-bottom: 2rem;
}

.rules-list {
  list-style: none;
  padding: 0;
}

.rules-list li {
  padding: 1rem;
  margin: 0.5rem 0;
  background: #f9f9f9;
  border-radius: 8px;
  border-left: 4px solid var(--ash-brown);
}

.categories-section {
  margin-bottom: 2rem;
}

.category-card {
  background: #f9f9f9;
  padding: 1.5rem;
  margin: 1rem 0;
  border-radius: 8px;
  border-left: 5px solid;
  transition: transform 0.3s, box-shadow 0.3s;
}

.category-card:hover {
  transform: translateX(5px);
  box-shadow: 0 4px 12px var(--dry-sage);
}

.category-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.category-color-badge {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

.category-header h4 {
  margin: 0;
  font-size: 1.25rem;
  color: #333;
}

.category-name-en {
  color: #666;
  font-size: 0.9rem;
  margin: 0;
}

.category-description {
  margin: 1rem 0;
  padding: 1rem;
  background: white;
  border-radius: 6px;
}

.description-en {
  color: #666;
  font-size: 0.9rem;
  margin-top: 0.5rem;
}

.category-examples {
  margin-top: 1rem;
}

.examples-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.example-tag {
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.875rem;
  border: 1px solid;
}

.tips-section {
  margin: 2rem 0;
}

.tips-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.tip-card {
  background: linear-gradient(135deg, var(--ash-brown) 0%, rgb(90, 100, 80) 100%);
  color: white;
  padding: 1.5rem;
  border-radius: 12px;
  text-align: center;
  transition: transform 0.3s;
}

.tip-card:hover {
  transform: translateY(-5px);
}

.tip-icon {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.tip-card h4 {
  margin: 0.5rem 0;
  font-size: 1rem;
}

.tip-card p {
  margin: 0.5rem 0;
  font-size: 0.875rem;
}

.tip-en {
  opacity: 0.9;
  font-size: 0.8rem;
}

.contact-section {
  background:#e4ece4;
  padding: 1.5rem;
  border-radius: 8px;
  margin-top: 2rem;
}

.contact-section p {
  margin: 0.5rem 0;
}

.contact-en {
  color: #666;
  font-size: 0.9rem;
}

.contact-section a {
  color: var(--ash-brown);
  text-decoration: none;
  font-weight: 500;
}

.contact-section a:hover {
  text-decoration: underline;
}

.error-message {
  background: #ffebee;
  color: var(--burnt-peach);
  padding: 1rem;
  border-radius: 8px;
  margin-top: 1rem;
  border-left: 4px solid var(--burnt-peach);
}

@media (max-width: 768px) {
  .card {
    padding: 1.5rem;
  }
  
  h2 {
    font-size: 1.5rem;
  }
  
  h3 {
    font-size: 1.25rem;
  }
  
  .tips-grid {
    grid-template-columns: 1fr;
  }
}
</style>