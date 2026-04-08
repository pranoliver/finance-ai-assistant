# LogisticRegression _for_ Categorization (Training Model)

## Let’s go **step by step**, how a robot learns from examples 🤖📘

We’ll explain this function:

```python
def train_category_model(save_path: str = MODEL_PATH):
```

---

## 🧠 Big Idea First

👉 This function is like a **school for the robot**

It teaches the robot:

> “If you see this merchant + amount → this is the category”

---

## 🧩 Step 1 — Get Training Data

```python
df = _fetch_training_dataframe()
```

👉 We collect data from database

Example:

| merchant | amount | category  |
| -------- | ------ | --------- |
| Amazon   | 1146   | Transport |
| Amazon   | 326    | Fuel      |
| Costco   | 1169   | Shopping  |

---

## 🧠 Kid Explanation

👉 “We give the robot past examples so it can learn”

---

## 🧩 Step 2 — Check if Data Exists

```python
if df.empty:
    raise RuntimeError(...)
```

👉 If no data → robot cannot learn 😅

---

## 🧩 Step 3 — Split Input & Output

```python
X = df[["merchant", "amount"]]
y = df["category"]
```

👉 Think like:

| Input (X)     | Output (y) |
| ------------- | ---------- |
| Amazon + 1000 | Transport  |

---

## 🧠 Simple Meaning

👉 X = question\
👉 y = answer

---

## 🧩 Step 4 — Preprocessing (Very Important)

```python
preprocessor = ColumnTransformer(...)
```

👉 This prepares data so robot can understand it

---

## 🔤 Part 1 — TF-IDF (for merchant)

```python
TfidfVectorizer()
```

### What is TF-IDF? 🤯

👉 Full form:

```text
Term Frequency - Inverse Document Frequency
```

---

## 🧠 Kid Explanation

👉 Robot cannot understand words like "Amazon"

So we convert words into numbers.

---

### Example:

```text
Amazon → [0.8, 0.1, 0.3]
Apple  → [0.2, 0.9, 0.4]
```

👉 Now robot understands!

---

## 🔢 Part 2 — StandardScaler (for amount)

```python
StandardScaler()
```

### What it does:

👉 Converts numbers into similar scale

---

## 🧠 Kid Explanation

Instead of:

```text
₹100 vs ₹10000
```

We convert to:

```text
0.1 vs 1.5
```

👉 So robot doesn’t get confused by big numbers

---

## 🧠 ColumnTransformer

```python
ColumnTransformer(
    transformers=[
        ("merchant_tfidf", TfidfVectorizer(), "merchant"),
        ("amount_scaler", StandardScaler(), ["amount"]),
    ]
)
```

👉 Means:

* apply TF-IDF to merchant
* apply scaling to amount

---

## 🧩 Step 5 — Create Full Pipeline

```python
pipeline = Pipeline(...)
```

---

## 🧠 What is Pipeline?

👉 A **machine that does everything in order**

---

### Steps inside:

```python
("preprocess", preprocessor),
("classifier", LogisticRegression(max_iter=1000))
```

---

## 🔍 Logistic Regression

👉 This is the **decision brain 🧠**

It decides:

```text
Amazon + 1000 → Shopping
```

---

## ⚙️ max_iter=1000

👉 Means:

> “Try learning up to 1000 times until you understand”

---

## 🧩 Step 6 — Split Data (Train/Test)

```python
train_test_split(...)
```

---

## 🧠 Why split?

👉 We want to test robot after teaching

---

### Example:

| Use           | Purpose     |
| ------------- | ----------- |
| Training data | teach robot |
| Testing data  | check robot |

---

## ⚙️ Parameters

```python
test_size=0.15
```

👉 15% data used for testing

---

```python
random_state=42
```

👉 Fixed random split (same result every time)

---

```python
stratify=y
```

👉 Keep category balance same

---

## 🧩 Step 7 — Train Model

```python
pipeline.fit(X_train, y_train)
```

👉 Robot learns patterns

---

## 🧠 Kid Explanation

👉 “Look at examples again and again and understand pattern”

---

## 🧩 Step 8 — Check Accuracy

```python
accuracy = pipeline.score(...)
```

---

## What is accuracy?

👉 How many correct answers robot gives

---

### Example:

```text
Correct: 8 out of 10 → 80%
```

---

## 🧩 Step 9 — Save Model

```python
joblib.dump(pipeline, save_path)
```

---

## What is joblib?

👉 It saves the robot brain to a file 🧠💾

---

### File created:

```text
data/models/category_pipeline.joblib
```

---

## 🧠 Kid Explanation

👉 “Save the robot so we don’t have to teach again”

---

## 🧩 Step 10 — Return Result

```python
return {"status": "trained", "accuracy": float(accuracy)}
```

---

## Output Example:

```text
{
  "status": "trained",
  "accuracy": 0.85
}
```

---

## 🎯 Final Flow (Very Simple)

```text
Data → Clean → Convert → Train → Test → Save
```

---

## 🧠 Super Simple Summary

👉 This function teaches the robot:

> “When you see this kind of data, predict this category”

---

## 🎮 Real-Life Analogy

Teacher teaches student:

* Amazon → Shopping
* Apple → Travel

Then tests:

👉 “What is Amazon + ₹1000?”

Student answers:

👉 “Shopping!”

---

## 🔥 Why This Is Powerful

Your app can now:

* auto-categorize transactions 🧾
* reduce manual work
* make dashboard smart 📊

---

## 🧠 One-Line Understanding

👉 “Train a robot to guess category from merchant + amount.”

---

## 🧠🧠🧠 We go **one level deeper** 

Explanation for:

1. Why Logistic Regression is used
2. How TF-IDF actually calculates numbers
3. How to improve accuracy

Let’s do all 3 👇

---

## 🧠 1️⃣ Why Logistic Regression is Used

---

## 🎯 Problem We Are Solving

We want:

```text
Amazon + ₹1000 → ?
```

👉 Answer should be one of:

```text
Shopping / Travel / Fuel / Transport
```

👉 This is a **choice problem** (pick one category)

---

## 🤖 What Logistic Regression Does

It is like a **smart judge ⚖️**

It looks at input and says:

```text
Shopping → 60%
Travel → 20%
Fuel → 10%
Transport → 10%
```

👉 Then picks highest:

```text
Shopping ✅
```

---

## 🧠 Kid Analogy

Imagine:

You ask your teacher:

> “What is this item?”

Teacher says:

* “Looks like shopping item (60%)”
* “Maybe travel (20%)”

👉 Teacher picks **Shopping**

---

## ⚙️ Why Not Linear Regression?

Linear Regression gives:

```text
Answer = 732 😅
```

👉 That’s useless for categories

---

## ✅ Why Logistic Regression?

| Feature               | Why good |
| --------------------- | -------- |
| Works with categories | Yes ✅    |
| Gives probabilities   | Yes ✅    |
| Fast                  | Yes ✅    |
| Simple                | Yes ✅    |

---

## 🎯 One-Line

👉 “It chooses the most likely category.”

---

## 🧠 2️⃣ How TF-IDF Works (Super Simple)

---

## 🤯 Problem

Robot sees:

```text
Amazon, Apple, Costco
```

👉 But robot only understands numbers 😅

---

## 🎯 TF-IDF Converts Words → Numbers

---

## 🧩 Step 1 — TF (Term Frequency)

👉 How often a word appears

Example:

```text
Amazon appears many times → important
```

---

## 🧩 Step 2 — IDF (Inverse Document Frequency)

👉 If word appears everywhere → not special

Example:

```text
"store" appears everywhere → not useful
"Amazon" → more unique → useful
```

---

## 🧠 Final Idea

👉 TF-IDF gives:

```text
Important words → bigger numbers
Common words → smaller numbers
```

---

## 🎮 Example

```text
Amazon → [0.8, 0.1, 0.3]
Apple  → [0.2, 0.9, 0.4]
```

👉 Now robot can compare them!

---

## 🧠 Kid Analogy

Imagine:

* “Amazon” is a rare Pokémon 🐉 → special
* “Shop” is everywhere → boring

👉 Special words get more importance

---

## 🎯 One-Line

👉 “TF-IDF tells robot which words are important.”

---

## 🧠 3️⃣ How to Improve Accuracy 🚀

This is VERY important for your project 🔥

---

## 🧩 Problem Now

Your model may be confused:

```text
Amazon → Fuel OR Transport 😵
```

---

## 🚀 Fix 1 — More Data

👉 Best solution

```text
More examples → better learning
```

---

## 🧠 Analogy

More practice → smarter student 📚

---

## 🚀 Fix 2 — Better Features

Instead of just:

```text
merchant + amount
```

Add:

* city 🌆
* payment method 💳
* time ⏰

---

## Example:

```text
Amazon + ₹1000 + Night → Shopping
Uber + ₹300 + Evening → Transport
```

---

## 🚀 Fix 3 — Better Models

Try:

* RandomForest 🌳
* XGBoost 🚀

These are smarter than Logistic Regression

---

## 🚀 Fix 4 — Clean Data

Remove:

```text
missing values
wrong categories
duplicates
```

---

## 🚀 Fix 5 — Balance Data

If you have:

```text
1000 Shopping
10 Fuel
```

👉 Model becomes biased 😬

Fix:

👉 Balance dataset

---

## 🚀 Fix 6 — Tune Parameters

Example:

```python
LogisticRegression(max_iter=2000)
```

👉 Give model more time to learn

---

## 🚀 Fix 7 — Feature Engineering (Advanced)

Example:

```text
amount_bucket:
0–500 → small
500–2000 → medium
```

👉 Makes model smarter

---

## 🎯 Final Summary (All 3 Together)

---

## 🧠 Logistic Regression

👉 “Choose best category”

---

## 🧠 TF-IDF

👉 “Convert words into meaningful numbers”

---

## 🚀 Accuracy Improvement

👉 “Better data + better features + better model”

---

## 🎮 Final Analogy

Imagine training a kid:

| Step                | Meaning            |
| ------------------- | ------------------ |
| TF-IDF              | Learn language     |
| Logistic Regression | Make decisions     |
| More data           | Practice more      |
| Better features     | Learn more context |

---

## 🧠 One-Line Master Summary

👉 “We convert words to numbers, learn patterns, and pick the best category — and we improve by giving better data.”

---
