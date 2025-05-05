import streamlit as st
from faq_generator import extract_text_from_pdf, generate_faq

st.set_page_config(page_title="AI FAQ Generator", layout="wide")
st.title("📄 AI FAQ Generator from PDF")

if "faq_output" not in st.session_state:
    st.session_state.faq_output = ""

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Reading and processing your PDF..."):
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        text = extract_text_from_pdf("temp.pdf")
        faq_output = generate_faq(text, num_questions=10)
        st.session_state.faq_output = faq_output

# Show generated FAQs if available
if st.session_state.faq_output:
    st.subheader("🤖 Generated FAQs")
    st.text_area("FAQs", st.session_state.faq_output, height=300)

    # Download button
    st.download_button(
        label="📥 Download FAQ as .txt",
        data=st.session_state.faq_output,
        file_name="generated_faq.txt",
        mime="text/plain"
    )

# Optional: Clear session state
if st.button("🧹 Clear"):
    st.session_state.faq_output = ""
    st.experimental_rerun()

