// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAxELZML5wAmj1qNM81K3EqtVzvBM2kM10",
  authDomain: "yakuohdoh-2021.firebaseapp.com",
  projectId: "yakuohdoh-2021",
  storageBucket: "yakuohdoh-2021.firebasestorage.app",
  messagingSenderId: "469049553416",
  appId: "1:469049553416:web:005005f7fde7717503d7bd",
  measurementId: "G-CC41GEHQCX"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app);