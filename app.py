import os
import streamlit as st
from google import genai
from PIL import Image

st.set_page_config(page_title="CodeSnap", page_icon="⚡", layout="centered")

st.title("⚡ CodeSnap")
st.caption("Instant Error Screenshot Fixer powered by Gemma")
st.markdown("---")

uploaded_file = st.file_uploader("Upload error screenshot or terminal stack trace", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Error", use_container_width=True)
    
    if st.button("🛠️ Analyze & Fix Error", type="primary", use_container_width=True):
        with st.spinner("Analyzing error with Gemma..."):
            try:
                client = genai.Client()
                
                prompt = """
                You are an expert software debugging assistant. 
                Analyze this error screenshot or stack trace.
                
                Provide your response in clear Markdown:
                ### 🔍 Root Cause
                Explain in 1-2 clear sentences why this error is happening.
                
                ### 🛠️ Quick Fix / Solution
                Provide the exact terminal command, package installation, or code snippet needed to fix it.
                """

                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=[image, prompt]
                )

                st.success("Analysis Complete!")
                st.markdown("---")
                st.markdown(response.text)

            except Exception as e:
                st.error("Error connecting to Gemini API.")
                st.info("Make sure your `GEMINI_API_KEY` environment variable is set.")
                st.code(str(e))