# 🎬 Movie Recommender System

An intelligent **Movie Recommendation Web App** built using **Streamlit**, **Python**, and **The Movie Database (TMDb) API**.  
It recommends similar movies based on a selected movie and displays useful details like **poster, rating, runtime, release date, trailer, genres**, and **overview**.



## 🚀 Features

- 🎥 **Movie Recommendation** based on similarity scores  
- 🖼️ **Posters & Trailers** fetched directly from **TMDb API**  
- ⭐ Displays **movie rating, runtime, and release date**  
- 📖 Expandable **overview section** for detailed movie info  
- 💬 **Interactive feedback section**  
- 💡 Modern **Streamlit UI with hover animations**

---

## 🧠 How It Works

1. **Data Preparation:**  
   Preprocessed movie data (`movies_recommond_dict.pkl`) and a **similarity matrix** (`similarity11.pkl`) are used.  
2. **Recommendation Logic:**  
   For a selected movie, similar movies are fetched based on cosine similarity from the precomputed similarity matrix.  
3. **API Integration:**  
   The app fetches:
   - Movie posters  
   - Trailers  
   - Ratings, genres, and overview  
   - Runtime and release date  
   using the **TMDb API**.



## 🗂️ Project Structure

📂 Movie-Recommender-System
│
├── app.py # Main Streamlit app file
├── movies_recommond_dict.pkl # Movie metadata (preprocessed)
├── similarity11.pkl # Similarity matrix
├── requirements.txt # Dependencies list
└── README.md # Project documentation



2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the App

streamlit run app.py

🔑 API Configuration

 api_key = "YOUR_TMDB_API_KEY"

🧩 Requirements

Create a requirements.txt file with the following:
streamlit
pandas
numpy
requests
pickle-mixin

🎨 UI Features

*Responsive layout using Streamlit columns
*Smooth hover animation on posters
*Expandable movie overview section
*Minimal and modern interface

💬 Feedback System

At the bottom of the app:
👍 Click “Yes” to send positive feedback
👎 Click “No” to mark it for improvement
