# AstraMind---AI-research-assistant



[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An AI-powered research assistant that processes PDFs/URLs/text, generates summaries, extracts code, and provides semantic search capabilities.

![App Screenshot]
![Screenshot 2025-02-11 225653](https://github.com/user-attachments/assets/d908c3ec-3291-492b-8bb7-21595a2ab873)
![Screenshot 2025-02-11 225709](https://github.com/user-attachments/assets/0d553433-9493-4425-a848-856320440166)
![Screenshot 2025-02-11 225730](https://github.com/user-attachments/assets/8ff0ea4a-f38e-4696-b84a-ec76a52e8355)
![Screenshot 2025-02-11 225743](https://github.com/user-attachments/assets/c8eee42c-12f9-4712-be7f-9e14b7653c4e)



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
cd AstraMind---AI-research-assistant

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Source\activate #windows
pip install -r requirements.txt

# Frontend setup (Streamlit)
cd ..
pip install streamlit
```

## 🛠 Tech Stack  

| **Component**           | **Technologies Used**                   |
|------------------------|---------------------------------------|
| **Backend Framework**  | FastAPI                               |
| **Frontend Framework** | Streamlit                             |
| **AI Models**         | BART-Large, SciBERT, CodeT5           |
| **Vector Database**    | AstraDB (Cassandra)                   |
| **Embeddings**        | HuggingFace all-mpnet-base-v2         |
| **NLP Pipeline**      | LangChain                              |
| **PDF Processing**    | PyPDF2                                 |
| **Web Scraping**      | BeautifulSoup4                        |
| **API Documentation** | Swagger/OpenAPI                       |
| **Cloud Deployment**  | Vercel (Backend), Streamlit Cloud (Frontend) |

---

## 🚀 Usage  

```bash
# Start backend
cd backend && uvicorn main:app --reload

# Start frontend (in separate terminal)
streamlit run frontend.py
```
## 🤝 Contributing  

Contributions are welcome! Follow these steps to contribute:  

1. **Fork the repository**  
2. **Create your feature branch:**  
   ```bash
   git checkout -b feature/amazing-feature


