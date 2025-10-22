````markdown
# Observo

**A Modern Smart Agent for Observing, Planning, and Summarizing Daily Meetings**

[🎬 Demo Video](https://drive.google.com/drive/folders/1Km6RDOt2cz7LKfz3ockOlvxfc91w5VkS)

---

## 🔹 Project Overview
Observo is a Python-based agent that leverages OpenAI's GPT-4o-mini to:

1. **Plan** the steps for fetching calendar events.
2. **Simulate fetching today's calendar events** (mock data for easy demo).
3. **Summarize** the results in a clear, human-readable format.

It includes a lightweight observability logger that prints detailed events and can optionally POST them to a webhook endpoint for monitoring.

This project is perfect for hackathons, demos, or anyone exploring smart automation agents.

---

## 🔹 Features
- Modern and aesthetic logging output `[OBSERVE]`.
- Fetches today's meetings (simulated events).
- Generates GPT-powered planning steps and summaries.
- Fully configurable via `.env` for OpenRouter API key.
- Easy to set up and run on any machine.

---

## 🔹 Files in the Repo
- `main.py` - Core agent code.
- `.env` - Hidden configuration file for your API key.
- `.gitignore` - Excludes sensitive and cache files.
- `friction_log.md` - Optional notes/log for your development process.
- `requirements.txt` - Python dependencies.
- `README.md` - This file.

---

## 🔹 Setup Instructions
Follow these steps to run Observo on your machine:

### 1️⃣ Clone the Repository
You can download the ZIP from GitHub or clone using HTTPS:
```bash
git clone https://github.com/Nitanshu715/observo.git
cd observo
````

### 2️⃣ Install Dependencies

Install Python 3.10+ and the required libraries:

```bash
pip install -r requirements.txt
```

### 3️⃣ Setup Environment Variables

Create a `.env` file in the root of the repo with the following:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

> **Note:** Replace `your_openrouter_api_key_here` with your real OpenRouter API key.

### 4️⃣ Run the Agent

Execute the main script:

```bash
python main.py
```

You will see real-time `[OBSERVE]` logs and the final summary output at the end.

### 5️⃣ Optional: Observability Webhook

You can replace the `endpoint` in `main.py` for `AgentObserver` with your own webhook to capture logs remotely.

Example:

```python
observer = AgentObserver(endpoint="https://webhook.site/YOUR_UNIQUE_ID")
```

---

## 🔹 How It Works

1. **Agent Start** - Logs the user input.
2. **Planning** - Calls GPT-4o-mini to create a short, step-by-step plan.
3. **Execution** - Fetches today's calendar events (mocked in `fetch_todays_events()`).
4. **Summarization** - GPT-4o-mini summarizes what the agent achieved.
5. **Agent End** - Logs the final output summary.

> Everything is printed with timestamps and optionally sent to the webhook.

---

## 🔹 Example Output

```
[OBSERVE] {
  "event": "agent_start",
  "details": {"input": "today's meetings"},
  "timestamp": 1761156314.3524206
}
...
🎯 Final Output: {
  "summary": "The agent effectively managed today's meetings by coordinating schedules, ensuring all participants were informed, and facilitating smooth discussions. Key objectives were met, decisions were made, and action items were assigned for follow-up. Overall, the meetings were productive and aligned with the team's goals."
}
```

---

## 🔹 Contributing

* Fork the repository.
* Create your branch: `git checkout -b feature/YourFeature`
* Commit your changes: `git commit -am 'Add new feature'`
* Push to the branch: `git push origin feature/YourFeature`
* Open a Pull Request.

---

## 🔹 License

This project is licensed under the MIT License.

---

## 🔹 Contact

Nitanshu Tak
[GitHub](https://github.com/Nitanshu715)
Email: [nitanshu@example.com](mailto:nitanshu@example.com)

---

> Build, observe, and automate your meetings seamlessly with **Observo**! 🚀

```
```
