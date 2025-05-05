from openai import OpenAI
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def generate_faq(text, num_questions=5):
    prompt = f"""
    You're an AI assistant. Based on the content below, generate {num_questions} frequently asked questions and their answers.

    Content:
    \"\"\"
    {text[:3000]}
    \"\"\"

    Return format:
    Q1: ...
    A1: ...
    ...
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )

    return response.choices[0].message.content

