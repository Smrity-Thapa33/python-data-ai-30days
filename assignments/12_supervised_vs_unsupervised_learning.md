# Assignment 4 — Supervised vs Unsupervised Learning
**Name:** Smrity Thapa  
**Track:** Dlytica Data & AI Foundations  
**Week:** 3 · Concept Worksheet

---

## Part A — Explanation

### 1. Supervised vs Unsupervised Learning

**Supervised learning** is when a model is trained on labeled data — meaning every training example already has the correct answer attached to it. The model learns by comparing its predictions to these known answers and adjusting until it gets better. The word "supervised" reflects that the correct answers guide the learning process.

**Unsupervised learning** is when the training data has no labels — no correct answers are given. The model must find patterns, groupings, or structure in the data on its own, without being told what to look for.

**Key difference:** supervised learning has labels (correct answers); unsupervised learning does not.

---

### 2. Real-Life Analogies

**Supervised →** Studying for an exam with an answer key. You practice problems, check your answers, and correct your mistakes. The answer key supervises your learning.

**Unsupervised →** Sorting your photo gallery with no instructions. You group photos by similarity — same people, same places — based on patterns you notice yourself, with no one telling you the categories in advance.

---

### 3. Classification vs Regression (both are Supervised)

**Classification →** The answer is a category. Example: is this email spam or not spam? The output is one of a fixed set of labels.

**Regression →** The answer is a number. Example: what will tomorrow's temperature be? The output is a continuous numeric value.

The key question to ask: *"Is the answer a category or a number?"*  
Category → Classification. Number → Regression.

---

## Part B — Classifying Each Scenario

| Real-world Task | Supervised or Unsupervised? | Classification / Regression? |
|---|---|---|
| Predict tomorrow's temperature from weather data | Supervised | Regression |
| Group 10,000 customers into similar segments (no labels given) | Unsupervised | — |
| Decide if an email is spam or not spam | Supervised | Classification |
| Predict the selling price of a used car | Supervised | Regression |
| Find unusual credit-card transactions that look like fraud (no fraud labels) | Unsupervised | — |
| Recognize whether a photo contains a cat, dog, or bird | Supervised | Classification |
| Organize news articles into topic groups without being told the topics | Unsupervised | — |

---

## Part C — Diving a Little Deeper

### 1. Chosen Task: Predict the selling price of a used car (Supervised → Regression)

**Features (inputs the model would need):**
- Mileage — how many km the car has been driven
- Car age — year of manufacture
- Brand/Model — e.g. Toyota, Honda

**Label (what the model predicts):**
- Selling price (a continuous number in Rs)

---

### 2. Why can't unsupervised learning predict an exact house price?

Unsupervised learning finds patterns and groups in data — it has no concept of a "correct answer." Predicting an exact price requires knowing what the right price is for each training example (a label), so the model can learn the relationship between features and price. Without labels, there is nothing to predict toward.

---

### 3. The 5-Step Model Pipeline (in order)

> Collect Data → Prepare / Clean Data → Train the Model → Evaluate the Model → Deploy / Use the Model

---

## Self-Check

- [x] I explained both learning types using the word "labels"
- [x] I filled in every row of the Part B table
- [x] For Part C, my features are inputs and my label is the answer (I didn't mix them up)
- [x] My answers are in my own words, not copied