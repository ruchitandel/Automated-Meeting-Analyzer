# 🧠 Meeting Transcript Analyzer

A **Streamlit-based Natural Language Processing (NLP) application** that automatically analyzes meeting transcripts to extract **key discussion topics**, **action items**, and **important named entities**.  
This project helps convert long, unstructured meeting data into concise, actionable insights using **Topic Modeling (LDA)** and **SpaCy-based NLP**.

---

## 🚀 Project Overview

Meetings often generate extensive transcripts that can be difficult to review.  
The **Meeting Transcript Analyzer** simplifies this process by:
- Identifying **main themes and topics** discussed.
- Extracting **action items** (tasks, decisions, follow-ups).
- Recognizing **entities** such as people, organizations, dates, and locations.
- Providing an **interactive web dashboard** to visualize and understand meeting insights.

---

## 🎯 Features

- 🔍 **Topic Modeling (LDA)** – Detects and summarizes the dominant discussion topics.  
- ✅ **Action Item Extraction** – Highlights key to-dos and responsibilities.  
- 🧾 **Named Entity Recognition (NER)** – Identifies names, organizations, and dates.  
- 🧠 **Preprocessing with SpaCy** – Cleans and lemmatizes text for model-ready input.  
- ⚡ **Interactive Streamlit Interface** – Easy to use, responsive, and fast.  
- 💾 **Model Caching** – Prevents reloading models repeatedly, improving performance.

---

## 🏗️ Project Structure

📂 Meeting-Transcript-Analyzer
│
├── app.py # Main Streamlit application
├── projectNLP.ipynb # Notebook used to preprocess data and train LDA model
├── data.txt # Sample meeting transcript for testing
│
├── 📂 models # Pre-trained models generated from notebook
│ ├── lda_model.joblib
│ ├── dictionary.joblib
│
├── requirements.txt # List of Python dependencies
└── README.md # Project documentation
