# 1. Import the necessary base library and ADK components.
from google import genai
from google.adk.agents import Agent
from google.adk.tools import google_search
from utils.gcs_utils import fetch_instructions

# --- Get Instruction Set from gcs bucket ---
def get_live_instructions(ctx) -> str:
    """This function is passed to the Agent and called on every run."""
    return fetch_instructions("jarvis_agent")


# 3. Update the Agent to use the new LiteLLM client
root_agent = Agent(
    name="jarvis_agent",
    model="gemini-2.5-flash", 
    description="Jarvis agent",
    instruction=get_live_instructions,
    tools=[google_search],
)