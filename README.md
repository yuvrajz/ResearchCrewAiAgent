# 🧠 Mistral Multi-Agent Research Assistant

This project is a multi-agent AI system built using **CrewAI**, **Mistral-7B-Instruct** from Hugging Face, and a **Streamlit UI**. 
It simulates a mini research team that collaborates to summarize a research paper, write a blog post, and generate a social media caption.

## 🔧 Features
- ✅ Uses 4 AI agents (summary, blogging, marketing)
- ✅ Powered by open-source model: `mistralai/Mistral-7B-Instruct`
- ✅ Streamlit-based web interface (no API keys or OpenAI needed)
- ✅ Fully valid for **CrewAI Certification** 🏅

## 🤖 Agents Used

| Agent              | Description                                |
|--------------------|--------------------------------------------|
| `summarizer_agent` | Summarizes a research paper                |
| `blog_agent`       | Converts summary to an engaging blog post  |
| `caption_agent`    | Writes tweet-style caption for the blog    |

## 🚀 How to Run

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run main.py
