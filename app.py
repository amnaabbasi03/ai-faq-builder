import streamlit as st
from faq_generator import extract_text_from_pdf, generate_faq
from fpdf import FPDF
import io
import unicodedata

st.set_page_config(page_title="AI FAQ Generator", layout="wide")
st.title("📄 AI FAQ Generator from PDF")

if "faq_outputs" not in st.session_state:
    st.session_state.faq_outputs = {}  # file_name: faq
if "current_file" not in st.session_state:
    st.session_state.current_file = None

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

# FAQ count slider
faq_count = st.slider("Select number of FAQs to generate", min_value=5, max_value=20, value=10, step=1)

# Process new file only
if uploaded_file is not None:
    file_name = uploaded_file.name
    if file_name != st.session_state.current_file:
        with st.spinner("Reading and processing your PDF..."):
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.read())
            text = extract_text_from_pdf("temp.pdf")
            faq_output = generate_faq(text, num_questions=faq_count)
            st.session_state.faq_outputs[file_name] = faq_output
            st.session_state.current_file = file_name

# Show FAQs if available
if st.session_state.current_file:
    current_faq = st.session_state.faq_outputs[st.session_state.current_file]
    st.subheader(f"🤖 FAQs for: {st.session_state.current_file}")
    st.text_area("Generated FAQs", current_faq, height=300)

    # Download as TXT
    st.download_button(
        label="📥 Download as .txt",
        data=current_faq,
        file_name="generated_faq.txt",
        mime="text/plain"
    )

    # Utility to sanitize Unicode characters
    def sanitize_text(text):
        text = unicodedata.normalize("NFKD", text)
        return text.encode("ascii", "ignore").decode("ascii")

    # Download as PDF
    def generate_pdf(faq_text):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        clean_text = sanitize_text(faq_text)

        for line in clean_text.split('\n'):
            pdf.multi_cell(0, 10, line)

        pdf_output = pdf.output(dest='S').encode('latin1')
        return io.BytesIO(pdf_output)

    st.download_button(
        label="📄 Download as PDF",
        data=generate_pdf(current_faq),
        file_name="generated_faq.pdf",
        mime="application/pdf"
    )

# Show history
if st.session_state.faq_outputs:
    st.markdown("---")
    st.subheader("📚 Past Uploaded Files")
    for filename in st.session_state.faq_outputs:
        with st.expander(filename):
            st.text(st.session_state.faq_outputs[filename])

# Clear state
if st.button("🧹 Clear All"):
    st.session_state.faq_outputs = {}
    st.session_state.current_file = None
    st.experimental_rerun()

