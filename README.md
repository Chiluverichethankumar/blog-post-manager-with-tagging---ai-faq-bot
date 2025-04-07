# 🚀 Coding Challenge Submission

Welcome! This repository contains solutions to the **two coding challenges** provided:

1. **Backend Application**: Enhanced Blog Post Management with Tagging  
2. **Conversational AI**: LangGraph-based FAQ Bot

Each section below outlines the problem, the solution, how to run the code, and any LLM tool usage (if applicable).

---

## 📘 Challenge 1: Backend Application – Blog Post Manager with Tagging

### ✅ Problem Statement
Build a backend Python application that allows users to:
- Create blog posts with `title`, `content`, and `tags`
- View, filter, and retrieve posts using `MySQL` database
- Support basic CLI operations

### 🛠️ Technologies Used
- Python
- MySQL
- `mysql-connector-python`
- `argparse`

### 📂 Folder Structure


### ▶️ How to Run

1. **Install dependencies**  

2. **Set up MySQL Database**
- Create a database and table as specified in `models.py`
- Update DB credentials in `db.py`

3. **Run the CLI**


### 📄 Features
- Add new blog posts
- List all posts
- Filter by tags
- Retrieve specific posts

### 🤖 LLM Tool Usage
Yes, LLM (ChatGPT) was used to:
- Design folder structure
- Draft boilerplate code
- Format SQL queries
- Validate CLI logic

---

## 🤖 Challenge 2: Conversational AI – LangGraph FAQ Bot

### ✅ Problem Statement
Create a conversational AI chatbot that answers FAQ-style questions related to Python, SQL, EDA, etc., using LangGraph.

### 🛠️ Technologies Used
- Python
- LangGraph
- Pydantic
- `fuzzywuzzy` for fuzzy matching

### 📂 Folder Structure



### ▶️ How to Run

1. **Install dependencies**


2. **Run the bot**


3. **Example Interaction**


### 🧠 Features
- Smart matching of user queries using `fuzzywuzzy`
- Modular and stateful with LangGraph
- Easy to extend FAQ dataset

### 🤖 LLM Tool Usage
Yes, LLM (ChatGPT) was used to:
- Design the modular architecture
- Integrate fuzzy logic
- Provide sample FAQ data
- Debug LangGraph integration

---

## 📦 requirements.txt (common)


---

## 📬 Final Notes
- All code is well-commented and modularized
- Each component can be tested independently
- You can scale both projects with more features (e.g., Web UI for Blog App, LLM backend for FAQ Bot)

---

