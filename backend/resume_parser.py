import re
import pdfplumber
from docx import Document

# -------------------------------
# Predefined skills list (can expand later)
# -------------------------------
SKILLS_DB = [
    "python", "java", "c", "c++", "javascript",
    "react", "node", "sql", "mysql", "mongodb",
    "html", "css", "machine learning", "deep learning",
    "data analysis", "pandas", "numpy", "flask", "django"
]


# -------------------------------
# Function 1: Extract Text from Resume
# Supports PDF and DOCX
# -------------------------------
def extract_text(file_path):
    text = ""

    # PDF files
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    # DOCX files
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"

    else:
        print("Unsupported file format")

    return text.lower()


# -------------------------------
# Function 2: Extract Email using Regex
# -------------------------------
def extract_email(text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"
    match = re.search(email_pattern, text)

    if match:
        return match.group(0)
    return None


# -------------------------------
# Function 3: Extract Skills (Simple Keyword Match)
# -------------------------------
def extract_skills(text):
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


# -------------------------------
# Function 4: Extract Experience (Simplified)
# Looks for patterns like:
# "2 years", "3+ years", "5 yrs"
# -------------------------------
def extract_experience(text):
    experience_pattern = r"(\d+)\+?\s*(years|year|yrs|yr)"

    matches = re.findall(experience_pattern, text)

    if matches:
        years = [int(match[0]) for match in matches]
        return max(years)

    return 0