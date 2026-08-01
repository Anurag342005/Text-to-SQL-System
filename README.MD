# 🤖 Text-to-SQL Assistant

An AI-powered **Text-to-SQL System** that converts natural language questions into SQL queries using Large Language Models (LLMs). Users can interact with relational databases by asking questions in plain English without writing SQL manually.

The system generates SQL queries, executes them on a database, displays results in an interactive table, and provides AI-generated explanations of query outputs.

---

## 🚀 Features

* ✅ Natural Language to SQL Query Generation
* ✅ LLM-based SQL Generation
* ✅ Database Schema-aware Prompt Engineering
* ✅ SQL Query Execution
* ✅ Interactive Result Visualization
* ✅ AI-generated Result Explanation
* ✅ Chat History Management
* ✅ Download Generated SQL Query
* ✅ Download Query Results as CSV
* ✅ Clean Streamlit User Interface

---

## 🏗️ Architecture

```
User Question
      |
      ↓
Prompt Engineering
      |
      ↓
Large Language Model (LLM)
      |
      ↓
SQL Query Generation
      |
      ↓
SQL Validation & Execution
      |
      ↓
Database
      |
      ↓
Query Result
      |
      ↓
AI Explanation
```

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Frameworks & Libraries

* Streamlit
* LangChain
* SQLAlchemy
* Pandas
* AgGrid

### Database

* SQLite

### AI Model

* Groq LLM API

---

## 📂 Project Structure

```
Text-to-SQL-System/

│
├── app.py                     # Streamlit UI
│
├── database/
│   ├── create_db.py           # Database creation
│
├── sql/
│   ├── generator.py           # Generate SQL query
│   └── executor.py            # Execute SQL query
│
├── llm/
│   ├── model.py               # LLM configuration
│   ├── prompt.py              # SQL generation prompt
│   └── explainer.py           # Result explanation
│
├── utils/
│   └── schema.py              # Database schema extraction
│
├── company.db                 # SQLite database
│
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone <repository-url>

cd Text-to-SQL-System
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Application

Start Streamlit:

```bash
streamlit run app.py
```

Application will open:

```
http://localhost:8501
```

---

## 💡 Example Queries

### Question:

```
Show all employees
```

Generated SQL:

```sql
SELECT *
FROM Employee;
```

---

### Question:

```
Find employees with salary greater than 70000
```

Generated SQL:

```sql
SELECT *
FROM Employee
WHERE Salary > 70000;
```

---

## 📊 Output

The application provides:

* Generated SQL Query
* Database Query Result
* AI Explanation
* Download Options

---

## 🧠 Prompt Engineering Approach

The LLM receives:

* Database schema
* User question
* SQL generation rules

Prompt constraints:

* Generate only SQL
* No explanation
* No markdown formatting
* Use only available tables and columns

This improves SQL generation accuracy and reliability.

---

## 🔮 Future Improvements

* [ ] Support Multiple Databases (MySQL, PostgreSQL)
* [ ] SQL Query Validation
* [ ] Automatic Query Correction
* [ ] Database Schema Visualization
* [ ] Voice-based Query Input
* [ ] User Authentication
* [ ] Persistent Chat Storage

---

## 👨‍💻 Author

**Anurag**

---

## ⭐ Project Highlights

This project demonstrates the implementation of:

* Large Language Models
* Prompt Engineering
* Natural Language Processing
* Database Interaction
* AI-powered Data Analysis
