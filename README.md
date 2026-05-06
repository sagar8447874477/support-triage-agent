# 🧠 Support Triage Agent (AI-based Ticket Classifier)

## 🚀 Overview

This project is an **AI-powered support triage system** that automatically:

* Classifies customer support tickets into predefined categories
* Generates suggested replies for common issues
* Flags tickets that require human intervention (escalation)

The goal is to **reduce manual effort** for support teams and improve response efficiency.

---

## 🏗️ Problem Statement

Customer support teams receive large volumes of tickets daily across categories like:

* Billing / Refunds
* Account Issues
* Technical Bugs
* Content Access Problems

Manually triaging these tickets is slow and inconsistent.

This project solves that by building a **lightweight, offline AI system** (no paid APIs).

---

## ⚙️ Approach

### 1. 📂 Category Taxonomy

Defined the following categories:

* Billing & Refunds
* Account Issues
* Technical Bugs
* Content Access
* General Feedback

👉 These categories are:

* Mutually exclusive
* Actionable for support teams

---

### 2. 🧹 Text Processing

Basic preprocessing applied:

* Lowercasing
* Removing special characters

This ensures consistent input for the model.

---

### 3. 🤖 Classification Model

Used:

* **TF-IDF Vectorization**
* **Logistic Regression**

#### Why this approach?

* Fast and lightweight
* Works offline (no API dependency)
* Easy to explain and debug
* Performs well on small datasets

---

### 4. ✉️ Suggested Replies

* Implemented **template-based replies**
* Only for top categories:

  * Billing
  * Account Issues

#### Why templates?

* Reliable and safe
* No hallucination risk (unlike generative models)
* Easy to control tone and content

---

### 5. 🚨 Escalation Logic

A ticket is escalated if:

* Model confidence < threshold (e.g., 0.6)
* Contains sensitive keywords (e.g., "refund immediately", "fraud")

#### Why this matters?

Prevents:

* Wrong auto-replies
* Poor customer experience

---

### 6. 🌐 Web Application

Built using **Streamlit**

Features:

* Input ticket text
* Shows:

  * Predicted category
  * Confidence score
  * Escalation decision
  * Suggested reply

#### Why Streamlit?

* Fastest way to build UI
* No frontend knowledge required
* Ideal for prototypes and demos

---

### 7. 🚀 Deployment

Deployed using:

* GitHub (code hosting)
* Streamlit Cloud (free hosting)

#### Why this setup?

* Zero cost
* Easy CI/CD
* Shareable public link

---

## 📊 Output

The system generates structured output:

* Ticket
* Predicted category
* Confidence score
* Escalation flag
* Suggested reply

---

## 🧪 Evaluation Strategy

If scaled, I would evaluate using:

* Accuracy
* Precision / Recall
* Confusion Matrix

Business metrics:

* Auto-resolution rate
* Escalation accuracy

---

## 🔄 Alternatives Considered

### ❌ LLM APIs (OpenAI, Anthropic)

* Not used due to constraint: **no paid APIs**

---

### 🤖 Transformer Models (BERT)

**Pros:**

* Higher accuracy
* Better context understanding

**Cons:**

* Heavier
* Slower
* Overkill for small dataset

👉 Could be used in production

---

### 🧠 Rule-Based System Only

**Pros:**

* Simple

**Cons:**

* Not scalable
* Hard to maintain

---

### ✍️ Generative Replies (LLMs)

**Pros:**

* Dynamic responses

**Cons:**

* Risk of incorrect replies
* Requires moderation

👉 Templates chosen for reliability

---

## ⚖️ Tradeoffs

| Decision                     | Benefit       | Tradeoff                         |
| ---------------------------- | ------------- | -------------------------------- |
| TF-IDF + Logistic Regression | Fast, simple  | Less accurate than deep learning |
| Template replies             | Safe          | Not flexible                     |
| No API usage                 | Free, offline | Limited intelligence             |

---

## 📈 Scaling to Production (10K tickets/month)

If scaling:

* Use BERT / fine-tuned transformer
* Add human feedback loop
* Store data in database
* Use async processing (queues)
* Add monitoring & logging

---

## 💰 Cost Estimate

Current system:

* ~$0 (fully local + free hosting)

At scale (with APIs):

* ~$20–100/month (depending on usage)

---

## 🛠️ Tech Stack

* Python
* scikit-learn
* Streamlit
* Pandas

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
python model.py
python -m streamlit run app.py
```

---

## 🌍 Live Demo

👉 [https://support-triage.streamlit.app/]

---

## 📌 Future Improvements

* Use transformer-based models
* Multi-label classification
* Better dataset (real-world tickets)
* UI improvements
* Analytics dashboard

---

## 🙌 Conclusion

This project demonstrates how to build a **practical AI system under constraints**:

* No paid APIs
* Fully offline
* Simple yet effective

It balances:

* Performance
* Cost
* Reliability

---
