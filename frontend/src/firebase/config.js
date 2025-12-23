// src/firebase/config.js
import { initializeApp } from 'firebase/app'
import { getFirestore } from 'firebase/firestore'
import { getStorage } from 'firebase/storage'
import { getAnalytics } from "firebase/analytics"

const firebaseConfig = {
  apiKey: "AIzaSyBOzK1xM-ydja74YViWesSBuqQlB-1zRFc",
  authDomain: "wasting-sort-app.firebaseapp.com",
  projectId: "wasting-sort-app",
  storageBucket: "wasting-sort-app.firebasestorage.app",
  messagingSenderId: "842976190260",
  appId: "1:842976190260:web:cec229ab141b2150eecf61",
  measurementId: "G-2B9QN725ZZ"
}

const firebaseApp = initializeApp(firebaseConfig)
const analytics = getAnalytics(firebaseApp)

export const db = getFirestore(firebaseApp)
export const storage = getStorage(firebaseApp)
export { analytics }
