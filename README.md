# 🤖 Customer Support AI Agent

An enterprise-grade multi-agent customer support assistant built with **CrewAI**, **OpenAI GPT-4.1**, **LangChain**, and **Streamlit**.

The application intelligently routes customer queries, remembers long-term user information, performs internet research when required, and maintains persistent conversation memory across sessions.

---

## ✨ Features

- 🧠 Persistent User Memory
- 🤖 Multi-Agent Architecture (CrewAI)
- 🌐 Automatic Internet Research
- 💬 Customer Support Assistant
- 📄 Conversation Logging
- 📊 Live Dashboard
- ⚡ Smart Routing
- 📝 Long-Term Memory Extraction
- 🎨 Beautiful Streamlit UI
- 🔄 Modular & Scalable Architecture

---

# 🏗 Architecture

```
                User

                  │
                  ▼

        Streamlit Frontend
                  │
                  ▼

          Chat Service Layer
                  │
      ┌───────────┴───────────┐
      │                       │
      ▼                       ▼

 Memory Router         Research Router
      │                       │
      ▼                       ▼

Memory Extractor      Search Tool
      │
      ▼

 Memory Service
      │
      ▼

     CrewAI
      │
      ▼

 ┌──────────────────────────────┐
 │ Assistant Agent              │
 │ Research Agent               │
 │ Audit Agent                  │
 └──────────────────────────────┘
      │
      ▼

 Final Response
```

---

# 🚀 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.12 | Backend |
| CrewAI | Multi-Agent Orchestration |
| OpenAI GPT-4.1 Mini | LLM |
| LangChain | LLM Integration |
| Streamlit | Frontend |
| DuckDuckGo Search | Internet Search |
| JSON Storage | Persistent Memory |

---

# 📂 Project Structure

```
customer-support-ai/

├── agents/
├── tasks/
├── crew/
├── services/
├── components/
├── tools/
├── core/
├── storage/
├── assets/
├── docs/
├── app.py
├── requirements.txt
└── README.md
```

---

# 🧠 AI Agents

### 1. Customer Support Agent

Responsible for:

- Understanding customer queries
- Answering using memory
- Producing accurate responses
- Maintaining conversational flow

---

### 2. Research Agent

Automatically activated for:

- Latest news
- Product pricing
- Current events
- Company research
- Market information

---

### 3. Conversation Audit Agent

Responsible for:

- Validating conversations
- Ensuring required outputs exist
- Final verification before archival

---

# 🧠 Memory Engine

The application automatically extracts:

- User Name
- Company
- Designation
- Email
- Location
- Long-term Facts

Example:

```
My name is Vijay.

I own Make Market.

I live in Chennai.
```

Automatically becomes

```
Profile

Name : Vijay

Company : Make Market

Location : Chennai

Facts

✓ User owns Make Market
```

---

# 🌐 Smart Research Routing

The application automatically decides whether internet search is required.

Example

```
What's my name?
```

❌ No Search

---

```
Latest iPhone price in India
```

✅ Internet Search

---

# 📊 Dashboard

The application displays:

- Total Questions
- Research Calls
- Memory Updates
- Average Response Time

---

# 📄 Answer Logger

Every interaction is automatically stored inside

```
storage/answers.txt
```

Useful for

- Debugging
- Auditing
- Evaluation
- Analytics

---

# 🚀 Installation

Clone repository

```bash
git clone https://github.com/consultvijayarumugam/customer-support-AI.git
```

Go inside project

```bash
cd customer-support-AI
```

Create virtual environment

```bash
python3.12 -m venv venv
```

Activate

Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create environment file

```
.env
```

```
OPENAI_API_KEY=your_key_here
MODEL=gpt-4.1-mini
TEMPERATURE=0.2
```

Run

```bash
streamlit run app.py
```

---

# 📸 Screenshots

Add screenshots here

- Dashboard
- Chat Window
- Memory Panel
- Answer Log

---

# 🎯 Future Improvements

- PostgreSQL Memory
- Vector Database
- RAG Support
- PDF Knowledge Base
- Voice Assistant
- WhatsApp Integration
- Slack Integration
- Gmail Integration
- Multi-user Authentication
- Docker Deployment
- Kubernetes Deployment

---

# 👨‍💻 Author

**Vijay Arumugam**

Performance Marketing Consultant

AI Automation Engineer

Specializing in:

- AI Agents
- CrewAI
- LangChain
- Business Automation
- Marketing Automation
- Customer Support AI

GitHub

https://github.com/consultvijayarumugam

---

# ⭐ If you found this project useful, consider giving it a Star.