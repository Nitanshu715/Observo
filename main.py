import os
import time
import json
import requests
from openai import OpenAI
import os
from dotenv import load_dotenv
from openai import OpenAI


# =======================
# SETUP
# =======================
# Initialize OpenAI client with OpenRouter endpoint
#Create Fake Calender event
def fetch_todays_events():
        # Simulated "today's events"
        events = [
            {"time": "09:00 AM", "title": "Team Standup"},
            {"time": "11:30 AM", "title": "Project Sync"},
            {"time": "02:00 PM", "title": "Client Call"},
            {"time": "04:00 PM", "title": "Wrap-up & Notes"},
        ]
        # format them as a string
        return "\n".join([f"{e['time']} - {e['title']}" for e in events])
    
load_dotenv()  # loads .env file

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),  # now key is hidden
    base_url="https://openrouter.ai/api/v1",
)

# =======================
# OBSERVABILITY LOGGER
# =======================
class AgentObserver:
    def __init__(self, endpoint="https://httpbin.org/post"):
        self.endpoint = endpoint

    def log_event(self, event_name, details):
        data = {
            "event": event_name,
            "details": details,
            "timestamp": time.time()
        }
        print(f"[OBSERVE] {json.dumps(data, indent=2)}")
        try:
            res = requests.post(self.endpoint, json=data, timeout=5)
            if res.status_code != 200:
                print(f"warning: logging endpoint returned {res.status_code}")
        except Exception as e:
            print("warning: could not POST to observability endpoint:", e)

# =======================
# SIMPLE AGENT
# =======================
class SimpleAgent:
    def __init__(self, observer):
        self.observer = observer

    def run(self, user_input):
        self.observer.log_event("agent_start", {"input": user_input})

        # Step 1: PLAN
        self.observer.log_event("planning", {"step": "Using GPT-4o-mini to create plan"})
        try:
            plan_response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Create 3 short, numbered steps to fetch calendar events for: {user_input}"}
                ]
            )
            plan_text = plan_response.choices[0].message.content.strip()
            self.observer.log_event("planning_result", {"plan": plan_text})
        except Exception as e:
            self.observer.log_event("planning_error", {"error": str(e)})
            plan_text = "Failed to generate plan."

        # Step 2: EXECUTE — fetch fake events
        self.observer.log_event("tool_execution", {"tool": "calendar.get_events", "based_on": plan_text})
        try:
            events = fetch_todays_events()
        except Exception as e:
            events = f"Error fetching events: {e}"

        self.observer.log_event("tool_execution_result", {"events": events})

        # Step 3: SUMMARIZE
        try:
            summary_response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Summarize briefly what the agent achieved for: {user_input}"}
                ]
            )
            summary_text = summary_response.choices[0].message.content.strip()
        except Exception as e:
            summary_text = f"Could not summarize: {e}"

        # Step 4: END
        result = {"summary": summary_text}
        self.observer.log_event("agent_end", {"output": result})
        return result

# =======================
# MAIN EXECUTION
# =======================
if __name__ == "__main__":
    observer = AgentObserver(endpoint="https://webhook.site/d82f54c1-e9d7-4d49-9257-e3521e078d06")
    agent = SimpleAgent(observer)
    output = agent.run("today's meetings")
    print("\n Final Output:", json.dumps(output, indent=2))
