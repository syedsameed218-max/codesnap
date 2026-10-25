⚡ CodeSnap

CodeSnap is a lightweight, multimodal AI error debugger powered by the Gemini API and Streamlit. It allows developers to instantly upload screenshots of errors or terminal stack traces to get an automated root cause analysis and quick fixes.

🚀 Features

Instant Error Diagnosis: Upload screenshots of terminal crashes, build errors, or UI bugs.

Powered by Gemini: Uses the latest Gemini models for rapid visual reasoning and technical analysis.

Minimal & Fast: Built with Python and Streamlit for zero-bloat, instant local execution.

🛠️ Prerequisites & Setup

Make sure you have Python 3.10+ installed on your machine.

1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/codesnap.git
cd codesnap


2. Install Dependencies

Install the required Python packages using pip:

pip install streamlit google-genai pillow


3. Set Up Your Gemini API Key

You need a free API key from Google AI Studio. Set it as an environment variable in your terminal:

Windows (Command Prompt):

set GEMINI_API_KEY=your_actual_api_key_here


Windows (PowerShell):

$env:GEMINI_API_KEY="your_actual_api_key_here"


Mac / Linux:

export GEMINI_API_KEY="your_actual_api_key_here"


▶️ Running the App Locally

Start the Streamlit application by running:

python -m streamlit run app.py


Open your browser and navigate to http://localhost:8501.
