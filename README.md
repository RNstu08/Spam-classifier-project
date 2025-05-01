# 📱 SMS Spam Classifier

A machine learning project that detects spam messages using Natural Language Processing (NLP). It includes a web interface built with Streamlit for users to test the model in real time.

---

## Project Overview

This project builds a binary classifier that can distinguish between **spam** and **ham** (not spam) SMS messages using NLP techniques.

### Core Features

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering using TF-IDF
- Model Training with Multinomial Naive Bayes
- Model Evaluation (Confusion Matrix, Accuracy, Precision, Recall)
- Streamlit App for User Interface
- Git version control and clean project structure

---

## Dataset

- Dataset: [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- Format: `spam` and `ham` labeled messages in CSV

---

## How to Run the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/spam_classifier_project.git
cd spam_classifier_project

### Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### Install Dependencies
pip install -r requirements.txt

### Launch Streamlit App
cd webapp
streamlit run app.py

## Tech Stack
Python
Pandas, NumPy, Scikit-learn, NLTK
Streamlit (for web app)
Jupyter Notebook (for EDA & modeling)

## Folder Structure

spam_classifier_project/
│
├── notebooks/              # EDA and Model Building
│   └── 01_EDA_Modeling.ipynb
│
├── webapp/                 # Streamlit App
│   ├── app.py
│   ├── vectorizer.pkl
│   └── model.pkl
│
├── requirements.txt        # Python dependencies
├── .gitignore
├── README.md
└── venv/                   # Virtual Environment (ignored)

## Inputs for Testing

### Spam Message Examples
1. Congratulations! You've won a $1000 Walmart gift card. Go to http://bit.ly/12345 to claim now!
2. FREE entry in 2 a weekly competition to win FA Cup tickets. Text WIN to 87066 to enter.
3. Urgent! Your mobile number has won £2,000 cash! Call 09061701461 now!
4. You have been selected for a cash reward. Reply with your bank details now!

### Ham Message Examples
1. Hey, are we still on for lunch today at 1pm?
2. Don't forget to bring your notes for the meeting tomorrow.
3. Can you please pick up the groceries on your way home?
4. I'm running a bit late, but I’ll be there in 10 minutes.

