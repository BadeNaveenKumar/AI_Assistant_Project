# 🤖 AI Assistant Project

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![AI](https://img.shields.io/badge/Artificial%20Intelligence-FF6F00?style=for-the-badge&logo=openai&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

**A Python-powered AI Assistant using Google's Gemini API — capable of answering questions, summarizing text, and generating creative content with real-time user feedback tracking.**

</div>

---

## 🌟 Project Overview

This is a **Prompt Engineering AI Assistant** built using **Google's Gemini 2.0 Flash API**. It provides an interactive command-line interface with 3 core AI-powered functions and a built-in feedback system to track response quality.

| 📋 Detail | ℹ️ Info |
|---|---|
| 👤 **Author** | Naveen Kumar Bade |
| 🔗 **GitHub** | [@BadeNaveenKumar](https://github.com/BadeNaveenKumar) |
| 🤖 **AI Model** | Google Gemini 2.0 Flash |
| 🐍 **Language** | Python 3 |
| 📅 **Created** | October 2025 |

---

## ✨ Features

| # | Feature | Description |
|---|---|---|
| 1️⃣ | 🔍 **Question Answering** | Get accurate, factual answers to any question |
| 2️⃣ | 📝 **Text Summarization** | Summarize long text into 3–5 concise sentences |
| 3️⃣ | 🎨 **Creative Content Generation** | Generate stories, poems, articles & more |
| 4️⃣ | 📊 **Feedback System** | Track helpful vs unhelpful responses with success rate |
| 5️⃣ | 🔐 **Secure API Key** | Loads API key from environment variables |

---

## 🧠 How It Works

```
User Input
    ↓
Main Menu (5 Options)
    ↓
┌─────────────────────────────────────┐
│  1. Answer Questions                │
│     → Gemini API (factual mode)     │
│                                     │
│  2. Summarize Text                  │
│     → Gemini API (summary mode)     │
│                                     │
│  3. Generate Creative Content       │
│     → Gemini API (creative mode)    │
│                                     │
│  4. View Feedback Summary           │
│     → Local feedback log            │
│                                     │
│  5. Exit                            │
└─────────────────────────────────────┘
    ↓
AI Response + Feedback Collection
```

---

## 📁 Repository Structure

```
📁 AI_Assistant_Project/
│
├── 🤖 ai_assistant.py                          ← Main Python source code
├── 📋 requirements.txt                          ← Python dependencies
├── 🔑 .env.template.txt                        ← API key setup template
├── 📄 AI BOT Project.pdf                       ← Project report
├── 📊 AI BOT Project Presentation.pdf          ← Project presentation
├── 🎨 Blue futurist...presentation.pptx        ← PowerPoint slides
├── 📁 venv/                                    ← Python virtual environment
└── 📖 README.md                                ← Project documentation
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3** | Core programming language |
| **Google Generative AI** | `google-generativeai` SDK |
| **Gemini 2.0 Flash** | AI model for generating responses |
| **OS Module** | Environment variable management |
| **DateTime Module** | Feedback timestamp logging |

---

## 🚀 Installation & Setup

### Step 1 — Clone the Repository
```bash
git clone https://github.com/BadeNaveenKumar/AI_Assistant_Project.git
cd AI_Assistant_Project
```

### Step 2 — Create Virtual Environment
```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Mac/Linux
source venv/bin/activate
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Set Your Google API Key

Get your FREE API key from: 👉 **[https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)**

**Option A — Set as Environment Variable (Recommended):**
```bash
# Windows
set GOOGLE_API_KEY=your_api_key_here

# Mac/Linux
export GOOGLE_API_KEY=your_api_key_here
```

**Option B — Use .env file:**
```bash
# Copy the template
cp .env.template.txt .env

# Edit .env and add your key
GOOGLE_API_KEY=your_api_key_here
```

### Step 5 — Run the Assistant
```bash
python ai_assistant.py
```

---

## 💻 Usage Demo

```
============================================================
     Welcome to Your AI Assistant (FREE)
============================================================

This assistant uses Google Gemini API (FREE)

Functions:
1. Answer factual questions
2. Summarize text
3. Generate creative content

============================================================
Main Menu
============================================================
1. Answer Questions
2. Summarize Text
3. Generate Creative Content
4. View Feedback Summary
5. Exit

Select an option (1-5): 1

=== Question Answering Mode ===

Enter your question: What is machine learning?

Answer: Machine learning is a subset of artificial intelligence...

Was this response helpful? (yes/no): yes
Thank you for your positive feedback!
```

---

## 📊 Feedback System

The assistant tracks every interaction and provides a summary:

```
=== Feedback Summary ===
Total interactions: 10
Helpful responses: 8
Success rate: 80.0%

Recent feedback:
✓ [2025-10-31 14:30:00] Question Answering
✓ [2025-10-31 14:31:15] Text Summarization
✗ [2025-10-31 14:32:45] Creative Content
✓ [2025-10-31 14:33:20] Question Answering
✓ [2025-10-31 14:34:00] Creative Content
```

---

## 🔧 Class Structure

```python
class AIAssistant:
    ├── __init__()                  # Initialize Gemini API & feedback log
    ├── get_ai_response()           # Core API call method
    ├── answer_questions()          # Function 1: Q&A mode
    ├── summarize_text()            # Function 2: Summarization mode
    ├── generate_creative_content() # Function 3: Creative mode
    ├── collect_feedback()          # Collect yes/no feedback
    ├── show_feedback_summary()     # Display feedback stats
    └── run()                       # Main menu loop
```

---

## ⚙️ Requirements

```txt
google-generativeai==0.3.0
```

> 💡 **Note:** Python 3.8+ required. Get your FREE Google API key at [Google AI Studio](https://makersuite.google.com/app/apikey)

---

## 🔍 Key Highlights

```
🤖 AI Model      : Google Gemini 2.0 Flash (Latest)
🐍 Language      : Python 3
🎯 Functions     : 3 AI-powered modes
📊 Feedback      : Real-time success rate tracking
🔐 Security      : API key via environment variables
📄 Documentation : Full project report + presentation included
💰 Cost          : FREE (uses Google's free API tier)
```

---

## 📬 Connect With Me

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-BadeNaveenKumar-181717?style=for-the-badge&logo=github)](https://github.com/BadeNaveenKumar)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Naveen%20Kumar%20Bade-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/naveenkumarbade)

</div>

---

<div align="center">

⭐ **If you found this project useful, please give it a star!** ⭐

*Made with ❤️ and 🤖 AI by Naveen Kumar Bade*

</div>