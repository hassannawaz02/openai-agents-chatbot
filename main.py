import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read Gemini API key from .env file
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini API client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Define the chat model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Define configuration for the run
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Create the AI Agent
agent: Agent = Agent(
    name="Gemini Assistant",
    instructions=(
        "You are a professional assistant specialized in web development, "
        "AI tools, and modern web technologies. "
        "Provide clear, concise, and helpful answers."
    ),
    model=model
)

# User input
query = "Explain what web development is in a short and beginner-friendly way."

# Run the agent
result = Runner.run_sync(agent, input=query, run_config=config)

# Print the response
print("Gemini Assistant says:")
print(result.final_output)
