# Insurance Charges Prediction

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.5-orange)](https://scikit-learn.org/)

---

## 🚀 Project Overview

**Insurance Charges Prediction** is a **Machine Learning project** designed to predict individual medical insurance charges based on personal and lifestyle factors like **age, BMI, gender, smoking habits, number of children, and region**.  

This project demonstrates **data preprocessing, feature engineering, exploratory data analysis (EDA), statistical testing, and building a Linear Regression model**.

---

## 📊 Dataset

The dataset contains the following features:

| Feature    | Description                                               |
|------------|-----------------------------------------------------------|
| age        | Age of the insured                                        |
| sex        | Gender (male/female)                                      |
| bmi        | Body Mass Index                                           |
| children   | Number of children covered by insurance                  |
| smoker     | Smoker status (yes/no)                                    |
| region     | Residential region (northeast, northwest, southeast, southwest) |
| charges    | Individual medical costs billed by insurance             |

---

## 🔍 Exploratory Data Analysis (EDA)

- Visualized distributions of numerical features using **histograms and KDE plots**
- Countplots for categorical features: **sex, smoker, children**
- Boxplots to detect **outliers**
- Correlation heatmap to examine **relationships between features**

**Example Correlation Heatmap:**

![Heatmap](screenshots/correlation_heatmap.png)

---

## 🧹 Data Cleaning & Preprocessing

- Removed duplicate records
- Encoded categorical variables:
  - `sex` → `is_female` (0/1)
  - `smoker` → `is_smoker` (0/1)
  - `region` → one-hot encoding
- Created **BMI categories**:
  - Underweight, Normal, Overweight, Obese
- Standardized numerical features using **StandardScaler**

---

## ⚙️ Feature Engineering & Selection

- Selected important features using:
  - **Pearson correlation** for numerical features
  - **Chi-square test** for categorical features
- Final features used for modeling:
```
age, is_female, bmi, children, is_smoker, region_southwest, bmi_category_Obese
```


---

## 📈 Model Building

- Split dataset into **train (80%)** and **test (20%)** sets
- Built a **Linear Regression model** using `scikit-learn`
- Evaluated performance using:
  - **R² Score**
  - **Adjusted R² Score**

## 🖥 Interactive Streamlit App

You can use the **Streamlit app** to get personalized insurance predictions:

**Features:**
- Input age, gender, BMI, number of children, smoker status, region
- Automatically calculates **BMI category**
- Displays **predicted insurance cost** in USD
- Shows **warnings for risk factors** like smoking and obesity
- Visual progress bar for reference

**Example usage:**

```bash
streamlit run app.py


python
```
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
print("R² Score:", r2)
```

🛠 Technologies Used

Python 3.x

NumPy

Pandas

Matplotlib & Seaborn

Scikit-learn

SciPy

Joblib

Sreamlit

💾 Repository Structure
```
insurance-charges-prediction/
│
├── insurance.csv                       # Dataset
├── app.py                              # Streamlit app for deployment (optional)
├── LinearRegression.pkl                # Trained Linear Regression model
├── scaler.pkl                          # StandardScaler for numerical features
├── columns.pkl                         # Feature columns
├── screenshots/                        # Folder for plots/screenshots
│   └── correlation_heatmap.png
├── Insurance_Charges_Prediction.ipynb  # Jupyter Notebook with full workflow
└── README.md
```
### 📌 Usage

### 1. Clone the repository:
```bash
git clone https://github.com/<your-username>/insurance-charges-prediction.git
cd insurance-charges-prediction
```
### 2. Install dependencies:
```bash
pip install -r requirements.txt
```
### 3. Load the trained model and make predictions:
```bash
import joblib
import pandas as pd

# Load model, scaler, and columns
model = joblib.load('LinearRegression.pkl')
scaler = joblib.load('scaler.pkl')
columns = joblib.load('columns.pkl')

# Example input
data = pd.DataFrame([[45,1,28.5,2,0,1,0]], columns=columns)
data[['age','bmi','children']] = scaler.transform(data[['age','bmi','children']])

# Predict insurance charges
prediction = model.predict(data)
print("Predicted Insurance Charges:", prediction)
```

### 📊 Screenshots

 <img width="619" height="734" alt="image" src="https://github.com/user-attachments/assets/cf5f09af-cd4d-4b73-a39f-ca0273e32f45" />

 <img width="624" height="882" alt="image" src="https://github.com/user-attachments/assets/65d871df-fda0-4aad-be51-f385bad31ed0" />

