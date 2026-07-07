🚀 Text2SQL Data Agent
A pure-Python, LLM-powered Text-to-SQL agent that turns your PostgreSQL database into a conversational partner.

Built entirely with Streamlit, this application eliminates the standard frontend/backend divide, offering a seamless, interactive chat interface where natural language questions instantly render as executable queries and interactive dataframes.

✨ Features
100% Python Architecture: No npm, no JavaScript, no complex API routing.

Native Chat Interface: Built-in Streamlit conversational UI optimized for AI agents.

Interactive DataFrames: Query results are instantly rendered as sortable, filterable, and downloadable tables.

Live Schema Introspection: A dynamic sidebar that automatically reads and maps your database schema for the AI.

LLM Agnostic: Designed to work smoothly with local models via Ollama (Qwen 2.5) or cloud providers.

🛠️ Tech Stack
Framework & UI
Streamlit (Provides both the web server and the reactive UI)

Pandas (For data manipulation and table rendering)

Data & AI Engine
Python 3.12+

SQLAlchemy & Psycopg2 (Database connection and schema extraction)

Ollama (Qwen 2.5) (Local LLM inference)

Database
PostgreSQL

🖥️ The Streamlit UI Experience
Instead of traditional web pages, the UI is built as an interactive dashboard:

The Control Panel (Sidebar): Contains your database connection parameters, model selection dropdowns, and an expandable accordion showing your current database schema (tables and columns).

The Chat Stream (Main Stage): A message history where you interact with the agent.

The Data Output: When the agent executes SQL, the response is injected directly into the chat stream as an interactive Pandas DataFrame that you can download as a CSV with one click.

📁 Project Structure
Plaintext
text2sql-agent/
│
├── core/
│   ├── __init__.py
│   ├── database.py       # SQLAlchemy engines & schema logic
│   ├── llm.py            # Ollama integrations & prompt chaining
│   └── sql_parser.py     # Cleans and validates LLM output
│
├── app.py                # The main Streamlit UI application
├── requirements.txt
├── .env
└── README.md
⚙️ Installation & Run Guide
Because the app is pure Python, setup takes less than a minute.

1. Clone the repository
Bash
git clone https://github.com/saurabhgupta/text2sql-agent.git
cd text2sql-agent
2. Set up the Python Environment
Bash
python -m venv .venv

source .venv/bin/activate      # macOS/Linux
# OR
.venv\Scripts\activate         # Windows

pip install -r requirements.txt
3. Environment Variables
Create a .env file in the root directory:

Code snippet
DB_URL=postgresql+psycopg2://postgres:your_password@localhost:5432/your_database
OLLAMA_MODEL=qwen2.5:7b
4. Launch the App
Bash
streamlit run app.py
A browser window will automatically open to http://localhost:8501.

🏛️ Architecture Flow
Plaintext
User Input (Streamlit Chat)
   │
   ▼
app.py (State Management)
   │
   ▼
Schema Injection (database.py)
   │
   ▼
Local LLM via Ollama (llm.py)
   │
   ▼
SQL Execution (Pandas `read_sql`)
   │
   ▼
Streamlit DataFrame Render
📌 Roadmap
[x] Streamlit UI scaffolding

[x] PostgreSQL connection pooling

[ ] Ollama prompt engineering for Qwen 2.5

[ ] Read-only execution safeguards

[ ] Natural language explanations of the generated SQL

[ ] Multi-database support (MySQL, SQLite)

[ ] Data visualization (Auto-generating charts using st.bar_chart based on query results)

🤝 Contributing
Contributions, suggestions, and issue reports are welcome.

Fork the repository

Create a feature branch

Commit your changes

Open a Pull Request

👨‍💻 Author
Saurabh Gupta

If you found this project interesting, feel free to ⭐ the repository.
