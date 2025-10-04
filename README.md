# 🤖 Gemini-Powered AI Chatbot (Agent)

This project is a simple yet intelligent AI Chatbot (Agent) built using the OpenAI Agents SDK and Google Gemini API.
It demonstrates how to connect external AI models with the OpenAI Agents framework to create conversational assistants in Python.

────────────────────────────────────────────

## 🚀 Features
- Conversational AI Agent built with OpenAI Agents SDK
- Powered by Gemini 2.0 Flash model for fast and accurate responses
- Secure API key management with .env
- Simple, readable, and extendable Python codebase
- Perfect for learning AI Agent structure and SDK integration

────────────────────────────────────────────

## 🧩 Project Structure
📂 Gemini-Chatbot-Agent  
├── .env                  → Contains your GEMINI_API_KEY  
├── .env.example          → Example environment file  
├── main.py               → Main chatbot code  
├── pyproject.toml        → Project dependencies (if used)  
├── requirements.txt      → Python dependencies  
├── README.md             → Project documentation  
└── .venv/                → Virtual environment (ignored in GitHub)  

────────────────────────────────────────────

## ⚙️ Setup Instructions
1️⃣ Clone the Repository  
   git clone https://github.com/hassannawaz02/AI-Chatbot--Agent--using-OpenAI-Agents-SDK---Gemini-API.git  
   cd gemini-chatbot-agent  

2️⃣ Create and Activate a Virtual Environment  
   python -m venv .venv  
   .venv\Scripts\activate   (Windows)  
   source .venv/bin/activate   (Mac/Linux)  

3️⃣ Install Dependencies  
   pip install -r requirements.txt  

4️⃣ Add Your .env File  
   GEMINI_API_KEY=your_real_gemini_api_key_here  

5️⃣ Run the Chatbot  
   python main.py  

────────────────────────────────────────────

## 💬 main.py Code
import os  
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig  
from dotenv import load_dotenv  

# Load environment variables  
load_dotenv()  

# Read Gemini API key from .env  
gemini_api_key = os.getenv("GEMINI_API_KEY")  

# Initialize Gemini client  
external_client = AsyncOpenAI(  
    api_key=gemini_api_key,  
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"  
)  

# Define the chat model  
model = OpenAIChatCompletionsModel(  
    model="gemini-2.0-flash",  
    openai_client=external_client  
)  

# Define run configuration  
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
        "AI tools, and modern technologies. "  
        "Provide concise, beginner-friendly answers."  
    ),  
    model=model  
)  

# User input  
query = "Explain web development briefly in simple words."  

# Run the chatbot  
result = Runner.run_sync(agent, input=query, run_config=config)  

# Print the result  
print("Gemini Assistant says:")  
print(result.final_output)  

────────────────────────────────────────────

## 🧠 Example Output
Gemini Assistant says:  
Web development means building and maintaining websites and web apps.  
It includes both frontend (design/UI) and backend (server logic).  

────────────────────────────────────────────

## 🏷️ Topics & Tags
#Python #AI #OpenAIAgents #Gemini #Chatbot #AI-Agent #MachineLearning #WebDevelopment  

────────────────────────────────────────────

## 👨‍💻 Author
Hassan  
Web Developer | AI & Automation Enthusiast  
"Crafting modern, intelligent, and scalable digital experiences."

────────────────────────────────────────────

## 📜 License
Licensed under the MIT License.  
You are free to use, modify, and distribute this project under the terms of the license.

────────────────────────────────────────────
