from resume_parser import extract_text, extract_email, extract_skills, extract_experience

file_path = r"C:\Users\intel\Desktop\College\Vaishnavi_Chunduru_Resume.pdf"

text = extract_text(file_path)

print("Email:", extract_email(text))
print("Skills:", extract_skills(text))
print("Experience:", extract_experience(text), "years")