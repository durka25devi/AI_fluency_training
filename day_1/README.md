# 🤖 Agentic AI — Day 1 Lab

This project demonstrates three approaches to solving a college course-fee problem:

1. **Plain LLM Chatbot**
2. **Rule-Based Workflow**
3. **Tool-Using AI Agent**

The main goal is to understand how an AI agent uses tools to solve tasks dynamically.

---

## 1. 🎯 Objective

This lab helps us learn how to:

- Connect Python with an LLM using the Groq API.
- Build a simple LLM chatbot.
- Build a rule-based workflow.
- Create an AI agent with tools.
- Understand tool calling and dynamic decision-making.

---

## 2. 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Groq API | LLM provider |
| OpenAI Python SDK | LLM integration |
| `openai/gpt-oss-20b` | Language model |
| `python-dotenv` | Environment variables |
| Git / GitHub | Version control |

---

## 3. 📁 Project Structure

```text
day_1/
│
├── .envaifluency/       # Python virtual environment
├── .env                 # API key and configuration
├── .gitignore
├── agent.py             # AI agent
├── challenge.py         # Challenge question
├── chatbot.py           # Plain LLM chatbot
├── check_setup.py       # Setup verification
├── config.py            # Configuration
├── README.md
├── requirements.txt     # Required packages
├── tools.py             # Agent tools
└── workflow.py          # Rule-based workflow

```
---


## 4. 💰 Course Fee Data

The project uses the following private course-fee data:

| Course  | Fee     |
|-------- |---------|
| `CS101` | ₹12,000 |
| `AI202` | ₹18,000 |
| `DS303` | ₹15,000 |

---

## 5. ❓ Questions Used

### Q1 — Course Fee
> What is the fee for AI202?

### Q2 — Scholarship Calculation
> What is the total fee for CS101 and AI202 after a 10% scholarship?

### Q3 — Compare Course Fees
> Is DS303 more expensive than CS101, and by how much?

### Q4 — General Question
> Write a two-line welcome message for new AI students.

---

## 6. 💬 Plain LLM Chatbot

The chatbot sends the user's question **directly to the LLM**.

User Question
      ↓
     LLM
      ↓
    Answer

The LLM does not receive the private course-fee data.

Therefore, it cannot reliably answer questions such as:

What is the fee for AI202?

However, it can answer general questions such as:

Write a welcome message for AI students.

💡 Main Idea

The chatbot is useful for general conversation, but it does not have access to the project's private data.

 ---

### 7. ⚙️ Rule-Based Workflow

The workflow does not use an LLM.

Instead, it uses predefined rules.

User Question
      ↓
Predefined Rules
      ↓
    Answer
Example

Question:

What is the fee for AI202?

Answer:

Fee for AI202: ₹18,000

Advantages
Fast execution
Predictable results
No LLM required
Limitation

It can only handle questions for which rules have already been written.

💡 Main Idea

Rule-Based Workflow = Fast and predictable, but limited to predefined rules.

---

### 8. 🤖 Tool-Using AI Agent

The AI agent combines:

LLM + Tools

The agent has two main tools:

🔧 1. get_course_fee

Retrieves the fee of a course.

get_course_fee("AI202")
        ↓
      18000
🧮 2. calculator

Performs mathematical calculations.

calculator("(12000+18000)*0.9")
        ↓
      27000

The LLM decides which tool to use and when to use it.

---

### 9. 🔄 Agent Flow

The agent works through the following steps:

User Question
      ↓
     LLM
      ↓
Select Required Tool
      ↓
Execute Tool
      ↓
Observe Result
      ↓
Use Another Tool if Required
      ↓
  Final Answer

Unlike the rule-based workflow, the agent can dynamically decide which tools are required to solve a question.

---

### 10. 🧮 Agent Example
Question

What is the total fee for CS101 and AI202 after a 10% scholarship?

Step 1 — Get CS101 Fee
get_course_fee("CS101")
        ↓
      12000
Step 2 — Get AI202 Fee
get_course_fee("AI202")
        ↓
      18000
Step 3 — Calculate Total
calculator("(12000+18000)*0.9")
        ↓
      27000
Final Answer

The total fee is ₹27,000.

---

## 11. 🧪 Challenge Question

### Question

> I can pay ₹30,000. Which two courses can I take together within this budget?

The agent checks different course combinations.

| Courses | Calculation | Total | Within Budget? |
|---|---|---:|:---:|
| CS101 + AI202 | ₹12,000 + ₹18,000 | ₹30,000 | ✅ |
| CS101 + DS303 | ₹12,000 + ₹15,000 | ₹27,000 | ✅ |
| AI202 + DS303 | ₹18,000 + ₹15,000 | ₹33,000 | ❌ |

### ✅ Valid Combinations

| Courses | Total |
|---|---:|
| **CS101 + AI202** | **₹30,000** |
| **CS101 + DS303** | **₹27,000** |

### 💡 What This Demonstrates

The agent can perform **multiple tool calls** and combine their results to solve a new problem.
 ---

### 12. 🔐 Environment Setup
Step 1 — Create .env

Create a file named:

.env

in the project root.

Add the following:

PROVIDER=groq
GROQ_API_KEY=YOUR_GROQ_API_KEY
MODEL=openai/gpt-oss-20b

Replace:

YOUR_GROQ_API_KEY

with your actual Groq API key.

⚠️ Never share or upload your API key.

Step 2 — Configure .gitignore

Make sure your .gitignore contains:

.env
.envaifluency/
__pycache__/
*.pyc

This prevents sensitive files and the virtual environment from being committed to GitHub.

 ---

### 13. 🐍 Activate Virtual Environment

Open the VS Code terminal inside the day_1 folder.

PowerShell
.envaifluency\Scripts\Activate.ps1
Command Prompt (CMD)
.envaifluency\Scripts\activate

After successful activation, you should see:

(.envaifluency)

at the beginning of your terminal.

---

### 14. 📦 Install Dependencies

Install the required Python packages:

pip install -r requirements.txt

---

### 15. ✅ Check Setup

Run:

python check_setup.py

If the setup is correct, you can continue running the programs.

---

### 16. ▶️ Run the Programs
💬 Run Chatbot
python chatbot.py
⚙️ Run Rule-Based Workflow
python workflow.py
🔧 Run Tools
python tools.py
🤖 Run AI Agent
python agent.py
🧪 Run Challenge
python challenge.py

---

### 17. ⚠️ Common Agent Error

If you get:

maximum number of agent steps reached

it means the agent used all the allowed steps without completing the task.

Step 1 — Check Setup
python check_setup.py
Step 2 — Try a Simple Question
What is the fee for AI202?
Step 3 — Check Agent Files

If the problem continues, check:

agent.py
tools.py

These files contain the agent and tool-calling logic.

---

### 18. 📊 Comparison
## 18. 📊 Comparison

| Feature | Plain LLM Chatbot | Rule-Based Workflow | Tool-Using Agent |
|---|:---:|:---:|:---:|
| Uses LLM | ✅ | ❌ | ✅ |
| Uses Tools | ❌ | ❌ | ✅ |
| Private Course Data | ❌ | ✅ | ✅ |
| Handles Calculations | Limited | Predefined | ✅ |
| Dynamic Tool Selection | ❌ | ❌ | ✅ |
| Flexible Questions | ✅ | Limited | ✅ |
