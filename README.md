# Smart Hospital AI Assistant

Smart Hospital AI Assistant adalah chatbot berbasis AI untuk membantu pengguna SIMRS.

## Fitur

- Semantic Search menggunakan Sentence Transformers + FAISS
- Knowledge Base berbasis JSON
- Fallback ke Groq LLM
- Conversation Memory
- Penyusunan laporan Helpdesk otomatis
- Streamlit UI
- Support Google Colab + Ngrok

## Struktur Project
smart-hospital-ai/
│
├── app.py
├── README.md
├── requirements.txt
├── backend/
├── frontend/
├── data/
├── examples/
│     └── chatbot_smart_hospital.ipynb
└── .gitignore

## Menjalankan

```bash
pip install -r requirements.txt
streamlit run app.py

## Menjalankan Project di Google Colab
1. Upload project ke Google Drive.
2. Buka notebook
3. Jalankan seluruh sel secara berurutan.
Notebook akan melakukan:
- Mount Google Drive
- Install dependencies
- Menjalankan Streamlit
- Membuat public URL menggunakan ngrok
