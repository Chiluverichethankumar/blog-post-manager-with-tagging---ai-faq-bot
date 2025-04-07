# 🧩 Blog Post Manager & Conversational AI FAQ Bot

This repository contains **two coding challenges**:

1. 📝 **Backend Blog Post Manager with Tagging**
2. 🤖 **Conversational AI FAQ Bot using LangGraph**

Each project is modular, well-structured, and includes detailed setup and instructions.

---

## 📝 Project 1: Blog Post Manager with Tagging

### 🚀 Features

- Add, view, and delete blog posts.
- Tag posts and search by tags.
- CLI-based backend system.
- Persistent storage using MySQL.

### 🗂️ Database Schema

- `posts` table with `id`, `title`, `content`.
- `tags` table with `id`, `name`.
- `post_tags` junction table for many-to-many mapping.
- Clean separation of concerns with normalized schema.

### 🔍 Search by Tag (How it works)

- Accepts user input as tag name.
- Performs SQL JOIN between `posts`, `post_tags`, and `tags`.
- Returns all posts associated with the given tag.

### 🤖 LLM Tool Usage

Yes, LLM (ChatGPT) was used to:

- Design schema and implement SQL queries
- Optimize Python-MySQL interactions
- Guide modular CLI structure
- Debug search logic

### 🛠️ Run Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/project-repo-name.git
   cd project-repo-name
   ```

python -m venv venv
source venv/bin/activate # on Windows use venv\Scripts\activate

pip install -r requirements.txt

python main.py

---

## 🤖 Project 2: Conversational AI FAQ Bot

### 🧠 Features

- Smart matching of user queries using `fuzzywuzzy`
- Modular and stateful with LangGraph
- Easy to extend FAQ dataset
- CLI-based interactive experience

### 🧰 How It Works

- The user types a question into the CLI.
- The question is passed through a fuzzy matching algorithm.
- The best match is selected from the FAQ dataset.
- LangGraph handles the stateful interaction for scalable flow management.

### 🤖 LLM Tool Usage

Yes, LLM (ChatGPT) was used to:

- Design the modular architecture
- Integrate fuzzy string matching
- Provide example FAQs and logic
- Debug LangGraph integration and CLI flow

### 🛠️ Run Instructions

1. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

cd faq_bot_project

python -m faq_bot.main

What is Python?
How to use MySQL?
What does EDA mean?

Let me know if you'd like this saved as an actual `README.md` file or zipped with both projects for upload.
