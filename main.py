import streamlit as st
from crew import run_crew

st.set_page_config(page_title="AI Research Assistant", layout="centered")
st.title("AI Research Paper Assistant")
st.markdown("Upload or paste content from a research paper and get a full summary, blog post, and social media caption.")

with st.form("input_form"):
    topic = st.text_input("Enter your research topic (e.g., LLMs in healthcare):", "Agentic AI")
    paper_text = st.text_area("Paste the research paper abstract or content:", height=300)
    submitted = st.form_submit_button("Generate")

if submitted and paper_text:
    with st.spinner("Thinking like a team of AI researchers..."):
        result = run_crew(topic, paper_text)

    st.subheader("🔍 Research Summary")
    st.write(result['summary'])

    st.subheader("✍️ Blog Post")
    st.write(result['blog'])

    st.subheader("📢 Social Media Caption")
    st.write(result['caption'])
