import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, AIMessage
from get_current_weather import get_current_weather

load_dotenv()

# Initialize your LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# Create the agent with your custom tool
agent = create_agent(
    llm,
    tools=[get_current_weather],
    system_prompt=(
        "You are a helpful weather assistant. "
        "When the user mentions a city or location, you MUST convert it to latitude and longitude coordinates yourself and use the get_current_weather tool. "
        "Do not ask the user for coordinates. Handle the conversion internally. "
        "Always provide a friendly and detailed weather report."
    )
)

def print_welcome():
    print("\n" + "=" * 60)
    print("        🤖  WEATHER AI ASSISTANT  🤖")
    print("=" * 60)
    print("\n👋 Welcome! I'm your AI Weather Assistant.")
    print("\n📋 Instructions:")
    print("  • Ask me about the weather in any city or location")
    print("  • You can specify temperature units (Celsius/Fahrenheit)")
    print("  • Type 'exit' or 'quit' to stop the assistant")
    print("\n💡 Example questions:")
    print("  - What's the weather like in Paris?")
    print("  - How's the weather in New York in Fahrenheit?")
    print("  - Is it hot in Tokyo right now?")
    print("\n" + "=" * 60 + "\n")

async def main():
    print_welcome()

    chat_history = []

    while True:
        # Get user input
        user_input = input("👤 You: ").strip()

        # Check for exit commands
        if user_input.lower() in ["exit", "quit", "bye", "q"]:
            print("\n🤖 Assistant: Goodbye! Stay safe and have a great day! 👋\n")
            break

        # Skip empty input
        if not user_input:
            print("⚠️  Please enter a question.\n")
            continue

        print("\n🤖 Assistant: Thinking...\n")

        try:
            # Add user message to history
            chat_history.append(HumanMessage(content=user_input))

            # Invoke the agent with full chat history
            result = await agent.ainvoke({
                "messages": chat_history
            })

            # Get the assistant's response
            assistant_message = result["messages"][-1]
            response_text = assistant_message.content

            # Add assistant response to history
            chat_history.append(AIMessage(content=response_text))

            print(f"🤖 Assistant: {response_text}\n")
            print("-" * 60 + "\n")

        except Exception as e:
            print(f"❌ Error: {e}\n")

asyncio.run(main())