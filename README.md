# 🚀 Observo: The AI-Powered Observability Agent

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🌟 Overview

**Observo** is an intelligent, event-driven observability agent that demonstrates how AI models can plan, execute, and summarize tasks while maintaining clear event logs.  
Built with **OpenRouter ( OpenAI GPT-4o-mini)**, it showcases structured AI reasoning and logging using Python - ideal for hackathons, observability tools, and lightweight automation agents.

🎥 **Demo Video:** [Click Here to Watch](https://drive.google.com/drive/folders/1Km6RDOt2cz7LKfz3ockOlvxfc91w5VkS)

---

## 🧠 What Observo Does

1. **Logs Every Step:** Tracks planning, execution, and results in real-time.
2. **Plans Intelligently:** Uses GPT-4o-mini to generate a short plan for a given task.
3. **Executes Smartly:** Simulates fetching “today’s meetings” from a fake calendar system.
4. **Summarizes Automatically:** Generates a natural-language summary of the agent’s work.
5. **Observes Everything:** Sends logs to an external webhook (observability endpoint).

---

## 🏗️ Project Structure

```
📦 agent-observability-bridge
├── main.py              # Core logic of the Observo agent
├── .env                 # API key stored securely (not shared)
├── .gitignore           # To prevent secrets from being pushed
├── requirements.txt     # All dependencies
├── friction_log.md      # Development notes (optional)
└── README.md            # You are here 😎
```

---

## ⚙️ Setup Instructions

Follow these **simple steps** to get Observo running locally:

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/observo.git
cd observo
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Create a `.env` File**
Inside your project folder, create a `.env` file and add this line:

```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

> ⚠️ **Important:** Never commit your real API key. This is your personal credential.

### **5️⃣ Run the Project**
```bash
python main.py
```

If successful, you’ll see structured logs in your terminal and the final AI-generated summary like this:

```
🎯 Final Output: {
  "summary": "The agent successfully organized today's meetings..."
}
```

---

## 📊 Example Output

```
[OBSERVE] { "event": "planning_result", "plan": "Access Calendar API, Set Date Range, Fetch Events..." }
[OBSERVE] { "event": "tool_execution_result", "details": { "events": "09:00 AM - Team Standup..." } }
🎯 Final Output: {
  "summary": "The agent effectively managed today's meetings..."
}
```

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|----------------|
| 💬 Language | Python 3.10+ |
| 🧠 AI Model | GPT-4o-mini (via OpenRouter) |
| 🧰 Logging | Webhook + Observability Layer |
| 🧪 Frameworks | `requests`, `dotenv`, `openai` |

---

## 🌍 Environment Variables

| Variable | Description |
|-----------|-------------|
| `OPENROUTER_API_KEY` | Your OpenRouter API key (kept private in `.env`) |

---

## 🪄 Example Workflow

| Step | Description |
|------|--------------|
| 🧩 Plan | The agent generates a plan using GPT |
| ⚙️ Execute | Fetches calendar data (simulated) |
| 🧾 Log | Sends logs to webhook |
| 🧠 Summarize | Summarizes what the agent accomplished |

---

## 🧠 How It Works Internally

The flow is divided into 3 stages:

1. **Planning Stage:** Uses GPT-4o-mini to design 3-step plan.  
2. **Execution Stage:** Simulates fetching meeting events.  
3. **Summarization Stage:** Produces a readable summary of achievements.

Each stage is **observed and logged** for transparency and debugging.

---

## 🧰 Dependencies

All required packages are listed in `requirements.txt`:

```
openai==1.30.0
requests==2.32.0
python-dotenv==1.0.1
```

To install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 📹 Demo Video

▶️ **Watch Demo:** [Click Here](https://drive.google.com/drive/folders/1Km6RDOt2cz7LKfz3ockOlvxfc91w5VkS)

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 💡 Future Enhancements

- Integration with Google or Outlook Calendar API  
- Real-time observability dashboard (with Grafana)  
- Add database logging (MongoDB or PostgreSQL)  
- Multi-agent collaboration  

---

## ✨ Author

👨‍💻 **Nitanshu Tak**  
🎓 B.Tech CSE | Cloud Computing & Virtualization Technology  
💭 Interests: AI/ML | Cloud

🔗 [LinkedIn](https://www.linkedin.com/in/nitanshu-tak-89a1ba289/?originalSubdomain=in) • [GitHub](https://github.com/Nitanshu715)

---

⭐ *If you like this project, consider giving it a star on GitHub!* ⭐

