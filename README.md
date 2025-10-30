# 🤖 ChatPot Pro – AI Chatbot with Flask + NLP

ChatPot Pro is an intelligent conversational chatbot built using **Python**, **Flask**, and **spaCy (NLP)**.  
It understands user queries semantically, responds naturally, and comes with a clean modern web UI.

---

## 🚀 Features

- 🧠 **NLP Understanding** with spaCy — understands meaning, not just words  
- 💬 **Dynamic Conversations** powered by intent matching  
- 🕒 **Tells time & date** on request  
- 🌐 **Built with Flask** — lightweight and fast backend  
- 🎨 **Responsive Chat UI** using HTML, CSS, and JavaScript  
- ⚙️ **Easily Expandable** — add new intents or responses via `intents.json`  

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Python 3, Flask |
| NLP Engine | spaCy (en_core_web_sm) |
| Frontend | HTML, CSS, JavaScript |
| Data | JSON-based Intent File |

---

## 📂 Project Structure

chatpot_pro_web/
│
├── app.py # Flask app
├── chatbot_engine.py # NLP + intent handler
├── requirements.txt # Required Python packages
├── data/
│ └── intents.json # Chatbot responses and patterns
├── static/
│ └── style.css # Chat UI styling
└── templates/
└── index.html # Frontend chat interface


---

## ⚙️ Installation Guide

### 1️⃣ Clone this repository
```bash
git clone https://github.com/vishvashah07/chatpot-pro.git
cd chatpot-pro

2️⃣ Create a Virtual Environment
python -m venv venv

3️⃣ Activate it
Windows (PowerShell)
.\venv\Scripts\Activate.ps1

Command Prompt
venv\Scripts\activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Download spaCy model
python -m spacy download en_core_web_sm

6️⃣ Run the App
python app.py


Then open http://127.0.0.1:5000 in your browser