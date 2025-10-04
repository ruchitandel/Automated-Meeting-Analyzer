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


---

## ⚙️ Installation & Setup


### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/Meeting-Transcript-Analyzer.git
cd Meeting-Transcript-Analyzer

### 2️⃣ Create a Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Train and Save Models
Run the notebook to preprocess data and generate model files:

jupyter notebook projectNLP.ipynb

This will create lda_model.joblib and dictionary.joblib inside the models/ folder.

### 5️⃣ Launch the Streamlit App
streamlit run app.py

Then open your browser and navigate to:
http://localhost:8501

---



## 🧩 How It Works

The input transcript is cleaned and tokenized using **SpaCy**.

**LDA (Latent Dirichlet Allocation)** identifies the most probable topic based on word distributions.

The script extracts sentences that include words like **“I will”**, **“We need to”**, **“Next step”**, etc., marking them as **action items**.

**Named Entity Recognition (NER)** identifies and counts mentions of people, organizations, locations, and dates.

Results are displayed in a clean and interactive **Streamlit interface**.

---

## 🧠 Example Usage

### **Input Transcript:**
Meeting Chairman (Mark): Good morning. The main agenda today is our Q3 marketing strategy.
Alice Linnes: I think our biggest gap is social media engagement. Customers expect faster responses.
Jennifer Miles: I will draft a proposal for a new engagement plan by next Friday.


### **Output:**
**Topic:** Marketing Strategy (Confidence: 91%)  
**Keywords:** marketing, engagement, social, customer  

**Action Items:**
1. I will draft a proposal for a new engagement plan by next Friday.  

**Entities:**
- Mark (PERSON)  
- Jennifer Miles (PERSON)  
- Friday (DATE)

---

## 🧰 Technologies Used

| Tool | Purpose |
|------|----------|
| **Python 3.x** | Core programming language |
| **Streamlit** | Interactive web UI framework |
| **SpaCy** | NLP preprocessing and Named Entity Recognition |
| **Gensim** | Topic Modeling (LDA) |
| **Joblib** | Model persistence and loading |
| **Pandas** | Data manipulation |
| **Jupyter Notebook** | Model training and experimentation |

---

## 📊 Results Visualization

The app provides:

- **Topic Summary:** Displays the dominant meeting theme with confidence level.  
- **Action Items Panel:** Lists all extracted next steps and decisions.  
- **Entity Table:** Shows the top 10 most frequently mentioned entities (People, Dates, Orgs, etc.).

---

## 🧩 Example Screenshot

*(Add your app screenshot above for a professional touch.)*

---

## 🧭 Future Improvements

- 🤖 Integrate **BERTopic** for more advanced topic modeling.  
- 🗂️ Add **multi-meeting analytics dashboard** to compare across sessions.  
- 🗣️ Include **sentiment and tone analysis** for speaker evaluation.  
- 📄 Enable **file upload (TXT, DOCX, PDF)** for transcript import.  
- 🧑‍💼 Build a **summary generator** using transformer-based models (BERT/GPT).  

---

## 👩‍💻 Author

**Developed by:** [Ruchi Tandel]  
**GitHub:** [https://github.com/your-username](https://github.com/your-username)  
**LinkedIn:** [https://linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)

---

## 🪪 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it for educational or personal use.

---

## ⭐ Show Your Support

If you found this project useful, please ⭐ **star this repository** on GitHub to show your support and help others discover it!
