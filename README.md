# Smart Hospital AI Assistant

Smart Hospital AI Assistant adalah chatbot berbasis AI untuk membantu pengguna SIMRS menggunakan. 
Menggunakan model LLaMA v.1

## Fitur

- Semantic Search menggunakan Sentence Transformers + FAISS
- Knowledge Base berbasis JSON
- Fallback ke Groq LLM
- Conversation Memory
- Penyusunan laporan Helpdesk otomatis
- Streamlit UI
- Support Google Colab + Ngrok

## Struktur Project
```bash
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
bash'''

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
- Clone reporitory
- Install requirements.txt
- Pastikan memiliki key GROQ dan NROK
- Menjalankan Streamlit
- Membuat public URL menggunakan ngrok
