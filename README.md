
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


## 🧠 How It Works

1. **Data Preparation:**  
   Uses preprocessed movie data (`movies_recommond_dict.pkl`) and a precomputed **similarity matrix** (`similarity11.pkl`).

2. **Recommendation Logic:**  
   When a user selects a movie, similar movies are found using cosine similarity from the matrix.

3. **API Integration:**  
   The app fetches:
   - 🎞️ Movie posters  
   - 🎬 Trailers  
   - ⭐ Ratings  
   - 🏷️ Genres and overview  
   - ⏳ Runtime and 📅 release date  
   via **TMDb API**.


## 🗂️ Project Structure



### 🧾 Explanation

- **app.py** → Main Streamlit application file  
- **movies_recommond_dict.pkl** → Pickle file storing movie titles, IDs, and metadata  
- **similarity11.pkl** → Pickle file storing cosine similarity matrix  
- **requirements.txt** → Python packages required to run the app  
- **README.md** → Documentation file



## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Movie-Recommender-System.git
cd Movie-Recommender-System
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run app.py
```


## 🔑 API Configuration

This project uses **The Movie Database (TMDb) API** to fetch movie details.
Get your API key from [TMDb](https://www.themoviedb.org/).

Replace the placeholder in your code with your API key:

```python
api_key = "YOUR_TMDB_API_KEY"
```



## 🧩 Requirements

Create a `requirements.txt` file with the following content:

```
streamlit
pandas
numpy
requests
pickle-mixin
```


## 🎨 UI Features

* ✅ Responsive layout using **Streamlit columns**
* 🖼️ Smooth hover animation on posters
* 📖 Expandable movie overview section
* ✨ Clean, minimal, and modern interface



## 💬 Feedback System

At the bottom of the app:

* 👍 Click **“Yes”** to send positive feedback
* 👎 Click **“No”** to mark it for improvement



