import streamlit as st
from utils.summarizer import load_model, summarize_text, convert_to_bullets
from utils.pdf_reader import extract_pdf_text
from utils.youtube_utils import get_transcript
from utils.language_utils import detect_language
from utils.text_utils import clean_text, split_text, clean_summary

# Load model once
@st.cache_resource
def load():
    return load_model()

model = load()

st.sidebar.image("assets/logo.png", width=150)
st.sidebar.title("Text Summarizer App")
mode = st.sidebar.radio("Select Input Type:", ["Text", "PDF", "YouTube Video"])

length_choice = st.sidebar.selectbox("Summary Length:", ["Short", "Medium", "Long"])
temperature = st.sidebar.slider("Creativity (Temperature)", 0.1, 2.0, 1.0)
bullet_points = st.sidebar.checkbox("Generate Bullet-Point Summary")

st.title("📝 Intelligent Text Summarizer")

text_input = ""

if mode == "Text":
    text_input = st.text_area("Enter text to summarize:", height=200)

elif mode == "PDF":
    uploaded_pdf = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded_pdf:
        text_input = extract_pdf_text(uploaded_pdf)
        st.success("PDF text extracted successfully!")

elif mode == "YouTube Video":
    yt_url = st.text_input("Enter YouTube Link:")
    if yt_url:
        try:
            text_input = get_transcript(yt_url)
            st.success("Transcript fetched successfully!")
        except:
            st.error("Unable to fetch transcript.")

if st.button("Summarize"):
    if not text_input.strip():
        st.warning("Please enter some text first.")
    else:
        lang = detect_language(text_input)
        st.write(f"**Detected Language:** {lang}")


    with st.spinner("Summarizing..."):
        cleaned = clean_text(text_input)
        chunks = split_text(cleaned)

        summaries = []

        for chunk in chunks:
            result = summarize_text(chunk, model, length_choice, temperature)
            cleaned_result = clean_summary(result)
            summaries.append(cleaned_result)

        final_output = " ".join(summaries)
        final_output = clean_summary(final_output)

    if bullet_points:
            final_output = convert_to_bullets(final_output)

    st.subheader("📌 Summary:")
    st.write(final_output)