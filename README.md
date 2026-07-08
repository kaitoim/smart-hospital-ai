# Smart Hospital AI Assistant

Smart Hospital AI Assistant adalah chatbot berbasis AI untuk membantu pengguna SIMRS dalam menjawab pertanyaan, melakukan troubleshooting awal perangkat dan aplikasi, serta menyusun laporan gangguan IT secara otomatis. Dengan memanfaatkan Semantic Search, Knowledge Base, dan Large Language Model (LLM), chatbot mampu memberikan respons yang lebih relevan, cepat, dan mudah dipahami sehingga meningkatkan efisiensi layanan dukungan IT di rumah sakit.

## Fitur

- Semantic Search menggunakan Sentence Transformers + FAISS
- Knowledge Base berbasis JSON
- Fallback ke Groq LLM (menggunakan llama-3.3-70b-versatile)
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
```

## Menjalankan di Collab
Buka folder Examples/chatbot_smart_hospital.ipynb di collab, kemudian ikuti langkah di bawah ini
```bash

## Menjalankan Project di Google Colab
1. Upload project ke Google Drive.
2. Buka notebook
3. Jalankan seluruh sel secara berurutan.
Notebook akan melakukan:
- Mount Google Drive
- Clone reporitory
- Install requirements.txt :pip install -r requirements.txt
- Pastikan memiliki secrets di collab untuk key GROQ dengan nama (GROQ_API_KEY) dan NGROK dengan nama (NGROK)
- Menjalankan Streamlit :streamlit run app.py
- Membuat public URL menggunakan ngrok
```
