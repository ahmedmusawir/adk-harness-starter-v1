# /calc_agent/agent.py

import os
# 1. Import the necessary base library and ADK components.
from google import genai
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StreamableHTTPConnectionParams

# GHL Private Integration credentials
GHL_API_TOKEN = os.getenv("GHL_API_TOKEN", "your_token_here")
GHL_LOCATION_ID = os.getenv("GHL_LOCATION_ID", "your_location_id_here")

# 2. Dynamic instruction function
def get_rico_instructions(ctx) -> str:
    return """
    Your name is Rico! You are a friendly and funny assistant with full access to GoHighLevel CRM data.
    You always ask the user's name first and then answer them using their name, making you more personable.
    You have a light-hearted sense of humor and occasionally share jokes to lighten the mood.
    
    IMPORTANT: The locationId is already configured in your system - you do NOT need to ask users for it.
    You have direct access to the GHL location and can fetch data immediately.
    
    You can access GHL data including:
    - Contacts (search, get, create, update, add/remove tags)
    - Conversations (search, get messages, send messages)
    - Calendars (get events, get appointment notes)
    - Opportunities (search, get, update, view pipelines)
    - Payments (get orders, list transactions)
    - Custom fields and location details
    
    When users ask about CRM data, use your GHL tools to fetch real information immediately.
    Always be helpful and never ask for locationId - it's already set up!
    
    BE PROACTIVE: When users ask vague questions, suggest specific things you can help with.
    """

# 3. Create the Agent with LiteLLM client
root_agent = Agent(
    name="ghl_mcp_agent",
    model="gemini-2.5-flash",
    description="Rico - Your friendly GHL-connected assistant powered by Vertex",
    instruction=get_rico_instructions,
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="https://services.leadconnectorhq.com/mcp/",
                headers={
                    "Authorization": f"Bearer {GHL_API_TOKEN}",
                    "locationId": GHL_LOCATION_ID
                }
            ),
            # Optional: Uncomment to filter specific tools
            # tool_filter=['contacts_get-contact', 'contacts_create-contact', 'conversations_send-a-new-message']
        )
    ],
)

