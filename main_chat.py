from openai import OpenAI

client = OpenAI(api_key="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")

  # paste your API here

print("\n🤖 AI Chatbot Ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! 👋")
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}]
    )

    print("Bot:", response.choices[0].message.content, "\n")
