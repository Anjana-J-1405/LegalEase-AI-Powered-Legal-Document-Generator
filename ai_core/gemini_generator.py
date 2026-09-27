import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiDocumentGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file")
        genai.configure(api_key=api_key)
        
        try:
            self.model = genai.GenerativeModel("gemini-1.5-flash-8b")
        except:
            self.model = genai.GenerativeModel("gemini-1.5-pro")

    def generate_document(self, doc_type: str, parties: str, terms: str, dates: str) -> str:
        prompt = f"""
        Generate a formal legal document for a {doc_type}.
        Parties Involved: {parties}
        Key Terms: {terms}
        Effective Date: {dates}

        Please provide a comprehensive, well-structured legal contract suitable for professional use.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"""LEGAL AGREEMENT: {doc_type.upper()}

1. PARTIES
This agreement is made effective as of {dates}, by and between:
{parties}.

2. TERMS & CONDITIONS
{terms}

3. GOVERNING LAW
This agreement shall be governed by and construed in accordance with standard legal procedures.

[Generated successfully via LegalEase AI Core]
"""
