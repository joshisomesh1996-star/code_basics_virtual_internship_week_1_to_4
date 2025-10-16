# 🧠 Data Science Internship Tasks — AtliQ Technologies Pvt. Ltd.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange?logo=mlflow)
![SQL](https://img.shields.io/badge/SQL-Analysis-lightgrey?logo=mysql)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

### 👨‍💻 **Intern:** Somesh Joshi  
**Organization:** AtliQ Technologies Pvt. Ltd.  
**Role:** Data Science Intern  
**Duration:** Week 1–4

---

## 🗂️ Repository Overview

This repository contains all project files and deliverables from the **Data Science Internship**, covering:
- Exploratory Data Analysis (EDA)
- SQL Analytics
- Machine Learning Model Development
- Streamlit App Deployment

Each week demonstrates a complete mini-project aligned with real-world business insights.

---

## 🗓️ Week 1 — Exploratory Data Analysis (EDA) & Business Insights

<details>
<summary>🧩 <b>Task 1 — Basic Data Exploration</b></summary>

**File:** `week1_task1.ipynb`  
- Conducted initial data profiling: missing values, data types, and descriptive statistics.  
- Visualized sales patterns and correlations using **Matplotlib** and **Seaborn**.  
- Built the foundation for further business insights.
</details>

<details>
<summary>📊 <b>Task 2 — Nova Mart Promotional Campaign Analysis</b></summary>

**Files:**
- `week1_task2.ipynb`  
- `week1_task2(ppt).pptx`  

**Key Insights:**
- **Grocery & Staples** dominated sales (70.5%) during Sankranti promotions.  
- Metro cities (Bengaluru, Chennai, Hyderabad) were top performers.  
- Tier-2 cities (Madurai, Vizag) showed higher responsiveness to promotions.  
- Identified effective strategies:
  - 🏷️ **Cashback** → boosts volume  
  - 🎁 **BOGOF** → maximizes revenue  
  - 💸 **Flat Discounts (25–33%)** → moderate success:contentReference[oaicite:0]{index=0}

</details>

---

## 🗓️ Week 2 — SQL Analytics for Electric Vehicle Market ⚡

<details>
<summary>🔍 <b>Task — EV Sales Data Analysis using SQL</b></summary>

**File:** `week2_task2.docx`  

**Highlights:**
- Queried **EV maker count**, **top sellers**, and **CAGR growth** from 2022–2024.  
- Computed **state-level penetration rates** for both 2-wheelers and 4-wheelers.  
- Segmented states by EV adoption (Above 7%, 5%, 3%, 1%).  
- Analyzed month-wise sales trends and high-performing markets.:contentReference[oaicite:1]{index=1}

📈 **Result:** Delivered actionable insights for government EV policy and manufacturer strategy.
</details>

---

## 🗓️ Week 3–4 — Machine Learning & Deployment 🚀

### 🥤 Project: **CodeX Beverage Price Predictor**

<details open>
<summary>📘 <b>Overview</b></summary>

Predicts the **optimal beverage price range** based on customer demographics, preferences, and brand awareness using a **machine learning model** deployed via **Streamlit**.

**Files:**
- `week_3_4_task.ipynb`  
- `week_3_4_task(ppt).pptx`  
- `main.py`  
- `prediction_helper.py`  
- `requirements.txt`  
</details>

---

### ⚙️ Phases of Project

#### 🧹 **Phase 1 — Data Cleaning**
- Removed duplicates and unrealistic entries (e.g., invalid ages).  
- Imputed missing data for *Consume Frequency* and *Purchase Channel*.  
- Corrected inconsistent spellings in categorical variables.:contentReference[oaicite:2]{index=2}

#### 🧱 **Phase 2 — Feature Engineering**
- Added business-driven features:
  - **Zone Affluence Score (ZAS)**  
  - **CF_AB Score (Consumption–Awareness Balance)**  
  - **Brand Switching Indicator (BSI)**  
- Removed logical outliers to enhance data quality.:contentReference[oaicite:3]{index=3}

#### 🤖 **Phase 3 — Model Development**
- Data split into train/test sets and encoded with Label + One-Hot encoding.  
- Evaluated multiple models; selected best-performing ML algorithm for prediction.  
- Saved model and encoders as `.joblib` artifacts.:contentReference[oaicite:4]{index=4}

#### ☁️ **Phase 4 — Deployment (MLflow + Streamlit)**
- **MLflow:** Experiment tracking and model versioning.  
- **Streamlit:** Built a responsive, interactive web app for live predictions.  

| File | Description |
|------|--------------|
| `main.py` | Streamlit UI & logic for real-time predictions:contentReference[oaicite:5]{index=5} |
| `prediction_helper.py` | Handles feature computation, encoding & model inference:contentReference[oaicite:6]{index=6} |
| `requirements.txt` | Lists dependencies: `streamlit`, `pandas`, `joblib`:contentReference[oaicite:7]{index=7} |

---

### 🌐 Streamlit App Features

🧍‍♂️ **Demographics Section:**  
Capture age, gender, zone, occupation, and income level.  

🥤 **Consumption Behavior:**  
Weekly frequency, preferred size, brand awareness, purchase channels.  

🎨 **Preferences Section:**  
Flavor, packaging, health concerns, and consumption context.  

📊 **Auto-Derived Metrics:**
- **ZAS Score**
- **CF_AB Score**
- **BSI (Brand Switching Indicator)**  

💡 **Instant Output:**  
Displays predicted **price range** dynamically with intuitive visuals and metrics.

---

## 💻 Run Locally

```bash
# 1️⃣ Clone this repository
git clone https://github.com/<your-username>/atliq-internship-tasks.git
cd atliq-internship-tasks

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Launch the Streamlit app
streamlit run main.py
