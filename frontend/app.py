import streamlit as st
import requests

st.title("LegalEase: AI Legal Document Generator")

doc_type = st.selectbox("Document Type", ["Employment Contract", "Non-Disclosure Agreement", "Rental Agreement"])
parties = st.text_input("Parties Involved", "Company A & John Doe")
terms = st.text_area("Terms & Conditions", "Salary: $5000; Working hours: 9 to 5")
dates = st.date_input("Effective Date")

if st.button("Generate Document"):
    payload = {
        "doc_type": doc_type,
        "parties": parties,
        "terms": terms,
        "dates": str(dates)
    }
    try:
        response = requests.post("http://127.0.0.1:8000/generate", json=payload, timeout=30)
        if response.status_code == 200:
            result = response.json()
            st.success("Document Generated Successfully!")
            st.write(result.get("content"))
        else:
            st.error(f"Backend Error ({response.status_code}): {response.text}")
    except Exception as e:
        st.error(f"Connection Failed: {e}")
