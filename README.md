# 📌 Recruiter AI Agent  
**AI-Powered Recruitment Automation Platform (Indian Market Focus)**

---

## 🚀 Project Overview

Recruiter AI Agent is an AI-powered recruitment assistant designed to automate candidate screening, resume parsing, job matching, and hiring workflow optimization.

This system helps recruiters:

- Automatically parse resumes (PDF/DOCX)
- Extract candidate skills and experience
- Match candidates with job descriptions
- Rank candidates based on scoring algorithm
- Manage recruitment pipeline
- Generate hiring insights

The project focuses on the Indian recruitment ecosystem, including:

- Notice period management (30/60/90 days)
- CTC and LPA salary structure handling
- Indian degree recognition (B.Tech, M.Tech, MCA)
- Tech stack specialization (Java, Python, React, Node, SQL, etc.)

---

## 🎯 Problem Statement

Recruiters spend significant time manually:

- Screening resumes  
- Matching candidates to job requirements  
- Ranking applicants  
- Managing hiring stages  

Manual processes:

- Slow down hiring  
- Introduce bias  
- Reduce efficiency  
- Increase cost-per-hire  

This project automates recruitment screening using AI to:

✔ Improve hiring speed  
✔ Reduce bias  
✔ Improve candidate-job fit  
✔ Provide structured hiring workflow  

---

## 🧠 Key Features

### 1️⃣ Resume Parsing Engine

- Supports PDF and DOCX resumes  
- Extracts:
  - Name
  - Email
  - Skills
  - Education
  - Experience  
- Uses spaCy NLP and regex techniques  

---

### 2️⃣ Job Description Analyzer

Recruiter inputs:

- Job title  
- Required skills  
- Experience requirement  
- Location  

System:

- Extracts structured job requirements  
- Prepares matching criteria  

---

### 3️⃣ Candidate Matching & Scoring Algorithm

Candidates are scored using:


Score =
( Skill Match % × 0.5 ) +
( Experience Match % × 0.3 ) +
( Education Match × 0.2 )


Outputs:

- Match percentage  
- Missing skills  
- Strength areas  
- Ranked candidate list  

---

### 4️⃣ Recruitment Pipeline Dashboard

Recruiters can:

- Upload multiple resumes  
- View ranked candidates  
- Update candidate status:
  - Applied
  - Shortlisted
  - Interviewed
  - Selected
  - Rejected  

Track hiring progress visually.

---

### 5️⃣ Indian Recruitment Specialization

The system includes:

- Notice period tracking (30/60/90 days)  
- Salary expectation handling (LPA format)  
- Indian education recognition  
- Tech-focused skill matching  
- Regional hiring preferences  

---

## 🏗️ System Architecture

### Frontend
- Streamlit dashboard  
- Candidate pipeline visualization  
- Resume upload interface  
- Job input form  

### Backend
- Python  
- spaCy for NLP  
- LangChain for AI logic  
- Resume parsing engine  
- Matching algorithm module  

### Database
- SQLite  

Stores:

- Candidate data  
- Job requirements  
- Scores  
- Recruitment status  

---

## 📂 Project Structure


Recruiter-AI-Agent/
│
├── backend/
│ ├── app.py
│ ├── resume_parser.py
│ ├── matcher.py
│ ├── database.py
│ └── models.py
│
├── database/
│ └── candidates.db
│
├── requirements.txt
└── README.md


---

## ⚙️ Tech Stack

- Python 3.11  
- Streamlit  
- spaCy  
- pdfplumber  
- python-docx  
- pandas  
- SQLite  
- LangChain  
- Google Generative AI (Gemini)

---

## 🛠 Installation Guide

### Step 1: Clone Repository


git clone <your-repository-link>
cd Recruiter-AI-Agent


---

### Step 2: Create Virtual Environment


py -3.11 -m venv venv
venv\Scripts\activate


---

### Step 3: Install Dependencies


pip install -r requirements.txt


Or manually:


pip install streamlit spacy pdfplumber python-docx pandas langchain google-generativeai


---

### Step 4: Install spaCy Model


python -m spacy download en_core_web_sm


---

### Step 5: Run Application


streamlit run app.py


---

## 📊 Database Schema

### Candidates Table

- id – Candidate ID  
- name – Candidate name  
- email – Candidate email  
- skills – Extracted skills  
- experience – Years of experience  
- education – Degree  
- score – Matching score  
- status – Hiring stage  

---

### Jobs Table

- id – Job ID  
- job_title – Role title  
- required_skills – Required skills  
- experience_required – Required experience  
- created_at – Date created  

---

## 📈 Success Metrics

- Resume parsing accuracy  
- Candidate matching relevance  
- Reduction in manual screening time  
- Time-to-hire optimization  
- Improved candidate-job fit score  

---

## 🔐 Ethical & Compliance Considerations

- Candidate data privacy  
- Secure database handling  
- Bias-free skill-based matching  
- No demographic-based filtering  
- Transparent scoring algorithm  

---

## 🎥 Demo Highlights

The demo includes:

- Resume upload  
- Automated skill extraction  
- Job requirement input  
- Ranked candidate list  
- Status tracking  
- Hiring analytics  

---

## 🚀 Future Improvements

- AI-generated interview questions  
- Automated email communication  
- Integration with assessment platforms  
- Background verification integration  
- Diversity analytics dashboard  
- Predictive hiring success model  

---

## 👩‍💻 Team Members

- Sudheepthi Yemunuri  
- (Add team members here)

---

## 🏆 Learning Outcomes

Through this project we gained:

- NLP-based resume parsing  
- AI-powered candidate matching  
- Recruitment workflow automation  
- Database management  
- Ethical AI design  
- Deployment experience  

---

## 📌 Industry Relevance

This project is aligned with HR-tech platforms like:

- :contentReference[oaicite:0]{index=0}  
- :contentReference[oaicite:1]{index=1}  
- :contentReference[oaicite:2]{index=2}  

---

## 📜 License

This project is developed for academic and portfolio purposes.