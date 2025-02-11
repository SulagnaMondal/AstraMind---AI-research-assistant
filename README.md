# AstraMind---AI-research-assistant



[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An AI-powered research assistant that processes PDFs/URLs/text, generates summaries, extracts code, and provides semantic search capabilities.

![App Screenshot](docs/screenshot.png)

## Features ✨
- **Multi-Modal Input**: Process PDFs, URLs, and raw text
- **AI Summarization**: BART/SciBERT models for key insights
- **Code Extraction**: Auto-generate code from ML/AI papers
- **Vector Search**: AstraDB + LangChain integration
- **Streamlit UI**: Interactive web interface

## Installation 🛠️
```bash
# Clone repository
git clone https://github.com/SulagnaMondal/AstraMind---AI-research-assistant.git
cd deepseat-research-assistant

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# Frontend setup (Streamlit)
cd ..
pip install streamlit
