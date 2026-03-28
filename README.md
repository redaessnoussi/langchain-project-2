# 🤖 Weather AI Assistant

An interactive command-line weather assistant powered by **LangChain**, **GPT-4o-mini**, and the **Open-Meteo API**. Just ask about the weather in any city — the AI handles the rest.

---

## ✨ Features

- 🌍 Ask about the weather in **any city or location** by name — no need to provide coordinates
- 🌡️ Supports both **Celsius** and **Fahrenheit**
- 💬 **Persistent chat history** — the assistant remembers context across your conversation
- ⚡ Powered by **GPT-4o-mini** via LangChain agents
- 🆓 Uses the **Open-Meteo API** — completely free, no API key required for weather data

---

## 📁 Project Structure

```
langchain-project-2/
├── agent.py                # Main entry point — runs the interactive assistant
├── get_current_weather.py  # LangChain tool that fetches weather from Open-Meteo
├── requirements.txt        # Python dependencies
└── .env                    # Your OpenAI API key (not committed to Git)
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/langchain-project-2.git
cd langchain-project-2
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your OpenAI API key

Create a `.env` file in the root of the project:

```env
OPENAI_API_KEY=your-openai-api-key-here
```

> Get your API key at [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

### 4. Run the assistant

```bash
python agent.py
```

---

## 💬 Example Usage

```
============================================================
        🤖  WEATHER AI ASSISTANT  🤖
============================================================

👋 Welcome! I'm your AI Weather Assistant.

📋 Instructions:
  • Ask me about the weather in any city or location
  • You can specify temperature units (Celsius/Fahrenheit)
  • Type 'exit' or 'quit' to stop the assistant

💡 Example questions:
  - What's the weather like in Paris?
  - How's the weather in New York in Fahrenheit?
  - Is it hot in Tokyo right now?

============================================================

👤 You: What's the weather like in London?

🤖 Assistant: Thinking...

🤖 Assistant: The current weather in London is 12°C with a wind speed
of 3.2 m/s. It's a mild day — perfect for a walk! ☁️
```

---

## 🛠️ Tech Stack

| Technology                                                     | Purpose                              |
| -------------------------------------------------------------- | ------------------------------------ |
| [LangChain](https://www.langchain.com/)                        | Agent framework & tool orchestration |
| [langchain-openai](https://pypi.org/project/langchain-openai/) | GPT-4o-mini LLM integration          |
| [Open-Meteo API](https://open-meteo.com/)                      | Free weather data (no key required)  |
| [Pydantic](https://docs.pydantic.dev/)                         | Tool input validation                |
| [python-dotenv](https://pypi.org/project/python-dotenv/)       | Environment variable management      |

---

## 📦 Dependencies

```
langchain
langchain-openai
pydantic
requests
asyncio
python-dotenv
```

---

## ⚠️ Notes

- This project requires **Python 3.10+** (Python 3.14 may have Pydantic V1 compatibility warnings)
- The OpenAI API key is **required** — weather data from Open-Meteo is free
- Never commit your `.env` file — add it to `.gitignore`

---

## 📄 License

MIT License — feel free to use and modify this project.
