# 🏋️‍♂️ FitBlitz: ML-Powered Fitness API

An intelligent, backend-first fitness tracking API that doesn't just log your workouts—it acts as your virtual coach. Built with **Django** and **PostgreSQL**, this API utilizes **Scikit-Learn** to analyze a user's historical training data and predict the optimal weight for their next session using linear regression and progressive overload principles.

## ✨ Key Features
* **Smart Workout Suggestions:** On-the-fly Machine Learning predictions calculate target weights based on past performance, sets, and reps.
* **Relational Workout Tracking:** Highly structured database schema linking Users, Workouts, Exercises, and individual Sets.
* **RESTful Architecture:** Fully exposed CRUD endpoints built with Django REST Framework (DRF) ready to be consumed by any frontend (React Native, Flutter, etc.).
* **Optimized Database:** PostgreSQL configuration utilizing compound indexing for lightning-fast ML data extraction and JSONB fields for flexible biometric logging.
* **Auto-Seeding:** Built-in Python script to instantly generate weeks of progressive overload data for testing the ML model locally.

---

## 🛠️ Tech Stack

**Backend & API**
* **Python:** Core application language
* **Django:** Web framework and ORM
* **Django REST Framework (DRF):** API routing and serialization

**Data & Machine Learning**
* **PostgreSQL:** Relational database 
* **Scikit-Learn:** Predictive modeling (Linear Regression)
* **Pandas:** Data extraction and feature engineering

---

## 🧠 How the Machine Learning Works
Instead of relying on static percentages (like traditional 1RM calculators), this API treats workout progression as a time-series forecasting problem. 

When a user requests a suggestion for an exercise (e.g., Bench Press):
1. **Pandas** extracts all historical sets for that specific user and exercise from PostgreSQL.
2. The data is structured into training features, recognizing the timeline of sessions and the rep ranges performed.
3. A **Scikit-Learn Linear Regression** model is trained on the fly against the user's specific progression curve.
4. The model returns the exact weight the user should load on the bar for their target rep range.

---

## 🚀 Local Setup & Installation

### 1. Clone the repository
bash - git clone [https://github.com/yourusername/fitpredict-api.git](https://github.com/yourusername/fitpredict-api.git)
cd fitpredict-api

### 2. Set up the virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

### 3. Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fitness_db',
        'USER': 'postgres',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

### 4. Run Migrations & Create Superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

### 5. Seed the Database (Test the ML!)
python seed.py

### 6. Start the Server
python manage.py runserver

##📡 API Endpoints
Once the server is running at http://127.0.0.1:8000/, you can access the Browsable API:

## Method,Endpoint,Description
### GET/POST,/api/exercises/,List or create available exercises
### GET/POST,/api/workouts/,Log a new gym session
### GET/POST,/api/sets/,"Log individual sets, reps, and weight"
### GET,/api/suggest/<id>/?reps=10,[ML Endpoint] Get weight prediction for the next set

## 🛣️ Future Roadmap
### Implement JWT Authentication for secure frontend communication.
### Upgrade the Scikit-Learn model to a Non-linear/Polynomial Regression model to account for natural strength plateaus.
### Factor in JSONB biometrics data (sleep, soreness) into the ML model's weight predictions.
