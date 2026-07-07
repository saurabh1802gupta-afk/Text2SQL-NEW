# 🚀 Text2SQL App

A full-stack **Text-to-SQL** application that converts natural language questions into executable SQL queries using Large Language Models (LLMs).

The application enables users to interact with relational databases using plain English instead of writing SQL manually.

---

## ✨ Features

* Convert natural language into SQL queries
* PostgreSQL database integration
* FastAPI REST API backend
* React + TypeScript frontend
* LLM-powered SQL generation
* Automatic database schema loading
* Modular project architecture
* Easily extensible for different LLMs

---

## 🛠️ Tech Stack

### Frontend

* React
* TypeScript
* Vite

### Backend

* FastAPI
* SQLAlchemy
* Psycopg2
* Python 3.12+

### Database

* PostgreSQL

### AI / NLP

* Qwen 2.5 (Planned)
* Prompt Engineering

---

## 📁 Project Structure

```text
text2sql-app/
│
├── backend/
│   ├── app/
│   ├── config/
│   ├── database/
│   ├── services/
│   ├── models/
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/saurabhgupta/text2sql-app.git
cd text2sql-app
```

### Backend Setup

```bash
cd backend

python -m venv .venv

source .venv/bin/activate      # macOS/Linux
# OR
.venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file inside the backend directory (see `backend/.env.example` for reference).

```env
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database

OLLAMA_MODEL=qwen2.5:7b
```

### Run Backend

```bash
uvicorn main:app --reload
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

## 🏛️ Architecture

```text
User
   │
   ▼
React Frontend
   │
   ▼
FastAPI Backend
   │
   ▼
Schema Extraction
   │
   ▼
LLM
   │
   ▼
Generated SQL
   │
   ▼
PostgreSQL
   │
   ▼
Query Results
```

---

## 📌 Roadmap

* [x] Backend setup
* [x] PostgreSQL connection
* [x] SQLAlchemy integration
* [x] React frontend setup
* [ ] LLM integration
* [ ] Prompt engineering
* [ ] SQL validation
* [ ] Query history
* [ ] Docker support
* [ ] CI/CD pipeline

---

## 🤝 Contributing

Contributions, suggestions, and issue reports are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 👨‍💻 Author

**Saurabh Gupta**

If you found this project interesting, feel free to ⭐ the repository.
