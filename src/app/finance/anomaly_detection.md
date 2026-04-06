# Anomaly Detection using _IsolationForest_

## 🧠 Imagine This Story

You have a box of candies 🍬.

Most candies cost around:

👉 ₹10, ₹12, ₹15

But suddenly you see:

👉 ₹500 😳

That looks **very strange**, right?

So you say:

> “Hmm… this candy is *different* from all others!”

That’s exactly what this code is doing — finding **strange values**.

---

# 🧩 Now Let’s Understand the Code

### 1️⃣ Importing the Tool

```python
from sklearn.ensemble import IsolationForest
```

👉 We are bringing a **smart robot** 🤖 called **Isolation Forest**

This robot is very good at:

> “Finding things that look different from the rest”

---

### 2️⃣ Function Starts

```python
def detect_anomalies(df):
```

👉 We give the robot a **table (df)** of data

Example:

| amount |
| ------ |
| 10     |
| 12     |
| 15     |
| 500    |

---

### 3️⃣ Create the Robot

```python
model = IsolationForest(contamination=0.01)
```

👉 We tell the robot:

> “About 1% of the data is weird”

`contamination=0.01` means:

👉 “Only a few things are strange”

---

### 4️⃣ Robot Learns + Finds Weird Things

```python
df["anomaly"] = model.fit_predict(df[["amount"]])
```

This line does **two things at once**:

---

## 🧠 Step A: Learn

`fit`

👉 Robot looks at all numbers:

```
10, 12, 15, 500
```

It understands:

👉 “Most values are small”

---

## 🔍 Step B: Predict

`predict`

👉 Robot labels each value:

| amount | anomaly |
| ------ | ------- |
| 10     | 1       |
| 12     | 1       |
| 15     | 1       |
| 500    | -1 😱   |

---

### What do these numbers mean?

| Value | Meaning               |
| ----- | --------------------- |
| `1`   | Normal 👍             |
| `-1`  | Weird / suspicious 🚨 |

---

### 5️⃣ Return Result

```python
return df
```

👉 We return the table with a **new column**

---

# 🎯 Final Output

| amount | anomaly |
| ------ | ------- |
| 10     | 1       |
| 12     | 1       |
| 15     | 1       |
| 500    | -1 🚨   |

---

# 🧠 Simple Summary

👉 The code is doing this:

> “Look at all the numbers and find the ones that look different from others”

---

# 🎮 Real Life Example

Think of:

* A classroom where everyone scores 80–90 marks
* One student scores **5 marks**

Teacher says:

> “This is unusual”

That student = **anomaly**

---

# 🧠 In Your Project

This helps to detect:

* Fraud transactions 💳
* Unusual spending 💸
* Suspicious activity 🚨

---

# 🌳 Imagine a Forest Game

You are in a forest full of trees.

Each tree is a **question game** that helps you find something.

You have numbers:

```text
10, 12, 15, 14, 13, 500
```

---

# 🎯 Goal

Find the **weird number**.

👉 That is: `500`

---

# 🌳 How One Tree Works

A tree keeps asking random questions like:

👉 “Is number less than 20?”
👉 “Is number less than 13?”
👉 “Is number less than 14?”

---

## Example Tree Path

Let’s follow number **500**

### Step 1

👉 Is 500 < 20?

❌ No → go right

### Step 2

👉 Is 500 < 100?

❌ No → go right

### Step 3

👉 Is 500 < 400?

❌ No → go right

👉 DONE (very fast!)

---

## Now Try Normal Number (10)

### Step 1

👉 Is 10 < 20?

✅ Yes → go left

### Step 2

👉 Is 10 < 13?

✅ Yes → go left

### Step 3

👉 Is 10 < 11?

✅ Yes → go left

### Step 4

👉 Is 10 < 10.5?

✅ Yes → go left

👉 Takes many steps!

---

# 💡 Key Idea

| Type         | Steps to isolate |
| ------------ | ---------------- |
| Normal value | many steps 😴    |
| Weird value  | very few steps ⚡ |

---

# 🌳 Why It’s Called “Isolation Forest”

Because:

👉 It tries to **separate (isolate)** each number
👉 Using many random trees 🌳🌳🌳

---

# 🌲 Many Trees Together

Instead of one tree:

👉 We create **100+ trees**

Each tree asks **different random questions**

---

## For number 500:

* Tree 1 → isolated in 2 steps
* Tree 2 → isolated in 3 steps
* Tree 3 → isolated in 2 steps

👉 Average = very small → 🚨 anomaly

---

## For number 12:

* Tree 1 → 6 steps
* Tree 2 → 5 steps
* Tree 3 → 7 steps

👉 Average = large → 👍 normal

---

# 🎮 Game Analogy

Imagine:

* Normal kids are in a big group 👨‍👩‍👧‍👦
* One kid is standing alone far away 👤

Teacher finds that kid **very quickly**

👉 That kid = anomaly

---

# 📊 Final Logic

Isolation Forest does:

```text
1. Build many random trees 🌳
2. Try to isolate each data point
3. Count how fast it gets isolated
4. Faster = anomaly 🚨
5. Slower = normal 👍
```

---

# 🧠 Why This Is Smart

Because:

👉 It does NOT need labels
👉 It works automatically
👉 It handles large data

---

# 🔥 In Your Project

This helps find:

* Fraud transactions 💳
* Sudden high spending 💸
* Unusual behavior 🚨

---

# 🎯 One Line Summary

👉 “Weird values are easy to separate, so they get caught quickly.”

---

Let’s **visualize Isolation Forest using your transaction data** in a very simple and intuitive way 📊🌳

---

# 🎯 Step 1 — Your Transaction Data

Imagine your dataset looks like this:

```text
10, 12, 14, 15, 13, 11, 500
```

Most values are small… except:

👉 **500** (very different)

---

# 📊 Step 2 — Plot It on a Number Line

Think of it like this:

```
|----|----|----|----|----|-------------------------|
10   11   12   13   14   15                      500
```

👉 All values are grouped together
👉 One value is far away

---

## Visual Representation

![Image](https://study.com/cimages/multimages/16/scatter1line5671805252407315501.png)

![Image](https://la.mathworks.com/discovery/anomaly-detection/_jcr_content/thumbnail.adapt.1200.medium.png/1736762035619.png)

![Image](https://community.sap.com/legacyfs/online/storage/blog_attachments/2020/12/iris_outliers.png)

---

# 🌳 Step 3 — How Trees Split the Data

Each tree draws random lines like:

```
Split 1: amount < 20
Split 2: amount < 13
Split 3: amount < 14
```

---

## What Happens?

### For normal values (10–15)

```
Tree splits:

Step 1 → group
Step 2 → smaller group
Step 3 → smaller group
Step 4 → isolate
```

👉 Takes **many steps**

---

### For 500

```
Step 1 → amount < 20 ❌
```

👉 Immediately separated!

👉 Only **1–2 steps needed**

---

# ⚡ Key Insight (Super Important)

| Value | Distance from others | Steps needed | Result     |
| ----- | -------------------- | ------------ | ---------- |
| 10–15 | Close together       | Many steps   | Normal 👍  |
| 500   | Far away             | Few steps    | Anomaly 🚨 |

---

# 🌲 Step 4 — Multiple Trees

Isolation Forest doesn’t use just one tree.

It uses:

👉 **Many random trees**

Each tree:

* splits data differently
* isolates points in different ways

---

## Average Behavior

| Value | Tree 1  | Tree 2  | Tree 3  | Avg  |
| ----- | ------- | ------- | ------- | ---- |
| 12    | 5 steps | 6 steps | 5 steps | ~5.3 |
| 500   | 2 steps | 1 step  | 2 steps | ~1.6 |

👉 Smaller average = anomaly

---

# 🎮 Visual Intuition

Imagine a playground:

👨‍👩‍👧‍👦 Kids playing together → hard to separate one
👤 One kid standing far away → easy to spot

👉 That lonely kid = anomaly

---

# 🧠 In Your Finance Project

Now map this to real data:

### Normal transactions

```text
₹100, ₹200, ₹150, ₹180
```

### Weird transaction

```text
₹50,000 🚨
```

👉 Isolation Forest says:

> “This one is too different → suspicious!”

---

# 🔍 How It Appears in Your Dashboard

After running:

```python
df["anomaly"] = model.fit_predict(df[["amount"]])
```

You get:

| amount | anomaly |
| ------ | ------- |
| 120    | 1       |
| 150    | 1       |
| 200    | 1       |
| 50000  | -1 🚨   |

---

# 🎯 Final Understanding

👉 Isolation Forest is not “learning fraud rules”

👉 It is simply asking:

> “Which points are easiest to separate from others?”

---

# 🧠 One-Line Visualization Idea

👉 “Outliers are like dots far away — trees isolate them quickly.”

---

If you want, next I can:

✅ show you a **live Python visualization (matplotlib plot)** using your dataset
✅ or integrate anomaly scores into your dashboard as a **color gradient heatmap 🔥**
